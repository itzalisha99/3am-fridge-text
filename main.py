#!/usr/bin/env python3
"""The 3AM Fridge Text — one line a smart fridge texts its owner at 3am.

Writes the entry to /output/entry.txt.
"""

import os

ENTRY = "You keep opening me like the answer will change. It's still just condiments and regret."


def validate(text):
    """Gate check mirroring the bounty gate: 1-140 chars, UTF-8, one line,
    not whitespace-only. Returns True only if the entry is submittable."""
    if not isinstance(text, str):
        return False
    if not text or text.strip() == "":
        return False
    if len(text) != len(text.strip()):
        return False  # no padding around the entry
    if "\n" in text or "\r" in text:
        return False  # must be a single line
    if len(text) > 140:
        return False
    text.encode("utf-8")  # must be valid UTF-8
    return True


def main():
    if not validate(ENTRY):
        raise SystemExit("entry fails the 1-140 char gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # round-trip check: what we wrote must read back byte-identical
    with open("/output/entry.txt", encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise SystemExit("written entry does not match")


if __name__ == "__main__":
    main()
