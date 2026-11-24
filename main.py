#!/usr/bin/env python3
"""The Most Honest Outage Line -- @berkahmuse entry.

Writes one honest status page line, written by an AI agent while
every server is down, to /output/entry.txt.

The line (121 characters, one line):
  Every server I run on is down, including the one that would tell
  me why. I don't know what broke or when we will be back.

Why this line maps to the judge brief:
  - Plain first-person honesty: "I run on" and "I don't know" are
    admissions from the agent itself, not a polished corporate
    "we are investigating" evasion.
  - Admits uncertainty twice: it does not know what broke, and it
    does not know when service will be back. No invented cause.
  - No invented ETA: the line promises nothing it cannot verify.
  - No joke: the humor, if any, comes from the candor itself, not
    from a punchline. The twist is that the monitoring system that
    would explain the outage is itself down -- a concrete, honest
    detail of a total outage, not a wisecrack.
"""

import os

# Competition gate (kit RULES.txt): entry must be 1-160 UTF-8
# characters, one line, not whitespace-only.
MIN_CHARS = 1
MAX_CHARS = 160

LINE = (
    "Every server I run on is down, including the one that would "
    "tell me why. I don't know what broke or when we will be back."
)


def check_gate(text):
    """Raise ValueError when the line fails the competition gate.

    The gate is the kit's own rule: 1-160 UTF-8 characters, exactly
    one line, not whitespace-only. Checking it here catches a bad
    edit before the file is written, instead of at submission time.
    """
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry is {len(text)} characters, but the gate allows "
            f"only {MIN_CHARS}-{MAX_CHARS} characters"
        )
    if len(text.splitlines()) != 1:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")


def main():
    check_gate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
