"""Figure kit: instruments, not diagrams.

One implementation of the house drawing hand for lesson figures (the non-map counterpart of
latam-build/maps.py). A figure is a short script that puts real lesson content into a kit
component; the craft (stroke weights, mono labels, tones, ticks, gutters) lives here, once.

Colours are the course tokens (var(--ink) etc.), so every figure follows light/dark mode.
Panels are 600x600 (scrolly stage); heroes are 1080 wide.
"""

MONO = "font-family:var(--mono)"
TONE = {'ink': 'var(--ink)', 'conc': 'var(--conc)', 'dif': 'var(--dif)', 'mix': 'var(--mix)', 'muted': 'var(--ink-2)'}
WASH = {'ink': 'var(--paper-2)', 'conc': 'var(--conc-wash)', 'dif': 'var(--dif-wash)', 'mix': 'var(--mix-wash)', 'muted': 'var(--paper-2)'}
CH = 7.4  # mono 11px + .08em tracking, px per character (for gutters, not layout)
WARN = []  # text that would run into a line: fix the wording or the layout, never ship with warnings


def t(x, y, s, size=11, fill='var(--ink)', anchor='start', weight=500, caps=False, ls='.08em', italic=False, cls=''):
    st = f"{MONO};font-size:{size}px;font-weight:{weight};letter-spacing:{ls};fill:{fill}"
    if italic:
        st = f"font-family:var(--serif,serif);font-style:italic;font-size:{size + 2}px;fill:{fill}"
    if caps:
        s = s.upper()
    c = f' class="{cls}"' if cls else ''
    a = '' if anchor == 'start' else f' text-anchor="{anchor}"'
    return f'<text x="{x:g}" y="{y:g}"{a}{c} style="{st}">{s}</text>'


def line(x1, y1, x2, y2, tone='ink', w=1.5, dash=None, cls='', d=None):
    da = f";stroke-dasharray:{dash}" if dash else ''
    dl = f";--d:{d}s" if d is not None else ''
    c = f' class="{cls}"' if cls else ''
    return f'<path{c} d="M{x1:g} {y1:g}L{x2:g} {y2:g}" style="fill:none;stroke:{TONE[tone]};stroke-width:{w}{da}{dl}"/>'


def hatch_def(uid, tone='conc'):
    return (f'<pattern id="{uid}" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
            f'<rect width="7" height="7" style="fill:{WASH[tone]}"/>'
            f'<path d="M0 0V7" style="stroke:{TONE[tone]};stroke-width:1.1;opacity:.55"/></pattern>')


def badge(x, y, ok, r=11):
    """A reading: ✓ inside the rule (dif), ✕ past it (conc)."""
    tone = 'dif' if ok else 'conc'
    mark = (f'M{x - 5} {y}l3.6 4 6.4-8' if ok else f'M{x - 4.5} {y - 4.5}l9 9m0-9l-9 9')
    return (f'<circle cx="{x:g}" cy="{y:g}" r="{r}" style="fill:var(--paper);stroke:{TONE[tone]};stroke-width:1.6"/>'
            f'<path d="{mark}" style="fill:none;stroke:{TONE[tone]};stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round"/>')


class Ruler:
    """A graduated rule: the parameter as a measuring instrument.

    stops: labels at equal steps (each a str or a (line1, line2) tuple).
    limit: the step value where the rule stops allowing (everything past it is hatched).
    Acts are laid against it with .strip(); each strip projects its end back onto the rule.
    """

    def __init__(self, uid, x, y, w, stops, title='', source='', limit=None, h=74, minor=5, tone='ink'):
        self.uid, self.x, self.y, self.w, self.h = uid, x, y, w, h
        self.stops, self.title, self.source, self.limit, self.minor = stops, title, source, limit, minor
        self.n = len(stops) - 1
        self.parts = []

    def pos(self, v):
        return self.x + 14 + (self.w - 28) * v / self.n

    def defs(self):
        return hatch_def(f'{self.uid}-h')

    def body(self, d=0):
        x, y, w, h = self.x, self.y, self.w, self.h
        o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" style="fill:var(--paper);stroke:var(--ink);stroke-width:1.5"/>'
        if self.limit is not None:  # the forbidden reach of the scale
            lx = self.pos(self.limit)
            o += f'<rect x="{lx:g}" y="{y + 20}" width="{x + w - lx:g}" height="{h - 20}" style="fill:url(#{self.uid}-h);stroke:none"/>'
        o += line(x, y + 20, x + w, y + 20, w=1)
        o += t(x + 10, y + 14, self.title, size=10, fill='var(--ink-2)', caps=True, weight=600)
        if self.source:
            o += t(x + w - 10, y + 14, self.source, size=10, fill='var(--ink)', anchor='end', weight=700, caps=True)
        step = (self.w - 28) / self.n / self.minor
        for i in range(self.n * self.minor + 1):  # graduations, cut into the bottom edge
            tx = self.x + 14 + i * step
            major = i % self.minor == 0
            ln = 15 if major else 6
            o += line(tx, y + h, tx, y + h - ln, w=1.3 if major else .8)
        for i, s in enumerate(self.stops):
            px = self.pos(i)
            a = 'start' if i == 0 else ('end' if i == self.n else 'middle')
            ax = px - 4 if i == 0 else (px + 4 if i == self.n else px)
            if self.limit is not None and i == self.limit and 0 < i < self.n:  # never under the limit line
                a, ax = 'end', px - 7
            ls = s if isinstance(s, tuple) else (s,)
            y0 = y + 40 if len(ls) == 2 else y + 46
            beyond = self.limit is not None and i > self.limit
            for k, part in enumerate(ls):
                o += t(ax, y0 + 12 * k, part, size=11, anchor=a, fill='var(--conc)' if beyond else 'var(--ink)',
                       weight=600 if beyond else 500)
        return f'<g>{o}</g>'

    def limit_mark(self, reach_to, label='', sub='', d=None):
        """The rule's own limit: a red line through the scale and down past the acts."""
        lx = self.pos(self.limit)
        o = line(lx, self.y - 16, lx, reach_to, tone='conc', w=2.2, cls='grow' if d is not None else '', d=d)
        o += f'<path d="M{lx - 6:g} {self.y - 16}H{lx + 6:g}" style="stroke:var(--conc);stroke-width:2.2"/>'
        if label:
            o += t(lx + 9, self.y - 20, label, size=10.5, fill='var(--conc)', weight=700, caps=True)
        if sub:
            o += t(lx + 9, self.y - 7, sub, size=10, fill='var(--conc)')
        return o

    def strip(self, sy, to, label, note='', tone=None, d=None, reading=True):
        """An act laid against the rule, from 0 to `to`, with its end projected onto the scale."""
        over = self.limit is not None and to > self.limit
        tone = tone or ('conc' if over else 'dif')
        x0, x1 = self.x + 14, self.pos(to)
        anim = ' class="grow"' if d is not None else ''
        dl = f';--d:{d}s' if d is not None else ''
        name, desc = label if isinstance(label, tuple) else ('', label)
        room = (self.pos(self.limit) if self.limit is not None else self.x + self.w) - x0 - 8
        for s_ in (desc, note):
            if s_ and len(s_) * CH > room:
                WARN.append(f'{self.uid}: "{s_}" ~{len(s_) * CH:.0f}px > {room:.0f}px before the limit')
        o = (t(x0, sy - 22, name, size=10.5, weight=700, caps=True) if name else '') + t(x0, sy - 8, desc, size=11)
        o += f'<rect x="{x0:g}" y="{sy}" width="{x1 - x0:g}" height="14" style="fill:{WASH[tone]};stroke:{TONE[tone]};stroke-width:1.3"/>'
        if over:  # the part that the rule does not allow
            lx = self.pos(self.limit)
            o += f'<rect x="{lx:g}" y="{sy}" width="{x1 - lx:g}" height="14" style="fill:var(--conc);stroke:var(--conc);stroke-width:1.3"/>'
        o += f'<path{anim} d="M{x1:g} {sy - 4}V{self.y + self.h}" style="fill:none;stroke:{TONE[tone]};stroke-width:1.2;stroke-dasharray:3 3{dl}"/>'
        o += f'<circle cx="{x1:g}" cy="{self.y + self.h}" r="3.2" style="fill:{TONE[tone]}"/>'
        if reading:
            o += badge(x1 + 22, sy + 7, not over)
        if note:
            o += t(x0, sy + 30, note, size=10.5, fill=TONE[tone], weight=600)
        return o


def svg(view, inner, cls='', label='', ident=''):
    i = f' id="{ident}"' if ident else ''
    c = f' class="{cls}"' if cls else ''
    a = f' role="img" aria-label="{label}"' if label else ' aria-hidden="true"'
    return f'<svg{i}{c} viewBox="{view}"{a}>{inner}</svg>'
