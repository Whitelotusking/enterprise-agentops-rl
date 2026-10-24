"""Read-only inventory of the public tau-bench banking_knowledge data.

No task prompts, answers or private records are printed or uploaded.
"""

import argparse
import hashlib
import json
from pathlib import Path


def inspect_data(repository: Path) -> int:
    base = repository.resolve() / "data" / "tau2" / "domains" / "banking_knowledge"
    if not base.is_dir():
        print(f"ERROR: banking_knowledge directory not found: {base}")
        return 1

    for name in ("db.json", "tasks.json"):
        path = base / name
        if not path.is_file():
            print(f"ERROR: missing {path}")
            return 1
        raw = path.read_bytes()
        parsed = json.loads(raw)
        print(
            f"{name}: {len(raw):,} bytes, JSON={type(parsed).__name__}, "
            f"SHA256={hashlib.sha256(raw).hexdigest()}"
        )

    docs = base / "documents"
    if not docs.is_dir():
        print("ERROR: documents directory missing")
        return 1

    documents = [p for p in docs.rglob("*") if p.is_file()]
    print(f"documents: {len(documents)} files (recursive)")
    print("Data inspected read-only. No benchmark expected answers exported.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inspect public tau-bench data without exporting content")
    parser.add_argument("--repo", type=Path, required=True, help="Path to the tau2-bench source repository")
    args = parser.parse_args()
    raise SystemExit(inspect_data(args.repo))
