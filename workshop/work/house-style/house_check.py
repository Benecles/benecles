#!/usr/bin/env python3
"""House-presence check for rebuilt lessons (PROC-R2 bar, CEO 07/10). marks_lint and slop_gate pass on ABSENCE
(no marks = no mark errors, no quotes = no quote errors); this one fails when the house layer isn't there.
  python3 work/house-style/house_check.py PAGE.html [...]   exit 1 on any FAIL
FAIL: casa.css/casa.js not loaded · <4 .fonte blocks · no doctrine block (plain .fonte = book/doctrine, ink bar)
      · <2 figures drawn in SVG · <3 inline marks (.held/.limit/.term) · a .term without data-def
WARN: one statute article named >5 times in our prose (outside .fonte): restating instead of quoting once."""
import re, sys, collections

def check(path):
    s = open(path, encoding='utf-8').read()
    fails, warns = [], []
    if 'casa.css' not in s: fails.append('casa.css not loaded')
    if 'casa.js' not in s: fails.append('casa.js not loaded (translation toggle, term popovers)')
    blocks = re.findall(r'(?is)<aside class="fonte([^"]*)"', s)
    if len(blocks) < 4: fails.append(f'{len(blocks)} source blocks (.fonte); the lesson should read through the sources: at least 4')
    if not any(not re.search(r'\b(dec|lim)\b', b) for b in blocks): fails.append('no doctrine block: quote the assigned reading or treatise at least once (plain .fonte)')
    figs = len(re.findall(r'(?is)<figure\b(?:(?!</figure>).)*<svg', s))
    if figs < 2: fails.append(f'{figs} drawn figure(s); at least 2 instruments (a table is not a figure, F-026)')
    marks = sum(len(re.findall(r'class="%s"' % c, s)) for c in ('held', 'limit', 'term'))
    if marks < 3: fails.append(f'{marks} inline marks (.held/.limit/.term); the house marks what was decided, the limit, the terms')
    for m in re.finditer(r'<span class="term"(?![^>]*data-def)', s): fails.append('.term without data-def')
    prose = re.sub(r'(?is)<(script|style|svg|head)\b.*?</\1>|<aside class="fonte.*?</aside>', ' ', s)
    prose = re.sub(r'<[^>]+>', ' ', prose)
    arts = collections.Counter(re.findall(r'\bart(?:igo|\.)\s*(\d{1,4})', prose))
    for a, n in arts.items():
        if n > 5: warns.append(f'art. {a} named {n}× in our prose: quote it once in a .fonte and stop restating it')
    return fails, warns

if __name__ == '__main__':
    bad = 0
    for p in sys.argv[1:]:
        f, w = check(p)
        print(('FAIL' if f else 'PASS'), p, f'({len(f)} fail, {len(w)} warn)')
        for x in f: print('  FAIL', x)
        for x in w: print('  warn', x)
        bad += bool(f)
    sys.exit(1 if bad else 0)
