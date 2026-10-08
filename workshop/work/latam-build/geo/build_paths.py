"""One-off: Natural Earth 1:50m (public domain) -> simplified SVG paths for a 600x600 Latin America panel.
Output: latam_paths.json  {ISO3: {"d": path, "c": [x, y] label anchor, "a": area_px2}}"""
import json, math

LON0, LON1, LAT0, LAT1 = -118.5, -33.0, -56.5, 33.5   # bbox
PAD = 12
W = H = 600
KX = math.cos(math.radians(8))                       # mild aspect correction around the equator
sx = (W - 2 * PAD) / ((LON1 - LON0) * KX)
sy = (H - 2 * PAD) / (LAT1 - LAT0)
S = min(sx, sy)
OX = PAD + ((W - 2 * PAD) - (LON1 - LON0) * KX * S) / 2
OY = PAD + ((H - 2 * PAD) - (LAT1 - LAT0) * S) / 2

def proj(lon, lat):
    return (OX + (lon - LON0) * KX * S, OY + (LAT1 - lat) * S)

def dp(pts, tol):
    if len(pts) < 3: return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy) or 1e-9
    imax, dmax = 0, -1
    for i in range(1, len(pts) - 1):
        x, y = pts[i]
        d = abs(dy * x - dx * y + x2 * y1 - y2 * x1) / L
        if d > dmax: imax, dmax = i, d
    if dmax > tol:
        return dp(pts[:imax + 1], tol)[:-1] + dp(pts[imax:], tol)
    return [pts[0], pts[-1]]

def area(pts):
    return abs(sum(pts[i][0] * pts[i - 1][1] - pts[i - 1][0] * pts[i][1] for i in range(len(pts)))) / 2

def centroid(pts):
    a = cx = cy = 0
    for i in range(len(pts)):
        x0, y0 = pts[i - 1]; x1, y1 = pts[i]
        f = x0 * y1 - x1 * y0; a += f; cx += (x0 + x1) * f; cy += (y0 + y1) * f
    if abs(a) < 1e-9: return pts[0]
    return (cx / (3 * a), cy / (3 * a))

KEEP = ['MEX', 'GTM', 'BLZ', 'SLV', 'HND', 'NIC', 'CRI', 'PAN', 'CUB', 'HTI', 'DOM', 'JAM', 'PRI', 'BHS', 'TTO',
        'COL', 'VEN', 'GUY', 'SUR', 'ECU', 'PER', 'BRA', 'BOL', 'PRY', 'CHL', 'ARG', 'URY', 'FLK']
TOL = 0.55          # px
MIN_AREA = 6.0      # px² — drops specks, keeps Caribbean main islands

d = json.load(open('ne50.geojson'))
out = {}
for f in d['features']:
    p = f['properties']; iso = p['ADM0_A3']
    g = f['geometry']
    polys = g['coordinates'] if g['type'] == 'MultiPolygon' else [g['coordinates']]
    if iso == 'FRA':   # keep only French Guiana
        polys = [pl for pl in polys if -55 < pl[0][0][0] < -51 and 1 < pl[0][0][1] < 6.5]; iso = 'GUF'
    elif iso not in KEEP:
        continue
    parts, best = [], (0, None)
    for pl in polys:
        ring = [proj(lon, lat) for lon, lat in pl[0] if LON0 - 2 < lon < LON1 + 2 and LAT0 - 2 < lat < LAT1 + 2]
        if len(ring) < 4: continue
        h = len(ring) // 2
        ring = dp(ring[:h + 1], TOL)[:-1] + dp(ring[h:], TOL)
        a = area(ring)
        if a < MIN_AREA: continue
        if a > best[0]: best = (a, ring)
        parts.append('M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in ring[:-1]) + 'Z')
    if not parts: continue
    c = centroid(best[1])
    out[iso] = {'d': ''.join(parts), 'c': [round(c[0], 1), round(c[1], 1)], 'a': round(best[0])}

json.dump({'proj': {'LON0': LON0, 'LAT1': LAT1, 'KX': KX, 'S': S, 'OX': OX, 'OY': OY}, 'c': out}, open('latam_paths.json', 'w'))
print(len(out), 'countries;', sum(len(v['d']) for v in out.values()), 'chars')
for k in ['SLV', 'CRI', 'PAN', 'HTI', 'DOM', 'URY', 'JAM', 'PRI']:
    print(k, out.get(k, {}).get('a'), out.get(k, {}).get('c'))
