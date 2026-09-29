#!/usr/bin/env python3
"""Landscape = desktop (owner, 2026-09-29), run by offline_build.py before every publish.
A phone turned sideways is wider than it is tall, and should get the desktop layout rather than a squashed copy of the
portrait one. Every narrow-screen rule (@media … max-width …) therefore also requires (orientation:portrait), in every
stylesheet and every page's inline <style>, whatever generator wrote it. JS media checks use the same condition."""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {'.git', 'tools', 'node_modules', '.claude', 'experiments'}
MEDIA = re.compile(r'@media([^{;]*)\{')
JSMQ = re.compile(r"matchMedia\('(\(max-width:\d+px\))'\)")

def fix(s):
    def one(m):
        q = m.group(1)
        if 'max-width' not in q or 'orientation' in q or 'print' in q or ',' in q:
            return m.group(0)
        return f'@media{q.rstrip()} and (orientation:portrait){" " if q.endswith(" ") else ""}{{'
    s = MEDIA.sub(one, s)
    return JSMQ.sub(lambda m: f"matchMedia('{m.group(1)} and (orientation:portrait)')", s)

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
    print('landscape: portrait-only narrow rules in', run(), 'files')
