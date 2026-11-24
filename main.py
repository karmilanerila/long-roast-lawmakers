#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Stdlib only, deterministic: the same bytes on every run.
"""

import os

LINE = (
    "The committee that wants to regulate AI, crypto and the internet just "
    "spent forty minutes trying to convert a Word file to PDF, then printed "
    "it, signed it in pen, scanned it upside down, and asked IT why the PDF "
    "was broken."
)


def main() -> None:
    # One sentence, one file: the whole entry is the LINE constant above.
    text = LINE
    if not (1 <= len(text) <= 320):
        raise SystemExit(f"entry length {len(text)} outside gate 1-320")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(text.encode("utf-8"))
    os.chmod(path, 0o644)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
