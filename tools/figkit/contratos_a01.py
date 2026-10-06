"""Contratos Aula 01: classify legal facts, read the contract, and test its destination."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))

from figkit import Document, Field, line, statute, svg, t

STEPS1 = [
    'Fato jurídico em sentido estrito',
    'Ato-fato',
    'Ato jurídico em sentido estrito',
    'Negócio jurídico',
]
IDS1 = ['p-lad0', 'p-lad1', 'p-lad2', 'p-lad3']

STEPS2 = [
    'O acordo de vontades',
    'A operação econômica e sua roupagem',
    'O contrato no Direito',
]
IDS2 = ['p-est', 'p-sub', 'p-nor']

STEPS3 = [
    'O bem termina no uso ou volta para o mercado?',
    'Três correntes',
    'Mesmo critério, resultados opostos',
]
IDS3 = ['p-dest', 'p-teo', 'p-cas']


def fact_field(k):
    """Classify the four legal-fact forms by human action and the will's role."""
    f = Field('tgc01-facts', x0=190, x1=540, y0=130, y1=430)
    f.axes(
        [(235, ('não', 'há ação humana')), (455, ('sim', 'há ação humana'))],
        [
            (150, ('vontade escolhe', 'conteúdo e efeitos')),
            (280, ('vontade age', 'a lei fixa os efeitos')),
            (410, ('vontade irrelevante', 'só o resultado conta')),
        ],
        xtitle='Ação humana',
        ytitle='Papel da vontade',
    )
    f.point(235, 410, 'Fato jurídico estrito', active=k == 0, tone='ink',
            dx=12, dy=-58, sub='natureza · nascimento · morte · tempo')
    f.point(455, 410, 'Ato-fato', active=k == 1, tone='ink',
            dx=-10, dy=-28, anchor='end', sub='caça · tomada de posse')
    f.point(455, 280, 'Ato jurídico em sentido estrito', active=k == 2, tone='ink',
            dx=-12, dy=-24, anchor='end', sub='domicílio · a lei define efeitos')
    f.point(510, 150, 'Negócio jurídico', active=k == 3, tone='ink',
            dx=-12, dy=-24, anchor='end', sub='contrato · vontade escolhe conteúdo')
    o = t(40, 60, 'QUATRO FORMAS DE FATO JURÍDICO', size=11, caps=True, weight=700,
          fill='var(--ink-2)')
    o += t(40, 82, 'Ação humana e papel da vontade organizam a classificação.',
           size=11, fill='var(--ink)')
    o += f.svg()
    o += t(40, 505, 'Do acontecimento natural à escolha de efeitos dentro dos limites legais.',
           size=10.5, fill='var(--ink-2)')
    return svg('24 44 552 484', o, cls='panel fig on' if k == 0 else 'panel fig',
               ident=IDS1[k], label=STEPS1[k])


def panels1():
    return [fact_field(k) for k in range(4)]


def contract_document(k):
    """The agreement as two declarations meeting in the real paper form."""
    proposal = Document('tgc01-proposal', 38, 82, 132, [
        ('title', 'Proposta', 'title'),
        ('clause', 'declaração', 'declaration'),
    ], lead=14, indent=0, foot=0)
    acceptance = Document('tgc01-acceptance', 210, 82, 132, [
        ('title', 'Aceitação', 'title'),
        ('clause', 'declaração', 'declaration'),
    ], lead=14, indent=0, foot=0)
    agreement = Document('tgc01-agreement', 86, 250, 208, [
        ('title', 'Acordo', 'title'),
        ('sign', ('proponente', 'aceitante'), 'signatures'),
    ], lead=14, indent=0, foot=2)

    o = proposal.paper() + ''.join(proposal.parts)
    o += acceptance.paper() + ''.join(acceptance.parts)
    # The two declaration paths meet before the resulting agreement sheet.
    o += '<path d="M104 166C104 194 154 194 184 224" style="fill:none;stroke:var(--dif);stroke-width:2.2"/>'
    o += '<path d="M276 166C276 194 226 194 196 224" style="fill:none;stroke:var(--conc);stroke-width:2.2"/>'
    o += '<path d="M180 220L190 226L182 233Z" style="fill:var(--dif)"/>'
    o += '<path d="M200 220L190 226L198 233Z" style="fill:var(--conc)"/>'
    o += '<circle cx="190" cy="226" r="4.2" style="fill:var(--mix)"/>'
    o += line(190, 231, 190, 248, tone='mix', w=2)
    o += '<path d="M184 242L190 250L196 242Z" style="fill:var(--mix)"/>'
    o += agreement.paper() + ''.join(agreement.parts)
    return svg('24 44 352 352', o,
               cls='panel fig on' if k == 0 else 'panel fig',
               ident=IDS2[k], label=STEPS2[k])


def economic_roupagem():
    """The agreement sheet clothes the goods/price loop; speculation is a sliver."""
    wrapper = Document('tgc01-roupage', 38, 56, 314,
                       [('title', 'Acordo', 'title')], foot=260)
    o = wrapper.paper() + ''.join(wrapper.parts)
    # Opposing arcs make the goods/price exchange a circulating relation.
    o += '<path d="M116 222C116 172 274 172 274 222" style="fill:none;stroke:var(--dif);stroke-width:2.5"/>'
    o += '<path d="M274 250C274 300 116 300 116 250" style="fill:none;stroke:var(--dif);stroke-width:2.5"/>'
    o += '<path d="M268 214L278 222L267 226Z" style="fill:var(--dif)"/>'
    o += '<path d="M122 258L112 250L123 246Z" style="fill:var(--dif)"/>'
    # A short accent on the larger circuit is the small speculative part of the whole.
    o += '<path d="M244 184C254 190 262 199 267 209" style="fill:none;stroke:var(--conc);stroke-width:4;stroke-linecap:round"/>'
    o += t(342, 163, 'Derivativos', size=10.5, anchor='end',
           fill='var(--conc)', weight=700)
    # The marks are objects; the words label them.
    o += '<path d="M101 225H131V247H101Z M101 225L116 236L131 225 M116 236V247" style="fill:none;stroke:var(--mix);stroke-width:1.8;stroke-linejoin:round"/>'
    o += '<circle cx="274" cy="236" r="15" style="fill:var(--paper);stroke:var(--mix);stroke-width:1.8"/>'
    o += line(274, 225, 274, 247, tone='mix', w=1.6)
    o += t(116, 320, 'Bens', size=11.5, anchor='middle', fill='var(--mix)', weight=700)
    o += t(274, 320, 'Preço', size=11.5, anchor='middle', fill='var(--mix)', weight=700)
    return svg('24 44 352 352', o, cls='panel fig', ident=IDS2[1],
               label=STEPS2[1])


# Exact excerpts checked against the official Civil Code at Planalto:
# https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm
def statute_cut():
    o = t(40, 58, 'A FORMA JURÍDICA DÁ FORÇA E IMPÕE LIMITES',
          size=10.5, caps=True, weight=700, fill='var(--ink-2)')
    s1, h1 = statute(40, 86, 520, 'Código Civil · art. 421', [
        ('A liberdade contratual será exercida ', False),
        ('nos limites da função social do contrato.', True),
    ], tone='conc')
    s2, h2 = statute(40, 86 + h1 + 18, 520, 'Código Civil · art. 421-A', [
        ('Os contratos civis e empresariais presumem-se ', False),
        ('paritários e simétricos', True),
        (' até a presença de elementos concretos que justifiquem o afastamento dessa presunção, ', False),
        ('ressalvados os regimes jurídicos previstos em leis especiais', True),
        (', garantido também que: […]', False),
    ], tone='conc')
    o += s1 + s2
    y = 86 + h1 + 18 + h2 + 44
    o += t(40, y, 'A FORMA JURÍDICA', size=10.5, caps=True, weight=700,
           fill='var(--conc)')
    o += t(40, y + 24, 'dá força obrigatória e orienta interpretação,',
           size=10.5, fill='var(--ink)')
    o += t(40, y + 38, 'execução e limites da operação.',
           size=10.5, fill='var(--ink)')
    return svg('24 42 552 426', o, cls='panel fig', ident=IDS2[2], label=STEPS2[2])


def panels2():
    return [contract_document(0), economic_roupagem(), statute_cut()]

def destination_field():
    f = Field('tgc01-destination', x0=142, x1=340, y0=133, y1=288)
    f.axes(
        [(185, ('necessidade', 'própria')), (311, ('na', 'atividade'))],
        [(152, ('uso', 'próprio')), (268, ('uso', 'na atividade'))],
        xtitle='Uso pelo adquirente',
        ytitle='Destino do bem',
    )
    f.point(185, 152, 'Destinatário final', active=True, tone='dif',
            dx=12, dy=-20, sub='necessidade própria')
    f.point(311, 268, 'Intermediário', active=True, tone='conc',
            dx=39, dy=-46, anchor='end', sub='insumo · peça · revenda')
    return svg('24 44 352 352', f.svg(), cls='panel fig on', ident=IDS3[0],
               label=STEPS3[0])

def theory_field():
    f = Field('tgc01-theories', x0=148, x1=342, y0=134, y1=285)
    f.axes(
        [(200, ('não', '')), (320, ('sim', ''))],
        [(150, ('sim', 'prova')), (266, ('não', 'sem prova'))],
        xtitle='Destinação econômica',
        ytitle='Vulnerabilidade',
    )
    f.point(200, 266, 'Maximalista', active=True, tone='ink',
            dx=12, dy=-45)
    f.point(320, 266, 'Finalista', active=True, tone='ink',
            dx=-12, dy=-29, anchor='end')
    f.point(320, 150, 'Finalismo aprofundado', active=True, tone='dif',
            dx=30, dy=-36, anchor='end', sub='vulnerabilidade provada')
    return svg('24 44 352 352', f.svg(), cls='panel fig', ident=IDS3[1],
               label=STEPS3[1])

def case_sheets():
    left = Document('tgc01-case-aircraft', 34, 70, 148,
                    [('title', 'Aeronave', 'title')], foot=218)
    right = Document('tgc01-case-ticket', 206, 70, 148,
                     [('title', 'Intermediação', 'title')], foot=218)
    o = left.paper() + ''.join(left.parts)
    o += right.paper() + ''.join(right.parts)
    o += left.stamp('CDC APLICADO', 108, 151, tone='dif', angle=-3)
    o += right.stamp('CDC AFASTADO', 280, 151, tone='conc', angle=-3)
    for x0, x1, cx in ((48, 168, 64), (220, 340, 324)):
        o += t((x0 + x1) / 2, 197, 'DESTINAÇÃO', size=9.5,
               anchor='middle', fill='var(--ink-2)', weight=700)
        o += line(x0, 221, x1, 221, tone='ink', w=1.4)
        o += line(x0, 215, x0, 227, tone='ink', w=1.2)
        o += line(x1, 215, x1, 227, tone='ink', w=1.2)
        o += f'<circle cx="{cx}" cy="221" r="6" style="fill:var(--mix);stroke:var(--paper);stroke-width:1.2"/>'
        o += t(x0, 246, 'PRÓPRIO', size=10, fill='var(--ink)')
        o += t(x1, 246, 'ATIVIDADE', size=10, anchor='end', fill='var(--ink)')
    return svg('24 44 352 352', o, cls='panel fig', ident=IDS3[2],
               label=STEPS3[2])

def panels3():
    return [destination_field(), theory_field(), case_sheets()]
