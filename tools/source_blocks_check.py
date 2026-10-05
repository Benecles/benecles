#!/usr/bin/env python3
"""Check that each source block's displayed original occurs in its local source.

The private source corpus is supplied at run time and is never copied to this
public repository. Example:
  python3 tools/source_blocks_check.py --source-root /path/to/sources-public
"""

from __future__ import annotations

import argparse
import html
import re
from html.parser import HTMLParser
from pathlib import Path
import sys


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


class BlockParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.block_file: str | None = None
        self.block_depth = 0
        self.in_original = False
        self.in_translation = False
        self.current: list[str] = []
        self.blocks: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_map = dict(attrs)
        classes = (attrs_map.get("class") or "").split()
        if "source-block" in classes:
            self.block_file = attrs_map.get("data-source-file")
            self.block_depth = len(self.stack) + 1
        if self.block_file and tag == "blockquote" and not self.in_translation:
            self.in_original = True
            self.current = []
        if self.block_file and "source-block__translation" in classes:
            self.in_translation = True
            self.in_original = False
        self.stack.append(tag)

    def handle_endtag(self, tag: str) -> None:
        if self.in_original and tag == "blockquote":
            self.blocks.append((self.block_file or "", "".join(self.current)))
            self.in_original = False
            self.current = []
        if self.in_translation and tag in ("div", "section"):
            self.in_translation = False
        if self.stack:
            self.stack.pop()
        if self.block_depth and len(self.stack) + 1 == self.block_depth:
            self.block_file = None
            self.block_depth = 0

    def handle_data(self, data: str) -> None:
        if self.in_original and not self.in_translation:
            self.current.append(data)


def read_source(path: Path) -> str:
    raw = path.read_bytes()
    for encoding in ("utf-8", "cp1252", "latin-1"):
        try:
            text = raw.decode(encoding)
            break
        except UnicodeDecodeError:
            continue
    parser = TextExtractor()
    parser.feed(text)
    return normalize(html.unescape("".join(parser.parts)))


def check(page_root: Path, source_root: Path) -> int:
    failures: list[str] = []
    checked = 0
    for page in sorted(page_root.rglob("*.html")):
        parser = BlockParser()
        parser.feed(page.read_text(encoding="utf-8"))
        for source_file, quote in parser.blocks:
            checked += 1
            if not source_file:
                failures.append(f"{page}: source block is missing data-source-file")
                continue
            source_path = (source_root / source_file).resolve()
            try:
                source_path.relative_to(source_root.resolve())
            except ValueError:
                failures.append(f"{page}: source path escapes source root: {source_file}")
                continue
            if not source_path.is_file():
                failures.append(f"{page}: source file not found: {source_file}")
                continue
            if normalize(quote) not in read_source(source_path):
                failures.append(f"{page}: quoted text does not match {source_file} (whitespace-normalized)")

    if failures:
        print("\n".join(f"FAIL {item}" for item in failures))
        return 1
    print(f"PASS: {checked} source block(s) match local source text (whitespace-normalized)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", required=True, type=Path)
    parser.add_argument("--page-root", type=Path, default=Path("."))
    args = parser.parse_args()
    if not args.source_root.is_dir():
        print(f"FAIL source root is not a directory: {args.source_root}", file=sys.stderr)
        return 2
    return check(args.page_root, args.source_root)


if __name__ == "__main__":
    raise SystemExit(main())
