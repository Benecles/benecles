"""Contratos Aula 01 · Fig. 2 (Três leituras do contrato, 4 steps) and Fig. 3 (Destinação final, 3 steps).
One real contract runs through both: Ana buys a notebook from Loja Pixel."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from figkit import Document, statute, badge, svg, t, line, TONE, WASH

LINES = [
    ('title', 'Contrato de compra e venda', 'tt'),
    ('party', ('Vendedora', 'Loja Pixel Ltda.'), 'pv'),
    ('party', ('Compradora', 'Ana Souza'), 'pc'),
    ('clause', ('Cl. 1ª', 'Objeto: um notebook novo, modelo Aurora 14.'), 'c1'),
    ('clause', ('Cl. 2ª', 'Preço: R$ 4.200,00, pagos à vista na assinatura.'), 'c2'),
    ('clause', ('Cl. 3ª', 'Entrega em até 5 dias, no endereço da compradora.'), 'c3'),
    ('clause', ('Cl. 4ª', 'Garantia contratual de 12 meses.'), 'c4'),
    ('place', 'Porto Alegre, 1º de outubro de 2026.', 'pl'),
    ('sign', ('Loja Pixel Ltda.', 'Ana Souza'), 's'),
]
STEPS2 = ['O acordo de vontades', 'A operação econômica', 'Operação econômica não é especulação', 'O contrato no Direito']
IDS2 = ['p-est', 'p-sub', 'p-esp', 'p-nor']


def chip(x, y, text, tone='ink', fill=True):
    w = len(text) * 7.4 + 20
    st = f'fill:{WASH[tone] if fill else "var(--paper)"};stroke:{TONE[tone]};stroke-width:1.3'
    return f'<rect x="{x:g}" y="{y - 15}" width="{w:g}" height="22" style="{st}"/>' + t(x + 10, y, text, size=11, weight=700, caps=True, fill=TONE[tone]), w


def fig2(k):
    d = Document(f'tgc01-{k}', 160, 34, 320, LINES, foot=40)
    o = d.paper()
    band = d.y + d.h + 48
    if k == 0:   # proposta + aceitação
        o = d.paper() + d.highlight(['c1', 'c2'], 'conc') + d.highlight(['s1'], 'dif')
        o += ''.join(d.parts)
        o += d.bracket(['c1', 'c2'], 'left', 'Proposta', 'o que e por quanto', tone='conc')
        o += d.bracket(['s1'], 'right', 'Aceitação', 'Ana assina', tone='dif')
        x = 60
        c, w = chip(x, band + 30, 'proposta', 'conc'); o += c; x += w + 14
        o += t(x, band + 30, '+', size=16, weight=700); x += 24
        c, w = chip(x, band + 30, 'aceitação', 'dif'); o += c; x += w + 14
        o += t(x, band + 30, '=', size=16, weight=700); x += 24
        c, w = chip(x, band + 30, 'acordo', 'ink', fill=False); o += c
        o += t(60, band + 64, 'duas declarações unilaterais que se encontram:', size=11, fill='var(--ink-2)')
        o += t(60, band + 80, 'negócio bilateral quanto à formação', size=11, weight=700)
    elif k == 1:  # bem ↔ preço
        o = d.paper() + d.highlight(['c1'], 'dif') + d.highlight(['c2'], 'conc') + ''.join(d.parts)
        o += d.bracket(['c1'], 'right', 'o bem', tone='dif')
        o += d.bracket(['c2'], 'left', 'o preço', tone='conc')
        y = band + 40
        o += f'<rect x="70" y="{y - 22}" width="140" height="44" style="fill:var(--paper);stroke:var(--ink);stroke-width:1.5"/>' + t(140, y + 4, 'Loja Pixel', size=11.5, anchor='middle', weight=700)
        o += f'<rect x="390" y="{y - 22}" width="140" height="44" style="fill:var(--paper);stroke:var(--ink);stroke-width:1.5"/>' + t(460, y + 4, 'Ana', size=11.5, anchor='middle', weight=700)
        o += f'<path d="M214 {y - 10}H380" style="stroke:var(--dif);stroke-width:2.2"/><path d="M386 {y - 10}l-9 -5v10z" style="fill:var(--dif)"/>'
        o += t(297, y - 18, 'notebook', size=11, anchor='middle', weight=700, fill='var(--dif)')
        o += f'<path d="M386 {y + 10}H220" style="stroke:var(--conc);stroke-width:2.2"/><path d="M214 {y + 10}l9 -5v10z" style="fill:var(--conc)"/>'
        o += t(300, y + 30, 'R$ 4.200,00', size=11, anchor='middle', weight=700, fill='var(--conc)')
        o += t(300, y + 64, 'a função do contrato: fazer a riqueza circular', size=11, anchor='middle', fill='var(--ink-2)')
    elif k == 2:  # operação econômica, sem aposta
        o = d.paper() + ''.join(d.parts) + d.stamp('USO PRÓPRIO', d.x + d.w - 100, d.y + d.h - 24, tone='dif', angle=-6)
        y = band + 8
        o += t(60, y, 'Operação', size=10, caps=True, weight=700, fill='var(--ink-2)')
        o += t(380, y, 'econômica?', size=10, caps=True, weight=700, fill='var(--ink-2)', anchor='middle')
        o += t(490, y, 'aposta?', size=10, caps=True, weight=700, fill='var(--ink-2)', anchor='middle')
        rows = [('o notebook de Ana, para uso próprio', True, False), ('seguro do próprio carro', True, False),
                ('serviço contratado para tocar a atividade', True, False), ('derivativo (especulativo: parte pequena)', True, True)]
        for i, (txt, eco, bet) in enumerate(rows):
            ry = y + 30 + i * 30
            o += line(60, ry - 19, 540, ry - 19, tone='muted', w=.8)
            o += t(60, ry, txt, size=11, weight=700 if i == 0 else 500)
            o += badge(380, ry - 4, eco, r=9)
            o += t(490, ry, 'sim' if bet else 'não', size=11, anchor='middle', weight=700 if bet else 500, fill='var(--conc)' if bet else 'var(--ink-2)')
    else:  # normativo: o contrato no Direito
        o = d.paper() + ''.join(d.parts)
        o += d.bracket(['c1', 'c2', 'c3', 'c4'], 'right', 'força', 'obrigatória', tone='ink')
        s1, h1 = statute(40, band - 6, 520, 'Código Civil · art. 421',
                         [('A liberdade contratual será exercida', False), ('nos limites da função social do contrato.', True)], tone='conc')
        s2, h2 = statute(40, band + h1 + 4, 520, 'Código Civil · art. 421-A',
                         [('Os contratos civis e empresariais', False), ('presumem-se paritários e simétricos', True),
                          ('até a presença de elementos concretos que justifiquem o afastamento dessa presunção,', False),
                          ('ressalvados os regimes jurídicos previstos em leis especiais', True), ('[…]', False)], source='→ CDC · Fig. 3', tone='conc')
        o += s1 + s2
    cls = 'panel fig on' if k == 0 else 'panel fig'
    return svg('0 0 600 600', o, cls=cls, ident=IDS2[k], label=STEPS2[k])


def route(k):
    """Destinação final: where the good ends. k=0 the question, k=2 the two STJ cases."""
    o = ''
    st = lambda x, y, tone='ink', r=8: f'<circle cx="{x}" cy="{y}" r="{r}" style="fill:var(--paper);stroke:{TONE[tone]};stroke-width:2.2"/>'
    o += line(300, 78, 300, 170, w=2.2) + line(300, 182, 300, 230, w=2.2)
    o += f'<path d="M300 230C300 290 160 270 160 322" style="fill:none;stroke:var(--dif);stroke-width:2.6"/>'
    o += f'<path d="M300 230C300 290 440 270 440 322" style="fill:none;stroke:var(--conc);stroke-width:2.6"/>'
    o += f'<path d="M448 330H540V70H316" style="fill:none;stroke:var(--conc);stroke-width:1.6;stroke-dasharray:5 4"/><path d="M310 70l9 -5v10z" style="fill:var(--conc)"/>'
    o += t(532, 214, 'volta ao', size=10, anchor='end', fill='var(--conc)', weight=700, caps=True)
    o += t(532, 228, 'mercado', size=10, anchor='end', fill='var(--conc)', weight=700, caps=True)
    o += st(300, 70) + t(284, 66, 'Fornecedor', size=11, weight=700, caps=True, anchor='end') + t(284, 80, 'produz, distribui, vende', size=10.5, fill='var(--ink-2)', anchor='end')
    o += st(300, 176) + t(316, 172, 'Adquirente', size=11, weight=700, caps=True) + t(316, 186, 'compra o bem ou serviço', size=10.5, fill='var(--ink-2)')
    o += f'<circle cx="300" cy="230" r="4" style="fill:var(--ink)"/>'
    o += t(262, 246, 'para onde vai o bem?', size=10.5, anchor='end', fill='var(--ink-2)')
    o += f'<circle cx="160" cy="330" r="10" style="fill:var(--dif);stroke:var(--dif)"/>'
    o += st(440, 330, 'conc')
    o += t(160, 362, 'Destinatário final', size=11, weight=700, caps=True, anchor='middle', fill='var(--dif)')
    o += t(160, 377, 'o bem termina no uso', size=10.5, anchor='middle')
    o += t(440, 362, 'Consumo intermediário', size=11, weight=700, caps=True, anchor='middle', fill='var(--conc)')
    o += t(440, 377, 'insumo, ferramenta, revenda', size=10.5, anchor='middle')
    c, w = chip(160 - 30, 404, 'CDC', 'dif'); o += c
    c, w = chip(440 - 63, 404, 'Código Civil', 'conc'); o += c
    if k == 0:
        o += t(160, 450, 'o notebook de Ana', size=11, anchor='middle', weight=700)
        o += t(160, 465, 'atende a necessidade própria', size=10.5, anchor='middle', fill='var(--ink-2)')
        o += t(440, 450, 'notebooks que a loja revende', size=11, anchor='middle', weight=700)
        o += t(440, 465, 'entram na atividade', size=10.5, anchor='middle', fill='var(--ink-2)')
        o += t(300, 530, 'conta a função econômica real, não o desgaste do bem', size=11, anchor='middle', fill='var(--ink-2)')
    else:
        for cx, tone, head, body, res in ((160, 'dif', 'STJ · aeronave', ['administradora de imóveis', 'usa o avião para si;', 'não integra o que vende'], 'CDC aplicado'),
                                          (440, 'conc', 'STJ · intermediação', ['vendedora de ingressos', 'usa o serviço para operar', 'o próprio negócio'], 'CDC afastado')):
            o += f'<rect x="{cx - 120}" y="440" width="240" height="118" style="fill:var(--paper);stroke:{TONE[tone]};stroke-width:1.4"/>'
            o += t(cx - 106, 462, head, size=11, weight=700, caps=True, fill=TONE[tone])
            for i, b in enumerate(body):
                o += t(cx - 106, 482 + i * 15, b, size=10.5)
            o += t(cx - 106, 544, res, size=11, weight=700, caps=True, fill=TONE[tone])
    return o


def matrix():
    o = t(40, 50, 'Pessoa jurídica: quando é destinatária final?', size=10.5, caps=True, weight=700, fill='var(--ink-2)')
    cols = [(360, ['aeronave', 'uso próprio']), (500, ['intermediação de', 'pagamentos · atividade'])]
    for cx, (a, b) in cols:
        o += t(cx, 96, a, size=10.5, anchor='middle', weight=700) + t(cx, 110, b, size=10, anchor='middle', fill='var(--ink-2)')
    rows = [('Finalista', 'retira o bem do mercado, de fato', 'e economicamente', (True, False), False),
            ('Maximalista', 'basta ser destinatária', 'de fato', (True, True), False),
            ('Finalismo aprofundado', 'finalista, mas cede se a empresa', 'prova vulnerabilidade · STJ', (True, False), True)]
    for i, (name, l1, l2, marks, stj) in enumerate(rows):
        y = 168 + i * 112
        if stj:
            o += f'<rect x="30" y="{y - 40}" width="540" height="98" style="fill:var(--dif-wash);opacity:.7"/>'
        o += line(30, y - 40, 570, y - 40, tone='muted', w=.8)
        o += t(44, y - 12, name, size=11.5, weight=700, caps=True, fill='var(--dif)' if stj else 'var(--ink)')
        o += t(44, y + 6, l1, size=10.5) + t(44, y + 20, l2, size=10.5, fill='var(--ink-2)')
        for (cx, _), ok in zip(cols, marks):
            o += badge(cx, y, ok, r=12)
            o += t(cx, y + 30, 'CDC' if ok else 'CC', size=10, anchor='middle', weight=700, fill=TONE['dif' if ok else 'conc'])
    o += line(30, 464, 570, 464, tone='muted', w=.8)
    o += t(44, 494, 'Por que o cuidado: se todos fossem consumidores,', size=11, fill='var(--ink-2)')
    o += t(44, 510, 'a proteção especial do CDC viraria direito comum.', size=11, fill='var(--ink-2)')
    return o


def fig3(k):
    ids, labels = ['p-dest', 'p-teo', 'p-cas'], ['O bem termina no uso ou volta para o mercado?', 'Três correntes', 'Mesmo critério, resultados opostos']
    body = route(0) if k == 0 else (matrix() if k == 1 else route(2))
    return svg('0 0 600 600', body, cls='panel fig on' if k == 0 else 'panel fig', ident=ids[k], label=labels[k])


def panels2():
    return [fig2(k) for k in range(4)]


def panels3():
    return [fig3(k) for k in range(3)]
