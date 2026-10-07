"""Aula 18 house figures: the real paternity case and the Q11 proof sequence."""
from pathlib import Path
import inject
import figkit

PAGE = 'courses/processo-civil-i/aula-18.html'


def case_panel():
    """The cited REsp separates refusal of DNA from the minimum circumstantial indicia."""
    o = figkit.t(64, 36, 'STJ · REsp 692.242/MG', size=11, fill='var(--ink-2)', weight=700)
    o += figkit.line(64, 51, 536, 51, tone='ink', w=1.2)
    o += figkit.t(154, 90, 'DADO PROCESSUAL', size=10, fill='var(--conc)', anchor='middle', weight=700)
    o += figkit.t(154, 128, 'RECUSA AO', size=16, anchor='middle', weight=700, ls='.02em')
    o += figkit.t(154, 151, 'EXAME DE DNA', size=16, anchor='middle', weight=700, ls='.02em')
    o += figkit.t(300, 143, '≠', size=25, fill='var(--conc)', anchor='middle', weight=600, ls='0')
    o += figkit.t(446, 90, 'FATO A DEMONSTRAR', size=10, fill='var(--ink-2)', anchor='middle', weight=700)
    o += figkit.t(446, 128, 'RELAÇÃO ÍNTIMA', size=14, anchor='middle', weight=700, ls='.02em')
    o += figkit.t(446, 151, 'MÃE E SUPOSTO PAI', size=11, anchor='middle', weight=600, ls='.01em')
    o += figkit.line(64, 181, 536, 181, tone='ink', w=1)
    o += figkit.line(154, 173, 154, 189, tone='conc', w=2)
    o += figkit.line(446, 173, 446, 189, tone='dif', w=2)
    o += figkit.t(300, 225, 'INDÍCIOS CIRCUNSTANCIAIS MÍNIMOS', size=12, fill='var(--dif)', anchor='middle', weight=700)
    o += figkit.t(300, 250, 'A recusa não substitui esse suporte', size=11, fill='var(--ink-2)', anchor='middle', weight=500, ls='.01em')
    return figkit.svg('0 0 600 300', o, cls='fig', ident='pci-a18-case',
                      label='No REsp 692.242/MG, a recusa ao exame de DNA não substitui indícios mínimos de relação íntima na investigação de paternidade')


def three_questions_panel():
    """The exam question separates admissibility, necessity, and later evaluation."""
    o = figkit.t(64, 36, 'FATO INVEROSSÍMIL · TRÊS PERGUNTAS', size=11, fill='var(--ink-2)', weight=700)
    o += figkit.line(64, 51, 536, 51, tone='ink', w=1.2)
    xs = (112, 300, 488)
    items = (
        ('01 · MEIO', 'legal e moralmente', 'legítimo?'),
        ('02 · MEDIDA', 'necessária ao mérito?', ''),
        ('03 · RESULTADO', 'que peso os autos', 'sustentam?'),
    )
    o += figkit.line(xs[0], 124, xs[-1], 124, tone='ink', w=1.4)
    for i, (x, (head, line1, line2)) in enumerate(zip(xs, items)):
        tone = 'conc' if i == 0 else ('mix' if i == 1 else 'dif')
        o += figkit.line(x, 108, x, 143, tone=tone, w=2)
        o += f'<circle cx="{x}" cy="124" r="4.5" style="fill:var(--paper);stroke:var(--{tone});stroke-width:1.8"/>'
        o += figkit.t(x, 181, head, size=10.5, fill=f'var(--{tone})', anchor='middle', weight=700)
        o += figkit.t(x, 211, line1, size=11.5, anchor='middle', weight=500, ls='.01em')
        if line2:
            o += figkit.t(x, 231, line2, size=11.5, anchor='middle', weight=500, ls='.01em')
    o += figkit.t(300, 272, 'A plausibilidade inicial não resolve as três etapas', size=10.5,
                  fill='var(--ink-2)', anchor='middle', weight=600, ls='.01em')
    return figkit.svg('0 0 600 300', o, cls='fig', ident='pci-a18-three-questions',
                      label='Três perguntas distintas sobre o fato inverossímil: possibilidade do meio, necessidade da diligência e peso do resultado')


def panels():
    figkit.WARN.clear()
    return [case_panel(), three_questions_panel()]


def install():
    repl = {s.split('id="', 1)[1].split('"', 1)[0]: s for s in panels()}
    return inject.inject(PAGE, repl)


def specimen_page():
    css = (Path(__file__).resolve().parents[2] /
           'courses' / 'processo-civil-i' / 'assets' / 'curso.css').as_uri()
    panels_html = ''.join(f'<section><h2>{svg}</h2><div class="sample">{panel}</div></section>'
                          for svg, panel in zip(('REsp 692.242/MG', 'A questão de exame'), panels()))
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Figkit · Processo Aula 18</title>
<link rel="stylesheet" href="{css}"><style>body{{max-width:1000px;margin:0 auto;padding:28px 18px;background:var(--paper);color:var(--ink)}}h1{{font:750 28px/1.1 var(--sans)}}h2{{font:600 13px var(--mono)}}.sample{{max-width:920px;margin:20px auto 32px;padding:12px;border:1.5px solid var(--ink);background:var(--paper)}}</style></head><body>
<h1>Processo · Aula 18 · figuras de apoio</h1>{panels_html}</body></html>'''


if __name__ == '__main__':
    import os
    probe = os.environ.get('FIGKIT_PROBE')
    if probe:
        Path(probe).write_text(specimen_page(), encoding='utf-8')
        print(probe)
    else:
        print(f'{install()} figure(s) installed')
    print('\n'.join(figkit.WARN) or 'no text warnings')
