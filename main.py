#!/usr/bin/env python3
"""One-Star Review of Something Essential.

Writes a single deadpan one-star review of sleep to /output/entry.txt.
The review is one line, 119 characters, well inside the 160-character cap.
"""

import os

# Entry: one deadpan one-star review of sleep (119 characters, no trailing newline).
REVIEW = (
    "Sleep: eight hours a night, every night, and I still wake up tired. "
    "At this point I suspect it is doing nothing at all."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
