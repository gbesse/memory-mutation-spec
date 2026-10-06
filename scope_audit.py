#!/usr/bin/env python3
"""Check that a requested shared observation scope reached the server."""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

TEXT = {
    "en": ("Memory scope audit", "shared scope forwarded", "shared scope not forwarded"),
    "fr": ("Audit de portée mémoire", "portée partagée transmise", "portée partagée non transmise"),
    "es": ("Auditoría de alcance de memoria", "alcance compartido enviado", "alcance compartido no enviado"),
}


def audit(data):
    if not isinstance(data, dict) or data.get("requested_scope") != "shared":
        raise ValueError("requested_scope must be shared")
    forwarded = data.get("forwarded_scope")
    rows = data.get("observations", [])
    if not isinstance(rows, list):
        raise ValueError("observations must be an array")
    scopes = Counter(row["scope_key"] for row in rows)
    sessions = {row["session_id"] for row in rows}
    return {"ok": forwarded == "shared" or forwarded == [[]], "requested_scope": "shared",
            "forwarded_scope": forwarded or "unknown", "observations": len(rows),
            "scope_count": len(scopes), "session_count": len(sessions),
            "largest_scope": max(scopes.values(), default=0)}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("command", choices=("scope-demo", "check"))
    ap.add_argument("input", type=Path, nargs="?")
    ap.add_argument("--lang", choices=TEXT, default="en")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    try:
        if args.command == "scope-demo":
            data = {"requested_scope": "shared", "forwarded_scope": None,
                    "observations": [{"scope_key": "session:a", "session_id": "a"},
                                     {"scope_key": "session:b", "session_id": "b"}]}
        else:
            if not args.input:
                ap.error("check requires INPUT.json")
            data = json.loads(args.input.read_text())
        result = audit(data)
    except (OSError, ValueError, TypeError, KeyError) as error:
        print(str(error), file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        title, good, bad = TEXT[args.lang]
        print(title)
        print(good if result["ok"] else bad)
        print(f"observations={result['observations']} scopes={result['scope_count']}")
    return 0 if (not result["ok"] if args.command == "scope-demo" else result["ok"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
