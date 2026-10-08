"""A02 Fig. 2 atlas (p-mp0, p-mp1): legend rows realigned with their swatches (texts had drifted 8 px per row),
the orphan scale-bar stroke removed (its labels were stripped earlier), Chile and Ecuador labels moved to the
Pacific beside their coasts instead of long leaders crossing Argentina and Peru; dotted meridians dropped."""
import re, sys
P = sys.argv[1]
s = open(P).read()
def fix(svg):
    rows = re.findall(r'<rect x="24" y="(\d+)" width="18" height="13"', svg)
    assert len(rows) == 4, rows
    for i, y in enumerate(rows):
        ny = 474 + 28 * i
        svg = svg.replace(f'<rect x="24" y="{y}" width="18" height="13"', f'<rect x="24" y="{ny - 11}" width="18" height="13"', 1)
    texts = list(re.finditer(r'<text x="50" y="(\d+)" class="t-small">', svg))
    assert len(texts) == 4
    for i, m in reversed(list(enumerate(texts))):
        svg = svg[:m.start()] + f'<text x="50" y="{474 + 28 * i + 1}" class="t-small">' + svg[m.end():]
    svg = svg.replace('<path d="M430.00 575.00L487.50 578.50" style="fill:none;stroke:var(--ink);stroke-width:1.2"></path>', '')
    svg = svg.replace('<path d="M328.20 455.10L172.17 417.49" class="thin" style="stroke-width:.8"></path><text x="170" y="420"',
                      '<path d="M329.5 412.0L306 412.0" class="thin" style="stroke-width:.8"></path><text x="302" y="416"')
    svg = svg.replace('<path d="M283.30 235.70L134.33 257.09" class="thin" style="stroke-width:.8"></path><text x="132" y="262"',
                      '<path d="M281.0 236.5L262 245" class="thin" style="stroke-width:.8"></path><text x="258" y="250"')
    n0 = len(svg)
    svg = re.sub(r'<path d="M[^"]*" style="fill:none;stroke:var\(--grid-major\);stroke-width:\.6;stroke-dasharray:1 6"></path>', '', svg)   # dotted meridians: no reading value, and their label gaps no longer match
    assert len(svg) < n0
    assert 'x="302" y="416"' in svg and 'x="258" y="250"' in svg
    return svg
for pid in ('p-mp0', 'p-mp1'):
    a = s.rindex('<svg', 0, s.index(f'id="{pid}"')); b = s.index('</svg>', a)
    s = s[:a] + fix(s[a:b]) + s[b:]
open(P, 'w').write(s); print('ok')
