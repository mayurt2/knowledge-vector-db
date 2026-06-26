# knowledge-vector-db

LanceDB-based vector knowledge store for semantic feature search.
100 feature `.md` files → 1310 chunks → 384-dim embeddings (sentence-transformers/all-MiniLM-L6-v2).

## Setup (run once after cloning)

```bash
bash setup.sh
```

Creates a Python venv, installs all dependencies, and runs the initial full ingest into LanceDB.

## Start the apps

```bash
bash start.sh
```

- **Feature Knowledge Retrieval Data** → http://localhost:8501
- **Vector Data Visualization Dashboard** → http://localhost:8502

Stop both with `Ctrl+C`.

## Re-sync knowledge after adding or editing .md files

```bash
python3 sync.py --hard    # full drop-and-rebuild (safe, always correct)
python3 sync.py --soft    # incremental — only re-embeds changed/new/deleted files
python3 sync.py --status  # show pending changes without syncing
```

Or use the **🔄 Sync** tab in the dashboard at http://localhost:8502.

## Adding new knowledge files

1. Drop `.md` files into `knowledge_files/`
2. Run `python3 sync.py --soft` (or hard if unsure)
3. Restart the apps if already running

## Key files

| File | Purpose |
|---|---|
| `knowledge_files/` | Source `.md` knowledge files — one per feature |
| `schema.py` | LanceDB table schema (`KnowledgeChunk`, `Vector(384)`) |
| `ingest.py` | Full ingest pipeline — parses, chunks, embeds, stores |
| `sync.py` | `hard_sync()` + `soft_sync()` + manifest tracking |
| `search.py` | `search(query, ...)` API — consumed by the Java backend |
| `app.py` | Streamlit search UI (port 8501) |
| `explorer.py` | Streamlit visualization + sync UI (port 8502) |
| `lancedb_store/` | Generated DB (gitignored — created by setup/sync) |

## search() API for the Java backend

The Java service calls `search.py` directly (e.g. via a Python subprocess or HTTP wrapper).

```
search(
    query: str,           # natural-language question
    top_k: int = 5,       # number of results
    threshold: float = None,  # min cosine similarity (0–1); None = no filter
    category: str = None,     # filter e.g. "Approvals"
    contact_team: str = None, # "Onboarding Team" or "Tech Team"
    section_types: list = None,
    status: str = None,   # "live" | "in-development" | None (all)
    use_fts: bool = False # True for exact technical key lookups
) -> List[dict]

Returns:
  chunk_text, feature_name, feature_id, category, contact_team,
  config_source, status, section_type, section_heading, tags,
  score (cosine similarity 0–1), source_file
```

## Troubleshooting

- **"No such table: knowledge"** — run `python3 ingest.py` or `python3 sync.py --hard`
- **Low relevance scores** — scores are cosine similarities (0–1); threshold default is 0.3
- **Stale results after file changes** — run `python3 sync.py --soft`
- **Port already in use** — kill with `pkill -f streamlit` then `bash start.sh`
