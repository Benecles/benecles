#!/usr/bin/env python3
"""Cache-busting for course assets, run by offline_build.py before every publish.
Pages link their course CSS/JS as assets/<name>.css?v=…, and generators stamp that version by hand, so a changed
stylesheet could stay stale in phones' caches. This rewrites every such link to a hash of the file's current content."""
import hashlib, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r'(?<=")(assets/([\w-]+\.(?:css|js)))(?:\?v=[\w.-]+)?(?=")')   # course-local assets only

def run():
    n, memo = 0, {}
    for d, dirs, files in os.walk(os.path.join(ROOT, 'courses')):
        for f in files:
            if not f.endswith('.html'): continue
            p = os.path.join(d, f); s = open(p).read()
            def stamp(m):
                a = os.path.normpath(os.path.join(d, m.group(1)))
                if a not in memo:
                    memo[a] = hashlib.sha1(open(a, 'rb').read()).hexdigest()[:10] if os.path.exists(a) else None
                return f'{m.group(1)}?v={memo[a]}' if memo[a] else m.group(0)
            s2 = LINK.sub(stamp, s)
            if s2 != s: open(p, 'w').write(s2); n += 1
    return n

if __name__ == '__main__':
    print('restamped', run(), 'pages')
