#!/usr/bin/env python3
# Emit the single meeting joke as /output/entry.txt; standard library only.

from pathlib import Path

JOKE = "Someone shared their screen to show us the email the meeting was about."
TARGET = Path("/output/entry.txt")


def run():
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    run()
