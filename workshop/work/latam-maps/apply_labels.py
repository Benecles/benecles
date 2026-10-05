"""Apply label placements computed in the browser (labeler.js: placeLabels) to a figure in a page.
usage: apply_labels.py PAGE SVG_START_MARKER placements.json [--join-routes]
Each g.pop with a pin circle and non-empty text gets its texts moved (x, y + 18·i, anchor) and its leader redrawn."""
import json, re, sys
page, marker, pj = sys.argv[1:4]
join = '--join-routes' in sys.argv
s = open(page).read()
a = s.index(marker); b = s.index('</svg>', a)
svg = s[a:b]
res = {o['gi']: o for o in json.load(open(pj))}
if join:   # routes had holes cut where old labels sat; make each one continuous
    svg = re.sub(r'(<path class="draw" d=")([^"]+)', lambda m: m.group(1) + m.group(2)[0] + m.group(2)[1:].replace('M', 'L'), svg)
gi = -1
def fix(m):
    global gi
    g = m.group(0)
    if '<circle' not in g or not any(t.strip() for t in re.findall(r'<text[^>]*>([^<]*)</text>', g)): return g
    gi += 1
    o = res[gi]; i = 0
    def tx(t):
        nonlocal i
        if not t.group(2).strip(): return t.group(0)
        r = re.sub(r' x="[^"]*" y="[^"]*" text-anchor="[^"]*"', f' x="{o["x"]}" y="{round(o["y"] + 18 * i, 1)}" text-anchor="{o["a"]}"', t.group(1)) + t.group(2) + '</text>'
        i += 1
        return r
    g = re.sub(r'(<text[^>]*>)([^<]*)</text>', tx, g)
    g = re.sub(r'<path d="M[^"]*" style="fill:none;stroke:var\(--ink-2\);stroke-width:\.9"></path>', '', g)
    if o['lead']:
        lead = f'<path d="M{o["pin"][0]} {o["pin"][1]}L{o["lead"][0]} {o["lead"][1]}" style="fill:none;stroke:var(--ink-2);stroke-width:.9"></path>'
        g = g.replace('<text', lead + '<text', 1)
    return g
svg = re.sub(r'<g class="pop"[^>]*>.*?</g>', fix, svg, flags=re.S)
assert gi + 1 == len(res), (gi, len(res))
open(page, 'w').write(s[:a] + svg + s[b:])
print('applied', gi + 1)
