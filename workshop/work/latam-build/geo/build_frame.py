"""Build a map frame from Natural Earth 1:50m (public domain): any bbox, any width.
usage: python3 build_frame.py NAME LON0 LON1 LAT0 LAT1 WIDTH
writes frame_NAME.json {proj, c: {ISO: {d, c, a}}}; every country touching the bbox is kept (context in base tone)."""
import json, math, sys

name, LON0, LON1, LAT0, LAT1, W = sys.argv[1], *map(float, sys.argv[2:6]), float(sys.argv[6])
KX = math.cos(math.radians((LAT0 + LAT1) / 2))
S = W / ((LON1 - LON0) * KX)
H = round((LAT1 - LAT0) * S)
OX, OY = 0.0, 0.0

def proj(lon, lat): return (OX + (lon - LON0) * KX * S, OY + (LAT1 - lat) * S)

def dp(pts, tol):
    if len(pts) < 3: return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy) or 1e-9
    imax, dmax = 0, -1
    for i in range(1, len(pts) - 1):
        x, y = pts[i]; d = abs(dy * x - dx * y + x2 * y1 - y2 * x1) / L
        if d > dmax: imax, dmax = i, d
    return dp(pts[:imax + 1], tol)[:-1] + dp(pts[imax:], tol) if dmax > tol else [pts[0], pts[-1]]

def area(p): return abs(sum(p[i][0] * p[i - 1][1] - p[i - 1][0] * p[i][1] for i in range(len(p)))) / 2
def centroid(p):
    a = cx = cy = 0
    for i in range(len(p)):
        x0, y0 = p[i - 1]; x1, y1 = p[i]; f = x0 * y1 - x1 * y0; a += f; cx += (x0 + x1) * f; cy += (y0 + y1) * f
    return (cx / (3 * a), cy / (3 * a)) if abs(a) > 1e-9 else p[0]

d = json.load(open('ne50.geojson'))
out = {}
TOL = float(sys.argv[7]) if len(sys.argv) > 7 else .6
M = 8  # degrees of slack so coastlines run off the frame edge instead of stopping short
for f in d['features']:
    iso = f['properties']['ADM0_A3']; g = f['geometry']
    polys = g['coordinates'] if g['type'] == 'MultiPolygon' else [g['coordinates']]
    parts, best = [], (0, None)
    for pl in polys:
        ring0 = pl[0]
        if not any(LON0 - M < lo < LON1 + M and LAT0 - M < la < LAT1 + M for lo, la in ring0): continue
        ring = [proj(lo, la) for lo, la in ring0]
        h = len(ring) // 2
        ring = dp(ring[:h + 1], TOL)[:-1] + dp(ring[h:], TOL)
        a = area(ring)
        if a < 5: continue
        if a > best[0]: best = (a, ring)
        parts.append('M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in ring[:-1]) + 'Z')
    if not parts: continue
    key = 'GUF' if iso == 'FRA' and best[1] and centroid(best[1])[1] > (LAT1 - 10) * 0 and False else iso
    c = centroid(best[1])
    out[key] = {'d': ''.join(parts), 'c': [round(c[0], 1), round(c[1], 1)], 'a': round(best[0])}

json.dump({'proj': {'LON0': LON0, 'LAT1': LAT1, 'KX': KX, 'S': S, 'OX': OX, 'OY': OY, 'W': W, 'H': H}, 'c': out}, open(f'frame_{name}.json', 'w'))
print(name, len(out), 'countries', f'{W:.0f}x{H}', sum(len(v['d']) for v in out.values()), 'chars')
