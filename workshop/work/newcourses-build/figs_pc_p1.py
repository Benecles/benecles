"""Processo Civil I-a · P1 figures (29/09). Seven genre figures in the house drawing style, content only from the
lesson drafts (course-drafts-2026-09-28/processo-civil/<packet>/draft.md) and the CPC articles they cite.
Registered into figs.FIGS by (course, page file) → {chapter number on that page: fn}."""
from figs import FIGS, S, src
import kit
from kit import T, R, P, G, box

COURSE = 'processo-civil'

# ------------------------------------------------------------------ small drawing helpers (auto-wrapped, overflow-warning)
def _w(txt, size):
    return kit.tw(txt, 't-mid') * size / 20.0

def wrap(txt, size, w):
    lines, cur = [], ''
    for wd in txt.split():
        t = (cur + ' ' + wd).strip()
        if _w(t, size) <= w or not cur:
            cur = t
        else:
            lines.append(cur); cur = wd
    if cur: lines.append(cur)
    return lines

def tx(x, y, txt, size=14, w=None, anchor=None, weight=560, tone=None, ctx='', light=False, extra=''):
    if w is not None and _w(txt, size) > w:
        kit.WARN.append(f'{ctx}: "{txt}" ~{_w(txt, size):.0f}px > {w}px')
    cls = 't-mid' + (' ' + {'conc': 'tc-conc', 'dif': 'tc-dif', 'mix': 'tc-mix'}.get(tone, '') if tone else '') + (' t-light' if light else '')
    a = f' text-anchor="{anchor}"' if anchor else ''
    return f'<text x="{x}" y="{y}" class="{cls.strip()}"{a} style="font-size:{size}px;font-weight:{weight}{extra}">{txt}</text>'

def hdr(txt, y=28):
    return T(30, y, txt, 't-small', style='letter-spacing:.1em;fill:var(--ink-2)')

def _tone(tone):
    rc, tc = kit.TONE[tone]
    st = 'fill:var(--mix-wash);stroke:var(--mix)' if tone == 'mix' else ''
    return rc, tc, st

def card(x, y, w, h, title, body=None, tone='paper', ts=16, bs=13, pad=12, ctx='', center=False, tcolor=None):
    """Box with a bold title and wrapped body lines (list of str = paragraphs). Warns when the text does not fit."""
    rc, tc, st = _tone(tone)
    o = R(x, y, w, h, rc, style=st)
    light = tone == 'ink'
    iw = w - 2 * pad
    tl = wrap(title, ts, iw) if title else []
    paras = ([body] if isinstance(body, str) else list(body or []))
    bl = [wrap(p, bs, iw) for p in paras]
    th = len(tl) * ts * 1.22
    bh = sum(len(b) for b in bl) * bs * 1.32 + (4 * (len(bl) - 1) if len(bl) > 1 else 0)
    total = th + (6 if tl and bl else 0) + bh
    if total > h - 2 * pad + 6:
        kit.WARN.append(f'{ctx}: card "{title}" text height ~{total:.0f} > {h - 2 * pad + 6}')
    yy = y + (h - total) / 2 + ts * .86 if center else y + pad + ts * .86
    if not title: yy -= ts * .86 - bs * .86
    col = tcolor or tc
    for l in tl:
        cls = 't-mid ' + col + (' t-light' if light else '')
        o += f'<text x="{x + pad}" y="{yy:.0f}" class="{cls.strip()}" style="font-size:{ts}px;font-weight:700">{l}</text>'
        yy += ts * 1.22
    if tl and bl: yy += 6 - ts * .86 + bs * .86 - (0 if True else 0)
    elif bl and not tl: pass
    for i, b in enumerate(bl):
        for l in b:
            cls = 't-mid' + (' t-light' if light else '')
            o += f'<text x="{x + pad}" y="{yy:.0f}" class="{cls}" style="font-size:{bs}px;font-weight:500">{l}</text>'
            yy += bs * 1.32
        yy += 4
    return o

def arr(pid, x1, y1, x2, y2, t='i', dash=False):
    col = {'i': 'var(--ink)', 'c': 'var(--conc)', 'd': 'var(--dif)', 'm': 'var(--mix)'}[t]
    d = 'stroke-dasharray:5 4;' if dash else ''
    return P(f'M{x1} {y1}L{x2} {y2}', 'ink', m=f'{pid}-{t}', style=f'stroke:{col};stroke-width:2;{d}')

def elbow(pid, pts, t='i', dash=False, head=True):
    col = {'i': 'var(--ink)', 'c': 'var(--conc)', 'd': 'var(--dif)', 'm': 'var(--mix)'}[t]
    d = 'M' + 'L'.join(f'{x} {y}' for x, y in pts)
    st = f'stroke:{col};stroke-width:2;' + ('stroke-dasharray:5 4;' if dash else '')
    return P(d, 'ink', m=(f'{pid}-{t}' if head else None), style=st)

def tag(x, y, txt, tone='ink', size=12, w=None, ctx=''):
    """A small filled label (SIM / NÃO ...) centred at x."""
    ww = int(_w(txt, size)) + 14
    col = {'ink': 'var(--ink)', 'conc': 'var(--conc)', 'dif': 'var(--dif)', 'mix': 'var(--mix)'}[tone]
    return (f'<rect x="{x - ww / 2:.0f}" y="{y - size}" width="{ww}" height="{size + 7}" style="fill:{col}"/>'
            + tx(x, y, txt, size, anchor='middle', weight=700, light=True))

def check(x, y, on=True):
    o = R(x, y, 26, 26, 'f-paper ink')
    if on: o += P(f'M{x + 5} {y + 14}l6 7l11 -14', 'c-dif', style='stroke-width:3.4;stroke-linecap:round;stroke-linejoin:round')
    return o


# ================================================================== 1 · Aula 01 · ANNOTATED DOCUMENT
def _pc01(k):
    pid = f'p-pi{k}'
    o = ''
    if k == 0:
        o += hdr('A PETIÇÃO INICIAL, PARTE POR PARTE')
        o += R(30, 40, 540, 512, 'f-paper ink')
        rows = [('Juízo', None, 'paper'),
                ('Partes', 'qualificação; sem o CPF, se ainda dá para citar, não indefere', 'paper'),
                ('Fatos e fundamentos jurídicos', 'causa de pedir: o fato e a relação jurídica', 'dif'),
                ('Pedido especificado', 'o resultado que se quer do Judiciário', 'conc'),
                ('Valor da causa', None, 'paper'),
                ('Provas pretendidas', None, 'paper'),
                ('Conciliação ou mediação', 'opção sobre a audiência', 'paper')]
        for i, (t, g, tone) in enumerate(rows):
            y = 54 + i * 56
            rc, tc, st = _tone(tone)
            o += R(44, y, 512, 50, rc, style=st)
            o += R(44, y, 34, 50, 'f-ink ink')
            o += tx(61, y + 32, str(i + 1), 18, anchor='middle', weight=700, light=True)
            if g:
                o += tx(92, y + 22, t, 16, w=450, tone=tone if tone != 'paper' else None, ctx='pc01a')
                o += tx(92, y + 41, g, 12.5, w=450, weight=500, ctx='pc01a')
            else:
                o += tx(92, y + 31, t, 16, w=450, ctx='pc01a')
        o += R(44, 454, 512, 88, 'f-paper ink', style='stroke-dasharray:6 4')
        o += tx(60, 482, 'ANEXO · art. 320', 16, w=440, tone='mix')
        o += tx(60, 504, 'Documentos indispensáveis à propositura.', 13, w=480, weight=500, ctx='pc01a')
        o += tx(60, 524, 'Se faltam e podem ser juntados, o caminho é a emenda.', 13, w=480, weight=500, ctx='pc01a')
    elif k == 1:
        o += hdr('O PEDIDO: COMO SE FORMULA')
        o += card(30, 40, 265, 96, 'CERTO', 'expresso: diz qual prestação se busca', 'conc', ctx='pc01b', center=True)
        o += card(305, 40, 265, 96, 'DETERMINADO', 'qualidade e quantidade', 'conc', ctx='pc01b', center=True)
        o += card(30, 148, 540, 82, 'Genérico só nos casos do art. 324, § 1º',
                  'ação universal sem bens individuados · consequências ainda indetermináveis · depende de ato do réu', 'grey', ts=15, ctx='pc01b')
        o += hdr('VÁRIOS PEDIDOS: CUMULAÇÃO', y=256)
        o += card(30, 266, 265, 134, 'ALTERNATIVO · art. 325', 'um pedido só; a prestação pode ser cumprida de modos distintos. Sem ordem.', 'dif', ts=15, ctx='pc01b')
        o += card(305, 266, 265, 134, 'ALTERNATIVA · art. 326, p.u.', 'dois pedidos autônomos; um deles acolhido, sem indicar preferência.', 'dif', ts=15, ctx='pc01b')
        o += card(30, 412, 265, 134, 'SUBSIDIÁRIA · art. 326', 'com ordem: o segundo só vale se o primeiro não for acolhido ou examinado.', 'conc', ts=15, ctx='pc01b')
        o += card(305, 412, 265, 134, 'PRÓPRIA · art. 327', 'todos juntos, simples ou sucessiva; compatíveis, mesmo juízo, procedimento adequado.', 'paper', ts=15, ctx='pc01b')
    else:
        o += hdr('EMENDAR NÃO É ALTERAR')
        o += card(30, 40, 540, 100, 'EMENDAR · art. 321',
                  'completar dado ou documento em 15 dias, com o defeito indicado pelo juiz. Não muda pedido nem causa de pedir.', 'paper', ts=16, ctx='pc01c', center=True)
        o += hdr('ALTERAR PEDIDO OU CAUSA DE PEDIR · ART. 329', y=170)
        o += P('M40 184V548', 'ink', m=f'{pid}-i', style='stroke-width:2.5')
        o += card(64, 184, 506, 84, 'ANTES DA CITAÇÃO', 'aditar ou alterar, sem consentimento do réu. Ex.: acrescentar lucros cessantes.', 'dif', ctx='pc01c')
        o += P('M30 292H52', 'ink', style='stroke-width:3')
        o += tx(64, 297, 'CITAÇÃO', 13, weight=700, extra=';letter-spacing:.08em')
        o += card(64, 312, 506, 96, 'ATÉ O SANEAMENTO', 'só com consentimento do réu, contraditório de ao menos 15 dias e prova suplementar.', 'mix', ctx='pc01c')
        o += P('M30 432H52', 'ink', style='stroke-width:3')
        o += tx(64, 437, 'SANEAMENTO', 13, weight=700, extra=';letter-spacing:.08em')
        o += card(64, 452, 506, 84, 'DEPOIS DO SANEAMENTO', 'o art. 329 não autoriza a alteração pela vontade do autor.', 'conc', ctx='pc01c')
    return o

def fig_pc01():
    ref = 'draft unit-01-petition-demand-amendment: "O que a inicial precisa apresentar", "Certeza, determinação e interpretação do pedido", "Um pedido ou vários", "Corrigir a inicial e alterar a demanda"; CPC arts. 319, 320, 321, 322-327, 329'
    return kit.scrolly('A petição inicial anotada', [
        ('p-pi0', _pc01(0), 'Requisitos da inicial'), ('p-pi1', _pc01(1), 'O pedido'), ('p-pi2', _pc01(2), 'Emendar e alterar')], [
        S('p-pi0', 'CPC, arts. 319 e 320', 'Sete elementos e um anexo',
          '<p>O art. 319 organiza os elementos centrais: juízo, qualificação das partes, fatos e fundamentos jurídicos, pedido especificado, valor da causa, provas pretendidas e opção sobre a audiência de conciliação ou mediação. O art. 320 exige os documentos indispensáveis. Falta de dado de qualificação não indefere a inicial se ainda é possível citar o réu (§ 2º). Na causa de pedir, não basta dizer &ldquo;sou credor&rdquo;: é preciso narrar o empréstimo e o vencimento sem pagamento.</p>' + src(ref), 'dif'),
        S('p-pi1', 'Arts. 322 a 327', 'Certo, determinado e, às vezes, cumulado',
          '<p>O pedido deve ser certo, isto é, expresso, e determinado quanto à qualidade e à quantidade; o pedido genérico só cabe nas três hipóteses do art. 324, § 1º. Na cumulação, o atalho errado em prova é confundir alternativo com subsidiário: no subsidiário há ordem de preferência; no alternativo não há. A cumulação própria busca todos os pedidos ao mesmo tempo (art. 327).</p>' + src(ref), 'conc'),
        S('p-pi2', 'Arts. 321 e 329', 'A linha do tempo da demanda',
          '<p>Emendar completa informação ou documento. Aditar ou alterar o pedido ou a causa de pedir depende do momento: até a citação, sem consentimento do réu; da citação ao saneamento, com consentimento, contraditório de pelo menos quinze dias e prova suplementar; depois do saneamento, o texto do art. 329 não autoriza a alteração unilateral. Erro material ou complemento formal que não muda o pedido nem os fatos não entra nessa regra.</p>' + src(ref), 'mix'),
    ])

FIGS[(COURSE, 'aula-01.html')] = {4: fig_pc01}


# ================================================================== 2 · Aula 02 · DECISION FLOWCHART
def _pc02(k):
    pid = f'p-lm{k}'
    o = ''
    if k == 0:
        o += hdr('O QUE FAZER COM A INICIAL QUE CHEGA')
        o += card(150, 38, 300, 46, 'A INICIAL CHEGA', None, 'ink', ts=17, center=True, ctx='pc02a')
        o += arr(pid, 300, 84, 300, 104)
        o += card(90, 104, 420, 64, 'Defeito da inicial ou mérito do pedido?', None, 'paper', ts=16, center=True, ctx='pc02a')
        o += elbow(pid, [(150, 168), (150, 188), (150, 200)], 'd')
        o += elbow(pid, [(450, 168), (450, 188), (450, 200)], 'c')
        o += arr(pid, 300, 168, 300, 522, 'm', dash=True)
        o += R(266, 320, 68, 26, 'f-paper ink', style='stroke:none')
        o += tx(300, 338, 'nenhum', 12, anchor='middle', weight=700)
        o += card(30, 200, 240, 116, 'DEFEITO DA INICIAL · art. 330', 'inépcia, ilegitimidade manifesta, falta de interesse, arts. 106 e 321 descumpridos', 'dif', ts=14, bs=12.5, ctx='pc02a')
        o += arr(pid, 150, 316, 150, 340, 'd')
        o += card(30, 340, 240, 76, 'Emenda em 15 dias', 'o juiz aponta com precisão o defeito (art. 321)', 'paper', ts=14, bs=12.5, ctx='pc02a')
        o += arr(pid, 150, 416, 150, 438, 'd')
        o += card(30, 438, 240, 74, 'NÃO EMENDOU: INDEFERE', 'extingue sem julgar o mérito', 'dif', ts=14, bs=12.5, ctx='pc02a')
        o += card(330, 200, 240, 116, 'IMPROCEDÊNCIA LIMINAR', 'causa sem instrução + súmula STF/STJ, repetitivo, IRDR/IAC, súmula de TJ local; ou prescrição/decadência', 'conc', ts=14, bs=11.5, ctx='pc02a')
        o += arr(pid, 450, 316, 450, 340, 'c')
        o += card(330, 340, 240, 76, 'SENTENÇA DE MÉRITO', 'sem ouvir o réu; apta à coisa julgada', 'conc', ts=14, bs=12.5, ctx='pc02a')
        o += card(30, 528, 540, 50, 'SE NENHUM DOS DOIS: AUDIÊNCIA · art. 334', None, 'mix', ts=16, center=True, ctx='pc02a')
    elif k == 1:
        o += hdr('E SE O AUTOR OU O JUIZ QUISER REVER: RECURSO')
        o += card(30, 40, 265, 92, 'INDEFERIMENTO TOTAL', 'art. 331 · sentença · apelação', 'dif', ts=16, ctx='pc02b', center=True)
        o += card(305, 40, 265, 92, 'IMPROCEDÊNCIA LIMINAR', 'art. 332 · sentença de mérito · apelação', 'conc', ts=16, ctx='pc02b', center=True)
        o += elbow(pid, [(162, 132), (162, 158), (300, 158), (300, 176)], 'i', head=False)
        o += elbow(pid, [(438, 132), (438, 158), (300, 158), (300, 176)], 'i')
        o += card(90, 176, 420, 92, 'RETRATAÇÃO EM 5 DIAS', 'o próprio juiz pode voltar atrás, dentro da apelação', 'paper', ts=17, ctx='pc02b', center=True)
        o += elbow(pid, [(180, 268), (180, 290), (162, 290), (162, 308)], 'd')
        o += elbow(pid, [(420, 268), (420, 290), (438, 290), (438, 308)], 'c')
        o += card(30, 308, 265, 130, 'MANTIDA', 'cita o réu para responder ao recurso', 'dif', ts=16, ctx='pc02b')
        o += card(305, 308, 265, 130, 'MANTIDA', 'cita o réu para contrarrazões em 15 dias, a primeira fala dele', 'conc', ts=16, ctx='pc02b')
        o += card(30, 452, 540, 96, 'INDEFERIMENTO PARCIAL: interlocutória', 'só um pedido encerrado: agravo de instrumento (art. 354, p.u.). Escolha o recurso pelo quanto foi encerrado, não pelo nome.', 'grey', ts=15, ctx='pc02b')
    else:
        o += hdr('SEM JULGAMENTO LIMINAR: A AUDIÊNCIA · ART. 334')
        o += card(30, 40, 540, 62, 'CONCILIAÇÃO OU MEDIAÇÃO: é a regra', None, 'mix', ts=17, center=True, ctx='pc02c')
        for i, (n, t, g) in enumerate([('30', 'dias de antecedência', 'a audiência é designada'), ('20', 'dias de antecedência', 'o réu já deve estar citado'), ('10', 'dias antes', 'petição do réu de desinteresse')]):
            y = 118 + i * 66
            o += R(30, y, 110, 56, 'f-ink ink')
            o += tx(85, y + 39, n, 30, anchor='middle', weight=750, light=True)
            o += R(140, y, 430, 56, 'f-paper ink')
            o += tx(154, y + 24, t, 15, w=400, weight=700, ctx='pc02c')
            o += tx(154, y + 44, g, 13, w=400, weight=500, ctx='pc02c')
        o += card(30, 322, 540, 100, 'NÃO HÁ AUDIÊNCIA SE', 'ambas as partes manifestam desinteresse (o autor na inicial; se há litisconsórcio, todos) ou o caso não admite autocomposição.', 'conc', ts=16, ctx='pc02c')
        o += card(30, 434, 265, 112, 'ACORDO', 'reduzido a termo e homologado por sentença', 'dif', ts=16, ctx='pc02c')
        o += card(305, 434, 265, 112, 'SEM ACORDO', 'a audiência não decide quem tem razão: o processo segue', 'paper', ts=16, ctx='pc02c')
        o += tx(30, 574, 'Ausência injustificada: ato atentatório, multa até 2%.', 13, w=540, weight=600, ctx='pc02c')
    return o

def fig_pc02():
    ref = 'draft unit-02-preliminary-dismissal-hearing: "Primeiro: é defeito da inicial ou improcedência do pedido?", "Indeferimento total: o caminho da apelação", "Improcedência liminar", "Se não houver julgamento liminar, vem a audiência"; CPC arts. 106, 321, 330-332, 334, 354 p.u.'
    return kit.scrolly('O caminho da inicial até a audiência', [
        ('p-lm0', _pc02(0), 'Fluxo da inicial'), ('p-lm1', _pc02(1), 'Recurso e retratação'), ('p-lm2', _pc02(2), 'Audiência')], [
        S('p-lm0', 'Arts. 321, 330 e 332', 'Primeiro classifique: defeito ou mérito?',
          '<p>Defeito da inicial (art. 330: inépcia, parte manifestamente ilegítima, falta de interesse, descumprimento dos arts. 106 e 321) leva a emenda em quinze dias, com o defeito indicado com precisão; só o descumprimento leva ao indeferimento, que extingue sem julgar o mérito. Já a improcedência liminar (art. 332) exige causa que dispense instrução e uma das hipóteses legais, e é sentença de mérito. Se nenhum dos dois ocorre, vem a audiência do art. 334.</p>' + src(ref), 'dif'),
        S('p-lm1', 'Arts. 331 e 332', 'Apelação e retratação em cinco dias',
          '<p>Nos dois casos o autor apela e o juiz pode retratar-se em cinco dias. Mantido o indeferimento, o réu é citado para responder ao recurso (art. 331); se o tribunal reformar, o prazo de contestação começa com a intimação do retorno dos autos. Mantida a improcedência liminar, o réu é citado para contrarrazões em quinze dias. Se o indeferimento atinge só um pedido, a decisão é interlocutória e cabe agravo de instrumento (art. 354, parágrafo único).</p>' + src(ref), 'conc'),
        S('p-lm2', 'CPC, art. 334', 'A audiência é a regra, com duas saídas',
          '<p>Audiência designada com pelo menos trinta dias de antecedência; o réu é citado com pelo menos vinte; o réu manifesta desinteresse por petição até dez dias antes. O autor declara o desinteresse na inicial, e um só não cancela a audiência: é preciso o desinteresse de ambos, de todos os litisconsortes, ou que o caso não admita autocomposição. Havendo acordo, sentença homologatória; sem acordo, o processo segue.</p>' + src(ref), 'mix'),
    ])

FIGS[(COURSE, 'aula-02.html')] = {4: fig_pc02}

# C8 integrated figures (Sol7, 2026-09-29)

# ================================================================== PC Aula 04 · RELATIONSHIP DIAGRAM · assistência
# Appendable snippet: expects the house helpers and FIGS namespace already loaded.
def _pc04(k):
    pid = f'p-as{k}'
    o = ''
    if k == 0:
        o += hdr('ASSISTÊNCIA SIMPLES · EFEITO REFLEXO')
        o += card(30, 94, 190, 82, 'LOCADOR', None, 'paper', ts=16, center=True, ctx='pc04a')
        o += card(380, 94, 190, 82, 'LOCATÁRIO', None, 'dif', ts=16, center=True, ctx='pc04a')
        o += arr(pid, 220, 135, 380, 135, 'd')
        o += tx(300, 120, 'despejo', 13, anchor='middle', weight=650, tone='dif')
        o += card(205, 354, 190, 82, 'SUBLOCATÁRIO', None, 'mix', ts=15, center=True, ctx='pc04a')
        o += arr(pid, 380, 176, 330, 354, 'm', dash=True)
        o += tx(400, 278, 'sublocação', 13, anchor='middle', weight=600, tone='mix')
        o += elbow(pid, [(125, 176), (125, 300), (205, 395)], 'c', dash=True)
        o += tx(116, 270, 'sentença', 13, anchor='middle', weight=650, tone='conc')
        o += card(30, 462, 540, 82, 'VÍNCULO COM O ASSISTIDO', 'A sentença repercute na sublocação; o objeto litigioso continua sendo o despejo.', 'paper', ts=14, bs=12.5, ctx='pc04a')
    elif k == 1:
        o += hdr('ASSISTÊNCIA LITISCONSORCIAL · EFEITO DIRETO')
        o += card(30, 150, 170, 86, 'ADVERSÁRIO', None, 'paper', ts=15, center=True, ctx='pc04b')
        o += card(400, 150, 170, 86, 'PARTE PRINCIPAL', None, 'dif', ts=15, center=True, ctx='pc04b')
        o += arr(pid, 200, 193, 400, 193, 'd')
        o += tx(300, 177, 'relação litigiosa', 13, anchor='middle', weight=650, tone='dif')
        o += card(215, 354, 170, 86, 'TERCEIRO', None, 'conc', ts=15, center=True, ctx='pc04b')
        o += elbow(pid, [(300, 354), (300, 280), (470, 236)], 'c')
        o += tx(410, 284, 'relação própria', 13, anchor='middle', weight=650, tone='conc')
        o += arr(pid, 470, 236, 385, 354, 'c', dash=True)
        o += card(30, 470, 540, 64, 'A SENTENÇA PODE ALCANÇAR DIRETAMENTE O TERCEIRO', 'Titularidade, cotitularidade ou legitimidade para defender a relação em juízo.', 'conc', ts=14, bs=12.5, ctx='pc04b')
    else:
        o += hdr('O VÍNCULO DEFINE A POSIÇÃO NO PROCESSO')
        o += card(30, 66, 260, 182, 'SIMPLES', ['relação conexa', 'efeito reflexo', 'auxilia o assistido', 'atuação subordinada'], 'mix', ts=17, bs=13, ctx='pc04c')
        o += card(310, 66, 260, 182, 'LITISCONSORCIAL', ['relação própria no objeto', 'efeito direto', 'litisconsorte da parte', 'atuação equivalente'], 'conc', ts=16, bs=13, ctx='pc04c')
        o += card(30, 278, 540, 78, 'EM AMBAS', 'O terceiro ingressa para assistir uma parte; não acrescenta, por si só, novo pedido.', 'paper', ts=15, bs=13, ctx='pc04c')
        o += card(30, 384, 540, 112, 'PODERES DO ASSISTENTE SIMPLES · ARTS. 121–122', 'Pode alegar, provar e recorrer; supre omissão do assistido. Não prevalece contra ato dispositivo expresso, como renúncia ou desistência.', 'grey', ts=14, bs=12.5, ctx='pc04c')
    return o

def fig_pc04():
    ref = 'draft unit-04-intervention-assistance: "Assistência simples: a sentença afeta uma relação conexa", quadro comparativo e "Assistência litisconsorcial: relação própria no objeto litigioso"; CPC arts. 119, 121, 122 e 124'
    return kit.scrolly('Assistência: o vínculo e o alcance da sentença', [
        ('p-as0', _pc04(0), 'Relação conexa'),
        ('p-as1', _pc04(1), 'Relação no objeto'),
        ('p-as2', _pc04(2), 'Posição e poderes')], [
        S('p-as0', 'Assistência simples · art. 119', 'A sentença repercute em relação conexa',
          '<p>Na ação de despejo, locador e locatário discutem a relação litigiosa. O sublocatário tem vínculo com o locatário, e a decisão pode repercutir na sublocação. Seu interesse é jurídico e reflexo; ele auxilia a parte titular da relação discutida.</p>' + src(ref), 'mix'),
        S('p-as1', 'Assistência litisconsorcial · art. 124', 'A sentença pode atingir relação do terceiro',
          '<p>O assistente litisconsorcial afirma titularidade, cotitularidade ou legitimidade para defender a própria relação jurídica que está em julgamento. A influência da sentença é direta, e o art. 124 o considera litisconsorte da parte principal.</p>' + src(ref), 'conc'),
        S('p-as2', 'Arts. 121–122', 'Poderes acompanham o tipo de vínculo',
          '<p>O assistente simples pode alegar, produzir prova e recorrer. Se o assistido é omisso, pode atuar como substituto processual; se há ato dispositivo expresso, como desistência ou renúncia, não pode contrariá-lo. Na assistência litisconsorcial, o interveniente atua com intensidade equivalente à da parte principal.</p>' + src(ref), 'dif'),
    ])

FIGS[(COURSE, 'aula-04.html')] = {4: fig_pc04}

# ---- PC Aula 05 · genre: decision tree · intervention, IDPJ, amicus
def _pc05(k):
    pid = f'p-pc05-{k}'
    o = hdr('QUEM ENTRA NO PROCESSO — E POR QUÊ')
    if k == 0:
        o += card(145, 78, 310, 82, 'Qual o vínculo?', 'Classifique a relação antes de escolher a técnica.', 'ink', ts=17, bs=13, ctx='pc05-root')
        o += elbow(pid, [(300, 160), (300, 188), (150, 188), (150, 213)], t='i')
        o += elbow(pid, [(300, 188), (450, 188), (450, 213)], t='i')
        o += card(45, 213, 210, 91, 'Mesmo credor?', 'O terceiro também deve ao autor.', 'conc', ts=16, bs=13, ctx='pc05-debt')
        o += card(345, 213, 210, 91, 'Garantia ou regresso?', 'O terceiro deve reembolsar a parte.', 'dif', ts=16, bs=13, ctx='pc05-regress')
        o += T(300, 362, 'Se não: veja o patrimônio ou a contribuição ao debate.', 't-small', anchor='middle', style='font-size:13px')
        o += src('draft unit-05-intervention-impleader-other: “Quando o réu chama os devedores do mesmo credor?”; “Até onde vai o direito de regresso?”')
    elif k == 1:
        o += card(145, 82, 310, 82, 'O terceiro também deve ao autor?', 'Fiador, cofiador ou codevedor solidário da dívida comum.', 'conc', ts=16, bs=13, ctx='pc05-call-q')
        o += arr(pid, 300, 164, 300, 206, 'c')
        o += card(145, 206, 310, 94, 'CHAMAMENTO AO PROCESSO', 'Só o réu pede, na contestação.', 'conc', ts=17, bs=13, ctx='pc05-call')
        o += arr(pid, 300, 300, 300, 340, 'c')
        o += card(95, 340, 410, 105, 'Uma causa, polo passivo ampliado', 'Chamados respondem ao credor; quem paga pode executar o título para cobrar o total do principal ou a quota dos codevedores.', 'paper', ts=15, bs=12, ctx='pc05-call-effect')
        o += src('draft unit-05-intervention-impleader-other: “Quando o réu chama os devedores do mesmo credor?”; arts. 130–132')
    elif k == 2:
        o += card(145, 70, 310, 90, 'Deve garantia ou regresso?', 'Por lei ou contrato, à parte que pode perder.', 'dif', ts=16, bs=13, ctx='pc05-den-q')
        o += arr(pid, 300, 160, 300, 194, 'd')
        o += card(145, 194, 310, 80, 'DENUNCIAÇÃO DA LIDE', 'Autor na inicial; réu na contestação.', 'dif', ts=17, bs=13, ctx='pc05-den')
        o += arr(pid, 300, 274, 300, 306, 'd')
        o += card(95, 306, 410, 108, 'Pedido regressivo eventual', 'O juiz examina o regresso se o denunciante perder a causa principal. Se não houver denunciação, o regresso pode seguir em ação autônoma.', 'paper', ts=15, bs=12, ctx='pc05-den-effect')
        o += T(300, 455, 'Limite: uma denunciação sucessiva.', 't-small', anchor='middle', style='font-size:13px;fill:var(--ink-2)')
        o += src('draft unit-05-intervention-impleader-other: “A denunciação da lide”; arts. 125–129')
    elif k == 3:
        o += card(145, 72, 310, 91, 'Alcançar patrimônio alheio?', 'Sócio, administrador ou pessoa jurídica, conforme a hipótese.', 'mix', ts=16, bs=13, ctx='pc05-idpj-q')
        o += arr(pid, 300, 163, 300, 198, 'm')
        o += card(145, 198, 310, 80, 'INCIDENTE: DESCONSIDERAÇÃO', 'A parte ou o MP pede; juiz não instaura de ofício.', 'mix', ts=16, bs=12, ctx='pc05-idpj')
        o += arr(pid, 300, 278, 300, 310, 'm')
        o += card(95, 310, 410, 108, 'Defesa antes da decisão', 'Citação para manifestação e provas em 15 dias. O incidente suspende o processo; pedido na inicial não abre incidente nem suspende.', 'paper', ts=15, bs=12, ctx='pc05-idpj-effect')
        o += src('draft unit-05-intervention-impleader-other: “Como alcançar o patrimônio de sócio ou sociedade?”; arts. 133–137')
    else:
        o += card(145, 72, 310, 91, 'Busca conhecimento especializado?', 'Ou representatividade para contribuir na causa.', 'paper', ts=16, bs=13, ctx='pc05-amicus-q')
        o += arr(pid, 300, 163, 300, 198, 'i')
        o += card(145, 198, 310, 80, 'AMICUS CURIAE', 'Juiz/relator admite ou solicita; partes ou interessado também podem pedir.', 'ink', ts=16, bs=12, ctx='pc05-amicus')
        o += arr(pid, 300, 278, 300, 310, 'i')
        o += card(95, 310, 410, 108, 'Contribui para a decisão', 'Matéria relevante, tema específico ou repercussão social, com representatividade adequada. O juiz fixa poderes; como regra, não há recurso.', 'paper', ts=15, bs=12, ctx='pc05-amicus-effect')
        o += src('draft unit-05-intervention-impleader-other: “O que o amicus curiae pode fazer?”; art. 138')
    return o


def fig_pc05():
    ref = 'draft unit-05-intervention-impleader-other: intervenção provocada, desconsideração e amicus curiae; CPC arts. 125–138'
    panels = [
        ('p-pc05-0', _pc05(0), 'Classifique o vínculo'),
        ('p-pc05-1', _pc05(1), 'Dívida comum: chamamento'),
        ('p-pc05-2', _pc05(2), 'Garantia ou regresso: denunciação'),
        ('p-pc05-3', _pc05(3), 'Patrimônio: desconsideração'),
        ('p-pc05-4', _pc05(4), 'Conhecimento: amicus curiae'),
    ]
    steps = [
        S('p-pc05-0', 'Comece pelo vínculo', 'Quem é o terceiro em relação à causa?', '<p>Se também deve ao autor a dívida comum, o réu pode pedir chamamento. Se deve garantia ou regresso à parte, cabe avaliar denunciação. Se a questão é alcançar outro patrimônio, avalia-se o incidente de desconsideração; se a contribuição é técnica ou representativa, pode caber amicus curiae.</p>' + src(ref)),
        S('p-pc05-1', 'Dívida comum ao autor', 'O réu pede chamamento na contestação', '<p>O chamamento reúne réu e outros devedores do mesmo credor: fiador, afiançado, cofiadores ou codevedores solidários nas hipóteses legais. Amplia o polo passivo. Quem pagar pode usar a sentença como título para cobrar o total do devedor principal ou a quota dos codevedores, conforme o caso.</p>' + src(ref), 'conc'),
        S('p-pc05-2', 'Garantia ou regresso', 'Autor ou réu formula pedido eventual', '<p>A parte pede a denunciação na inicial ou na contestação, conforme sua posição. Se perder a causa principal, o juiz examina o pedido regressivo; perder não prova, por si só, a obrigação do denunciado. Se a intervenção não ocorrer, o regresso pode ser proposto em ação autônoma.</p>' + src(ref), 'dif'),
        S('p-pc05-3', 'Alcançar outro patrimônio', 'A parte ou o MP provoca o incidente', '<p>O pedido indica os pressupostos da lei material. O sócio ou a pessoa jurídica é citado para se manifestar e pedir provas em 15 dias. O incidente suspende o processo, salvo quando a desconsideração é pedida já na inicial; o juiz não o instaura de ofício.</p>' + src(ref), 'mix'),
        S('p-pc05-4', 'Contribuir para o debate', 'O juiz ou relator define os poderes do amicus', '<p>O juiz ou relator pode solicitar ou admitir a participação de ofício ou a pedido das partes ou do interessado. Exige relevância, especificidade do tema ou repercussão social, além de representatividade adequada. O amicus contribui para a decisão e, como regra, não recorre.</p>' + src(ref)),
    ]
    return kit.scrolly('Que intervenção corresponde ao vínculo?', panels, steps)


FIGS[(COURSE, 'aula-05.html')] = {4: fig_pc05}

# PC06 · Aula 06 · route map, contrast, and carta types
# Appendable snippet for figs.py; shared helpers (card, tx, arr, hdr, S, src, kit) are defined there.

def _pc06(k):
    pid = f'p-cit{k}'
    o = ''
    if k == 0:
        o += hdr('CITAÇÃO · ORDEM DE PREFERÊNCIA')
        o += card(30, 48, 540, 70, '1 · ELETRÔNICA', 'Preferencial · até 2 dias úteis; aguarde confirmação por 3 dias úteis.', 'conc', ts=16, bs=12.5, ctx='pc06a')
        o += arr(pid, 300, 118, 300, 132)
        o += card(30, 132, 250, 82, '2 · CORREIO', 'Qualquer comarca, salvo as exceções do art. 247.', 'paper', ts=15, bs=12.5, ctx='pc06a')
        o += card(320, 132, 250, 82, '3 · OFICIAL', 'Quando a lei determina ou o correio fracassa.', 'paper', ts=15, bs=12.5, ctx='pc06a')
        o += elbow(pid, [(155, 214), (155, 229), (300, 229), (300, 246)], 'i')
        o += tx(300, 239, 'SEM CONFIRMAÇÃO · OUTRA VIA', 11, anchor='middle', weight=700, ctx='pc06a')
        o += card(30, 246, 250, 82, '4 · ESCRIVÃO', 'Se o citando comparece ao cartório.', 'paper', ts=15, bs=12.5, ctx='pc06a')
        o += card(320, 246, 250, 82, '5 · EDITAL', 'Hipóteses legais; publicação por 20 a 60 dias.', 'dif', ts=15, bs=12.5, ctx='pc06a')
        o += card(30, 346, 540, 178, 'HORA CERTA · VIA DO OFICIAL', 'Citação ficta: duas procuras sem êxito e suspeita de ocultação. O oficial avisa familiar ou vizinho e retorna no dia útil seguinte.', 'mix', ts=16, bs=13, ctx='pc06a')
        o += tx(30, 555, 'Hora certa e edital: ciência presumida.', 12.5, weight=600, ctx='pc06a')
    elif k == 1:
        o += hdr('CITAÇÃO CONVOCA · INTIMAÇÃO INFORMA')
        o += card(30, 54, 260, 128, 'CITAÇÃO · art. 238', 'Convoca réu, executado ou interessado para integrar o processo; dá ciência da demanda.', 'conc', ts=16, bs=13, ctx='pc06b')
        o += card(310, 54, 260, 128, 'INTIMAÇÃO · art. 269', 'Dá ciência a alguém dos atos e termos do processo.', 'dif', ts=16, bs=13, ctx='pc06b')
        o += arr(pid, 290, 118, 310, 118, 'm')
        o += hdr('MEIOS E MARCOS', y=216)
        o += card(30, 230, 260, 126, 'CITAÇÃO', 'Eletrônica é preferencial; sem confirmação em 3 dias úteis, passa a outra modalidade.', 'paper', ts=15, bs=12.5, ctx='pc06b')
        o += card(310, 230, 260, 126, 'INTIMAÇÃO', 'Eletrônica sempre que possível; fora dela, publicação no órgão oficial.', 'paper', ts=15, bs=12.5, ctx='pc06b')
        o += card(30, 372, 260, 142, 'CIÊNCIA DO PROCESSO', 'Comparecimento espontâneo supre falta ou nulidade da citação e inicia o prazo de resposta.', 'grey', ts=14.5, bs=12.5, ctx='pc06b')
        o += card(310, 372, 260, 142, 'PUBLICAÇÃO NULA', 'Faltam nomes das partes ou dos advogados com inscrição na OAB; cabe arguir no próprio ato.', 'mix', ts=14.5, bs=12.5, ctx='pc06b')
        o += tx(30, 552, 'Citação integra; intimação comunica o que ocorre.', 12.5, weight=600, ctx='pc06b')
    else:
        o += hdr('CARTAS · QUANDO O ATO SAI DO TERRITÓRIO')
        o += card(30, 50, 540, 66, 'REGRA', 'Ato fora dos limites territoriais do juízo, salvo previsão legal.', 'ink', ts=15, bs=12, pad=10, ctx='pc06c')
        o += card(30, 132, 260, 132, 'DE ORDEM', 'Tribunal → juízo vinculado. Cumpre ato determinado pelo tribunal.', 'conc', ts=15, bs=12.5, ctx='pc06c')
        o += card(310, 132, 260, 132, 'ROGATÓRIA', 'Juízo brasileiro → órgão jurisdicional estrangeiro. Cooperação internacional.', 'dif', ts=15, bs=12.5, ctx='pc06c')
        o += card(30, 280, 260, 132, 'PRECATÓRIA', 'Juízo brasileiro → outro juízo brasileiro de competência territorial diversa.', 'paper', ts=15, bs=12.5, ctx='pc06c')
        o += card(310, 280, 260, 132, 'ARBITRAL', 'Juízo arbitral → órgão do Judiciário; cooperação para ato pedido pelo árbitro.', 'paper', ts=15, bs=12.5, ctx='pc06c')
        o += arr(pid, 155, 412, 155, 438, 'm')
        o += arr(pid, 440, 412, 440, 438, 'm')
        o += card(30, 438, 540, 96, 'COOPERAÇÃO ENTRE JUÍZOS · art. 69', 'Pedido para qualquer ato processual: dispensa forma específica. Reunião, informação ou ato concertado podem bastar sem carta.', 'mix', ts=15, bs=12.5, ctx='pc06c')
    return o


def fig_pc06():
    r0 = 'draft unit-06-procedural-acts-service, “Modalidades de citação”; CPC arts. 246–259'
    r1 = 'draft unit-06-procedural-acts-service, “O que a citação faz e o que acontece sem ela”, “Modalidades de citação”, “Intimação”; CPC arts. 238–239, 246, 269–272'
    r2 = 'draft unit-06-procedural-acts-service, “Cooperação nacional e cartas”; CPC arts. 67–69, 236–237'
    return kit.scrolly('Citação, intimação e cartas: três caminhos', [
        ('p-cit0', _pc06(0), 'Modalidades de citação'),
        ('p-cit1', _pc06(1), 'Citação e intimação'),
        ('p-cit2', _pc06(2), 'Cartas e cooperação')], [
        S('p-cit0', 'CPC, arts. 246–259', 'Siga a preferência; diante da falha, use outra via',
          '<p>A citação eletrônica é preferencial: deve ser feita em até dois dias úteis, e o citando tem três dias úteis para confirmar. Sem confirmação, a citação segue por correio, oficial de justiça, escrivão se houver comparecimento ao cartório, ou edital. O correio vale em qualquer comarca, ressalvadas as exceções do art. 247; o oficial atua quando a lei determina ou o correio fracassa. Hora certa exige duas procuras sem êxito e suspeita de ocultação; edital cabe nas hipóteses do art. 256 e tem prazo de vinte a sessenta dias. Hora certa e edital são fictas.</p>' + src(r0), 'conc'),
        S('p-cit1', 'Arts. 238–239 e 269–272', 'Uma convoca; a outra dá ciência',
          '<p>Citação convoca réu, executado ou interessado para integrar o processo e dá ciência da demanda. Intimação dá ciência dos atos e termos. Comparecimento espontâneo supre falta ou nulidade da citação e faz correr o prazo de resposta. A intimação é eletrônica sempre que possível; quando não eletrônica, em regra ocorre pela publicação no órgão oficial. A publicação é nula se não indicar nomes das partes e dos advogados com número de inscrição na OAB; a nulidade é arguida no próprio ato que couber à parte praticar.</p>' + src(r1), 'dif'),
        S('p-cit2', 'CPC, arts. 67–69, 236–237', 'Quatro cartas; cooperação pode dispensá-las',
          '<p>A carta é instrumento formal quando o ato precisa ser praticado fora dos limites territoriais, salvo previsão legal. A de ordem parte do tribunal para juízo vinculado; a rogatória vai do juízo brasileiro a órgão estrangeiro; a precatória liga juízos brasileiros de competências territoriais diferentes; a arbitral parte do juízo arbitral para órgão do Judiciário. Já o pedido de cooperação entre juízos para qualquer ato dispensa forma específica e pode ser atendido por auxílio direto, reunião ou apensamento, informação ou ato concertado.</p>' + src(r2), 'mix'),
    ])


FIGS[(COURSE, 'aula-06-citacao.html')] = {3: fig_pc06}

"""Aula 08 figure scratch: contestação as a checklist dossier."""

def _pc08(k):
    pid = f'p-pc08-{k}'
    o = hdr({0: 'CONTESTAÇÃO · TRIAGEM PROCESSUAL',
             1: 'CONTESTAÇÃO · MÉRITO E PROVA',
             2: 'ART. 335 · MARCO INICIAL'}[k])
    if k == 0:
        o += card(30, 48, 540, 66, '1 · PRELIMINARES · ART. 337',
                  'Alegue antes do mérito: organize as questões processuais.', 'ink', ts=16, bs=13, ctx='pc08a')
        rows = [
            ('CITAÇÃO · FORO · CAUSA', 'falta ou nulidade da citação · incompetência absoluta ou relativa · valor da causa · inépcia', 'paper'),
            ('PROCESSO · REPRESENTAÇÃO', 'perempção · litispendência · coisa julgada · conexão · capacidade ou representação irregular', 'paper'),
            ('ARBITRAGEM · PARTES · OUTRAS', 'convenção de arbitragem · ilegitimidade ou falta de interesse · caução · gratuidade indevida', 'paper'),
        ]
        for i, (title, body, tone) in enumerate(rows):
            o += card(30, 126 + i * 86, 540, 76, title, body, tone, ts=14, bs=12.5, ctx='pc08a')
        o += card(30, 390, 264, 120, 'EXCEÇÃO · INCOMPETÊNCIA RELATIVA',
                  'Depende de alegação do réu; não conte com exame de ofício.', 'dif', ts=13.5, bs=12.5, ctx='pc08a')
        o += card(306, 390, 264, 120, 'EXCEÇÃO · CONVENÇÃO ARBITRAL',
                  'Alegue e indique a convenção: o silêncio importa aceitação da jurisdição estatal.', 'conc', ts=13.5, bs=11.5, ctx='pc08a')
    elif k == 1:
        o += card(30, 48, 540, 66, '2 · MÉRITO · ART. 341',
                  'Responda separadamente a cada fato relevante da inicial.', 'ink', ts=16, bs=13, ctx='pc08b')
        o += card(30, 126, 258, 94, 'FATO POR FATO',
                  'Admita, negue ou explique: recebimento, acordo e pagamento não são uma só pergunta.', 'paper', ts=14, bs=12.5, ctx='pc08b')
        o += card(302, 126, 268, 94, 'EVITE A NEGATIVA GENÉRICA',
                  'Fato sem impugnação específica presume-se verdadeiro, ressalvadas as exceções legais.', 'dif', ts=14, bs=12.5, ctx='pc08b')
        o += card(30, 234, 540, 112, 'TRÊS LIMITES À PRESUNÇÃO',
                  '1 · fato que não admite confissão  |  2 · ato cuja substância exige instrumento legal  |  3 · fato incompatível com a defesa lida em conjunto', 'paper', ts=14, bs=13, ctx='pc08b')
        o += card(30, 360, 258, 106, 'EXCEÇÃO AO ÔNUS',
                  'Defensor público · advogado dativo · curador especial.', 'conc', ts=14, bs=12.5, ctx='pc08b')
        o += card(302, 360, 268, 106, 'LIGUE FATO E PROVA',
                  'Negou assinatura? Indique documento e perícia. Afirmou pagamento? Junte recibo ou extrato.', 'ink', ts=14, bs=12.5, ctx='pc08b')
        o += tx(42, 501, 'Teses subsidiárias: ordene-as e explique sua relação.', 12.5, w=520, weight=550, ctx='pc08b')
    else:
        o += card(30, 48, 540, 82, '3 · QUINZE DIAS · IDENTIFIQUE O CASO',
                  'O prazo é de quinze dias; o começo varia conforme o processo chegou à resposta.', 'ink', ts=15, bs=12.5, ctx='pc08c')
        o += card(30, 140, 540, 104, 'I · AUDIÊNCIA SEM ACORDO',
                  'Conte da audiência ou da última sessão de conciliação ou mediação.', 'conc', ts=15, bs=13, ctx='pc08c')
        o += card(30, 256, 540, 104, 'II · CANCELAMENTO PEDIDO PELO RÉU',
                  'Na hipótese legal de cancelamento, conte do protocolo do pedido.', 'dif', ts=15, bs=13, ctx='pc08c')
        o += card(30, 372, 540, 104, 'III · DEMAIS CASOS',
                  'Conte da data prevista para a modalidade de citação usada.', 'paper', ts=15, bs=13, ctx='pc08c')
        o += tx(42, 500, 'Primeiro encontre o marco; depois conte os quinze dias.', 13, w=520, weight=600, ctx='pc08c')
    return o


def fig_pc08():
    ref = 'CPC arts. 335, 337 e 341; draft unit-08-defendant-response: “O prazo depende de como o processo chegou à fase de resposta”, “Concentre a defesa na contestação”, “Conteste cada fato que importa”, “O que a contestação deve entregar”'
    panels = [
        ('p-pc08-0', _pc08(0), 'Preliminares'),
        ('p-pc08-1', _pc08(1), 'Mérito e prova'),
        ('p-pc08-2', _pc08(2), 'Prazo'),
    ]
    steps = [
        S('p-pc08-0', '1 · Triagem', 'Preliminares antes do mérito',
          '<p>Organize as matérias do art. 337 antes de discutir o mérito. Duas dependem de alegação do réu: incompetência relativa e convenção de arbitragem. A falta de alegação da convenção importa aceitação da jurisdição estatal.</p>' + src(ref), 'dif'),
        S('p-pc08-1', '2 · Resposta', 'Fato, posição e prova',
          '<p>O art. 341 exige manifestação precisa sobre os fatos. A presunção de veracidade não alcança fato que não admite confissão, não supre instrumento legalmente exigido para a substância do ato e não prevalece contra a defesa lida em conjunto. Defensor público, advogado dativo e curador especial estão dispensados do ônus de impugnação específica. Indique as provas ligadas aos fatos controvertidos.</p>' + src(ref), 'conc'),
        S('p-pc08-2', '3 · Prazo', 'Quinze dias a partir do marco aplicável',
          '<p>O art. 335 prevê três começos: audiência ou última sessão sem acordo; protocolo do pedido de cancelamento feito pelo réu, na hipótese legal; ou data prevista para a modalidade de citação nos demais casos.</p>' + src(ref), 'dif'),
    ]
    return kit.scrolly('Dossiê de contestação', panels, steps)


FIGS[(COURSE, 'aula-08.html')] = {4: fig_pc08}

def _pc09(k):
    pid = f'p-pc09-{k}'
    o = ''
    if k == 0:
        o += hdr('DO DEFEITO À INVALIDAÇÃO: UMA ESCADA')
        o += card(70, 52, 460, 72, '1 · FINALIDADE', 'A forma falhou. O ato ainda cumpriu seu papel?', 'paper', ts=16, ctx='pc09a', center=True)
        o += arr(pid, 300, 124, 300, 144)
        o += card(70, 144, 460, 82, 'SIM · aproveite', 'Marta recebeu a intimação por outro meio, compareceu e se defendeu. Art. 277.', 'conc', ts=16, bs=13, ctx='pc09a')
        o += elbow(pid, [(300, 226), (300, 246), (180, 246), (180, 264)], 'c')
        o += card(30, 264, 265, 100, 'SEM PREJUÍZO', 'Sem dano à parte: não repita o ato (art. 282, § 1º).', 'conc', ts=15, ctx='pc09a')
        o += elbow(pid, [(300, 226), (300, 246), (420, 246), (420, 264)], 'd')
        o += card(305, 264, 265, 100, 'NÃO · houve prejuízo', 'Bruno soube da audiência só depois da sentença: faltou chance de defesa.', 'dif', ts=15, bs=13, ctx='pc09a')
        o += arr(pid, 438, 364, 438, 388, 'd')
        o += card(305, 388, 265, 104, '2 · TENTE APROVEITAR', 'Corrigir ou aproveitar como outro ato, se a defesa não sofrer prejuízo (art. 283).', 'mix', ts=14, bs=12.5, ctx='pc09a')
        o += arr(pid, 438, 492, 438, 516, 'd')
        o += card(305, 516, 265, 62, '3 · SÓ ENTÃO: INVALIDAR', 'Se nada resolve o prejuízo.', 'dif', ts=14, bs=12, ctx='pc09a')
    elif k == 1:
        o += hdr('A NULIDADE ALCANÇA O QUE DEPENDE DO ATO')
        o += card(30, 54, 250, 84, 'CITAÇÃO NULA', 'O réu não soube da ação.', 'dif', ts=16, ctx='pc09b', center=True)
        o += card(320, 54, 250, 84, 'FICAM', 'Petição inicial e despacho que mandou citar: são anteriores.', 'paper', ts=14, bs=12.5, ctx='pc09b')
        o += elbow(pid, [(280, 96), (300, 96), (300, 164)], 'i')
        o += hdr('CAEM SE DEPENDEM DA CITAÇÃO', y=184)
        o += card(30, 204, 540, 88, 'REVELIA → SANEAMENTO → SENTENÇA', 'Atos subsequentes dependentes perdem efeito (art. 281).', 'dif', ts=16, ctx='pc09b', center=True)
        o += card(30, 308, 265, 92, 'ATO INDEPENDENTE', 'Pode permanecer. O juiz fundamenta o alcance em fatos concretos.', 'conc', ts=14, bs=12.5, ctx='pc09b')
        o += card(305, 308, 265, 92, 'DÚVIDA: PERÍCIA', 'Se depende da citação? O juiz decide caso a caso e fundamenta.', 'mix', ts=14, bs=12.5, ctx='pc09b')
        o += card(30, 416, 540, 106, 'O JUIZ DELIMITA', 'Ao pronunciar a nulidade, indica os atos atingidos e ordena repetição ou retificação (art. 282). Comparecimento do réu pode suprir citação defeituosa (art. 239, § 1º).', 'paper', ts=15, bs=12.5, ctx='pc09b')
    else:
        o += hdr('QUEM ALEGA — E EM QUAL MOMENTO')
        o += card(30, 52, 540, 76, 'A PARTE PREJUDICADA', 'Alega na primeira oportunidade em que puder falar nos autos (art. 278).', 'paper', ts=16, ctx='pc09c', center=True)
        o += arr(pid, 300, 128, 300, 148)
        o += card(30, 148, 265, 112, 'CARLA SABE DO DEFEITO', 'Comparece à audiência e fica em silêncio.', 'mix', ts=15, ctx='pc09c')
        o += card(305, 148, 265, 112, 'PRIMEIRA OPORTUNIDADE', 'Era o momento de alegar, se o tipo de defeito preclui.', 'conc', ts=15, bs=12.5, ctx='pc09c')
        o += arr(pid, 162, 260, 162, 284, 'm')
        o += card(30, 284, 265, 108, 'SÓ DEPOIS DE PERDER', 'A nulidade de algibeira chega tarde: silêncio pode gerar preclusão.', 'dif', ts=14, bs=12.5, ctx='pc09c')
        o += card(305, 284, 265, 108, 'DEU CAUSA AO VÍCIO?', 'O art. 276 impede a parte de pedir a nulidade que ela própria provocou.', 'dif', ts=14, bs=12.5, ctx='pc09c')
        o += card(30, 416, 540, 118, 'EXCEÇÕES DO ART. 278, p.u.', 'Sem preclusão para nulidade que o juiz deve decretar de ofício; também se a parte provar legítimo impedimento. O juiz pode reconhecê-la de ofício.', 'paper', ts=15, bs=12.5, ctx='pc09c')
    return o


def fig_pc09():
    ref = 'draft unit-09-nullities: “Finalidade, prejuízo e aproveitamento”; “Quais atos caem com o ato invalidado”; “Quem pode alegar o defeito e até quando”; CPC arts. 239 § 1º, 276, 278, 281, 282, 283'
    return kit.scrolly('Nulidade: da finalidade ao alcance', [
        ('p-pc09-0', _pc09(0), 'Finalidade, prejuízo, aproveitamento'),
        ('p-pc09-1', _pc09(1), 'Atos dependentes'),
        ('p-pc09-2', _pc09(2), 'Quem alega e quando')], [
        S('p-pc09-0', 'CPC, arts. 277, 282 § 1º e 283', 'A forma falhou: qual foi o prejuízo?',
          '<p>Comece pela finalidade. Marta recebeu a intimação por outro meio, compareceu e se defendeu: o ato cumpriu seu papel (art. 277). Bruno só soube da audiência depois da sentença e perdeu a chance de defesa: há prejuízo. Ainda assim, tente aproveitar ou corrigir o ato sem prejuízo à defesa (arts. 282, § 1º, e 283). A nulidade é a última saída.</p>' + src(ref), 'dif'),
        S('p-pc09-1', 'CPC, arts. 281 e 282', 'A nulidade se propaga pelos atos dependentes',
          '<p>Se a citação é nula, permanecem a inicial e o despacho que mandou citar. Revelia, saneamento e sentença dependentes da citação perdem efeito. A perícia exige análise concreta: o juiz fundamenta se dependia do ato inválido. Ao pronunciar a nulidade, indica os atos atingidos e ordena repetição ou retificação (art. 282). O comparecimento pode suprir a citação defeituosa (art. 239, § 1º).</p>' + src(ref), 'conc'),
        S('p-pc09-2', 'CPC, arts. 276 e 278', 'A parte alega na primeira oportunidade',
          '<p>Carla comparece, silencia e só alega a falha depois de perder. Se aquele defeito está sujeito à preclusão, o art. 278 barra a alegação tardia; se Carla provocou o vício, o art. 276 também a impede. A lei excepciona a preclusão quando o juiz deve decretar a nulidade de ofício ou quando há legítimo impedimento provado. A nulidade de algibeira não deve ser guardada para depois do resultado.</p>' + src(ref), 'mix'),
    ])

FIGS[('processo-civil', 'aula-09.html')] = {5: fig_pc09}
