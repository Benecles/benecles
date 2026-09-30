#!/usr/bin/env python3
"""usage: check_register_data.py <course-slug>...  Checks the class-register data in tools/fronts/data/<slug>.json.

The register (below each course's feature drawing) is one shared instrument. Its data lives under `reg`, which
front.py does not render until the register ships, so filling it never changes a live page.

  reg.exams      [{"label": "P1", "date": "07/10", "covers": [href, ...]}, ...]  the course's assessments, in order.
                 label <= 12 chars (the sign carries it; dates/points live on the exam card). date optional (DD/MM).
                 covers lists only the lessons a source (exam card, plano, professor) says it covers; unknown = omit.
                 A lesson no exam covers simply gets no fold mark: a quiet gap, never a guess. Recuperação is not listed.
  reg.units      only for courses whose data has no `units`: [{"label", "title", "lessons": [href, ...]}]
  lesson.reg     {"does": "..."}  on every lesson row (units[].lessons[] or lessons[])
     does  = what the lesson lets the reader DO: one line, max 90 chars, starting with an INFINITIVE
             (Distinguir…, Montar…, Classificar…; never imperative "Distinga…"). Function, not description:
             never "A aula…", "Estuda…", "Apresenta…".
FAIL on any missing/invalid field. The check is presence and shape only; whether a line is good is the gate's call."""
import json, os, re, sys
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
BANNED = re.compile(r'^(a aula|esta aula|nesta aula|estuda|apresenta|aborda|trata|introdu[çz]|vis[ãa]o geral|o que [ée])', re.I)
INFINITIVE = re.compile(r'^(P[ôo]r|\w+(ar|er|ir|or))\b', re.I)
bad = 0
def fail(s, msg):
    global bad; bad += 1; print(f'FAIL {s}: {msg}')
for slug in sys.argv[1:]:
    d = json.load(open(os.path.join(DATA, slug + '.json'), encoding='utf-8'))
    reg = d.get('reg') or {}
    lessons = [l for u in d.get('units', []) for l in u.get('lessons', [])] or d.get('lessons', [])
    hrefs = {l['href'] for l in lessons}
    exams = reg.get('exams')
    if not (isinstance(exams, list) and exams): fail(slug, 'reg.exams missing'); exams = []
    for e in exams:
        if not isinstance(e, dict) or not e.get('label'): fail(slug, f'reg.exams entry needs a label: {e!r}'); continue
        if len(e['label']) > 12: fail(slug, f'exam label "{e["label"]}" > 12 chars')
        if e.get('date') and not re.fullmatch(r'\d{2}/\d{2}', e['date']): fail(slug, f'exam date "{e["date"]}" not DD/MM')
        for h in e.get('covers', []):
            if h not in hrefs: fail(slug, f'exam {e["label"]} covers unknown lesson {h}')
    if not d.get('units'):
        listed = [h for u in reg.get('units', []) for h in u.get('lessons', [])]
        if not reg.get('units'): fail(slug, 'no units: reg.units required')
        elif sorted(listed) != sorted(hrefs): fail(slug, 'reg.units must list every lesson href exactly once')
        for u in reg.get('units', []):
            if not (u.get('label') and u.get('title')): fail(slug, f'reg.units entry missing label/title: {u}')
    for l in lessons:
        r = l.get('reg') or {}; does = (r.get('does') or '').strip(); h = l.get('href')
        if 'exam' in r: fail(slug, f'{h}: reg.exam is retired; list the lesson in reg.exams[].covers')
        if not does: fail(slug, f'{h}: reg.does missing'); continue
        if len(does) > 90: fail(slug, f'{h}: reg.does {len(does)} chars > 90')
        if BANNED.match(does): fail(slug, f'{h}: reg.does describes instead of saying what it lets you do: "{does[:40]}"')
        if not INFINITIVE.match(does): fail(slug, f'{h}: reg.does must start with an infinitive: "{does[:30]}"')
    print(f'{slug}: {len(lessons)} lessons checked')
sys.exit(1 if bad else 0)
