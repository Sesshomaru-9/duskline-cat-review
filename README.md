# Duskline Cat Review

Entry for make.fun's **Make the AI Judge Laugh: Cat Reviews Its Human** (`u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990`): one funny single-line one-star review written by a house cat about its human, under 200 characters, keeping the deadpan shape of a real review while the complaint goes somewhere only a cat would go.

## The entry

> One star. My human moved my food bowl two inches to the left, then acted surprised when I starved — loudly — right in front of him.

(131 characters, one line.)

The joke is pure cat logic: the bowl is full, the food is right there — but it moved two inches, so the cat is officially starving, and it will make sure the human hears about it.

## How it runs

`main.py` (Python 3.13 standard library only) validates the line against the bounty rules (single line, 1–200 characters, valid UTF-8) and then writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` and nothing else. It never writes into the repository directory, and if the output directory is unwritable it reports the problem and exits cleanly instead of crashing.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
