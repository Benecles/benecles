"""Build a map frame from Natural Earth 1:50m (public domain): any bbox, any width.
usage: python3 build_frame.py NAME LON0 LON1 LAT0 LAT1 WIDTH
writes frame_NAME.json {proj, c: {ISO: {d, c, a}}}; every country touching the bbox is kept (context in base tone)."""
import json, math, sys

name, LON0, LON1, LAT0, LAT1, MAP_W = sys.argv[1], *map(float, sys.argv[2:6]), float(sys.argv[6])
KX = math.cos(math.radians((LAT0 + LAT1) / 2))
S = MAP_W / ((LON1 - LON0) * KX)
MAP_H = round((LAT1 - LAT0) * S)
PAD = float(sys.argv[8]) if len(sys.argv) > 8 else 40.0
OX, OY = PAD, PAD
W, H = MAP_W + 2 * PAD, MAP_H + 2 * PAD

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
# Finer than the former .6 px tolerance: the Atlantic frame has long, exposed
# coast runs and is rendered at desktop scale.
TOL = float(sys.argv[7]) if len(sys.argv) > 7 else .2
M = 8  # degrees of slack so coastlines run off the frame edge instead of stopping short
edge_counts = {}
for f in d['features']:
    iso = f['properties']['ADM0_A3']; g = f['geometry']
    polys = g['coordinates'] if g['type'] == 'MultiPolygon' else [g['coordinates']]
    parts, best = [], (0, None)
    for pl in polys:
        ring0 = pl[0]
        # Keep unsimplified source edges for a dissolved outer coastline. Shared
        # country borders occur twice and are excluded from the coast linework.
        if any(LON0 - M < lo < LON1 + M and LAT0 - M < la < LAT1 + M for lo, la in ring0):
            for a, b in zip(ring0, ring0[1:]):
                ka, kb = tuple(a), tuple(b)
                key = tuple(sorted((ka, kb)))
                edge_counts[key] = edge_counts.get(key, 0) + 1
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

# Coastline paths use Natural Earth polygon edges with shared country borders
# dissolved away. SVG clipPath in the renderer trims these to the frame without
# creating a stroke along the frame edge.
coast_edges = [edge for edge, count in edge_counts.items() if count == 1]
adj = {}
for i, (a, b) in enumerate(coast_edges):
    adj.setdefault(a, []).append(i); adj.setdefault(b, []).append(i)
unused = set(range(len(coast_edges)))
coast_parts = []
while unused:
    # Start at an open end where possible; otherwise walk a closed island ring.
    seed = min(unused, key=lambda i: (len(adj[coast_edges[i][0]]) == 2, i))
    a, b = coast_edges[seed]
    cur = a if len(adj[a]) != 2 else b if len(adj[b]) != 2 else a
    chain, prev = [cur], None
    while True:
        nxt = next((i for i in adj[cur] if i in unused), None)
        if nxt is None: break
        unused.remove(nxt)
        u, v = coast_edges[nxt]
        dest = v if u == cur else u
        chain.append(dest); prev, cur = cur, dest
        if cur == chain[0]: break
    pts = [proj(*p) for p in chain]
    if len(pts) > 2:
        h = len(pts) // 2
        pts = dp(pts[:h + 1], TOL)[:-1] + dp(pts[h:], TOL)
    if len(pts) > 1:
        coast_parts.append('M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in pts))

json.dump({'proj': {'LON0': LON0, 'LAT1': LAT1, 'KX': KX, 'S': S, 'OX': OX, 'OY': OY,
                    'W': W, 'H': H, 'MAP_W': MAP_W, 'MAP_H': MAP_H, 'PAD': PAD},
           'c': out, 'coast': ''.join(coast_parts)}, open(f'frame_{name}.json', 'w'))
print(name, len(out), 'countries', f'{W:.0f}x{H:.0f}', f'map {MAP_W:.0f}x{MAP_H}',
      'pad', PAD, sum(len(v['d']) for v in out.values()), 'chars')
