#!/usr/bin/env python3
"""Rewrite path references after moving folders, so briefs, ledgers and notes keep pointing at the right place.

    python3 rewrite_paths.py MAP.json ROOT [ROOT ...] [--dry-run]

MAP.json is a list of [old, new] pairs of path fragments, e.g.
    [["Desktop/New moodle scrape", "Desktop/UFRGS 2026-2/Controle de Constitucionalidade/03 Moodle/2026-09-20 scrape"]]
Use fragments that start at a stable anchor such as "Desktop/" or "Documents/", which covers both
"~/Desktop/..." and "/Users/<name>/Desktop/...".

- Matches NFC and NFD spellings (macOS paths often arrive decomposed).
- Replaces longest fragments first, in a single pass, so a new path is never re-rewritten.
- Only edits text files (.md .txt .csv .tsv .json .toml .yaml .yml .py .sh .js .html) and skips .git, node_modules and
  anything inside git-tracked repos, unless --include-git is given.
- Prints every file it changed, with its count.
"""
import json, os, re, subprocess, sys, unicodedata

EXT = ('.md', '.txt', '.csv', '.tsv', '.json', '.toml', '.yaml', '.yml', '.py', '.sh', '.js', '.html')

def tracked(path):
    d = os.path.dirname(path)
    r = subprocess.run(['git', '-C', d, 'ls-files', '--error-unmatch', path], capture_output=True)
    return r.returncode == 0

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    dry, inc_git = '--dry-run' in sys.argv, '--include-git' in sys.argv
    if len(args) < 2:
        print(__doc__); sys.exit(2)
    pairs = {}
    for old, new in json.load(open(args[0])):
        for form in ('NFC', 'NFD'):
            pairs[unicodedata.normalize(form, old)] = unicodedata.normalize(form, new)
    rx = re.compile('|'.join(re.escape(k) for k in sorted(pairs, key=len, reverse=True)))
    total = files = 0
    for root in args[1:]:
        for d, dirs, fs in os.walk(os.path.expanduser(root)):
            dirs[:] = [x for x in dirs if x not in ('.git', 'node_modules', '.venv')]
            for f in fs:
                if not f.endswith(EXT):
                    continue
                p = os.path.join(d, f)
                try:
                    s = open(p, encoding='utf-8', errors='surrogateescape').read()
                except OSError:
                    continue
                n = len(rx.findall(s))
                if not n or (not inc_git and tracked(p)):
                    continue
                files += 1; total += n
                print(f'{n:5d}  {p}')
                if not dry:
                    open(p, 'w', encoding='utf-8', errors='surrogateescape').write(rx.sub(lambda m: pairs[m.group(0)], s))
    print(f'{"would replace" if dry else "replaced"} {total} references in {files} files')

if __name__ == '__main__':
    main()
