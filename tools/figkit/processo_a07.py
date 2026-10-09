"""Aula 07: source certificate and proportional 2017/2 P1 Q1 deadlines.

Run ``python3 tools/figkit/processo_a07.py`` to insert these two generated
panels into the lesson and its polish layer. The certificate remains an
unaltered image asset; the first SVG only crops it and places reading marks.
"""
from __future__ import annotations

import json
from pathlib import Path

from figkit import line, svg, t

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / 'courses/processo-civil-i/aula-07.html'
POLISH = ROOT / 'tools/polish/courses/processo-civil-i/aula-07.html.json'
ASSET = 'assets/aula-07-certidao.png'


def certificate() -> str:
    """Facsimile crops in their printed order, with marks over the source."""
    # Source is 1440 × 2560. The two nested viewBoxes omit the intervening
    # case text while keeping the certificate header, event, and final line.
    upper = (f'<svg x="30" y="20" width="720" height="400" '
             f'viewBox="0 0 1440 800" preserveAspectRatio="none">'
             f'<image href="{ASSET}" width="1440" height="2560"/></svg>')
    lower = (f'<svg x="30" y="438" width="720" height="180" '
             f'viewBox="0 1810 1440 360" preserveAspectRatio="none">'
             f'<image href="{ASSET}" width="1440" height="2560"/></svg>')
    # A restrained reading hand: no transcription, inferred date, or event path.
    marks = (
        '<ellipse cx="545" cy="233" rx="70" ry="19" '
        'style="fill:none;stroke:var(--conc);stroke-width:2.2"/>'
        '<ellipse cx="678" cy="268" rx="36" ry="19" '
        'style="fill:none;stroke:var(--conc);stroke-width:2.2"/>'
        '<ellipse cx="628" cy="303" rx="79" ry="19" '
        'style="fill:none;stroke:var(--conc);stroke-width:2.2"/>'
        '<path d="M82 355L644 355" '
        'style="fill:none;stroke:var(--conc);stroke-width:2.2;stroke-linecap:round"/>'
        '<path d="M216 497L550 497" '
        'style="fill:none;stroke:var(--conc);stroke-width:2.2;stroke-linecap:round"/>'
    )
    panel = svg('0 0 780 638', upper + lower + marks, cls='fig',
               ident='pci-a07-certificate',
               label='Fac-símile da certidão: PODER JUDICIÁRIO, CERTIDÃO; '
                     'Nota nº 1690/2015; disponibilização na edição nº 5561 '
                     'do Diário da Justiça Eletrônico em 21/05/2015; '
                     'fórmula de publicação no primeiro dia útil seguinte; '
                     'certificação em Porto Alegre em 22/05/2015.')
    return panel.replace('<svg id=', '<svg style="display:block;width:100%;height:auto" id=', 1)


def doubled_periods() -> str:
    """One unit scale makes thirty business days twice as long as fifteen."""
    x0, unit = 170, 17
    x15, x30 = x0 + 15 * unit, x0 + 30 * unit
    o = t(x0, 42, '02/03/2018', size=14, weight=700, ls='0')
    o += line(x0, 58, x0, 244, tone='ink', w=1.5)
    o += t(20, 112, 'ODRAUDE', size=15, weight=700, ls='0')
    o += line(x0, 106, x15, 106, tone='ink', w=12)
    o += line(x15, 91, x15, 121, tone='ink', w=2.2)
    o += t(x15, 146, '22/03/2018', size=14, anchor='middle', weight=700, ls='0')
    o += t((x0 + x15) / 2, 87, '15 DIAS ÚTEIS', size=11.5,
           anchor='middle', weight=700)
    o += t(20, 202, 'UFRGS', size=15, weight=700,
           fill='var(--conc)', ls='0')
    o += line(x0, 196, x30, 196, tone='conc', w=12)
    o += line(x30, 181, x30, 211, tone='conc', w=2.2)
    o += t(x30, 236, '13/04/2018', size=14, anchor='middle', weight=700,
           fill='var(--conc)', ls='0')
    o += t((x0 + x30) / 2, 177, '30 DIAS ÚTEIS', size=11.5,
           anchor='middle', weight=700, fill='var(--conc)')
    panel = svg('0 0 775 260', o, cls='fig', ident='pci-a07-periods',
               label='P1 2017/2, questão 1: início comum em 02/03/2018. '
                     'ODRAUDE: 15 dias úteis até 22/03/2018. UFRGS: '
                     '30 dias úteis até 13/04/2018, excluído o feriado '
                     'de 30/03 indicado na prova.')
    return panel.replace('<svg id=', '<svg style="display:block;width:100%;height:auto" id=', 1)


def panels() -> tuple[str, str]:
    return certificate(), doubled_periods()


def insert(s: str) -> str:
    a, b = panels()
    old = '<img src="assets/aula-07-certidao.png" alt="Fac-símile da certidão de publicação da Nota nº 1690/2015">'
    if 'id="pci-a07-certificate"' not in s:
        if s.count(old) != 1:
            raise ValueError('A07 certificate insertion point changed')
        s = s.replace(old, a, 1)
    old = 'O dia final é 13/04.</p>'
    if 'id="pci-a07-periods"' not in s:
        if s.count(old) != 1:
            raise ValueError('A07 deadline insertion point changed')
        figure = (f' <figure class="source-record" style="max-width:900px;margin:32px auto">'
                  f'{b}<figcaption>P1 2017/2 · questão 1 · prazos de contestação</figcaption></figure>')
        s = s.replace(old, old + figure, 1)
    return s


def integrate() -> None:
    before = PAGE.read_text()
    after = insert(before)
    data = json.loads(POLISH.read_text())
    touched = 0
    for op in data:
        old = op['after']
        if '<img src="assets/aula-07-certidao.png"' in old:
            a, _ = panels()
            op['after'] = old.replace(
                '<img src="assets/aula-07-certidao.png" alt="Fac-símile da certidão de publicação da Nota nº 1690/2015">',
                a, 1)
            touched += 1
        elif 'O dia final é 13/04.</p>' in old:
            _, b = panels()
            op['after'] = old.replace(
                'O dia final é 13/04.</p>',
                'O dia final é 13/04.</p> <figure class="source-record" style="max-width:900px;margin:32px auto">'
                + b + '<figcaption>P1 2017/2 · questão 1 · prazos de contestação</figcaption></figure>',
                1)
            touched += 1
    if touched == 0:
        if not all(sum(f'id="{ident}"' in op['after'] for op in data) == 1
                   for ident in ('pci-a07-certificate', 'pci-a07-periods')):
            raise ValueError('A07 polish figures are missing')
    elif touched != 2:
        raise ValueError(f'Expected both A07 polish figure insertions, found {touched}')
    PAGE.write_text(after)
    POLISH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print('A07: inserted 2 inline SVG panels in page and polish layer')


def specimen_sections() -> str:
    a, b = panels()
    return (f'<section class="ref"><h2>Processo · Aula 07 · Certidão</h2>'
            f'<div class="grid"><div class="s">{a}</div></div></section>'
            f'<section class="ref"><h2>Processo · Aula 07 · P1 2017/2</h2>'
            f'<div class="grid"><div class="s">{b}</div></div></section>')


if __name__ == '__main__':
    integrate()
