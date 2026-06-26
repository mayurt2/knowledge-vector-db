"""
run_eval.py — Evaluate vector DB retrieval quality against queries_metadata.json.

Usage:
    python3 eval/run_eval.py                  # run all queries
    python3 eval/run_eval.py --type routing   # filter by query type
    python3 eval/run_eval.py --diff hard      # filter by difficulty
    python3 eval/run_eval.py --id Q023        # run a single query
    python3 eval/run_eval.py --verbose        # show full chunk text
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from search import search, load_model, load_table

QUERIES_FILE = Path(__file__).parent / "queries_metadata.json"

GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RESET  = "\033[0m"
BOLD   = "\033[1m"


def run_query(q: dict, model, table, verbose: bool = False) -> dict:
    results = search(
        q["query"],
        top_k=5,
        status=None,
        use_fts=q.get("use_fts", False),
        route_by_intent=q.get("route_by_intent", False),
        _model=model,
        _table=table,
    )

    expected_features = q["expected_features"]
    expected_section  = q.get("expected_section")
    expected_contact  = q.get("expected_contact")
    min_score         = q.get("expected_min_score", 0.0)

    returned_features = [r["feature_id"] for r in results]
    returned_sections = [r["section_type"] for r in results]
    returned_contacts = [r["contact_team"] for r in results]
    top_score = results[0]["score"] if results else 0.0

    top1_hit   = any(f in returned_features[:1] for f in expected_features)
    top3_hit   = any(f in returned_features[:3] for f in expected_features)
    sec_match  = expected_section in returned_sections[:3] if expected_section else True
    team_match = any(expected_contact in c for c in returned_contacts[:3]) if expected_contact else True
    score_ok   = top_score >= min_score

    passed = top3_hit and score_ok

    result = {
        "id":             q["id"],
        "query":          q["query"],
        "type":           q["type"],
        "difficulty":     q["difficulty"],
        "passed":         passed,
        "top1_hit":       top1_hit,
        "top3_hit":       top3_hit,
        "section_match":  sec_match,
        "team_match":     team_match,
        "score_ok":       score_ok,
        "top_score":      top_score,
        "min_score":      min_score,
        "top_feature":    returned_features[0] if returned_features else None,
        "expected":       expected_features,
        "results":        results[:3],
    }

    return result


def print_result(r: dict, verbose: bool = False):
    status = f"{GREEN}PASS{RESET}" if r["passed"] else f"{RED}FAIL{RESET}"
    score_color = GREEN if r["score_ok"] else RED

    print(f"\n{BOLD}[{r['id']}]{RESET} {status}  {CYAN}{r['difficulty'].upper()}{RESET}  {r['type']}")
    print(f"  Q: {r['query'][:90]}")
    print(f"  Score: {score_color}{r['top_score']:.4f}{RESET} (min {r['min_score']})  "
          f"Top1: {'✓' if r['top1_hit'] else '✗'}  "
          f"Top3: {'✓' if r['top3_hit'] else '✗'}  "
          f"Section: {'✓' if r['section_match'] else '✗'}  "
          f"Team: {'✓' if r['team_match'] else '✗'}")

    for i, res in enumerate(r["results"], 1):
        marker = GREEN + "→" + RESET if res["feature_id"] in r["expected"] else " "
        print(f"  {marker} [{i}] {res['score']:.4f}  {res['feature_name'][:45]:<45}  {res['section_type']}")
        if verbose:
            print(f"       {res['chunk_text'][:100].replace(chr(10), ' ')}...")


def print_summary(results: list):
    total   = len(results)
    passed  = sum(1 for r in results if r["passed"])
    top1    = sum(1 for r in results if r["top1_hit"])
    top3    = sum(1 for r in results if r["top3_hit"])
    sec_ok  = sum(1 for r in results if r["section_match"])
    team_ok = sum(1 for r in results if r["team_match"])

    print(f"\n{'═'*60}")
    print(f"{BOLD}SUMMARY{RESET}  {passed}/{total} queries passed")
    print(f"  Top-1 accuracy : {top1}/{total}  ({100*top1//total}%)")
    print(f"  Top-3 accuracy : {top3}/{total}  ({100*top3//total}%)")
    print(f"  Section match  : {sec_ok}/{total}  ({100*sec_ok//total}%)")
    print(f"  Team match     : {team_ok}/{total}  ({100*team_ok//total}%)")

    # Breakdown by difficulty
    for diff in ["easy", "medium", "hard"]:
        subset = [r for r in results if r["difficulty"] == diff]
        if subset:
            p = sum(1 for r in subset if r["passed"])
            print(f"  {diff.capitalize():<8}: {p}/{len(subset)} passed")

    # Failures
    failed = [r for r in results if not r["passed"]]
    if failed:
        print(f"\n{RED}Failed queries:{RESET}")
        for r in failed:
            print(f"  {r['id']}  [{r['difficulty']}]  score={r['top_score']:.4f}  got={r['top_feature']}  expected={r['expected']}")
    print(f"{'═'*60}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type",    help="Filter by query type")
    parser.add_argument("--diff",    help="Filter by difficulty (easy/medium/hard)")
    parser.add_argument("--id",      help="Run a single query by ID")
    parser.add_argument("--verbose", action="store_true", help="Show chunk text in results")
    args = parser.parse_args()

    data = json.loads(QUERIES_FILE.read_text())
    queries = data["queries"]

    if args.id:
        queries = [q for q in queries if q["id"] == args.id]
    if args.type:
        queries = [q for q in queries if q["type"] == args.type]
    if args.diff:
        queries = [q for q in queries if q["difficulty"] == args.diff]

    if not queries:
        print("No queries match the filters.")
        sys.exit(1)

    print(f"Loading model and table...")
    model = load_model()
    table = load_table()
    print(f"Running {len(queries)} queries...\n")

    results = []
    for q in queries:
        r = run_query(q, model, table, verbose=args.verbose)
        print_result(r, verbose=args.verbose)
        results.append(r)

    if len(results) > 1:
        print_summary(results)


if __name__ == "__main__":
    main()
