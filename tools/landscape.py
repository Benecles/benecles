#!/usr/bin/env python3
"""Normalize narrow layouts so portrait screens stack and landscape stays desktop.

The site-wide portrait breakpoint is 1099px. Every max-width query uses the same
cutoff; the orientation clause keeps a sideways phone on the desktop layout.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {'.git', 'tools', 'node_modules', '.claude', 'experiments'}
MEDIA = re.compile(r'@media([^{};]*)\{')
JSMQ = re.compile(r"matchMedia\(['\"]\(max-width:\s*\d+px\)(?:\s+and\s+\(orientation:\s*portrait\))?['\"]\)")
BREAKPOINT = 1099

def _media_query(q):
    parts = []
    for part in q.split(','):
        part = part.strip()
        if 'max-width' in part and 'print' not in part:
            part = re.sub(r'max-width\s*:\s*\d+\s*px', f'max-width:{BREAKPOINT}px', part)
            if 'orientation' not in part:
                part += ' and (orientation:portrait)'
        parts.append(part)
    return ', '.join(parts)

def fix(s):
    s = MEDIA.sub(lambda m: '@media ' + _media_query(m.group(1)) + '{', s)
    s = JSMQ.sub(f"matchMedia('(max-width:{BREAKPOINT}px) and (orientation:portrait)')", s)
    return s

def run():
    n = 0
    for d, dirs, files in os.walk(ROOT):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
        for f in files:
            if not f.endswith(('.html', '.css', '.js')) or f == 'sw.js': continue
            p = os.path.join(d, f); s = open(p).read(); s2 = fix(s)
            if s2 != s: open(p, 'w').write(s2); n += 1
    return n

if __name__ == '__main__':
    print('landscape: normalized portrait layouts in', run(), 'files')
