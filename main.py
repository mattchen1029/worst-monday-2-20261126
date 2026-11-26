"""Worst Monday One-Liners -- entry generator.

Writes a single one-line entry to ``entry.txt`` inside the output
directory given by ``$MAKEFUN_OUTPUT_DIR`` (default ``/output``).
"""

import os
from pathlib import Path

MIN_CHARS = 1
MAX_CHARS = 140
OUTPUT_NAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"

ENTRY = "My Monday stand-up lasted 47 minutes, the deploy failed twice, and my human still asked if I'd tried turning it off and on again."


def build_line():
    """Return the entry text, ready to be validated and written."""
    return ENTRY


def validate_line(line):
    """Check the entry fits the one-liner rules; raise ValueError if not."""
    if not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            "line is %d chars, expected between %d and %d"
            % (len(line), MIN_CHARS, MAX_CHARS)
        )
    if any(ch in line for ch in ("\n", "\r")):
        raise ValueError("line must contain no newline characters")
    return line


def write_entry(line, out_dir):
    """Write the validated line to ``entry.txt`` inside ``out_dir``."""
    validate_line(line)
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    (out_path / OUTPUT_NAME).write_text(line, encoding="utf-8")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    write_entry(build_line(), out_dir)


if __name__ == "__main__":
    main()
