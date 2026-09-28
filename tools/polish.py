#!/usr/bin/env python3
"""Polish layer: hand edits to generated pages survive regeneration.

Generators rebuild pages from their sources, which would wipe prose edits made directly in the HTML
(the gardeners' ~1,000 fixes). This stores each edit as an exact before→after replacement, with enough context
to be unique, and re-applies it after a page is generated.

    python3 tools/polish.py capture [FILE ...]    # record the working-tree edits vs git HEAD (default: all changed pages)
    python3 tools/polish.py apply FILE ...        # re-apply stored patches to generated files
    python3 tools/polish.py check                 # report patches that no longer apply anywhere

Generators call apply_polish(path) after writing a page (kit.page and delito_common do this).
Patches live in tools/polish/<path relative to the repo>.json."""
import difflib, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORE = os.path.join(ROOT, 'tools', 'polish')
TOK = re.compile(r'<[^>]+>|[^\s<]+|\s+')

def _rel(path):
    return os.path.relpath(os.path.abspath(path), ROOT).replace(os.sep, '/')

def _store_path(rel):
    return os.path.join(STORE, rel + '.json')

def _hunks(old, new):
    a, b = TOK.findall(old), TOK.findall(new)
    ops = [o for o in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if o[0] != 'equal']
    # merge edits whose context windows would overlap, so every stored hunk applies independently
    K, groups = 6, []
    for op in ops:
        if groups and op[1] - groups[-1][-1][2] <= 2 * K:
            groups[-1].append(op)
        else:
            groups.append([op])
    out = []
    for g in groups:
        i1, i2, j1, j2 = g[0][1], g[-1][2], g[0][3], g[-1][4]
        k = K
        while True:            # grow context until the "before" text is unique in the old page
            lo, hi = max(0, i1 - k), min(len(a), i2 + k)
            before = ''.join(a[lo:hi])
            if old.count(before) == 1 or (lo == 0 and hi == len(a)):
                break
            k *= 2
        after = ''.join(a[lo:i1]) + ''.join(b[j1:j2]) + ''.join(a[i2:hi])
        out.append({'before': before, 'after': after})
    return out

def capture(files):
    n = 0
    for f in files:
        rel = _rel(f)
        try:
            old = subprocess.run(['git', '-C', ROOT, 'show', f'HEAD:{rel}'], capture_output=True, text=True, check=True).stdout
        except subprocess.CalledProcessError:
            continue
        new = open(os.path.join(ROOT, rel)).read()
        if old == new:
            continue
        hs = _hunks(old, new)
        # verify: applying the hunks to the old page reproduces the new page
        t = old
        for h in hs:
            t = t.replace(h['before'], h['after'], 1)
        if t != new:
            print(f'!! {rel}: hunks do not reproduce the edit exactly; stored anyway, check by hand')
        p = _store_path(rel); os.makedirs(os.path.dirname(p), exist_ok=True)
        prev = json.load(open(p)) if os.path.exists(p) else []
        seen = {(h['before'], h['after']) for h in prev}
        merged = prev + [h for h in hs if (h['before'], h['after']) not in seen]
        json.dump(merged, open(p, 'w'), ensure_ascii=False, indent=0)
        n += len(hs)
        print(f'captured {len(hs):4} edits  {rel}')
    print(f'total {n} edits')

def apply_polish(path, quiet=True):
    """Re-apply stored edits to a freshly generated page. Returns (applied, already, missing)."""
    rel = _rel(path); p = _store_path(rel)
    if not os.path.exists(p):
        return (0, 0, 0)
    s = open(path).read(); applied = already = missing = 0
    for h in json.load(open(p)):
        if h['before'] in s:
            s = s.replace(h['before'], h['after'], 1); applied += 1
        elif h['after'] in s:
            already += 1
        else:
            missing += 1
    open(path, 'w').write(s)
    if missing and not quiet:
        print(f'polish {rel}: {applied} applied, {already} already in place, {missing} no longer match (source text changed)')
    return (applied, already, missing)

def check():
    for d, _, fs in os.walk(STORE):
        for f in fs:
            rel = os.path.relpath(os.path.join(d, f), STORE)[:-5]
            page = os.path.join(ROOT, rel)
            if not os.path.exists(page):
                print('missing page', rel); continue
            s = open(page).read(); hs = json.load(open(os.path.join(d, f)))
            bad = sum(1 for h in hs if h['after'] not in s and h['before'] not in s)
            if bad:
                print(f'{rel}: {bad}/{len(hs)} edits no longer locatable')

if __name__ == '__main__':
    cmd, args = (sys.argv[1] if len(sys.argv) > 1 else ''), sys.argv[2:]
    if cmd == 'capture':
        if not args:
            args = [os.path.join(ROOT, x) for x in subprocess.run(['git', '-C', ROOT, 'diff', '--name-only'], capture_output=True, text=True).stdout.split() if x.endswith('.html')]
        capture(args)
    elif cmd == 'apply':
        for f in args: print(f, apply_polish(f, quiet=False))
    elif cmd == 'check':
        check()
    else:
        print(__doc__)
