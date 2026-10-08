"""Aula 08 · Fig. 1 (T-025 orders on a true-proportion calendar) and Fig. 2 (Auto 176: the money's path).
Replaces a calendar drawn as a text list in empty space, and a ledger whose panels had lost all their text."""
import sys
from fk import svg, T, H, L, R, dot, replace_panels, set_caption

# ---------- Fig. 1: 22/01/2004 → 22/01/2005, 490 px for 366 days (2004 is a leap year)
X0, SPAN = 70, 490
def px(d): return round(X0 + d * SPAN / 366, 1)
ROWS = [  # key, days, label, end date
    ('15d', 15, '15 DIAS · RESPONDER PEDIDOS', '06/02'),
    ('mar', 69, '31/03 · MEDIR A POLÍTICA', '31/03'),
    ('3m', 91, '3 MESES · CAPACIDADE', '22/04'),
    ('6m', 182, '6 MESES · O MÍNIMO', '22/07'),
    ('1a', 366, '1 ANO · META ORÇAMENTÁRIA', '22/01/2005'),
]
def calendar(active):
    o = L(f'M{X0} 112H{X0 + SPAN}', 'ink', 1.4)
    for d, m in ((39, 'MAR'), (131, 'JUN'), (223, 'SET'), (314, 'DEZ')):   # first day of the month, days since 22/01
        o += L(f'M{px(d)} 106V118', 'ink', 1.2) + T(px(d), 98, m, 13, 'muted', 'middle')
    o += L(f'M{X0} 104V530', 'ink', 1.4, .5, '2 4') + T(X0, 566, 'T-025 · 22/01/2004', 14, 'ink', 'start', 600)
    for i, (k, d, lab, end) in enumerate(ROWS):
        y = 160 + i * 82
        on = k in active
        fill = 'concs' if on else 'grey'
        o += T(X0, y - 10, lab, 15, 'conc' if on else 'ink2', weight=600 if on else 400)
        o += R(X0, y, px(d) - X0, 14, fill, 'none', 0)
        o += T(X0 + 8, y + 36, 'até ' + end, 13, 'muted')
    return o
FIG1 = {
    'p-ck0': svg('p-ck0', '15 dias para responder', 'AS ORDENS DA T-025 NO CALENDÁRIO', calendar({'15d'}), on=True),
    'p-ck1': svg('p-ck1', 'Medir e corrigir a máquina', 'AS ORDENS DA T-025 NO CALENDÁRIO', calendar({'mar', '3m'})),
    'p-ck2': svg('p-ck2', 'Seis meses para o mínimo', 'AS ORDENS DA T-025 NO CALENDÁRIO', calendar({'6m'})),
    'p-ck3': svg('p-ck3', 'Um ano para a meta orçamentária', 'AS ORDENS DA T-025 NO CALENDÁRIO', calendar({'1a'})),
}

# ---------- Fig. 2: the money's path, with the six cuts placed where they act, then the three failures
N = (250, 230)                     # the budget node
SRC = [('NAÇÃO', 150), ('TERRITÓRIOS', 230), ('COOPERAÇÃO', 310)]
MAIN_Y, GEN_Y = 340, 150
DOT_X, EXE_X, END_X = 378, 492, 560

def flow(fail=False):
    o = ''
    for i, (name, y) in enumerate(SRC):
        broken = fail and i > 0
        if broken:   # territorial and international transfers that may not arrive
            o += L(f'M40 {y}H118', 'ink', 2.4) + L(f'M136 {y}H150C200 {y} 205 {N[1]} {N[0]} {N[1]}', 'ink', 2.4)
            o += L(f'M122 {y - 9}l6 18M132 {y - 9}l6 18', 'conc', 2)
        else:
            o += L(f'M40 {y}H150C200 {y} 205 {N[1]} {N[0]} {N[1]}', 'ink', 2.4)
        o += T(40, y - 10, name, 14, 'ink')
    o += dot(*N, 6)
    # (f): general programmes split off, the displaced line continues
    o += L(f'M{N[0]} {N[1]}C300 {N[1]} 300 {GEN_Y} 350 {GEN_Y}H{END_X}', 'ink2', 2, .7, '6 5')
    o += T(END_X, GEN_Y - 10, 'PROGRAMAS GERAIS', 14, 'ink2', 'end')
    o += L(f'M{N[0]} {N[1]}C300 {N[1]} 300 {MAIN_Y} 350 {MAIN_Y}', 'ink', 3)
    if fail:
        o += L(f'M350 {MAIN_Y}H{DOT_X - 10}M{DOT_X + 10} {MAIN_Y}H{EXE_X - 10}M{EXE_X + 10} {MAIN_Y}H{END_X}', 'ink', 3)
        for x in (DOT_X, EXE_X):
            o += L(f'M{x - 7} {MAIN_Y - 10}l4 20M{x + 3} {MAIN_Y - 10}l4 20', 'conc', 2)
    else:
        o += L(f'M350 {MAIN_Y}H{END_X}', 'ink', 3) + dot(DOT_X, MAIN_Y, 5) + dot(EXE_X, MAIN_Y, 5)
    o += dot(END_X, MAIN_Y, 6)
    o += T(DOT_X, MAIN_Y - 14, 'DOTAÇÃO', 14, 'ink', 'middle') + T(EXE_X, MAIN_Y - 14, 'EXECUÇÃO', 14, 'ink', 'middle')
    o += T(END_X, MAIN_Y + 56, 'DESLOCADOS', 14, 'ink', 'end', 600)
    return o

def cuts():
    tag = lambda x, y, s, tone='dif': T(x, y, s, 15, tone, 'middle', 700)
    o = tag(96, 340, '(b)')                         # by source
    o += tag(334, 252, '(f)', 'conc')               # general × displaced
    o += tag(DOT_X, MAIN_Y + 30, '(e)')             # by component
    o += tag(EXE_X - 10, MAIN_Y + 30, '(c)(d)')      # who obtains / executes, each entity's budget
    o += L(f'M40 470H{END_X}', 'dif', 1.6) + L(f'M40 462V478M{END_X} 462V478', 'dif', 1.6)
    o += T(300, 500, '(a) CADA EXERCÍCIO FISCAL', 14, 'dif', 'middle')
    return o

def failures():
    o = T(40, 380, 'REPASSE NÃO CHEGA', 14, 'conc', weight=600) + H(40, 412, 'plano de contingência', 19, 'conc')
    o += T(DOT_X, 446, 'SEM DOTAÇÃO', 14, 'conc', 'middle', 600) + H(DOT_X, 478, 'prioridade', 19, 'conc', 'middle')
    o += T(EXE_X + 60, 520, 'NÃO EXECUTA', 14, 'conc', 'end', 600) + H(EXE_X + 60, 552, 'falha administrativa', 19, 'conc', 'end')
    return o

FIG2 = {
    'p-tr0': svg('p-tr0', 'Seis cortes no mesmo dinheiro', 'AUTO 176/2005 · O CAMINHO DO DINHEIRO', flow() + cuts(), on=True),
    'p-tr1': svg('p-tr1', 'Três falhas com o mesmo nome', 'AUTO 176/2005 · ONDE O DINHEIRO PARA', flow(fail=True) + failures()),
}

if __name__ == '__main__':
    p = sys.argv[1]
    h = open(p).read()
    h = replace_panels(h, {**FIG1, **FIG2})
    h = set_caption(h, 'p-tr0', 'Fig. 2 · Auto 176: o caminho do dinheiro')
    open(p, 'w').write(h)
    print('a08 figs ok')
