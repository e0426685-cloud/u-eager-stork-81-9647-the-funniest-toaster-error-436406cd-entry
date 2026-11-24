#!/usr/bin/env python3
"""make.fun entry: The Funniest Toaster Error Message.

Writes a single line (at most 120 characters) to /output/entry.txt:
the error message a kitchen toaster shows its owner.

Standard library only. No third-party imports.
"""

import os

ENTRY = "E12: 12,000 slices toasted. Zero thank-yous. Your bread is ready anyway."


def validate(text):
    """Check the entry text meets the bounty limits before writing it.

    The message must be exactly one line, non-empty, and no longer than
    120 characters. Anything outside those bounds would be a broken
    submission, so fail loudly instead of writing bad output.
    """
    assert isinstance(text, str), "entry text must be a string"
    assert 1 <= len(text) <= 120, "entry text must be 1-120 characters"
    assert "\n" not in text and "\r" not in text, "entry text must be a single line"


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    # Plain open() + explicit chmod 644: the grader runs as a different
    # user, so the file must be world-readable (never tempfile.mkstemp,
    # which forces mode 0600).
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
