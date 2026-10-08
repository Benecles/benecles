"""CI figures, P1 batch (29/09): Aula 01 timeline strata, Aula 03 constitutional strata.
Content comes only from the lesson drafts (unit-01-history-origins, unit-03-brazilian-constitutionalism)."""
from figs import FIGS, S, src
import kit
from kit import T, R, P, G, box

# ---------------------------------------------------------------- CI Aula 01 · timeline strata
_TL_SEGS = [('ANTES', 'ANTES DAS REVOLUÇÕES'), ('INGLATERRA', 'INGLATERRA · 1215–1689'), ('EUA/FRANÇA', 'EUA E FRANÇA · 1639–1791')]
_TL_TONE = ['grey', 'dif', 'conc']
_TL = [  # per panel: (tick label, row title, row sub, row sub2)
    [('hebreus', 'Hebreus · a lei do Senhor', 'Mesmo num Estado teocrático, a lei do Senhor limitava o poder', 'Experiência tímida, na qualificação de Tavares'),
     ('séc. V a.C.', 'Séc. V a.C. · a pólis grega', 'Funções divididas entre cargos, por sorteio e tempo determinado', 'Acesso a qualquer cidadão; participação direta'),
     ('Idade Média', 'Idade Média · lois de royaume', 'Leis superiores da sociedade, que o rei devia respeitar', 'Diferentes das lois du roi, feitas e revogáveis pelo rei')],
    [('1215', '1215 · Magna Carta', 'Início convencional da sequência britânica', 'Documentos e conflitos entre Coroa e Parlamento'),
     ('1628', '1628 · Petition of Right', 'Vinculada às liberdades públicas', None),
     ('1688', '1688 · Revolução Gloriosa', 'Linha de continuidade: reforça garantias já disputadas', 'Diferente da ruptura francesa, um século depois'),
     ('1689', '1689 · Bill of Rights', 'Culmina na monarquia constitucional', 'Poder régio condicionado por instituições e normas')],
    [('1639', '1639 · Connecticut', 'Documento de ordenação política, antes de 1787', None),
     ('1776', '1776 · Filadélfia', 'Congresso propõe que os Estados formulem Constituições', 'Proposta de 15 de maio'),
     ('1787', '1787 · Constituição dos EUA', 'Supremacia da Constituição escrita, em texto unificado', None),
     ('1789', '1789 · Revolução Francesa', 'Declaração dos Direitos do Homem e do Cidadão', None),
     ('1791', '1791 · Constituição francesa', 'A Declaração é seu preâmbulo', 'Primeira Constituição formal europeia')],
]
_TL_NOTE = ['A ideia de limite antecede a Constituição escrita.', 'Continuidade e costumes, sem código único.', 'O texto escrito e unificado vira o modelo moderno.']

def _tl(k):
    rows = _TL[k]
    tone = _TL_TONE[k]
    o = T(30, 40, 'DA LIMITAÇÃO À CONSTITUIÇÃO ESCRITA', 't-small', style='letter-spacing:.1em')
    # time band: the lit segment is expanded, the others compressed (not to scale)
    x = 30
    lit_x = 30
    for i, (short, full) in enumerate(_TL_SEGS):
        w = 340 if i == k else 90
        lit = i == k
        o += R(x, 96, w, 30, 'w-' + _TL_TONE[i] + ' ink' if lit else 'f-paper ink')
        o += T(x + w / 2, 116, full if lit else short, 't-small', anchor='middle', maxw=w - 8, ctx=f'ci01 seg{i}',
               style='' if lit else 'fill:var(--ink-2)')
        if lit: lit_x = x
        x += w + 10
    n = len(rows)
    span = 340 - 90
    for j, (tick, *_r) in enumerate(rows):
        tx = lit_x + 45 + (span * j / (n - 1) if n > 1 else span / 2)
        o += P(f'M{tx:.0f} 96V84', 'ink')
        o += T(round(tx), 76, tick, 't-small', anchor='middle', maxw=105 if n < 5 else 58, ctx=f'ci01 tick{k}.{j}')
    rh = {3: 104, 4: 84}.get(n, 66)
    for j, (tick, title, sub, sub2) in enumerate(rows):
        y = 150 + j * (rh + 10)
        o += box(30, y, 540, rh, title, sub, tone, sub2=sub2, ctx=f'ci01 p{k}.{j}')
    o += T(30, 566, _TL_NOTE[k], 't-small', style='font-size:13px;fill:var(--ink)')
    o += T(30, 584, 'Faixa fora de escala: o trecho em foco é ampliado.', 't-small', style='font-size:11px;fill:var(--ink-2)', maxw=540, ctx='ci01 scale')
    return o

def fig_ci01():
    r1 = 'draft unit-01-history-origins "Há constitucionalismo antes das revoluções modernas?" (Loewenstein, Tavares, Canotilho)'
    r2 = 'draft unit-01-history-origins "Como a experiência inglesa limitou a Coroa?" (Tavares, Jorge Miranda)'
    r3 = 'draft unit-01-history-origins "Como Estados Unidos e França formaram o modelo moderno?" (Tavares, Santi Romano)'
    return kit.scrolly('Da limitação do poder à Constituição escrita', [
        ('p-tl0', _tl(0), 'Limites antes das revoluções'), ('p-tl1', _tl(1), 'A experiência inglesa'), ('p-tl2', _tl(2), 'Estados Unidos e França')], [
        S('p-tl0', 'Antes das revoluções', 'A autoridade já se submetia a uma regra',
          '<p>Entre os hebreus, a lei do Senhor limitava o poder mesmo num Estado teocrático. No século V a.C., a pólis grega distribuiu funções entre cargos ocupados por sorteio e por tempo determinado. Na Idade Média, cartas e práticas comunitárias compuseram uma lei superior que o rei devia respeitar. Ainda não havia a Constituição escrita moderna: havia a ideia de limite.</p>' + src(r1), ''),
        S('p-tl1', 'Inglaterra', 'Limites por documentos e por continuidade',
          '<p>Da Magna Carta de 1215 à Bill of Rights de 1689, passando pela Petition of Right de 1628, a limitação avançou em conflitos entre Coroa e Parlamento e terminou numa monarquia constitucional. A Revolução Gloriosa de 1688 confirma garantias já disputadas, sem refazer o Estado. As instituições britânicas ficaram assentadas em costumes e tradições, sem um código único.</p>' + src(r2), 'dif'),
        S('p-tl2', 'Estados Unidos e França', 'A Constituição escrita como modelo',
          '<p>Em 15 de maio de 1776, o Congresso de Filadélfia propôs que os Estados formulassem Constituições próprias, e em 1787 veio a Constituição dos Estados Unidos, com a supremacia do texto escrito. A França seguiu por via revolucionária: a Declaração de 1789 precedeu a Constituição de 1791, primeira Constituição formal europeia. A influência foi circular, e por isso nenhum instituto cabe a um país só.</p>' + src(r3), 'conc'),
    ])

FIGS.setdefault(('constitucional', 'aula-01.html'), {})[6] = fig_ci01

# ---------------------------------------------------------------- CI Aula 03 · constitutional strata
_CS = [  # oldest first: (year, regime, defining feature, how it began)
    ('1824', 'Império', 'Carta com Poder Moderador; parlamentarismo por costume', 'outorgada'),
    ('1891', 'República federativa', 'Presidencialismo e federalismo de modelo norte-americano', 'após o golpe de 1889'),
    ('1934', 'Democracia social', 'Direitos sociais e ordem econômica; texto dúbio', 'após a Revolução de 1930'),
    ('1937', 'Estado Novo, a “Polaca”', 'Sem constituinte; Executivo supremo e decretos-leis', 'golpe de Estado'),
    ('1946', 'Fim do Estado Novo', 'Constituinte genuína; Poderes independentes e harmônicos', 'após a queda de 1945'),
    ('1967/69', 'Ditadura militar', 'Atos institucionais; Emenda n. 1, “estatuto da ditadura”', 'após o golpe de 1964'),
    ('1988', 'Redemocratização', 'Direitos fundamentais no início do texto, de aplicação imediata', 'Constituinte de 1987–88'),
]

def _cs(lit, tone, note):
    o = T(30, 40, 'SETE CONSTITUIÇÕES, DE 1824 A 1988', 't-small', style='letter-spacing:.1em')
    rh, gap, y0 = 56, 6, 60
    for i, (yr, regime, feat, born) in enumerate(_CS):
        y = y0 + (6 - i) * (rh + gap)       # oldest at the bottom
        on = i in lit
        o += box(30, y, 540, rh, f'{yr} · {regime}', feat, tone if on else 'grey', ctx=f'ci03 {yr}')
        o += T(556, y + 18, born, 't-small', anchor='end', maxw=200, ctx=f'ci03 born{yr}', style='font-size:11px;fill:var(--ink-2)')
    for j, line in enumerate(note):
        o += T(30, 540 + j * 20, line, 't-small', style='font-size:13px;fill:var(--ink)', maxw=540, ctx='ci03 note')
    return o

def fig_ci03a():
    r = 'draft unit-03 Parte I: "A Constituinte de 1823 e a Carta de 1824", "Uma Carta flexível", "A Constituição de 1891 no papel e na prática"'
    return kit.scrolly('Império e Primeira República', [
        ('p-cs0', _cs({0}, 'dif', ['Uma Carta outorgada, mudada por costume e por lei.']), '1824'),
        ('p-cs1', _cs({1}, 'conc', ['O modelo mudou; o poder pessoal passou ao Presidente.']), '1891')], [
        S('p-cs0', '1824 · Império', 'Outorgada, com quarto poder',
          '<p>Depois de dissolver a Constituinte em 12 de novembro de 1823, o Imperador fez outorgar a Carta de 1824, que somou aos três poderes clássicos o Poder Moderador. O art. 101, VI, lhe dava a nomeação livre dos ministros, e o parlamentarismo do Segundo Reinado nasceu de costume, só reconhecido pelo Decreto n. 523, de 1847. Por ser semirrígida, parte de suas normas mudou por lei ordinária.</p>' + src(r), 'dif'),
        S('p-cs1', '1891 · República', 'Federação e presidencialismo, no modelo dos EUA',
          '<p>Promulgada em 24 de fevereiro de 1891, a Constituição extinguiu o Poder Moderador e adotou o federalismo e o presidencialismo de inspiração norte-americana, com uma Suprema Corte. Era a mais concisa das cartas brasileiras. Na prática, o poder pessoal antes concentrado no Imperador passou ao Presidente, exercido por militares e depois pelas oligarquias.</p>' + src(r), 'conc'),
    ])

def fig_ci03b():
    r = 'draft unit-03 Parte II: "A Constituição de 1934", "A Constituição de 1937: a Polaca", "A Constituição de 1946", "De 1964 a 1969", "Da abertura à Constituinte de 1987 e 1988"'
    return kit.scrolly('De 1930 a 1988', [
        ('p-cs2', _cs({2, 3, 4}, 'dif', ['1934 corrige 1891, 1937 rompe 1934,', '1946 desfaz 1937.']), '1934, 1937, 1946'),
        ('p-cs3', _cs({5, 6}, 'conc', ['1964–1969 anula 1946; 1988 reage a 1964–1969.']), '1967/69 e 1988')], [
        S('p-cs2', '1930–1946', 'Democracia social, Polaca e retorno',
          '<p>A Constituição de 1934 rompeu com a tradição liberal e estabeleceu uma democracia social, mas seu texto era dúbio. Em 1937, o golpe dispensou qualquer constituinte: a Polaca deu ao Executivo posição suprema. Com a queda do Estado Novo em 1945, a Constituição de 1946 restabeleceu o equilíbrio entre os Poderes e retomou o federalismo.</p>' + src(r), 'dif'),
        S('p-cs3', '1964–1988', 'Da ditadura à Constituinte',
          '<p>Após o golpe de 31 de março de 1964, os atos institucionais convocaram o Congresso para uma Constituição que os autores chamam de farsa constituinte (1967), e a Emenda n. 1, de 1969, foi o estatuto da ditadura. A abertura levou à Assembleia Constituinte de 1987, sem eleição exclusiva, e à Constituição de 1988, que põe os direitos fundamentais no início do texto.</p>' + src(r), 'conc'),
    ])

FIGS.setdefault(('constitucional', 'aula-03.html'), {})[6] = fig_ci03a
FIGS.setdefault(('constitucional', 'aula-03-republica.html'), {})[7] = fig_ci03b
