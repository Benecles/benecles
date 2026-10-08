#!/usr/bin/env python3
"""Mechanical gate for the current-live plates-2 redo."""
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path('/Users/benecles/Documents/Codex/2026-09-23/you-h/work')
R = ROOT / 'relay-design-2026-09-29'
BASE = ROOT / 'program/ships/baselines/plates-2-r1'
REPORT = Path('/private/tmp/ordenacoes-captures/plates-2-r1/gate-report.json')
GATE = R / 'program/plates-2-r1-GATE.md'
NODE = Path('/Users/benecles/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node')
PUBLISH_COURSES = Path('/Users/benecles/Documents/Codex/2026-09-05/okay-couple-things-so-first-of/work/study-lab-publish/courses')
PAGES = [
    ('direito-constitucional-i', 'aula-01.html'),
    ('direito-constitucional-i', 'aula-03.html'),
    ('direito-latino-americano', 'aula-01.html'),
]

def run(label, args):
    print(f'## {label}')
    result = subprocess.run([str(x) for x in args], cwd=ROOT)
    if result.returncode:
        raise SystemExit(result.returncode)

for course, page in PAGES:
    staged = R / 'site/courses' / course / page
    baseline = BASE / course / page
    if not staged.is_file() or not baseline.is_file():
        raise SystemExit(f'FAIL missing staged page or immutable current-live baseline: {staged} | {baseline}')

run('plate sourcing and current-live text preservation', [
    sys.executable, R / 'd2/check_plate.py', '--baseline-root', BASE,
])
collision_args = [sys.executable, R / 'd2/check_collisions.py', '--report', REPORT]
for course, page in PAGES:
    staged = R / 'site/courses' / course / page
    collision_args += ['--contains', f'/courses/{course}/{page}', '--freshness-page', staged]
run('fresh capture collision and clipping report', collision_args)
report = json.loads(REPORT.read_text())
required_states = {(viewport, theme) for viewport in ('desktop', 'phone') for theme in ('light', 'dark')}
for course, page in PAGES:
    route = f'/courses/{course}/{page}'
    selected = [result for result in report.get('results', []) if result.get('page') == route]
    states = {(result.get('viewport', {}).get('name'), result.get('theme')) for result in selected}
    if len(selected) != 4 or states != required_states:
        raise SystemExit(f'FAIL incomplete selector-only capture states: {route}: {sorted(states)}')
    for result in selected:
        crops = result.get('crops', [])
        crop = next((item for item in crops if item.get('selector') == 'figure.plate'), None)
        if not crop or crop.get('missing') or not crop.get('screenshot') or not (REPORT.parent / crop['screenshot']).is_file():
            raise SystemExit(f'FAIL missing selector crop for {route} {result.get("viewport", {}).get("name")} {result.get("theme")}')
for course, page in PAGES:
    out = ROOT / 'program' / f'plates-2-r1-{course}-{page.removesuffix(".html")}-jank.csv'
    run(f'jank scan {course}/{page}', [
        NODE, R / 'gates/jank.mjs', '--site', R / 'site', '--course', course,
        '--page', page, '--out', out,
    ])

if not GATE.is_file():
    raise SystemExit(f'FAIL missing handoff: {GATE}')
lines = GATE.read_text(errors='replace').splitlines()
for prefix in ('REFERENCE: PASS', 'SHIPCHANGE: ', 'SHIPCHECK: PASS', 'SHIPCROP: ', 'SHIPCOPY: '):
    if not any(line.startswith(prefix) for line in lines):
        raise SystemExit(f'FAIL GATE missing {prefix}')
copies = [line for line in lines if line.startswith('SHIPCOPY: ')]
expected = [f'{course}/{page}' for course, page in PAGES]
expected_copy = [str(R / 'site/courses'), str(PUBLISH_COURSES), str(BASE), ','.join(expected)]
if not any([part.strip() for part in line.split(':', 1)[1].split('|')] == expected_copy for line in copies):
    raise SystemExit('FAIL SHIPCOPY must map exactly the three changed pages to current-live baselines')
crops = next(line for line in lines if line.startswith('SHIPCROP: ')).split(':', 1)[1].strip().split(';')
crops = [crop.strip() for crop in crops if crop.strip()]
if not 1 <= len(crops) <= 3 or any(not Path(crop).is_absolute() for crop in crops) or 'aula-01' not in crops[0]:
    raise SystemExit('FAIL SHIPCROP must list 1–3 absolute paths, with an aula-01 crop first')
print('PASS plates-2-r1 mechanical gate')
