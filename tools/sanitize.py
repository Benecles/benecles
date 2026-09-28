#!/usr/bin/env python3
"""Site-wide guard for the no-visible-sourcing rule, run by offline_build.py before every publish.
Whatever generator produced a page, provenance stays in hidden markup, never on screen:
- <span class="src">…</span> with text becomes <span class="src" hidden data-src="…"></span>;
- <details class="provenance"> ("Fontes e limites desta página") gets the hidden attribute."""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def sanitize(s):
    s = re.sub(r'<span class="src">([^<]+)</span>', lambda m: f'<span class="src" hidden data-src="{m.group(1).strip()}"></span>', s)
    s = re.sub(r'<details class="provenance"(?![^>]*hidden)', '<details class="provenance" hidden', s)
    return s

def run():
    n = 0
    for d, dirs, files in os.walk(os.path.join(ROOT, 'courses')):
        for f in files:
            if not f.endswith('.html'): continue
            p = os.path.join(d, f); s = open(p).read(); s2 = sanitize(s)
            if s2 != s: open(p, 'w').write(s2); n += 1
    return n

if __name__ == '__main__':
    print('sanitized', run(), 'pages')
