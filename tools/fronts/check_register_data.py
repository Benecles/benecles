#!/usr/bin/env python3
"""usage: check_register_data.py <course-slug>...  Checks the class-register data in tools/fronts/data/<slug>.json.

The register (below each course's feature drawing) is one shared instrument. Its data lives under `reg`, which
front.py does not render until the register ships, so filling it never changes a live page.

  reg.exams      ["P1", "P2", ...]  the course's assessments, in order (from the plano de ensino / exam card)
  reg.units      only for courses whose data has no `units`: [{"label", "title", "lessons": [href, ...]}]
  lesson.reg     {"does": "...", "exam": "P1"}  on every lesson row (units[].lessons[] or lessons[])
     does  = what the lesson lets the reader DO, one line, starting with a verb (Distinguir…, Montar…, Reconhecer…).
             Function, not description: never "A aula…", "Esta aula…", "Estuda…", "Apresenta…". Max 90 chars.
     exam  = which of reg.exams this lesson is assessed in.
FAIL on any missing/invalid field. The check is presence and shape only; whether a line is good is the gate's call."""
import json, os, re, sys
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
BANNED = re.compile(r'^(a aula|esta aula|nesta aula|estuda|apresenta|aborda|trata|introdu[çz]|vis[ãa]o geral|o que [ée])', re.I)
bad = 0
def fail(s, msg):
    global bad; bad += 1; print(f'FAIL {s}: {msg}')
for slug in sys.argv[1:]:
    d = json.load(open(os.path.join(DATA, slug + '.json'), encoding='utf-8'))
    reg = d.get('reg') or {}
    exams = reg.get('exams')
    if not (isinstance(exams, list) and exams): fail(slug, 'reg.exams missing'); exams = []
    lessons = [l for u in d.get('units', []) for l in u.get('lessons', [])] or d.get('lessons', [])
    if not d.get('units'):
        hrefs = [h for u in reg.get('units', []) for h in u.get('lessons', [])]
        if not reg.get('units'): fail(slug, 'no units: reg.units required')
        elif sorted(hrefs) != sorted(l['href'] for l in lessons): fail(slug, 'reg.units must list every lesson href exactly once')
        for u in reg.get('units', []):
            if not (u.get('label') and u.get('title')): fail(slug, f'reg.units entry missing label/title: {u}')
    for l in lessons:
        r = l.get('reg') or {}; does = (r.get('does') or '').strip(); h = l.get('href')
        if not does: fail(slug, f'{h}: reg.does missing'); continue
        if len(does) > 90: fail(slug, f'{h}: reg.does {len(does)} chars > 90')
        if BANNED.match(does): fail(slug, f'{h}: reg.does describes instead of saying what it lets you do: "{does[:40]}"')
        if r.get('exam') not in exams: fail(slug, f'{h}: reg.exam {r.get("exam")!r} not in reg.exams')
    print(f'{slug}: {len(lessons)} lessons checked')
sys.exit(1 if bad else 0)
