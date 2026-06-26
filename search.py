import json
from typing import List, Optional

import lancedb
from lancedb.rerankers import LinearCombinationReranker
from sentence_transformers import SentenceTransformer

DB_PATH = "lancedb_store"
TABLE_NAME = "knowledge"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# FTS reranker — weight=0.3 means 30% vector + 70% FTS, good for exact technical key lookups.
_fts_reranker = LinearCombinationReranker(weight=0.3)


def load_model() -> SentenceTransformer:
    """Load the embedding model. Call once and cache the result externally."""
    return SentenceTransformer(EMBED_MODEL)


def load_table():
    """Open the LanceDB table. Call once and cache the result externally."""
    return lancedb.connect(DB_PATH).open_table(TABLE_NAME)


def search(
    query: str,
    top_k: int = 5,
    threshold: Optional[float] = None,
    category: Optional[str] = None,
    contact_team: Optional[str] = None,
    section_types: Optional[List[str]] = None,
    status: Optional[str] = None,
    use_fts: bool = False,
    _model: Optional[SentenceTransformer] = None,
    _table=None,
) -> List[dict]:
    """
    Semantic search over the knowledge base.

    Args:
        query:         Natural-language question from the user.
        top_k:         Number of results to return.
        threshold:     Minimum cosine similarity (0.0–1.0) to include a result.
                       Results below this are dropped. Pass None to return all top_k.
        category:      Filter to a specific category (e.g. "Approvals").
        contact_team:  Filter by team ("Onboarding Team" or "Tech Team").
        section_types: Limit to specific section types, e.g. ["summary", "sample_question"].
        status:        "live" | "in-development" | None (default, returns all).
        use_fts:       Set True for exact keyword/technical-key lookups (e.g. "noOfApprovers").
                       Default False uses pure vector search, best for natural-language queries.
        _model:        Pre-loaded SentenceTransformer (pass from @st.cache_resource to avoid reload).
        _table:        Pre-opened LanceDB table (pass from @st.cache_resource to avoid stale refs).

    Returns:
        List of dicts with keys: chunk_text, feature_name, feature_id, category,
        contact_team, config_source, status, section_type, section_heading, tags, score, source_file.
        Returns empty list if no results meet the threshold.
    """
    model = _model or load_model()
    table = _table or load_table()

    query_vec = model.encode(query, normalize_embeddings=True).tolist()

    filters = []
    if status:
        filters.append(f"status = '{status}'")
    if category:
        safe_cat = category.replace("'", "''")
        filters.append(f"category = '{safe_cat}'")
    if contact_team:
        safe_team = contact_team.replace("'", "''")
        filters.append(f"contact_team = '{safe_team}'")
    if section_types:
        types_str = ", ".join(f"'{t}'" for t in section_types)
        filters.append(f"section_type IN ({types_str})")

    where_clause = " AND ".join(filters) if filters else None

    if use_fts:
        q = (
            table.search(query_type="hybrid")
            .vector(query_vec)
            .text(query)
            .rerank(_fts_reranker)
        )
    else:
        q = table.search(query_vec)

    if where_clause:
        q = q.where(where_clause, prefilter=True)
    results = q.limit(top_k).to_list()

    output = [
        {
            "chunk_text": r["chunk_text"],
            "feature_name": r["feature_name"],
            "feature_id": r["feature_id"],
            "category": r["category"],
            "contact_team": r["contact_team"],
            "config_source": r["config_source"],
            "status": r["status"],
            "section_type": r["section_type"],
            "section_heading": r["section_heading"],
            "tags": json.loads(r["tags"]),
            # LanceDB uses L2 distance on normalized vectors.
            # cosine_similarity = 1 - (L2_distance² / 2) for unit vectors.
            "score": round(r.get("_relevance_score", 1 - (r.get("_distance", 2) ** 2 / 2)), 4),
            "source_file": r["source_file"],
        }
        for r in results
    ]

    if threshold is not None:
        output = [r for r in output if r["score"] >= threshold]

    return output


if __name__ == "__main__":
    import sys
    model = load_model()
    table = load_table()
    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "How does trip approval work?"
    print(f"Query: {query}\n")
    for i, r in enumerate(search(query, top_k=5, _model=model, _table=table), 1):
        print(f"{i}. [{r['score']}] {r['feature_name']} — {r['section_type']}")
        print(f"   {r['chunk_text'][:120].replace(chr(10), ' ')}...")
        print(f"   Contact: {r['contact_team']} | Category: {r['category']}\n")
