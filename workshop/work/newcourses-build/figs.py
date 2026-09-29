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

# ---- CI Aula 04 · genre: genealogy. Two lineages of constitutional review and the Brazilian mixed system
def _gen(k):
    """k = 0 US lineage lit, 1 Austrian lineage lit, 2 both converge on Brazil."""
    on = lambda i: (k == i) or k == 2
    o = T(30, 44, 'DE ONDE VEM O CONTROLE BRASILEIRO', 't-small', style='letter-spacing:.1em')
    def root(x, title, sub1, sub2, sub3, tone, lit):
        col = f'var(--{tone})' if lit else 'var(--ink-2)'
        g = f'<rect x="{x}" y="80" width="250" height="150" style="fill:var(--paper);stroke:{col};stroke-width:{2 if lit else 1}"/>'
        g += f'<rect x="{x}" y="80" width="250" height="34" style="fill:{col if lit else "var(--grid-major)"}"/>'
        g += T(x + 16, 103, title, 't-small', style=f'font-size:13px;letter-spacing:.1em;fill:{"var(--paper)" if lit else "var(--ink-2)"}')
        for i, t in enumerate((sub1, sub2, sub3)):
            g += T(x + 16, 146 + i * 26, t, 't-small', style=f'font-size:13px;fill:{"var(--ink)" if lit else "var(--ink-2)"}')
        return g
    o += root(30, 'EUA · 1803', 'Marbury v. Madison', 'todos os juízes: difuso', 'no caso: concreto', 'dif', on(0))
    o += root(320, 'ÁUSTRIA · KELSEN', 'Tribunal Constitucional', 'um só órgão: concentrado', 'a lei em tese: abstrato', 'conc', on(1))
    lit = k == 2
    o += P('M155 230V300H300V330', style=f'fill:none;stroke:{"var(--dif)" if lit else "var(--grid-major)"};stroke-width:{2.5 if lit else 1.5}')
    o += P('M445 230V300H300V330', style=f'fill:none;stroke:{"var(--conc)" if lit else "var(--grid-major)"};stroke-width:{2.5 if lit else 1.5}')
    col = 'var(--ink)' if lit else 'var(--ink-2)'
    o += f'<rect x="60" y="330" width="480" height="240" style="fill:var(--paper);stroke:{col};stroke-width:{2 if lit else 1}"/>'
    o += T(80, 360, 'BRASIL · MODELO MISTO', 't-small', style=f'font-size:13px;letter-spacing:.1em;fill:{col}')
    rows = [('difuso-concreto', 'qualquer juiz, e o STF no recurso extraordinário;', 'efeitos entre as partes, gerais via art. 52, X', 'dif'),
            ('abstrato-concentrado', 'desde a EC 16/1965, só no STF;', 'erga omnes e efeito vinculante', 'conc'),
            ('depois de 1988', 'acesso direto ampliado:', 'ADI, ADC, ADPF, ADO, súmula vinculante', 'ink')]
    for i, (a, b1, b2, tone) in enumerate(rows):
        y = 394 + i * 60
        o += f'<rect x="80" y="{y - 13}" width="8" height="48" style="fill:{"var(--" + tone + ")" if lit else "var(--grid-major)"}"/>'
        o += T(100, y, a.upper(), 't-small', style=f'letter-spacing:.08em;fill:{col}')
        o += T(100, y + 17, b1, 't-small', style='font-size:12px;fill:var(--ink-2)')
        o += T(100, y + 32, b2, 't-small', style='font-size:12px;fill:var(--ink-2)')
    return o

def fig_ci04():
    ref = 'Tavares cap. XIII via draft unit-04 ("Que modelos de defesa existem?", "Como o Brasil combinou os modelos?")'
    return kit.scrolly('Os dois modelos e o sistema brasileiro', [
        ('p-gen0', _gen(0), 'Modelo norte-americano'), ('p-gen1', _gen(1), 'Modelo austríaco'), ('p-gen2', _gen(2), 'Brasil')], [
        S('p-gen0', 'Modelo norte-americano', 'Todos os juízes, dentro de um caso',
          '<p>A matriz é <em>Marbury v. Madison</em> (1803). O controle se exerce durante um processo, para resolver o ponto de direito de que depende uma controvérsia entre partes: é difuso, porque cabe a qualquer juiz, e concreto.</p>' + src(ref), 'dif'),
        S('p-gen1', 'Modelo austríaco', 'Um só tribunal, a lei em tese',
          '<p>Na concepção de Kelsen, a defesa da Constituição cabe a um órgão técnico fora da estrutura do Judiciário, o Tribunal Constitucional. O controle é concentrado, porque só ele decide, e abstrato, porque examina a lei em tese. Concentrado e abstrato são eixos diferentes: o modelo italiano é concentrado, mas incidental.</p>' + src(ref), 'conc'),
        S('p-gen2', 'Modelo misto', 'O Brasil junta os dois',
          '<p>O controle difuso-concreto continua com todos os juízes, e o STF também o exerce no recurso extraordinário, com efeitos entre as partes, que só se tornam gerais pela resolução do Senado (art. 52, X). Desde a EC 16/1965 existe o controle abstrato, concentrado no STF, com eficácia <em>erga omnes</em> e efeito vinculante. Depois de 1988, o acesso direto se ampliou e surgiu uma pluralidade de ações.</p>' + src(ref), ''),
    ])

FIGS[('constitucional', 'aula-04.html')] = {5: fig_ci04}

# ---- PC Aula 03 · genre: matrix. The two axes of joinder cross in four combinations (draft unit-03-integrated)
_Q = [  # (row, col, title, example, tone)  row 0 necessário / 1 facultativo; col 0 unitário / 1 simples
    (0, 0, 'NECESSÁRIO-UNITÁRIO', ['relação indivisível que exige', 'todos no polo passivo;', 'composse na possessória'], 'conc'),
    (0, 1, 'NECESSÁRIO-SIMPLES', ['a lei exige a presença conjunta', '(cônjuges como réus), mas', 'admite capítulos individuais'], 'dif'),
    (1, 0, 'FACULTATIVO-UNITÁRIO', ['um colegitimado pode demandar', 'sozinho, e o mérito ainda', 'exige resultado uniforme'], 'dif'),
    (1, 1, 'FACULTATIVO-SIMPLES', ['pedidos individuais reunidos', 'por conexão ou afinidade;', 'cada um com resultado próprio'], 'ink'),
]
def _mx(k):
    o = T(30, 44, 'DOIS EIXOS, QUATRO COMBINAÇÕES', 't-small', style='letter-spacing:.1em')
    o += T(330, 92, 'UNITÁRIO', 't-small', anchor='middle', style='letter-spacing:.1em;fill:var(--ink-2)')
    o += T(490, 92, 'SIMPLES', 't-small', anchor='middle', style='letter-spacing:.1em;fill:var(--ink-2)')
    o += T(250, 72, 'O MÉRITO PRECISA SER IGUAL PARA TODOS?', 't-small', style='fill:var(--ink-2)')
    o += f'<text transform="translate(52 330) rotate(-90)" class="t-small" text-anchor="middle" style="letter-spacing:.08em;fill:var(--ink-2)">TODOS PRECISAM ESTAR NO POLO?</text>'
    o += T(150, 210, 'NECESSÁRIO', 't-small', anchor='end', style='letter-spacing:.1em;fill:var(--ink-2)')
    o += T(150, 420, 'FACULTATIVO', 't-small', anchor='end', style='letter-spacing:.1em;fill:var(--ink-2)')
    for i, (r, c, title, ex, tone) in enumerate(_Q):
        x, y = 170 + c * 200, 110 + r * 210
        lit = (k == i) or k == 4
        col = f'var(--{tone})'
        o += f'<rect x="{x}" y="{y}" width="190" height="200" style="fill:{"var(--paper)" if lit else "var(--grid-major)"};stroke:{col if lit else "var(--ink-2)"};stroke-width:{2 if lit else .8}"/>'
        o += f'<rect x="{x}" y="{y}" width="190" height="28" style="fill:{col if lit else "var(--ink-2)"}"/>'
        o += T(x + 12, y + 19, title, 't-small', style='fill:var(--paper);font-size:10px;letter-spacing:.06em')
        for j, line in enumerate(ex):
            o += T(x + 12, y + 56 + j * 19, line, 't-small', style=f'font-size:10px;fill:{"var(--ink)" if lit else "var(--ink-2)"}')
    o += T(30, 560, 'Fonte da necessidade e regime da decisão são perguntas diferentes.', 't-small', style='font-size:12.5px;fill:var(--ink)')
    return o

def fig_pc03():
    ref = 'draft unit-03-integrated: "Unitário ou simples" (four combinations), REsp 1.811.718/SP; CPC arts. 114, 116'
    bodies = [
        '<p>Quando uma relação indivisível exige a presença de todos e a decisão tem de ser a mesma para todos, o litisconsórcio é necessário e unitário. É frequente no polo passivo. Na composse, a reintegração tinha de citar todos os co-possuidores: sem isso, o STJ anulou a sentença (REsp 1.811.718/SP).</p>',
        '<p>A necessidade pode vir da lei e não da relação. Se a lei impõe a presença dos cônjuges como réus, todos precisam estar no processo, mas isso não obriga a solução uniforme: cada um pode receber um capítulo próprio.</p>',
        '<p>No polo ativo, um colegitimado pode iniciar a demanda sozinho, e mesmo assim o mérito exige resultado uniforme entre os envolvidos. A unitariedade se examina pelo art. 116, e não pela obrigatoriedade da formação.</p>',
        '<p>Pedidos individuais reunidos por conexão ou afinidade formam o caso mais comum: ninguém é obrigado a litigar junto, e cada litisconsorte recebe o seu resultado. A solidariedade, sozinha, não muda isso, se a obrigação for divisível.</p>',
    ]
    labels = ['Necessário e unitário', 'Necessário e simples', 'Facultativo e unitário', 'Facultativo e simples']
    tones = ['conc', 'dif', 'dif', '']
    return kit.scrolly('Necessidade e unitariedade', [(f'p-mx{i}', _mx(i), labels[i]) for i in range(4)],
                       [S(f'p-mx{i}', labels[i], _Q[i][2].capitalize().replace('-', ' e '), bodies[i] + src(ref), tones[i]) for i in range(4)])

FIGS[('processo-civil', 'aula-03.html')] = {4: fig_pc03}

# ---- PC Aula 03 · genre: matrix. The two axes of joinder in four combinations (draft unit-03-integrated)
_Q = [(0, 0, 'NECESSÁRIO-UNITÁRIO', ['relação indivisível:', 'todos no processo;', 'ex.: composse'], 'conc'),
      (0, 1, 'NECESSÁRIO-SIMPLES', ['a lei exige todos', '(cônjuges réus), mas', 'cada um tem capítulo'], 'dif'),
      (1, 0, 'FACULTATIVO-UNITÁRIO', ['um colegitimado', 'demanda sozinho;', 'mérito uniforme'], 'dif'),
      (1, 1, 'FACULTATIVO-SIMPLES', ['pedidos reunidos', 'por conexão; cada', 'um com seu resultado'], 'ink')]
def _mx(k):
    o = T(30, 44, 'DOIS EIXOS, QUATRO COMBINAÇÕES', 't-small', style='letter-spacing:.1em')
    o += T(265, 98, 'UNITÁRIO', 't-small', anchor='middle', style='letter-spacing:.1em;fill:var(--ink-2)')
    o += T(465, 98, 'SIMPLES', 't-small', anchor='middle', style='letter-spacing:.1em;fill:var(--ink-2)')
    o += T(160, 230, 'NECESSÁRIO', 't-small', anchor='end', style='letter-spacing:.06em;fill:var(--ink-2)')
    o += T(160, 440, 'FACULTATIVO', 't-small', anchor='end', style='letter-spacing:.06em;fill:var(--ink-2)')
    for i, (r, c, title, ex, tone) in enumerate(_Q):
        x, y = 170 + c * 200, 112 + r * 210
        lit = k == i
        col = f'var(--{tone})'
        o += R(x, y, 190, 200, 'ink', style=f'fill:{"var(--paper)" if lit else "var(--grid-major)"};stroke:{col if lit else "var(--ink-2)"};stroke-width:{2 if lit else .8}')
        o += R(x, y, 190, 28, 'ink', style=f'fill:{col if lit else "var(--ink-2)"};stroke:none')
        o += T(x + 10, y + 19, title, 't-small', style='fill:var(--paper);font-size:9.5px;letter-spacing:.04em')
        for j, line in enumerate(ex):
            o += T(x + 10, y + 58 + j * 20, line, 't-small', style=f'font-size:10px;fill:{"var(--ink)" if lit else "var(--ink-2)"}')
    o += T(30, 566, 'Fonte da necessidade e regime da decisão: perguntas diferentes.', 't-small', style='font-size:12px;fill:var(--ink)')
    return o

def fig_pc03():
    ref = 'draft unit-03-integrated "Unitário ou simples" (four combinations); REsp 1.811.718/SP; CPC arts. 114, 116'
    B = ['<p>Uma relação indivisível exige a presença de todos, e a decisão tem de ser igual para todos. Na composse, a reintegração tinha de citar todos os co-possuidores; sem isso, o STJ anulou a sentença (REsp 1.811.718/SP).</p>',
         '<p>A necessidade pode vir da lei, e não da relação. Se a lei impõe os cônjuges como réus, os dois precisam estar no processo, mas cada um pode receber um capítulo próprio.</p>',
         '<p>Um colegitimado pode iniciar a demanda sozinho, e mesmo assim o mérito exige resultado uniforme. A unitariedade se examina pelo art. 116, não pela obrigatoriedade da formação.</p>',
         '<p>Pedidos individuais reunidos por conexão ou afinidade: ninguém é obrigado a litigar junto, e cada litisconsorte recebe o seu resultado. A solidariedade, sozinha, não muda isso se a obrigação for divisível.</p>']
    L = ['Necessário e unitário', 'Necessário e simples', 'Facultativo e unitário', 'Facultativo e simples']
    tones = ['conc', 'dif', 'dif', '']
    return kit.scrolly('Necessidade e unitariedade', [(f'p-mx{i}', _mx(i), L[i]) for i in range(4)],
                       [S(f'p-mx{i}', L[i], L[i], B[i] + src(ref), tones[i]) for i in range(4)])

FIGS[('processo-civil', 'aula-03.html')] = {4: fig_pc03}

# ---- CI Aula 02 · genre: ledger. Each axis answers one question; 1988 on every axis (draft unit-02, last section)
_AX = [('CONTEÚDO', ['formal', 'material'], 0), ('FORMA', ['escrita', 'costumeira'], 0), ('EXTENSÃO', ['sintética', 'analítica'], 1),
       ('ESTABILIDADE', ['flexível', 'semirrígida', 'rígida'], 2), ('PROJETO', ['garantia', 'social-dirigente'], 1)]
def _ledger(k):
    o = T(30, 44, 'UMA PERGUNTA POR EIXO' if k == 0 else 'A CONSTITUIÇÃO DE 1988 EM CADA EIXO', 't-small', style='letter-spacing:.1em')
    for i, (ax, opts, pick) in enumerate(_AX):
        y = 80 + i * 92
        o += R(30, y, 540, 78, 'ink', style='fill:var(--paper);stroke:var(--ink);stroke-width:1')
        o += T(46, y + 26, ax, 't-small', style='letter-spacing:.1em;fill:var(--ink-2)')
        w = 380 / len(opts)
        for j, op in enumerate(opts):
            x = 180 + j * w
            on = k == 1 and j == pick
            o += R(x, y + 38, w - 10, 28, 'ink', style=f'fill:{"var(--conc)" if on else "var(--paper)"};stroke:{"var(--conc)" if on else "var(--ink-2)"};stroke-width:1')
            o += T(x + (w - 10) / 2, y + 57, op, 't-small', anchor='middle', style=f'font-size:12px;fill:{"var(--paper)" if on else "var(--ink)"}')
    if k == 1:
        o += T(30, 556, 'Rígida pelo art. 60; alguns autores dizem super-rígida pelo § 4º.', 't-small', style='font-size:12px;fill:var(--ink)')
        o += T(30, 576, 'Os rótulos não competem: cada um responde a um critério.', 't-small', style='font-size:12px;fill:var(--ink-2)')
    return o

def fig_ci02():
    ref = 'draft unit-02 "Como classificar sem misturar os eixos" (Tavares); CF art. 60 and § 4º'
    return kit.scrolly('Classificar sem misturar os eixos', [('p-lg0', _ledger(0), 'Os eixos'), ('p-lg1', _ledger(1), 'A Constituição de 1988')], [
        S('p-lg0', 'Método', 'Cada eixo responde a uma pergunta',
          '<p>Conteúdo, forma, extensão, estabilidade e projeto político são critérios independentes. A pergunta sobre como a Constituição se altera não diz nada sobre sua extensão, e a forma escrita não decide sua origem.</p>' + src(ref), 'dif'),
        S('p-lg1', 'Aplicação', 'A de 1988 em cada eixo',
          '<p>Formal, porque integra o documento aprovado como texto constitucional; escrita; analítica, porque contém muitas regras e detalhes; rígida, pelo procedimento de emenda do art. 60, e super-rígida para quem destaca o § 4º; social-dirigente, porque o texto também orienta a ação estatal.</p>' + src(ref), 'conc'),
    ])

# FIGS[('constitucional', 'aula-02.html')] = {7: fig_ci02}   # held: page overflows to 405 px at 390 px width in 2 of 4 QA runs (both themes); not the SVG itself, check the scrolly stage/figcaption at phone width
