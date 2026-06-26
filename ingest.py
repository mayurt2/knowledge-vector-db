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


def extract_frontmatter(text):
    match = re.match(r"^---\n(.*?)\n---\n?(.*)", text, re.DOTALL)
    if not match:
        return {}, text
    frontmatter = yaml.safe_load(match.group(1))
    body = match.group(2)
    return frontmatter, body


def split_by_h2(body):
    """Return ordered list of (heading, content) tuples split on ## headings."""
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


def parse_file(path):
    text = path.read_text(encoding="utf-8")
    frontmatter, body = extract_frontmatter(text)
    sections = dict(split_by_h2(body))
    chunks = []

    # Type A: section chunks
    # Merge "Summary" + "What this feature does" into one chunk
    summary = sections.get("Summary", "")
    functionality = sections.get("What this feature does", "")
    merged = summary
    if functionality:
        merged = summary + "\n\n## What this feature does\n" + functionality
    if merged.strip():
        chunks.append(_make_chunk(frontmatter, path, "Summary", "summary", merged))

    skip = {"Summary", "What this feature does", "Sample questions this feature answers"}
    for heading, content in sections.items():
        if heading in skip:
            continue
        section_type = HEADING_TO_SECTION_TYPE.get(heading, "other")
        chunks.append(_make_chunk(frontmatter, path, heading, section_type, content))

    # Type B: each sample question becomes its own row
    sample_text = sections.get("Sample questions this feature answers", "")
    feature_id = frontmatter.get("feature_id", path.stem)
    for i, question in enumerate(extract_bullet_points(sample_text)):
        cid = f"{feature_id}__sample_q_{i}"
        chunks.append(
            _make_chunk(frontmatter, path, "Sample questions", "sample_question", question, chunk_id=cid)
        )

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
