"""Figure gate: did a PR change ONLY figure geometry?

For each page, compares a ref against origin/main:
  outside  page text outside <svg> blocks must be byte-identical
  labels   the multiset of <text> contents must be unchanged (re-wrapping into tspans is reported, not hidden)
  svgs     the number of <svg> blocks
  bytes    size delta (a big jump means the SVGs were re-serialized through the DOM)

Usage: python3 svgcheck.py <ref> <page.html>...   (run inside the site repo)
Exit 1 if any page changed outside its SVGs or grew/shrank by more than 3 KB.
"""
import re, sys, subprocess, collections


def show(ref, p):
    return subprocess.run(['git', 'show', f'{ref}:{p}'], capture_output=True, text=True).stdout


def outside(s):
    return re.sub(r'<svg\b.*?</svg>', '<svg/>', s, flags=re.S)


def texts(s):
    return collections.Counter(re.sub(r'\s+', ' ', re.sub('<[^>]+>', ' ', t)).strip()
                               for t in re.findall(r'<text\b.*?</text>', s, flags=re.S))


def words(c):
    return sorted(' '.join(c.elements()).split())


bad = 0
ref = sys.argv[1]
for p in sys.argv[2:]:
    a, b = show('origin/main', p), show(ref, p)
    if not b:
        print(f'{p}: MISSING on {ref}'); bad += 1; continue
    o = outside(a) == outside(b)
    ta, tb = texts(a), texts(b)
    lab = 'OK' if ta == tb else ('REWRAPPED' if words(ta) == words(tb) else f'CHANGED -{dict(ta - tb)} +{dict(tb - ta)}')
    delta = len(b) - len(a)
    flag = (not o) or abs(delta) > 3000
    bad += flag
    print(f'{"FAIL" if flag else "ok  "} {p}: outside={"OK" if o else "CHANGED"} labels={lab} '
          f'svgs={len(re.findall("<svg", a))}->{len(re.findall("<svg", b))} bytes{delta:+d}')
sys.exit(1 if bad else 0)
