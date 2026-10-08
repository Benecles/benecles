"""Relief layers for a map frame: hypsometric bands + continental shelf, as SVG paths in the frame's projection.
Elevation: Mapzen/AWS 'Terrarium' open terrain tiles (s3 elevation-tiles-prod), decoded locally.
usage: .venv/bin/python relief.py FRAME_JSON OUT_JSON [zoom] [step_deg]
FRAME_JSON is latam_paths.json or frame_NAME.json (anything with a 'proj' block)."""
import json, math, os, sys, io, urllib.request
import numpy as np
from PIL import Image
import contourpy

fj, outp = sys.argv[1], sys.argv[2]
Z = int(sys.argv[3]) if len(sys.argv) > 3 else 4
STEP = float(sys.argv[4]) if len(sys.argv) > 4 else .2
pj = json.load(open(fj))['proj']
W = pj.get('W', 600); H = pj.get('H', 600)
LON0, LAT1, KX, S, OX, OY = pj['LON0'], pj['LAT1'], pj['KX'], pj['S'], pj['OX'], pj['OY']
LON1 = LON0 + (W - OX) / (KX * S) + 1; LAT0 = LAT1 - (H - OY) / S - 1
LON0b, LAT1b = LON0 - 1, LAT1 + 1

CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tiles'); os.makedirs(CACHE, exist_ok=True)
def tile(z, x, y):
    p = os.path.join(CACHE, f'{z}_{x}_{y}.png')
    if not os.path.exists(p):
        urllib.request.urlretrieve(f'https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png', p)
    a = np.asarray(Image.open(p).convert('RGB')).astype(np.float64)
    return a[..., 0] * 256 + a[..., 1] + a[..., 2] / 256 - 32768

n = 2 ** Z
def mx(lon): return (lon + 180) / 360 * n * 256
def my(lat):
    r = math.radians(max(-85, min(85, lat)))
    return (1 - math.log(math.tan(r) + 1 / math.cos(r)) / math.pi) / 2 * n * 256

lons = np.arange(LON0b, LON1 + STEP, STEP); lats = np.arange(LAT1b, LAT0 - STEP, -STEP)
tx0, tx1 = int(mx(lons[0]) // 256), int(mx(lons[-1]) // 256)
ty0, ty1 = int(my(lats[0]) // 256), int(my(lats[-1]) // 256)
mosaic = np.zeros(((ty1 - ty0 + 1) * 256, (tx1 - tx0 + 1) * 256))
for ty in range(ty0, ty1 + 1):
    for tx in range(tx0, tx1 + 1):
        mosaic[(ty - ty0) * 256:(ty - ty0 + 1) * 256, (tx - tx0) * 256:(tx - tx0 + 1) * 256] = tile(Z, tx % n, ty)
print('tiles', (tx1 - tx0 + 1) * (ty1 - ty0 + 1))
px = np.clip((np.array([mx(l) for l in lons]) - tx0 * 256).astype(int), 0, mosaic.shape[1] - 1)
py = np.clip((np.array([my(l) for l in lats]) - ty0 * 256).astype(int), 0, mosaic.shape[0] - 1)
E = mosaic[np.ix_(py, px)]
# light smoothing so contours read as drawn lines, not pixel stairs
K = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16
Ep = np.pad(E, 1, mode='edge'); E = sum(K[i, j] * Ep[i:i + E.shape[0], j:j + E.shape[1]] for i in range(3) for j in range(3))

X = OX + (lons - LON0) * KX * S; Y = OY + (LAT1 - lats) * S
XX, YY = np.meshgrid(X, Y)
gen = contourpy.contour_generator(XX, YY, E, fill_type=contourpy.FillType.OuterOffset, line_type=contourpy.LineType.Separate)

def dp(pts, tol):
    if len(pts) < 3: return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]; dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy) or 1e-9
    d = np.abs(dy * pts[1:-1, 0] - dx * pts[1:-1, 1] + x2 * y1 - y2 * x1) / L
    i = int(np.argmax(d)) + 1
    if d[i - 1] > tol: return np.vstack([dp(pts[:i + 1], tol)[:-1], dp(pts[i:], tol)])
    return np.array([pts[0], pts[-1]])
def ring(pts, tol=.7):
    h = len(pts) // 2
    return np.vstack([dp(pts[:h + 1], tol)[:-1], dp(pts[h:], tol)])
def pathd(rings, minpts=4, minlen=10):
    out = ''
    for r in rings:
        if len(r) < minpts: continue
        r = ring(np.asarray(r))
        if len(r) < 3 or np.ptp(r[:, 0]) + np.ptp(r[:, 1]) < minlen: continue
        out += 'M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in r) + 'Z'
    return out

res = {'bands': {}, 'lines': {}}
for lo in (500, 1500, 3000, 4500):
    polys, offs = gen.filled(lo, 99999)
    d = ''
    for pts, off in zip(polys, offs):
        rings = [pts[off[i]:off[i + 1]] for i in range(len(off) - 1)]
        d += pathd(rings)
    res['bands'][str(lo)] = d
for lv in (-200, -3000):
    lines = gen.lines(lv)
    res['lines'][str(lv)] = ''.join('M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in ring(np.asarray(l), .9)) for l in lines if len(l) > 6 and np.ptp(l[:, 0]) + np.ptp(l[:, 1]) > 25)
json.dump(res, open(outp, 'w'))
print({k: len(v) for k, v in res['bands'].items()}, {k: len(v) for k, v in res['lines'].items()})

# ---- hachures: short strokes along the fall line, weight by steepness (engraved-atlas relief)
SP = float(os.environ.get('HACH_SP', 4.2))          # px spacing of the sampling lattice
Ex = np.gradient(E, axis=1) / (STEP * KX * 111320)   # dz/dx (m/m)
Ey = np.gradient(E, axis=0) / (-STEP * 111320)       # dz/dy, north-positive
slope = np.hypot(Ex, Ey)
land = slope[E > 150]
Q0, Q1, Q2 = np.quantile(land, [.45, .75, .92])
print('slope quantiles', Q0, Q1, Q2)
rng = np.random.default_rng(7)
segs = {1: [], 2: [], 3: []}
for yy in np.arange(0, H, SP):
    for xx in np.arange(0, W, SP):
        x = xx + rng.uniform(-.35, .35) * SP; y = yy + rng.uniform(-.35, .35) * SP
        j = int((x - OX) / (KX * S) / STEP + (LON0 - LON0b) / STEP); i = int((y - OY) / S / STEP + (LAT1b - LAT1) / STEP)
        if not (0 <= i < E.shape[0] and 0 <= j < E.shape[1]): continue
        if E[i, j] < 150: continue
        sl = slope[i, j]
        if sl < Q0: continue
        # fall line: downslope direction in screen coords (x right, y down)
        gx, gy = -Ex[i, j], Ey[i, j]
        n = math.hypot(gx, gy) or 1
        L = SP * (.55 + .7 * min(1, (sl - Q0) / (Q2 - Q0)))
        dx, dy = gx / n * L / 2, gy / n * L / 2
        w = 1 if sl < Q1 else 2 if sl < Q2 else 3
        segs[w].append(f'M{x - dx:.1f} {y - dy:.1f}L{x + dx:.1f} {y + dy:.1f}')
res['hach'] = {str(k): ''.join(v) for k, v in segs.items()}
json.dump(res, open(outp, 'w'))
print('hachures', {k: len(v) for k, v in segs.items()})
