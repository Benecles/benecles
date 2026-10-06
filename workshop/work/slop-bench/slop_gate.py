#!/usr/bin/env python3
"""SLOP gate, one command (CEO, 06/10). Wires the pieces Codex built in SLOP-2.

  python3 work/slop-bench/slop_gate.py PAGE.html [--out DIR] [--mode conform|preserve]

1. Runs protocols/tools/slop_lint.py (deterministic layer) and saves lint.json.
2. Assembles critic_input.md for a *separate* reviewer model: critic_prompt.md + STYLE.md +
   Writing Standard Part D + the lint findings + the page's visible text.
3. The reviewer returns spans JSON (see critic_prompt.md). The writer applies span patches ONLY,
   then re-runs this gate. Never rewrite unflagged text (Writing Standard Part D preamble).
"""
import argparse, json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'protocols', 'tools'))
from slop_lint import lint, text_of
from marks_lint import check as marks_check

ap = argparse.ArgumentParser(); ap.add_argument('page'); ap.add_argument('--out'); ap.add_argument('--mode', default='conform')
a = ap.parse_args()
out = a.out or os.path.join(HERE, 'runs', os.path.splitext(os.path.basename(a.page))[0])
os.makedirs(out, exist_ok=True)
res = lint(a.page, None)
json.dump(res, open(os.path.join(out, 'lint.json'), 'w'), ensure_ascii=False, indent=2)
ws = open(os.path.join(ROOT, 'protocols', 'CUFRGS Writing Standard.md')).read()
part_d = ws[ws.index('## Part D.'):ws.index('## Part E.')]
style = open(os.path.join(ROOT, 'protocols', 'STYLE.md')).read()
prompt = open(os.path.join(HERE, 'critic_prompt.md')).read()
lint_lines = '\n'.join(f"- line {f['line']} `{f['rule']}`: “{f['span']}”" for f in res['findings']) or '- none'
with open(os.path.join(out, 'critic_input.md'), 'w') as fh:
    fh.write(f"{prompt}\n\nMode: **{a.mode}**\n\n---\n# STYLE.md\n{style}\n\n---\n# Writing Standard, Part D\n{part_d}\n\n---\n"
             f"# Deterministic findings (review prompts, not verdicts)\n{lint_lines}\n\n---\n# Frozen draft: {os.path.basename(a.page)}\n\n{text_of(a.page).strip()}\n")
marks = marks_check(a.page)
for ln, rule, msg in marks: print(f'  marks line {ln} {rule}: {msg}')
print(f"{res['status']} · {res['finding_count']} lint findings ({res['findings_per_1000']}/1000) · critic input: {os.path.join(out, 'critic_input.md')}")
