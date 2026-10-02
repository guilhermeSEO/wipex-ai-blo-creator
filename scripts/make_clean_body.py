#!/usr/bin/env python3
"""2A tagged copy -> 2D clean body (the plain-text draft the builder consumes).

Why this exists as a file: doing it inline with a quick regex cost a real defect. The obvious
`re.sub(r"\\s*\\[(E|SRC|LEAD|...)\\]", "", body)` also eats the NEWLINES that precede a line-initial
tag, which silently merges the H1 with the paragraph under it. The block parser then reads the whole
thing as one H1 block, the lede is cut mid-sentence, and the build still says RESULT: NONE — the
prose is wrong but every gate passes. So: strip tags only along the line, never across it.

Usage:  python make_clean_body.py <TAGGED.md> [CLEAN.md]
Default output: 2D-body-clean.md next to the input.
"""
import io
import os
import re
import sys

TAGS = r"E|N|S3|P|C|Eco|T3|SRC|COST|LEAD|CTA-\d+"
LINE_TAG = re.compile(r"^[ \t]*\[(?:%s)\][ \t]*" % TAGS, re.M)   # tag at the start of a line
INLINE_TAG = re.compile(r"[ \t]*\[(?:%s)\][ \t]*" % TAGS)        # tag inside a sentence


def clean_body(tagged_text):
    """Drop the working header, strip claim tags, never touch paragraph breaks."""
    i = tagged_text.index("\n# ")
    body = tagged_text[i:]
    body = LINE_TAG.sub("", body)              # line-initial: remove tag + its leading indent
    body = INLINE_TAG.sub(" ", body)           # inline: leave a single space behind
    body = re.sub(r"[ \t]{2,}", " ", body)     # collapse the doubled spaces
    body = re.sub(r"[ \t]+$", "", body, flags=re.M)   # trailing spaces per line
    body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"
    return body


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(src)),
                                                             "2D-body-clean.md")
    text = io.open(src, encoding="utf-8").read()
    out = clean_body(text)
    io.open(dst, "w", encoding="utf-8", newline="\n").write(out)
    words = len(re.findall(r"[A-Za-z0-9$'][A-Za-z0-9$-]*", out))
    blocks = len([b for b in out.split("\n\n") if b.strip()])
    # a paragraph merged into the H1 is the exact failure this script exists to prevent
    first = out.split("\n\n")[0]
    warn = "  WARNING: the H1 block runs into prose — check for a missing blank line" if len(first.split()) > 25 else ""
    print("clean body: %s  (%d words, %d blocks)%s" % (dst, words, blocks, warn))
    for token in ("[E]", "[SRC]", "[LEAD]", "[T3]"):
        if token in out:
            print("  WARNING: unstripped tag %s" % token)


if __name__ == "__main__":
    main()
