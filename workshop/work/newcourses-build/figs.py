"""Genre figures for the new courses (cloud session, 2026-09-29). Each entry is a house scrolly (kit.scrolly):
600×600 panels with kit drawing helpers, one step card per panel. FIGS maps (course, page file) to
{chapter number on that page: function returning the scrolly HTML}; build.py places it after that chapter."""
import kit
from kit import T, R, P, G, box

def src(ref):
    return f'<span class="src" hidden data-src="{ref}"></span>'

def S(panel, label, h3, body, lcls=''):
    return dict(panel=panel, label=label, lcls=lcls, h3=h3, body=body)

FIGS = {}

# ---- PC Aula 07 · genre: calendar. The 2025 P1 count: embargos interrupt the appeal deadline (CPC 224, 1.026)
import datetime as _dt
def _cal(k):
    """k = 0 embargos window, 1 interruption and restart, 2 appeal deadline and the trap."""
    D = _dt.date
    start = D(2025, 9, 1)
    x0, y0, cw, ch = 30, 96, 77, 72
    o = T(30, 44, 'SETEMBRO · OUTUBRO DE 2025', 't-small', style='letter-spacing:.1em')
    for i, d in enumerate(['SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SÁB', 'DOM']):
        o += T(x0 + i * cw + cw / 2, 80, d, 't-small', anchor='middle', style='letter-spacing:.08em;fill:var(--ink-2)')
    ev = {}
    if k == 0:
        ev = {D(2025, 9, 4): ('conc', 'disponível'), D(2025, 9, 5): ('ink', 'publicada'), D(2025, 9, 8): ('dif', 'dia 1'),
              D(2025, 9, 10): ('conc', 'embargos'), D(2025, 9, 12): ('ink', 'dia 5')}
        span = (D(2025, 9, 8), D(2025, 9, 12))
    elif k == 1:
        ev = {D(2025, 9, 10): ('conc', 'embargos'), D(2025, 9, 12): ('conc', 'decisão'), D(2025, 9, 15): ('ink', 'publicada'),
              D(2025, 9, 16): ('dif', 'dia 1')}
        span = (D(2025, 9, 16), D(2025, 9, 16))
    else:
        ev = {D(2025, 9, 16): ('dif', 'dia 1'), D(2025, 9, 26): ('conc', 'armadilha'), D(2025, 10, 6): ('dif', 'dia 15')}
        span = (D(2025, 9, 16), D(2025, 10, 6))
    for w in range(6):
        for dow in range(7):
            d = start + _dt.timedelta(days=w * 7 + dow)
            x, y = x0 + dow * cw, y0 + w * ch
            weekend = dow >= 5
            inspan = span[0] <= d <= span[1] and not weekend
            fill = 'var(--grid-major)' if weekend else ('var(--dif-wash)' if inspan else 'var(--paper)')
            o += R(x, y, cw - 4, ch - 4, 'ink', style=f'fill:{fill};stroke:var(--ink);stroke-width:{1.6 if d in ev else .6}')
            o += T(x + 8, y + 20, str(d.day), 't-small', style=f'font-size:14px;fill:{"var(--ink-2)" if d.month == 10 else "var(--ink)"}')
            if d in ev:
                tone, lab = ev[d]
                col = {'conc': 'var(--conc)', 'dif': 'var(--dif)', 'ink': 'var(--ink)'}[tone]
                o += f'<rect x="{x}" y="{y + ch - 22}" width="{cw - 4}" height="18" style="fill:{col}"/>'
                o += T(x + (cw - 4) / 2, y + ch - 9, lab.upper(), 't-small', anchor='middle', style='fill:var(--paper);font-size:9.5px;letter-spacing:.06em')
    o += T(30, 552, {0: 'Cinco dias úteis para os embargos: de 8 a 12/9.', 1: 'Embargos interrompem: o prazo da apelação recomeça inteiro.',
                     2: 'Quinze dias úteis a partir de 16/9: vence em 06/10.'}[k], 't-small', style='font-size:13px;fill:var(--ink)')
    o += T(30, 574, 'Sem feriados no período (suposição do enunciado).', 't-small', style='fill:var(--ink-2)')
    return o

def fig_pc07():
    ref = 'CPC arts. 219, 224 §§ 2º-3º, 1.003 § 5º, 1.023, 1.026; draft unit-07 "Uma contagem completa"'
    return kit.scrolly('A contagem da questão de 2025, dia a dia', [
        ('p-cal0', _cal(0), 'Prazo dos embargos'), ('p-cal1', _cal(1), 'Interrupção'), ('p-cal2', _cal(2), 'Prazo da apelação')], [
        S('p-cal0', 'Disponibilização e publicação', 'Quinta disponível, sexta publicada, segunda o dia 1',
          '<p>A sentença é disponibilizada no DJe na quinta, 4/9. Considera-se publicada no primeiro dia útil seguinte, a sexta, 5/9 (art. 224, § 2º), e a contagem começa no dia útil seguinte à publicação, a segunda, 8/9 (§ 3º). Os cinco dias úteis dos embargos vão até a sexta, 12/9: os de quarta, 10/9, são tempestivos.</p>' + src(ref), 'conc'),
        S('p-cal1', 'CPC, art. 1.026', 'Os embargos interrompem o prazo da apelação',
          '<p>Os embargos são desprovidos, e a decisão é disponibilizada na sexta, 12/9. Publicada na segunda, 15/9, a contagem começa na terça, 16/9. Interromper é mais que suspender: o prazo da apelação não retoma o saldo, recomeça inteiro.</p>' + src(ref), 'dif'),
        S('p-cal2', 'Quinze dias úteis', 'Vence na segunda, 6 de outubro',
          '<p>Quatro dias na primeira semana, cinco em cada uma das duas seguintes e o último na segunda-feira: 06/10/2025. Quem ignora a interrupção conta desde 8/9 e chega à sexta, 26/9, dez dias corridos antes. É esse o erro que a questão testa.</p>' + src(ref), 'conc'),
    ])

FIGS[('processo-civil', 'aula-07.html')] = {6: fig_pc07}
