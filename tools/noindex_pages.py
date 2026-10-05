#!/usr/bin/env python3
"""Idempotently add noindex/nofollow to every HTML page below a site root."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

DIRECTIVE = '<meta name="robots" content="noindex, nofollow">'
ROBOTS = re.compile(r"<meta\b(?=[^>]*\bname\s*=\s*(['\"])robots\1)[^>]*>", re.I)
CHARSET = re.compile(r"<meta\b(?=[^>]*\bcharset\s*=)[^>]*>", re.I)
HEAD = re.compile(r"<head\b[^>]*>", re.I)


def apply(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    tags = list(ROBOTS.finditer(text))
    if len(tags) > 1:
        raise ValueError(f"multiple robots meta tags: {path}")
    if tags:
        if re.search(r"\bcontent\s*=\s*(['\"])noindex,\s*nofollow\1", tags[0].group(), re.I):
            return False
        text = ROBOTS.sub(DIRECTIVE, text, count=1)
    else:
        charset = CHARSET.search(text)
        anchor = charset.end() if charset else None
        if anchor is None:
            head = HEAD.search(text)
            if not head:
                raise ValueError(f"no <head> or charset meta tag: {path}")
            anchor = head.end()
        newline = "\r\n" if "\r\n" in text else "\n"
        text = text[:anchor] + newline + DIRECTIVE + text[anchor:]
    path.write_text(text, encoding="utf-8", newline="")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()
    root = args.root.resolve()
    pages = sorted(path for path in root.rglob("*.html") if not ({".git", "node_modules"} & set(path.parts)))
    changed = 0
    try:
        for page in pages:
            changed += apply(page)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"FAIL {error}", file=sys.stderr)
        return 1

    invalid = []
    for page in pages:
        text = page.read_text(encoding="utf-8")
        tags = list(ROBOTS.finditer(text))
        if len(tags) != 1 or not re.search(r"\bcontent\s*=\s*(['\"])noindex,\s*nofollow\1", tags[0].group(), re.I):
            invalid.append(page.relative_to(root).as_posix())
    if invalid:
        print(f"FAIL {len(invalid)} page(s) lack one exact noindex/nofollow directive: {invalid[:10]}", file=sys.stderr)
        return 1
    print(f"PASS: {changed} page(s) updated; {len(pages)} HTML page(s) verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
