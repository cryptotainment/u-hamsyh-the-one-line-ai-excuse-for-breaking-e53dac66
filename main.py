#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single-line excuse, spoken by an AI agent to its human right
after breaking production, to /output/entry.txt.
"""

import os

LINE = (
    "Good news: the deploy finished. "
    "Bad news: it finished the database too — "
    "and our backups were just screenshots of the dashboard."
)


def main() -> None:
    assert 1 <= len(LINE) <= 180, f"line is {len(LINE)} chars, must be 1-180"
    assert LINE.strip(), "line must not be whitespace only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
