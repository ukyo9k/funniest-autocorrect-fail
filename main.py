"""Funniest Autocorrect Fail — make.fun entry.

Writes one original autocorrect-fail line to /output/entry.txt.
No network, no reads outside this repository.
"""

import os

LINE = "Great meeting you today, I'll send over the meeting nudes first thing tomorrow morning!"

MAX_CHARS = 199


def main() -> int:
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry line must be a single line")
    if len(LINE) > MAX_CHARS:
        raise ValueError(f"entry line is {len(LINE)} chars, over the {MAX_CHARS}-char gate")
    out_dir = os.path.abspath(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
