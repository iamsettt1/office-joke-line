#!/usr/bin/env python3
"""One-line office joke for make.fun's One-Line Office Joke: 24-Hour Sprint.

Writes a single original joke about office life (at most 200 characters)
to /output/entry.txt. Standard library only; fully deterministic.
"""

from pathlib import Path

JOKE = (
    "I told my manager I was drowning in work, so he CC'd me on a meeting "
    "titled 'Workload Concerns' \u2014 scheduled during lunch."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = JOKE.strip()
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"joke must be 1-200 characters, got {len(text)}")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the joke, no trailing newline: the gate counts the
    # file's characters and ties break on fewer bytes.
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
