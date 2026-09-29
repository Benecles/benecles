"""Latin America map for 600x600 kit panels, drawn in the house style.
Country shapes come from Natural Earth 1:50m (public domain), projected and simplified once by geo/build_paths.py.
Each page embeds the shapes once (map_defs) and panels reference them with <use>, so a four-step scrolly
costs one copy of the geometry."""
import json, os
from kit import T, P, C, G

_D = json.load(open(os.path.join(os.path.dirname(__file__), 'geo', 'latam_paths.json')))
PJ, CT = _D['proj'], _D['c']
NAMES = {'MEX': 'México', 'GTM': 'Guatemala', 'BLZ': 'Belize', 'SLV': 'El Salvador', 'HND': 'Honduras', 'NIC': 'Nicarágua',
         'CRI': 'Costa Rica', 'PAN': 'Panamá', 'CUB': 'Cuba', 'HTI': 'Haiti', 'DOM': 'Rep. Dominicana', 'JAM': 'Jamaica',
         'PRI': 'Porto Rico', 'COL': 'Colômbia', 'VEN': 'Venezuela', 'GUY': 'Guiana', 'SUR': 'Suriname', 'GUF': 'Guiana Fr.',
         'ECU': 'Equador', 'PER': 'Peru', 'BRA': 'Brasil', 'BOL': 'Bolívia', 'PRY': 'Paraguai', 'CHL': 'Chile',
         'ARG': 'Argentina', 'URY': 'Uruguai'}
# countries too small for an inside label: label sits in open sea, joined by a short leader
OUTSIDE = {'GTM': (120, 118, 'end'), 'SLV': (120, 146, 'end'), 'HND': (286, 146, 'start'), 'NIC': (150, 176, 'end'),
           'CRI': (180, 204, 'end'), 'CHL': (170, 420, 'end'), 'PAN': (232, 226, 'end'), 'CUB': (262, 58, 'end'), 'HTI': (300, 70, 'middle'),
           'DOM': (392, 100, 'start'), 'URY': (500, 470, 'start'), 'PRY': (500, 395, 'start'), 'ECU': (132, 262, 'end'),
           'JAM': (262, 126, 'end'), 'PRI': (392, 122, 'start')}
TONES = {'dif': 'fill:var(--dif-wash);stroke:var(--dif)', 'conc': 'fill:var(--conc-wash);stroke:var(--conc)',
         'mix': 'fill:var(--mix-wash);stroke:var(--mix)', 'ink': 'fill:var(--ink);stroke:var(--ink)',
         'hatch': 'fill:url(#lm-hatch);stroke:var(--ink-2)', 'base': 'fill:var(--paper);stroke:var(--grid-major)',
         'grey': 'fill:color-mix(in srgb,var(--ink) 10%,var(--paper));stroke:var(--ink-2)'}

def xy(lon, lat):
    return (round(PJ['OX'] + (lon - PJ['LON0']) * PJ['KX'] * PJ['S'], 1), round(PJ['OY'] + (PJ['LAT1'] - lat) * PJ['S'], 1))

_RP = os.path.join(os.path.dirname(__file__), 'geo', 'relief_latam.json')
RELIEF = None   # relief retired (Benecles, 2026-09-25): maps stay flat; pipeline kept in geo/relief.py
BAND_OP = {'500': .07, '1500': .11, '3000': .15, '4500': .2}

def map_defs():
    paths = ''.join(f'<path id="lm-{k}" d="{v["d"]}"/>' for k, v in CT.items())
    if RELIEF:
        paths += ''.join(f'<path id="lr-l{k.replace("-", "m")}" d="{v}"/>' for k, v in RELIEF['lines'].items())
        paths += ''.join(f'<path id="lr-h{k}" d="{v}"/>' for k, v in RELIEF.get('hach', {}).items() if v)
    hatch = ('<pattern id="lm-hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
             '<rect width="6" height="6" style="fill:var(--paper)"/><path d="M0 0V6" style="stroke:var(--ink-2);stroke-width:1.4"/></pattern>')
    return f'<svg width="0" height="0" style="position:absolute;overflow:hidden" aria-hidden="true"><defs>{paths}{hatch}</defs></svg>\n'

KM_PER_DEG = 111.32
# map labels sit above the land with a paper halo, so coastlines and fills never swallow them
HALO = 'paint-order:stroke;stroke:var(--paper);stroke-width:3.5px;stroke-linejoin:round'

def _graticule():
    o = ''
    for lat, name in ((0, 'Equador'), (23.44, 'Trópico de Câncer'), (-23.44, 'Trópico de Capricórnio')):
        x0, y = xy(-118.5, lat); x1, _ = xy(-33, lat)
        dash = '' if lat == 0 else ';stroke-dasharray:2 5'
        o += f'<path d="M{x0} {y}H{x1}" style="fill:none;stroke:var(--grid-major);stroke-width:{1 if lat == 0 else .8}{dash}"/>'
    for lon in (-100, -80, -60, -40):
        x, y0 = xy(lon, 33.5); _, y1 = xy(lon, -56.5)
        o += f'<path d="M{x} {y0}V{y1}" style="fill:none;stroke:var(--grid-major);stroke-width:.6;stroke-dasharray:1 6"/>'
    return o

def _grat_labels():
    o = ''
    for lat, name in ((0, 'Equador'), (23.44, 'Trópico de Câncer'), (-23.44, 'Trópico de Capricórnio')):
        x1, y = xy(-33, lat)
        o += f'<text x="{x1 - 4}" y="{y - 4}" text-anchor="end" style="font:italic 10px var(--serif,serif);fill:var(--muted);letter-spacing:.04em;{HALO}">{name}</text>'
    for lon in (-100, -80, -60, -40):
        x, _ = xy(lon, 33.5); _, y1 = xy(lon, -56.5)
        o += f'<text x="{x + 3}" y="{y1 - 4}" style="font:9px var(--mono);fill:var(--muted);{HALO}">{abs(lon)}°O</text>'
    return o

SEAS = [(-99, -33, 'OCEANO PACÍFICO'), (-44, -40, 'OCEANO ATLÂNTICO'), (-75, 15.5, 'MAR DO CARIBE')]
def _seas(skip=()):
    o = ''
    for lon, lat, name in SEAS:
        if name in skip: continue
        x, y = xy(lon, lat)
        o += f'<text x="{x}" y="{y}" text-anchor="middle" style="font:italic 11px var(--serif,serif);letter-spacing:.32em;fill:var(--muted);{HALO}">{name}</text>'
    return o

def _waterlines():
    # engraved-map coast rings: wide faint strokes alternating with paper-coloured ones, under the land fills
    o = ''
    for w, col in ((15, 'var(--grid-major)'), (12, 'var(--paper)'), (8.5, 'var(--grid-major)'), (6, 'var(--paper)'), (3, 'var(--grid-major)')):
        o += '<g style="fill:none;stroke:{};stroke-width:{};stroke-linejoin:round;opacity:{}">'.format(col, w, .55 if 'grid' in col else 1)
        o += ''.join(f'<use href="#lm-{k}"/>' for k in CT) + '</g>'
    return o

def scale_bar(x=430, y=575, km=1000):
    px = km / KM_PER_DEG * PJ['S']
    return (f'<path d="M{x} {y}H{x + px:.1f}M{x} {y - 4}V{y + 4}M{x + px / 2:.1f} {y - 3}V{y + 3}M{x + px:.1f} {y - 4}V{y + 4}" style="fill:none;stroke:var(--ink);stroke-width:1.2"/>'
            f'<text x="{x}" y="{y - 8}" style="font:9px var(--mono);fill:var(--ink-2)">0</text>'
            f'<text x="{x + px:.1f}" y="{y - 8}" text-anchor="end" style="font:9px var(--mono);fill:var(--ink-2)">{km} km</text>')

def flow(a, b, text='', bend=.25, tone='ink', d=.3, dy=-6):
    """curved flow line between two (lon, lat) points, with an arrowhead drawn inline"""
    (x1, y1), (x2, y2) = xy(*a), xy(*b)
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    nx, ny = -(y2 - y1) * bend, (x2 - x1) * bend
    cx, cy = mx + nx, my + ny
    col = {'ink': 'var(--ink)', 'dif': 'var(--dif)', 'conc': 'var(--conc)'}[tone]
    # arrowhead along the tangent at the end
    tx, ty = x2 - cx, y2 - cy
    L = (tx * tx + ty * ty) ** .5 or 1
    ux, uy = tx / L, ty / L
    h1 = (x2 - ux * 9 - uy * 5, y2 - uy * 9 + ux * 5); h2 = (x2 - ux * 9 + uy * 5, y2 - uy * 9 - ux * 5)
    o = (f'<path class="draw" d="M{x1} {y1}Q{cx:.1f} {cy:.1f} {x2} {y2}" style="fill:none;stroke:{col};stroke-width:1.8;--d:{d}s"/>'
         f'<path class="draw" d="M{h1[0]:.1f} {h1[1]:.1f}L{x2} {y2}L{h2[0]:.1f} {h2[1]:.1f}" style="fill:none;stroke:{col};stroke-width:1.8;--d:{d + .4}s"/>')
    if text:
        o += G(f'<text x="{cx:.1f}" y="{cy + dy:.1f}" text-anchor="middle" style="font:11px var(--mono);fill:{col}">{text}</text>', 'fade', d=d + .5)
    return o

def _bathy():
    if not RELIEF: return ''
    return ('<use href="#lr-lm3000" style="fill:none;stroke:var(--grid-major);stroke-width:.7;stroke-dasharray:1 3"/>'
            '<use href="#lr-lm200" style="fill:none;stroke:var(--ink-2);stroke-width:.6;opacity:.45"/>')

HACH_W = {'1': .45, '2': .75, '3': 1.1}
def _relief():
    # engraved hachures in ink: they invert with the theme and never muddy the washes
    if not RELIEF or 'hach' not in RELIEF: return ''
    return ''.join(f'<use href="#lr-h{k}" style="fill:none;stroke:var(--ink);stroke-width:{w};stroke-linecap:round;opacity:.7;pointer-events:none"/>'
                   for k, w in HACH_W.items() if RELIEF['hach'].get(k))

def latam_map(fills=None, labels=(), pins=(), title='', note='', key=(), dim_label=False, sw=1.1,
              graticule=True, seas=True, water=True, scale=True, skip_seas=(), extra='', relief=False):
    """fills: {ISO: tone}; labels: ISO codes to name (inside if room, else leader to sea);
    pins: (lon, lat, text, anchor, dx, dy); key: [(tone, text)] legend drawn bottom-left; extra: svg drawn above land."""
    fills = fills or {}
    o = ''
    if graticule: o += _graticule()
    if water: o += _waterlines()
    if relief: o += _bathy()
    if title: o += T(584, 30, title, 't-small', anchor='end', style='letter-spacing:.1em')
    for k in CT:
        tone = fills.get(k, 'base')
        o += f'<use href="#lm-{k}" style="{TONES[tone]};stroke-width:{sw if tone != "base" else .8};stroke-linejoin:round"/>'
    if relief: o += _relief()
    if graticule: o += _grat_labels()
    if seas: o += _seas(skip_seas)
    o += extra
    for k in labels:
        cx, cy = CT[k]['c']
        name = NAMES[k]
        on = k in fills and fills[k] != 'base'
        cls = 't-small' + ('' if on or not dim_label else ' t-muted')
        if k in OUTSIDE:
            lx, ly, anc = OUTSIDE[k]
            ex = lx + (4 if anc == 'start' else -4 if anc == 'end' else 0)
            o += P(f'M{cx} {cy}L{ex} {ly - 4}', 'thin', style='stroke-width:.8')
            o += T(lx, ly, name, cls, anchor=anc, style=HALO)
        else:
            o += T(cx, cy + 4, name, cls, anchor='middle', style=HALO)
    for lon, lat, text, anc, dx, dy in pins:
        x, y = xy(lon, lat)
        o += C(x, y, 3.2, 'f-ink') + C(x, y, 6, 'ink', style='fill:none;stroke-width:.8')
        if text:
            if abs(dx) > 24 or abs(dy) > 24:   # far label: leader line out to open sea
                o += P(f'M{x} {y}L{x + dx - (4 if anc == "start" else -4 if anc == "end" else 0)} {y + dy - 4}', 'thin', style='stroke-width:.8')
            o += T(x + dx, y + dy, text, 't-small', anchor=anc, style=HALO)
    for i, (tone, text) in enumerate(key):
        y = 470 + i * 24
        o += f'<rect x="24" y="{y - 11}" width="18" height="13" style="{TONES[tone]};stroke-width:1.1"/>'
        o += T(50, y, text, 't-small')
    if scale: o += scale_bar()
    if note: o += G(T(584, 52, note, 't-hand', anchor='end'), 'fade', d=.3)
    return o

def inset(uid, lon0, lon1, lat0, lat1, rx, ry, rw, fills=None, pins=(), label=''):
    """Zoomed inset (classic atlas style): frame at (rx, ry) of width rw, locator box drawn on the main map.
    pins: (lon, lat, text, anchor, dx, dy) placed in inset coordinates."""
    fills = fills or {}
    (ax, ay), (bx, by) = xy(lon0, lat1), xy(lon1, lat0)
    k = rw / (bx - ax)
    rh = round((by - ay) * k, 1)
    o = f'<path d="M{ax} {ay}H{bx}V{by}H{ax}Z" style="fill:none;stroke:var(--ink);stroke-width:.9"/>'
    o += f'<path d="M{bx} {ay}L{rx} {ry}M{bx} {by}L{rx} {ry + rh}" style="fill:none;stroke:var(--ink-2);stroke-width:.6;stroke-dasharray:2 3"/>'
    o += f'<clipPath id="{uid}"><rect x="{rx}" y="{ry}" width="{rw}" height="{rh}"/></clipPath>'
    o += f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" style="fill:var(--paper)"/>'
    o += f'<g clip-path="url(#{uid})"><g transform="translate({rx} {ry}) scale({k:.3f}) translate({-ax} {-ay})">'
    for w, col in ((15, 'var(--grid-major)'), (12, 'var(--paper)'), (8.5, 'var(--grid-major)'), (6, 'var(--paper)'), (3, 'var(--grid-major)')):
        o += f'<g style="fill:none;stroke:{col};stroke-width:{w / k:.2f};opacity:{.55 if "grid" in col else 1}">' + ''.join(f'<use href="#lm-{c}"/>' for c in CT) + '</g>'
    for c in CT:
        tone = fills.get(c, 'base')
        o += f'<use href="#lm-{c}" style="{TONES[tone]};stroke-width:{(1.1 if tone != "base" else .8) / k:.2f};stroke-linejoin:round"/>'
    o += '</g></g>'
    o += f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" style="fill:none;stroke:var(--ink);stroke-width:1.2"/>'
    for lon, lat, text, anc, dx, dy in pins:
        x, y = xy(lon, lat); x = round(rx + (x - ax) * k, 1); y = round(ry + (y - ay) * k, 1)
        o += C(x, y, 3.2, 'f-ink') + C(x, y, 6, 'ink', style='fill:none;stroke-width:.8')
        if text: o += T(x + dx, y + dy, text, 't-small', anchor=anc)
    if label: o += T(rx + 6, ry + rh - 6, label, 't-small', style='font-style:italic')
    return o


class Frame:
    """Any map frame built by geo/build_frame.py (e.g. 'atlantic'). Same house style as latam_map."""
    def __init__(self, name):
        d = json.load(open(os.path.join(os.path.dirname(__file__), 'geo', f'frame_{name}.json')))
        self.name, self.pj, self.ct = name, d['proj'], d['c']
        self.W, self.H = round(self.pj['W']), self.pj['H']
        rp = os.path.join(os.path.dirname(__file__), 'geo', f'relief_{name}.json')
        self.relief = None   # relief retired
    def xy(self, lon, lat):
        p = self.pj
        return (round(p['OX'] + (lon - p['LON0']) * p['KX'] * p['S'], 1), round(p['OY'] + (p['LAT1'] - lat) * p['S'], 1))
    def defs(self):
        paths = ''.join(f'<path id="f{self.name}-{k}" d="{v["d"]}"/>' for k, v in self.ct.items())
        if self.relief:
            paths += ''.join(f'<path id="f{self.name}-rl{k.replace("-", "m")}" d="{v}"/>' for k, v in self.relief['lines'].items())
            paths += ''.join(f'<path id="f{self.name}-rh{k}" d="{v}"/>' for k, v in self.relief.get('hach', {}).items() if v)
        return f'<defs>{paths}</defs>'
    def km_px(self, km): return km / KM_PER_DEG * self.pj['S']
    def base(self, fills=None, water=True, sw=1.1):
        fills = fills or {}
        o = ''
        if water:
            for w, col in ((18, 'var(--grid-major)'), (14, 'var(--paper)'), (10, 'var(--grid-major)'), (7, 'var(--paper)'), (3.5, 'var(--grid-major)')):
                o += f'<g style="fill:none;stroke:{col};stroke-width:{w};stroke-linejoin:round;opacity:{.5 if "grid" in col else 1}">'
                o += ''.join(f'<use href="#f{self.name}-{k}"/>' for k in self.ct) + '</g>'
        if self.relief:
            o += (f'<use href="#f{self.name}-rlm3000" style="fill:none;stroke:var(--grid-major);stroke-width:.8;stroke-dasharray:1 3"/>'
                  f'<use href="#f{self.name}-rlm200" style="fill:none;stroke:var(--ink-2);stroke-width:.7;opacity:.45"/>')
        for k in self.ct:
            tone = fills.get(k, 'base')
            o += f'<use href="#f{self.name}-{k}" style="{TONES[tone]};stroke-width:{sw if tone != "base" else .8};stroke-linejoin:round"/>'
        if self.relief:
            o += ''.join(f'<use href="#f{self.name}-rh{k}" style="fill:none;stroke:var(--ink);stroke-width:{w * 1.2:.2f};stroke-linecap:round;opacity:.7;pointer-events:none"/>'
                         for k, w in HACH_W.items() if self.relief.get('hach', {}).get(k))
        return o
    LATS = ((0, 'Equador'), (23.44, 'Trópico de Câncer'), (-23.44, 'Trópico de Capricórnio'))
    def graticule(self, lats=LATS, labels=True):
        o = ''
        for lat, name in lats:
            _, y = self.xy(0, lat)
            dash = '' if lat == 0 else ';stroke-dasharray:2 5'
            o += f'<path d="M0 {y}H{self.W}" style="fill:none;stroke:var(--grid-major);stroke-width:{1 if lat == 0 else .8}{dash}"/>'
        return o + (self.grat_labels(lats) if labels else '')
    def grat_labels(self, lats=LATS):
        # call after base() so the land never covers the names
        return ''.join(f'<text x="8" y="{self.xy(0, lat)[1] - 5}" style="font:italic 12px var(--serif,serif);fill:var(--muted);{HALO}">{name}</text>' for lat, name in lats)
    def sea(self, lon, lat, name, size=13):
        x, y = self.xy(lon, lat)
        return f'<text x="{x}" y="{y}" text-anchor="middle" style="font:italic {size}px var(--serif,serif);letter-spacing:.34em;fill:var(--muted);{HALO}">{name}</text>'
    def pin(self, lon, lat, r=4):
        x, y = self.xy(lon, lat)
        return f'<circle cx="{x}" cy="{y}" r="{r}" style="fill:var(--ink)"/><circle cx="{x}" cy="{y}" r="{r + 3.5}" style="fill:none;stroke:var(--ink);stroke-width:.9"/>'
    def flow(self, a, b, bend=.25, tone='ink', d=.3, w=2.2, dash=False):
        (x1, y1), (x2, y2) = self.xy(*a), self.xy(*b)
        cx, cy = (x1 + x2) / 2 - (y2 - y1) * bend, (y1 + y2) / 2 + (x2 - x1) * bend
        col = {'ink': 'var(--ink)', 'dif': 'var(--dif)', 'conc': 'var(--conc)', 'mix': 'var(--mix)'}[tone]
        tx, ty = x2 - cx, y2 - cy; L = (tx * tx + ty * ty) ** .5 or 1; ux, uy = tx / L, ty / L
        h1 = (x2 - ux * 12 - uy * 6, y2 - uy * 12 + ux * 6); h2 = (x2 - ux * 12 + uy * 6, y2 - uy * 12 - ux * 6)
        da = ';stroke-dasharray:7 5' if dash else ''
        return (f'<path class="draw" d="M{x1} {y1}Q{cx:.1f} {cy:.1f} {x2} {y2}" style="fill:none;stroke:{col};stroke-width:{w};--d:{d}s{da}"/>'
                f'<path class="draw" d="M{h1[0]:.1f} {h1[1]:.1f}L{x2} {y2}L{h2[0]:.1f} {h2[1]:.1f}" style="fill:none;stroke:{col};stroke-width:{w};--d:{d + .5}s"/>')
