"""Latam figure pass (Claude, 05/10): four text-in-cells / box figures recast as instruments.
A01 Fig. 2  · two-axis field: the three founding projects, the fusions, and the empty corner the winner took.
A03 Fig. 1  · the text of art. 1º § 1º and what each reading of "conexos" covers.
A04 Fig. 1  · each reform's sheet marked up by the Corte Constitucional: stays / struck / conditioned.
A07 Fig. 1  · two remedies as lanes in time: T-153 leaves the Court; ADPF 347 comes back to it."""
import sys
from fk import svg, T, H, L, R, dot, replace_panels, set_caption

# ------------------------------------------------------------------ A01 · the field
FX0, FX1, FY0, FY1 = 110, 560, 96, 506          # plot box
MX, MY = (FX0 + FX1) / 2, (FY0 + FY1) / 2
PROJ = {  # name, position, constitutions (two short lines)
    'CON': ('CONSERVADOR', (215, 392), 'CHL 1823 · COL 1843', 'MÉX 1843 · PER 1839'),
    'REP': ('REPUBLICANO', (215, 180), 'VEN 1811 · MÉX 1814', 'PER 1823 · EQU 1830'),
    'LIB': ('LIBERAL', (455, 236), 'ARG 1826 · CHL 1828', 'PER 1828 · URY 1830'),
}
def field(active=(), fusion=None):
    o = R(FX0, FY0, FX1 - FX0, FY1 - FY0, 'none', 'ink', 1.2)
    o += L(f'M{MX} {FY0}V{FY1}M{FX0} {MY}H{FX1}', 'grid', 1, 1, '3 5')
    # axes, named at their ends
    o += T(FX0, FY1 + 24, 'RESTRITOS', 13, 'muted') + T(FX1, FY1 + 24, 'INVIOLÁVEIS', 13, 'muted', 'end')
    o += T(MX, FY1 + 54, 'DIREITOS INDIVIDUAIS', 13, 'ink2', 'middle', 600)
    o += T(FX0 + 10, FY0 + 22, 'PODER DA MAIORIA', 13, 'muted') + T(FX0 + 10, FY1 - 12, 'PODER DO EXECUTIVO', 13, 'muted')
    if fusion == 'CR':      # conservatives + radical republicans: the left half (no inviolable rights)
        o += R(FX0 + 4, FY0 + 4, MX - FX0 - 8, FY1 - FY0 - 8, 'conc', 'none', 0)
    if fusion == 'RL':      # republicans + liberals: the upper half (against the concentrated Executive)
        o += R(FX0 + 4, FY0 + 4, FX1 - FX0 - 8, MY - FY0 - 8, 'dif', 'none', 0)
    if fusion == 'LC':      # the winner: the corner none of the three occupied
        o += R(MX + 4, MY + 4, FX1 - MX - 8, FY1 - MY - 8, 'concs', 'none', 0, .18)
        o += L(f'M{MX + 4} {MY + 4}h{FX1 - MX - 8}v{FY1 - MY - 8}h-{FX1 - MX - 8}z', 'conc', 2)
        o += T(FX1 - 16, FY1 - 52, 'DIREITOS AMPLOS', 15, 'conc', 'end', 700) + T(FX1 - 16, FY1 - 24, 'PRESIDENTE FORTE', 15, 'conc', 'end', 700)
    for k, (name, (x, y), c1, c2) in PROJ.items():
        on = k in active or not active
        o += dot(x, y, 8, 'ink' if on else 'muted')
        o += T(x, y - 18, name, 15, 'ink' if on else 'muted', 'middle', 700)
        if not fusion:
            o += T(x, y + 32, c1, 13, 'ink2', 'middle') + T(x, y + 56, c2, 13, 'ink2', 'middle')
    return o
A01 = {
    'p-pj0': svg('p-pj0', 'Os três projetos no campo', 'TRÊS PROJETOS', field(), on=True),
    'p-pj1': svg('p-pj1', 'Conservadores e republicanos', 'A FUSÃO IMPROVÁVEL', field(('CON', 'REP'), 'CR')),
    'p-pj2': svg('p-pj2', 'Republicanos e liberais', 'A FUSÃO ANTIBOLIVARIANA', field(('REP', 'LIB'), 'RL')),
    'p-pj3': svg('p-pj3', 'Liberais e conservadores', 'A FUSÃO QUE VENCEU', field(('LIB', 'CON'), 'LC')),
}

# ------------------------------------------------------------------ A03 · art. 1º § 1º and two readings
def statute():
    o = R(36, 64, 528, 130, 'paper2', 'none', 0)
    o += T(52, 92, 'LEI 6.683/1979 · ART. 1º, § 1º', 13, 'ink', weight=700)
    o += H(52, 122, '“Consideram-se conexos [...] os crimes', 19)
    o += H(52, 152, 'de qualquer natureza relacionados com crimes', 19)
    o += H(52, 182, 'políticos ou praticados por motivação política.”', 19)
    return o
COLS = [(50, 'OPOSITORES', ['crime político', 'crime conexo']),
        (318, 'AGENTES DO ESTADO', ['tortura de presos', 'desaparecimento'])]
def reading(wide):
    o = statute()
    o += H(300, 226, '“conexos”', 22, 'conc', 'middle')
    o += L('M300 234V252', 'conc', 1.6)
    for i, (x, head, acts) in enumerate(COLS):
        covered = (i == 0) or wide
        o += T(x, 286, head, 14, 'ink', weight=700)
        for j, a in enumerate(acts):
            y = 330 + j * 56
            o += R(x, y - 26, 232, 40, 'conc' if covered else 'paper', 'conc' if covered else 'grid', 1.4)
            o += T(x + 14, y, a.upper(), 14, 'ink' if covered else 'muted')
    span = 532 if wide else 264
    o += L(f'M50 450v14h{span - 18}v-14', 'conc', 2)
    o += T(50 + (span - 18) / 2, 494, 'A ANISTIA ALCANÇA', 14, 'conc', 'middle', 700)
    o += H(50 + (span - 18) / 2, 524, 'bilateral' if wide else 'só os opositores', 22, 'conc', 'middle')
    if wide:
        o += T(50, 566, '§ 2º: EXCETO OS JÁ CONDENADOS', 13, 'muted')
    return o
A03 = {
    'p-rd0': svg('p-rd0', 'A leitura da OAB', 'A LEITURA DA OAB · CONEXÃO EXIGE VÍNCULO', reading(False), on=True),
    'p-rd1': svg('p-rd1', 'A leitura do relator', 'EROS GRAU · A LEI-MEDIDA DE 1979', reading(True)),
}

# ------------------------------------------------------------------ A04 · the reform's sheet, marked up
def sheet(head, sub, rows, verdict):
    """rows: (item, mark, note) with mark in {'fica', 'cai', 'cond', 'muted'}"""
    o = R(36, 60, 528, 120 + len(rows) * 74 + 50, 'paper', 'ink', 1.4)
    o += T(56, 94, head, 15, 'ink', weight=700) + T(56, 118, sub, 13, 'muted')
    o += L('M56 134H544', 'ink', 1, .5)
    y = 172
    for item, mark, note in rows:
        tone = {'fica': 'ink', 'cai': 'conc', 'cond': 'conc', 'muted': 'muted'}[mark]
        deco = ';text-decoration:line-through' if mark == 'cai' else ''
        o += T(56, y, item, 15, tone, weight=600, extra=deco)
        if mark == 'cond':
            o += L(f'M46 {y - 14}V{y + 30}', 'conc', 3)
        o += H(56, y + 28, note, 19, 'conc' if mark in ('cai', 'cond') else 'ink2')
        y += 74
    o += L(f'M56 {y - 22}H544', 'ink', 1, .5) + T(56, y + 8, verdict, 14, 'dif', weight=700)
    return o
A04 = {
    'p-dc0': svg('p-dc0', 'C-579/2013', 'C-579/2013 · MARCO JURÍDICO', sheet(
        'ACTO LEGISLATIVO 01/2012', 'julgado em 28/08/2013', [
            ('SELECIONAR E PRIORIZAR', 'fica', 'legítimo, em nome da paz'),
            ('RENUNCIAR À PERSECUÇÃO', 'cond', 'só dos não selecionados'),
            ('MÁXIMOS RESPONSÁVEIS', 'cond', 'esses têm de ser julgados'),
            ('DIREITOS DAS VÍTIMAS', 'fica', 'verdade, justiça, reparação'),
        ], 'NÃO SUBSTITUI A CONSTITUIÇÃO'), on=True, vb='0 0 600 540'),
    'p-dc1': svg('p-dc1', 'C-694/2015', 'C-694/2015 · JUSTIÇA E PAZ', sheet(
        'LEI 1.592/2012', 'julgada em 11/11/2015', [
            ('PRIORIZAR CASOS', 'fica', 'priorizar não é excluir'),
            ('MACROCRIMINALIDADE', 'fica', 'a estrutura, não o caso isolado'),
            ('OUTROS DISPOSITIVOS', 'muted', 'inibida ou remete a precedentes'),
            ('REPARAÇÃO EM OUTRO PROCESSO', 'fica', 'fica; Calle diverge'),
        ], 'EXEQUÍVEL NOS CARGOS EXAMINADOS'), vb='0 0 600 540'),
    'p-dc2': svg('p-dc2', 'C-674/2017', 'C-674/2017 · A JEP', sheet(
        'ACTO LEGISLATIVO 01/2017', 'julgado em 14/11/2017', [
            ('JEP OBRIGATÓRIA A CIVIS', 'cai', 'juiz natural: só voluntária'),
            ('TUTELA RESTRITA', 'cai', 'a JEP não fica imune'),
            ('ESTRANGEIROS NAS SALAS', 'cai', 'só como amicus curiae'),
            ('PENA ESPECIAL', 'cond', 'só com verdade e reparação'),
        ], 'A ARQUITETURA FICA; QUATRO LIMITES'), vb='0 0 600 540'),
}

# ------------------------------------------------------------------ A07 · two remedies in time
CY, EY = 150, 330          # lanes: the Court, the executive / control bodies
def lanes(case, sub):
    o = T(36, 76, case, 15, 'ink', weight=700) + T(36, 104, sub, 13, 'muted')
    o += T(564, CY - 14, 'CORTE', 13, 'muted', 'end') + L(f'M36 {CY}H564', 'grid', 1.2)
    o += T(564, EY - 14, 'QUEM EXECUTA', 13, 'muted', 'end') + L(f'M36 {EY}H564', 'grid', 1.2)
    return o
def t153():
    o = lanes('T-153/1998 · COLÔMBIA', 'ordens diretas, prazos, deveres')
    o += dot(80, CY, 7) + T(80, CY - 16, 'SENTENÇA', 13, 'ink', 'middle', 700)
    o += L(f'M80 {CY}C130 {CY} 130 {EY} 180 {EY}H330', 'ink', 2.6)
    o += L(f'M330 {EY}H560', 'ink', 2.6, .35, '4 6')
    o += T(196, EY + 30, 'DEFENSORÍA · PROCURADURÍA', 13, 'ink')
    o += H(560, CY + 64, 'o caso não volta à Corte', 22, 'conc', 'end')
    o += L(f'M330 {CY}H560', 'conc', 1.6, 1, '2 6')
    return o
def adpf():
    # relative durations: 6 months, 6 months, up to 3 years (36) → 48 units over 440 px
    u = 440 / 48
    x0 = 100; a = x0 + 6 * u; b = a + 6 * u; c = b + 36 * u
    o = lanes('ADPF 347 · MÉRITO, 2023', 'objetivos e monitoramento')
    o += dot(60, CY, 7) + T(60, CY - 16, 'STF', 13, 'ink', 'middle', 700)
    o += L(f'M60 {CY}C80 {CY} 80 {EY} {x0} {EY}H{a:.0f}', 'dif', 2.6)
    o += L(f'M{a:.0f} {EY}C{a + 20:.0f} {EY} {a + 20:.0f} {CY} {a + 30:.0f} {CY}C{a + 40:.0f} {CY} {a + 40:.0f} {EY} {a + 60:.0f} {EY}H{c:.0f}', 'dif', 2.6)
    o += dot(a + 30, CY, 6, 'dif') + T(a + 30, CY - 16, 'HOMOLOGA', 13, 'dif', 'middle', 700)
    for k, (x1, x2, lab, sub) in enumerate(((x0, a, '6 MESES', 'plano nacional'), (a + 60, b + 60, '6 MESES', 'estados e DF'), (b + 60, c, 'ATÉ 3 ANOS', 'implementação'))):
        dy = 56 if k == 1 else 0
        o += L(f'M{x1:.0f} {EY + 18}V{EY + 26}H{x2:.0f}V{EY + 18}', 'dif', 1.4)
        if dy: o += L(f'M{(x1 + x2) / 2:.0f} {EY + 30}V{EY + 30 + dy}', 'dif', 1, .6)
        o += T((x1 + x2) / 2, EY + 50 + dy, lab, 13, 'dif', 'middle', 700) + T((x1 + x2) / 2, EY + 76 + dy, sub, 13, 'ink2', 'middle')
    o += T(c, EY + 132, 'DMF/CNJ ACOMPANHA', 13, 'ink', 'end')
    o += H(c, CY + 64, 'a decisão vira processo', 22, 'dif', 'end')
    return o
A07 = {
    'p-rm0': svg('p-rm0', 'T-153: ordens e acompanhamento fraco', 'DOIS REMÉDIOS · QUEM ACOMPANHA', t153(), on=True, vb='0 0 600 480'),
    'p-rm1': svg('p-rm1', 'ADPF 347: planos, homologação, monitoramento', 'DOIS REMÉDIOS · QUEM ACOMPANHA', adpf(), vb='0 0 600 480'),
}

JOBS = {'aula-01.html': (A01, 'p-pj0', 'Fig. 2 · Os projetos fundacionais e suas fusões'),
        'aula-03.html': (A03, 'p-rd0', 'Fig. 1 · Duas leituras de “conexos”'),
        'aula-04.html': (A04, 'p-dc0', 'Fig. 1 · A Corte e a transição'),
        'aula-07.html': (A07, 'p-rm0', 'Fig. 1 · Dois remédios estruturais')}

if __name__ == '__main__':
    d = sys.argv[1]
    for f, (panels, first, cap) in JOBS.items():
        p = f'{d}/{f}'; h = open(p).read()
        h = replace_panels(h, panels)
        h = set_caption(h, first, cap)
        open(p, 'w').write(h)
        print('ok', f)
