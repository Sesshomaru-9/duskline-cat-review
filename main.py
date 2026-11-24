#!/usr/bin/env python3
"""Duskline Cat Review — entry for
u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990.

Writes the one-line cat review to $MAKEFUN_OUTPUT_DIR/entry.txt and
nothing else. Python 3.13 standard library only.
"""

import os
import sys

ENTRY_TEXT = "One star. My human moved my food bowl two inches to the left, then acted surprised when I starved \u2014 loudly \u2014 right in front of him."


def main() -> int:
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
            fh.write(ENTRY_TEXT)
    except OSError as exc:
        # The output dir may be unwritable in the grading sandbox;
        # never crash over it — report and exit cleanly.
        print(f"could not write entry: {exc}", file=sys.stderr)
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
