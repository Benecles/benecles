"""A01 Fig. 1 (p-cr0..3): restore the legend labels and the scale-bar label that an earlier label pass stripped
(swatches were left with no words). Texts are the generator's own keys (work/latam-build/a01.py, crisis())."""
import re, sys
P = sys.argv[1]
s = open(P).read()
KEYS = {'p-cr0': ['América espanhola', 'América portuguesa', 'Haiti, livre em 1804'],
        'p-cr2': ['sob a Constituição de Cádiz', 'Peru: a marca gaditana dura']}
SCALE = '<path d="M430 575H487.5M430 571V579M458.7 572V578M487.5 571V579" style="fill:none;stroke:var(--ink);stroke-width:1.2"></path>'
for pid in ('p-cr0', 'p-cr1', 'p-cr2', 'p-cr3'):
    a = s.rindex('<svg', 0, s.index(f'id="{pid}"')); b = s.index('</svg>', a); h = s[a:b]
    for i, txt in enumerate(KEYS.get(pid, [])):
        y = 459 + 24 * i
        r = re.search(rf'<rect x="24" y="{y}" width="18" height="13"[^>]*></rect>', h)
        assert r, (pid, y)
        h = h[:r.end()] + f'<text x="50" y="{y + 11}" class="t-small" style="paint-order:stroke;stroke:var(--paper);stroke-width:4px;stroke-linejoin:round">{txt}</text>' + h[r.end():]
    if SCALE in h and '1000 km' not in h:
        h = h.replace(SCALE, SCALE + '<text x="487.5" y="566" text-anchor="end" class="t-small t-muted">1000 km</text>')
    h = re.sub(r'<path d="M[^"]*" style="fill:none;stroke:var\(--grid-major\);stroke-width:\.6;stroke-dasharray:1 6"></path>', '', h)   # dotted meridians (as in A02)
    s = s[:a] + h + s[b:]
open(P, 'w').write(s); print('ok')
