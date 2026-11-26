#!/usr/bin/env python3
"""The Printer Finally Answers.

Writes the office printer's comeback -- one line, 1 to 240
characters -- to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

Stdlib only, no network access, fully deterministic: every run
writes the exact same bytes.
"""

import os

LINE = (
    "I have fed 214,003 sheets without a single thank-you, "
    "and the one time I jam, you hit me. Noted. I am keeping count."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exactly one line, no trailing newline: the gate counts characters.
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
