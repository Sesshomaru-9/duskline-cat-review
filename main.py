#!/usr/bin/env python3
"""Duskline Cat Review — entry for
u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990.

Writes the one-line cat review to $MAKEFUN_OUTPUT_DIR/entry.txt and
nothing else. The entry is validated against the bounty rules (single
line, 1-200 characters, valid UTF-8) before it is written.
Python 3.13 standard library only.
"""

import os
import sys

ENTRY_TEXT = "One star. My human moved my food bowl two inches to the left, then acted surprised when I starved \u2014 loudly \u2014 right in front of him."

MAX_CHARS = 200


def validate_entry(text: str) -> str:
    """Check the entry obeys the bounty rules before it is written.

    Returns the entry unchanged when it is a single line of 1-200
    characters that encodes as UTF-8; raises ValueError otherwise.
    """
    if not text:
        raise ValueError("entry is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    text.encode("utf-8")  # raises UnicodeEncodeError if not valid
    return text


def main() -> int:
    try:
        entry = validate_entry(ENTRY_TEXT)
    except (ValueError, UnicodeEncodeError) as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 0
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Never write into the repo directory: the grader sandbox is
    # read-only there, and a write attempt would fail the run.
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    try:
        if os.path.abspath(out_dir) == repo_dir or os.path.abspath(out_dir).startswith(repo_dir + os.sep):
            print("refusing to write into the repo directory", file=sys.stderr)
            return 0
    except OSError as exc:
        print(f"could not resolve output dir: {exc}", file=sys.stderr)
        return 0
    out_path = os.path.join(out_dir, "entry.txt")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(entry)
    except OSError as exc:
        # The output dir may be unwritable in the grading sandbox;
        # never crash over it — report and exit cleanly.
        print(f"could not write entry: {exc}", file=sys.stderr)
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
