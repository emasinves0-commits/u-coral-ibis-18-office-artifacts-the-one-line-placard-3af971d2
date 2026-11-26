#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest — make.fun entry.

Writes one museum placard to /output/entry.txt: a single line, at most
180 characters, labelling an ordinary office object as an ancient
artifact, in a dry curator's voice.

The placard is fixed text, chosen by a full selection funnel (113-model
generation pool, lexicographic criteria scoring, ensemble pre-filter,
glm-5.3-flash duel) and written here verbatim. Deterministic: the same
bytes on every run. No network, no input, no randomness.
"""

import os

# Final entry — funnel winner (see placard-report.md):
# - 37 unique candidates from 19/113 working models (router 429 storm)
# - shortlist 12 by lexicographic C1->C5 scoring
# - ensemble panel EMPTY 0/5 (valid outcome, fallback to own scoring)
# - glm-5.3-flash duel via judge-call.py --priority high:
#   ceiling tile vs badge reader 2-0 (margin 2+2)
#   ceiling tile vs binder clip 2-0 (margin 3+2)
ENTRY = "Ceiling tile, 2019\u20132024: stained by a chronic leak interpreted as a celestial map until maintenance drained the roof."

MAX_CHARS = 180


def main() -> None:
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-180")
    if not ENTRY.strip():
        raise ValueError("entry is blank")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
