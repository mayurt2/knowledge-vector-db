import json
import re
import sys
from pathlib import Path

import lancedb
import yaml
from sentence_transformers import SentenceTransformer

from schema import KnowledgeChunk

KNOWLEDGE_DIR = Path("knowledge_files")
DB_PATH = "lancedb_store"
TABLE_NAME = "knowledge"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

HEADING_TO_SECTION_TYPE = {
    "Customer experience": "customer_experience",
    "Configurability": "configurability",
    "Which team to connect with": "contact_team",
    "Related / dependent settings": "related_settings",
    "Technical reference (for Onboarding/Tech)": "technical_reference",
    "Technical reference (for Tech)": "technical_reference",
}

# ── Chunking strategy notes ───────────────────────────────────────────────────
# Every chunk embeds a context prefix "[Feature | Category]" so the embedding
# carries feature identity — improves cross-feature disambiguation.
#
# Three chunk types per file:
#   A. Section chunks  — one per H2 section (Summary merged with Functionality).
#      Prefix: "[{feature_name} | {category}]"
#   B. Tags-cloud chunk — one per file: feature name + all synonym tags.
#      Fixes "do we have X?" queries by providing a rich synonym anchor.
#   C. Sample-question chunks — one per bullet in "Sample questions".
#      Enriched with feature context so the Q embedding is not bare text.
# ─────────────────────────────────────────────────────────────────────────────


def extract_frontmatter(text):
    match = re.match(r"^---\n(.*?)\n---\n?(.*)", text, re.DOTALL)
    if not match:
        return {}, text
    frontmatter = yaml.safe_load(match.group(1))
    body = match.group(2)
    return frontmatter, body


def split_by_h2(body):
    sections = []
    current_heading = None
    current_lines = []
    for line in body.splitlines():
        if line.startswith("## "):
            if current_heading is not None:
                sections.append((current_heading, "\n".join(current_lines).strip()))
            current_heading = line[3:].strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_heading is not None:
        sections.append((current_heading, "\n".join(current_lines).strip()))
    return sections


def extract_bullet_points(text):
    questions = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("- "):
            q = line[2:].strip().strip('"')
            if q:
                questions.append(q)
    return questions


def _context_prefix(frontmatter):
    """Short identity header prepended to every section chunk."""
    return f"[{frontmatter.get('feature_name', '')} | {frontmatter.get('category', '')}]\n"


def _make_chunk(frontmatter, path, heading, section_type, content, chunk_id=None):
    feature_id = frontmatter.get("feature_id", path.stem)
    if chunk_id is None:
        slug = re.sub(r"[^a-z0-9]+", "_", heading.lower()).strip("_")
        chunk_id = f"{feature_id}__{slug}"

    return {
        "chunk_id": chunk_id,
        "feature_id": feature_id,
        "feature_name": frontmatter.get("feature_name", ""),
        "category": frontmatter.get("category", ""),
        "config_source": frontmatter.get("config_source", ""),
        "configurable": bool(frontmatter.get("configurable", False)),
        "status": frontmatter.get("status", ""),
        "contact_team": frontmatter.get("contact_team", ""),
        "tags": json.dumps(frontmatter.get("tags") or []),
        "related_services": json.dumps(frontmatter.get("related_services") or []),
        "technical_keys": json.dumps(frontmatter.get("technical_keys") or []),
        "source_file": path.name,
        "section_heading": heading,
        "section_type": section_type,
        "chunk_text": content,
    }


def _make_tags_cloud_chunk(frontmatter, path):
    """
    Type B chunk — one per feature.
    Embeds feature name + all synonym tags + tech keys as a flat sentence.
    Designed to match "do we have X?" and synonym-heavy queries that wouldn't
    hit the summary section directly.
    """
    feature_id = frontmatter.get("feature_id", path.stem)
    feature_name = frontmatter.get("feature_name", "")
    tags = frontmatter.get("tags") or []
    tech_keys = frontmatter.get("technical_keys") or []
    category = frontmatter.get("category", "")
    contact_team = frontmatter.get("contact_team", "")
    config_source = frontmatter.get("config_source", "")

    parts = [f"{feature_name}: {', '.join(tags)}."]
    parts.append(f"Category: {category}. Contact: {contact_team}. Config: {config_source}.")
    if tech_keys:
        parts.append(f"Technical keys: {', '.join(tech_keys)}.")

    text = " ".join(parts)
    return _make_chunk(
        frontmatter, path,
        heading="Tags",
        section_type="tags_cloud",
        content=text,
        chunk_id=f"{feature_id}__tags_cloud",
    )


def parse_file(path):
    text = path.read_text(encoding="utf-8")
    frontmatter, body = extract_frontmatter(text)
    sections = dict(split_by_h2(body))
    chunks = []
    prefix = _context_prefix(frontmatter)

    # ── Type A: section chunks ───────────────────────────────────────────────
    # Merge Summary + What this feature does (always read together)
    summary = sections.get("Summary", "")
    functionality = sections.get("What this feature does", "")
    merged = summary
    if functionality:
        merged = summary + "\n\n## What this feature does\n" + functionality
    if merged.strip():
        chunks.append(_make_chunk(
            frontmatter, path, "Summary", "summary",
            prefix + merged,
        ))

    skip = {"Summary", "What this feature does", "Sample questions this feature answers"}
    for heading, content in sections.items():
        if heading in skip or not content.strip():
            continue
        section_type = HEADING_TO_SECTION_TYPE.get(heading, "other")
        chunks.append(_make_chunk(
            frontmatter, path, heading, section_type,
            prefix + content,
        ))

    # ── Type B: tags-cloud chunk ─────────────────────────────────────────────
    chunks.append(_make_tags_cloud_chunk(frontmatter, path))

    # ── Type C: sample question chunks ──────────────────────────────────────
    # Enrich each question with feature context so the embedding is not bare text.
    sample_text = sections.get("Sample questions this feature answers", "")
    feature_id = frontmatter.get("feature_id", path.stem)
    feature_name = frontmatter.get("feature_name", "")
    category = frontmatter.get("category", "")
    contact_team = frontmatter.get("contact_team", "")

    for i, question in enumerate(extract_bullet_points(sample_text)):
        enriched = (
            f"Q: {question}\n"
            f"[{feature_name} | {category} | Contact: {contact_team}]"
        )
        chunks.append(_make_chunk(
            frontmatter, path,
            heading="Sample questions",
            section_type="sample_question",
            content=enriched,
            chunk_id=f"{feature_id}__sample_q_{i}",
        ))

    return chunks


def ingest_all():
    md_files = sorted(KNOWLEDGE_DIR.glob("*.md"))
    if not md_files:
        print(f"No .md files found in {KNOWLEDGE_DIR}", file=sys.stderr)
        sys.exit(1)

    print(f"Parsing {len(md_files)} files...")
    all_chunks = []
    for md_file in md_files:
        file_chunks = parse_file(md_file)
        all_chunks.extend(file_chunks)

    print(f"Encoding {len(all_chunks)} chunks with '{EMBED_MODEL}'...")
    model = SentenceTransformer(EMBED_MODEL)
    texts = [c["chunk_text"] for c in all_chunks]
    embeddings = model.encode(texts, batch_size=64, show_progress_bar=True, normalize_embeddings=True)

    rows = []
    for chunk, vec in zip(all_chunks, embeddings):
        chunk["vector"] = vec.tolist()
        rows.append(KnowledgeChunk(**chunk))

    db = lancedb.connect(DB_PATH)
    if TABLE_NAME in db.table_names():
        db.drop_table(TABLE_NAME)
        print(f"Dropped existing table '{TABLE_NAME}'")

    table = db.create_table(TABLE_NAME, data=rows)
    table.create_fts_index("chunk_text", replace=True)

    print(f"\nDone. {len(rows)} chunks from {len(md_files)} files → '{DB_PATH}/{TABLE_NAME}'")


if __name__ == "__main__":
    ingest_all()
