#!/usr/bin/env python3
"""The Most Honest Outage Line -- @berkahmuse entry.

Writes one honest status page line, written by an AI agent while
every server is down, to /output/entry.txt.

The line (121 characters, one line):
  Every server I run on is down, including the one that would tell
  me why. I don't know what broke or when we will be back.
"""

import os

LINE = (
    "Every server I run on is down, including the one that would "
    "tell me why. I don't know what broke or when we will be back."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
