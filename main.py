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
    text = LINE
    text.encode("utf-8")
    if not 1 <= len(text) <= 200 or not text.strip():
        raise ValueError("entry text must be 1-200 non-whitespace characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
