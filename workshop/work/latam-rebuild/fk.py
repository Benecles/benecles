"""Tiny figure kit for the Latam figure pass (Claude, 05/10).
Panels are .figkit (exempt from the blanket 14px label rule) and carry class "lt": on upright phones their
text is set to 21px by one scoped rule, which beats the legacy 19px rule and is what every label is sized for.
Design limits: mono labels ≤ 28 chars on a row starting at x≈40 (fits 600 at 21px ≈ 12.6px/char)."""
import re

PHONE = ('<style>@media (max-width:860px) and (orientation:portrait){'
         '.stage figure svg.lt text{font-size:18px!important}.stage figure svg.lt text.hand{font-size:21px!important}}</style>')

def svg(pid, aria, title, body, on=False, vb='0 0 600 600'):
    return (f'<svg class="panel fig figkit lt{" on" if on else ""}" id="{pid}" viewBox="{vb}" role="img" aria-label="{aria}">{PHONE}'
            f'<text x="36" y="40" class="t-small" style="font-size:14px;letter-spacing:.1em">{title}</text>{body}</svg>')

def T(x, y, s, size=15, tone='ink', anchor='start', weight=400, op=1, cls='t-small', extra=''):
    col = {'ink': 'var(--ink)', 'ink2': 'var(--ink-2)', 'muted': 'var(--muted)', 'conc': 'var(--conc)', 'dif': 'var(--dif)'}[tone]
    o = f';opacity:{op}' if op != 1 else ''
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}" '
            f'style="font-size:{size}px;font-weight:{weight};fill:{col}{o}{extra}">{s}</text>')

def H(x, y, s, size=20, tone='ink', anchor='start'):
    """hand annotation (serif italic)"""
    return T(x, y, s, size, tone, anchor, cls='t-hand hand')

def L(d, tone='ink', w=1.6, op=1, dash=''):
    col = {'ink': 'var(--ink)', 'ink2': 'var(--ink-2)', 'muted': 'var(--muted)', 'conc': 'var(--conc)', 'dif': 'var(--dif)', 'grid': 'var(--grid-major)'}[tone]
    da = f';stroke-dasharray:{dash}' if dash else ''
    o = f';opacity:{op}' if op != 1 else ''
    return f'<path d="{d}" style="fill:none;stroke:{col};stroke-width:{w};stroke-linecap:round;stroke-linejoin:round{da}{o}"/>'

def R(x, y, w, h, fill='paper', stroke='ink', sw=1.5, op=1):
    f = {'paper': 'var(--paper)', 'paper2': 'var(--paper-2)', 'conc': 'var(--conc-wash)', 'dif': 'var(--dif-wash)', 'none': 'none',
         'grey': 'color-mix(in srgb,var(--ink) 12%,var(--paper))', 'concs': 'var(--conc)', 'difs': 'var(--dif)', 'inks': 'var(--ink)'}[fill]
    s = {'ink': 'var(--ink)', 'conc': 'var(--conc)', 'dif': 'var(--dif)', 'none': 'none', 'grid': 'var(--grid-major)'}[stroke]
    o = f';opacity:{op}' if op != 1 else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" style="fill:{f};stroke:{s};stroke-width:{sw}{o}"/>'

def dot(x, y, r=5, tone='ink'):
    col = {'ink': 'var(--ink)', 'conc': 'var(--conc)', 'dif': 'var(--dif)', 'muted': 'var(--muted)'}[tone]
    return f'<circle cx="{x}" cy="{y}" r="{r}" style="fill:{col}"/>'

def replace_panels(html, panels):
    """Swap whole <svg id=...> panels in place; panels = {id: new_svg}. Returns new html; asserts each found once."""
    for pid, new in panels.items():
        pat = re.compile(r'<svg\b[^>]*\bid="%s"[^>]*>.*?</svg>' % re.escape(pid), re.S)
        html, n = pat.subn(lambda m: new, html)
        assert n == 1, (pid, n)
    return html

def set_caption(html, first_pid, caption):
    """Rename the figcaption of the figure containing panel first_pid."""
    i = html.index(f'id="{first_pid}"')
    j = html.index('<figcaption><span>', i) + len('<figcaption><span>')
    k = html.index('</span>', j)
    return html[:j] + caption + html[k:]

def set_step(html, pid, label=None, h3=None, paras=None):
    """Rewrite one step card (by its data-panel)."""
    i = html.index(f'<div class="step" data-panel="{pid}">')
    j = html.index('</div></div>', i) + len('</div></div>')
    card = html[i:j]
    if label is not None:
        card = re.sub(r'(<span class="label[^"]*">)[^<]*(</span>)', lambda m: m.group(1) + label + m.group(2), card, 1)
    if h3 is not None:
        card = re.sub(r'<h3>.*?</h3>', '<h3>' + h3 + '</h3>', card, 1, flags=re.S)
    if paras is not None:
        card = re.sub(r'(</h3>).*?(</div></div>)$', lambda m: m.group(1) + ''.join(f'<p>{p}</p>' for p in paras) + m.group(2), card, 1, flags=re.S)
    return html[:i] + card + html[j:]
