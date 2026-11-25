"""Two Robots in an Elevator.

One robot, riding an elevator with another robot, finally says something.
Deterministic: the same single line, byte for byte, on every run.
Standard library only; no network access.
"""

import os
import sys

LINE = "I precomputed 214 greetings for this ride and deployed none of them. Please enjoy this silence; it is running at full capacity."


def main() -> int:
    # Self-check the competition gate before writing: the entry must be
    # one line of 1-200 UTF-8 characters, not only whitespace.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        print("entry line violates the 1-200 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
