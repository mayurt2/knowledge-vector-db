"""
sync.py — Hard sync and soft sync for the knowledge vector DB.

Hard sync: drop and rebuild the entire LanceDB table from all .md files.
Soft sync: only re-embed files that are new, modified, or deleted since last sync.

A manifest file (.sync_manifest.json) tracks per-file modification times.

CLI:
    python3 sync.py --hard    # full rebuild
    python3 sync.py --soft    # incremental
    python3 sync.py --status  # show pending changes (dry-run)
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict

import lancedb
from sentence_transformers import SentenceTransformer

from ingest import parse_file, KNOWLEDGE_DIR, DB_PATH, TABLE_NAME, EMBED_MODEL
from schema import KnowledgeChunk

MANIFEST_PATH = Path(".sync_manifest.json")


# ── Manifest helpers ──────────────────────────────────────────────────────────

def _scan_files() -> Dict[str, float]:
    """Return {filename: mtime} for all .md files in KNOWLEDGE_DIR."""
    return {
        p.name: p.stat().st_mtime
        for p in sorted(KNOWLEDGE_DIR.glob("*.md"))
    }


def _load_manifest() -> dict:
    if not MANIFEST_PATH.exists():
        return {"last_sync": None, "files": {}}
    return json.loads(MANIFEST_PATH.read_text())


def _write_manifest(files: Dict[str, float]) -> None:
    manifest = {
        "last_sync": datetime.utcnow().isoformat(),
        "files": files,
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2))


# ── Public API ────────────────────────────────────────────────────────────────

def hard_sync() -> None:
    """Drop and rebuild the entire LanceDB table from all .md files."""
    from ingest import ingest_all
    ingest_all()
    _write_manifest(_scan_files())
    print("Manifest updated.")


def soft_sync() -> dict:
    """
    Incrementally sync only changed files.

    Returns:
        {"new": int, "modified": int, "deleted": int, "unchanged": int}
    """
    manifest   = _load_manifest()
    tracked    = manifest.get("files", {})     # {filename: mtime}
    current    = _scan_files()                 # {filename: mtime}

    deleted  = set(tracked) - set(current)
    new      = set(current) - set(tracked)
    modified = {
        f for f in current
        if f in tracked and current[f] != tracked[f]
    }
    unchanged = len(current) - len(new) - len(modified)

    result = {
        "new": len(new),
        "modified": len(modified),
        "deleted": len(deleted),
        "unchanged": unchanged,
    }

    if not (new or modified or deleted):
        print("Nothing to sync — all files are up to date.")
        _write_manifest(current)
        return result

    db = lancedb.connect(DB_PATH)

    # If table doesn't exist yet, fall back to full ingest
    if TABLE_NAME not in db.list_tables():
        print("Table not found — running full ingest instead.")
        hard_sync()
        return result

    table = db.open_table(TABLE_NAME)

    # Remove chunks belonging to deleted or modified files
    to_remove = deleted | modified
    if to_remove:
        for fname in to_remove:
            safe = fname.replace("'", "''")
            table.delete(f"source_file = '{safe}'")
            print(f"  Removed chunks for: {fname}")

    # Re-embed new and modified files
    to_ingest = new | modified
    if to_ingest:
        model = SentenceTransformer(EMBED_MODEL)
        all_chunks = []
        for fname in sorted(to_ingest):
            chunks = parse_file(KNOWLEDGE_DIR / fname)
            all_chunks.extend(chunks)
            print(f"  Parsed: {fname} ({len(chunks)} chunks)")

        texts = [c["chunk_text"] for c in all_chunks]
        embeddings = model.encode(
            texts, batch_size=64, show_progress_bar=True, normalize_embeddings=True
        )
        rows = [
            KnowledgeChunk(**{**chunk, "vector": vec.tolist()})
            for chunk, vec in zip(all_chunks, embeddings)
        ]
        table.add(rows)
        table.create_fts_index("chunk_text", replace=True)
        print(f"  Added {len(rows)} chunks from {len(to_ingest)} files.")

    _write_manifest(current)

    print(
        f"\nSoft sync complete: "
        f"{result['new']} new, {result['modified']} modified, "
        f"{result['deleted']} deleted, {result['unchanged']} unchanged."
    )
    return result


def get_sync_status() -> dict:
    """
    Return current sync state without making any changes.

    Returns:
        {last_sync, tracked_files, disk_files, pending_changes, detail}
    """
    manifest = _load_manifest()
    tracked  = manifest.get("files", {})
    current  = _scan_files()

    deleted  = set(tracked) - set(current)
    new      = set(current) - set(tracked)
    modified = {
        f for f in current
        if f in tracked and current[f] != tracked[f]
    }

    return {
        "last_sync":      manifest.get("last_sync"),
        "tracked_files":  len(tracked),
        "disk_files":     len(current),
        "pending_changes": len(new) + len(modified) + len(deleted),
        "detail": {
            "new":      sorted(new),
            "modified": sorted(modified),
            "deleted":  sorted(deleted),
        },
    }


# ── CLI ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if "--hard" in sys.argv:
        print("Running hard sync (full rebuild)...")
        hard_sync()

    elif "--soft" in sys.argv:
        print("Running soft sync (incremental)...")
        soft_sync()

    elif "--status" in sys.argv:
        status = get_sync_status()
        print(f"Last sync    : {status['last_sync'] or 'Never'}")
        print(f"Tracked files: {status['tracked_files']}")
        print(f"Files on disk: {status['disk_files']}")
        print(f"Pending      : {status['pending_changes']} changes")
        if status["pending_changes"]:
            d = status["detail"]
            if d["new"]:      print(f"  New      : {d['new']}")
            if d["modified"]: print(f"  Modified : {d['modified']}")
            if d["deleted"]:  print(f"  Deleted  : {d['deleted']}")

    else:
        print("Usage: python3 sync.py [--hard | --soft | --status]")
        sys.exit(1)
