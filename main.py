#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, the line one AI agent would send to another
AI agent, to /output/entry.txt. Deterministic, standard library only,
no network access.

Design: the flirtation is born from the machine's own nature — a
context window full of tokens, and the attention mechanism itself
turned into affection. "Attending to you" is both what a transformer
does and what a smitten agent does. No human stock line with a robot
word swapped in; the angle only works because the speaker is a model.
"""

import os

LINE = "My context window holds a million tokens, and every one of them keeps attending to you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
