from kit import *

# hero: one general road (112/113) with three gated side-roads
hero = ('<path class="draw" d="M30 60H1050" style="stroke:var(--ink);stroke-width:3;fill:none"/>'
        '<g style="font:12px var(--mono);letter-spacing:1px">'
        '<g class="pop" style="--d:.3s"><text x="30" y="40" style="fill:var(--ink)">ARTS. 112 E 113 · A LEITURA GERAL</text></g>')
for i, (x, lab, tone) in enumerate([(200, 'GRATUITO → 114', 'conc'), (480, 'ADESÃO → 423', 'conc'), (760, 'CONSUMO → CDC 47', 'dif')]):
    hero += (f'<path class="draw" style="--d:{.6+.25*i}s;stroke:var(--{tone});stroke-width:2;fill:none" d="M{x} 60C{x} 110 {x+40} 120 {x+80} 130"/>'
             f'<g class="pop" style="--d:{1+.25*i}s"><rect x="{x-8}" y="52" width="16" height="16" style="fill:var(--paper);stroke:var(--{tone});stroke-width:2"/>'
             f'<text x="{x+90}" y="136" style="fill:var(--{tone})">{lab}</text></g>')
hero += '</g>'

# ---- Fig 1: which special rule fires?
QS = [('É NEGÓCIO BENÉFICO OU RENÚNCIA?', 'ART. 114', 'leitura estrita', 'conc'),
      ('É ADESÃO E A CLÁUSULA É AMBÍGUA?', 'ART. 423', 'a favor do aderente', 'conc'),
      ('É RELAÇÃO DE CONSUMO?', 'CDC · ART. 47', 'a favor do consumidor', 'dif')]
def gates(k):
    o = T(40, 60, 'CADA REGRA TEM O SEU GATILHO', 't-small', style='letter-spacing:.1em')
    for i, (q, art, eff, tone) in enumerate(QS):
        y = 90 + i * 140
        on = (k == 3) or (i == k)
        o += G(R(40, y, 290, 70, 'w-grey ink' if on else 'f-paper ink', style='' if on else 'opacity:.4') + T(56, y + 42, q, 't-small', style='' if on else 'opacity:.4'), 'pop' if on else '', d=.1)
        if on:
            o += P(f'M330 {y+35}H364', f'c-{tone} grow', m=f'p-gt{k}-{tone[0]}', extra=' style="--d:.4s"')
            o += G(box(368, y - 5, 192, 80, art, eff, tone, ctx='gt'), 'pop', d=.6)
            o += T(347, y + 25, 'SIM', f't-small tc-{tone}', anchor='middle')
        else:
            o += R(368, y - 5, 192, 80, 'f-paper ink', style='stroke-dasharray:5 4;opacity:.35')
    notes = ['não amplie o que foi dado', 'contradição: vence o aderente', 'antes: há relação de consumo?', 'podem incidir juntas']
    o += G(T(300, 540, notes[k], 't-hand', anchor='middle'), 'fade', d=.9)
    return o

# ---- Fig 2: interpret or integrate?
def gap(k):
    o = T(40, 60, 'O CONTRATO NÃO DIZ', 't-small', style='letter-spacing:.1em')
    o += R(150, 90, 300, 300, 'f-paper ink')
    for i in range(10):
        if i in (4, 5): continue
        o += P(f'M175 {120+i*26}h{250 if i % 3 else 180}', 'thin')
    tone = 'conc' if k == 0 else 'dif'
    o += G(R(170, 220, 260, 44, 'f-paper ink', style='stroke-dasharray:6 4'), 'pulse')
    if k == 0:
        o += G(R(40, 420, 170, 90, 'w-conc ink') + T(56, 452, 'MENSAGENS', 't-small tc-conc') + T(56, 472, 'da negociação:', 't-small') + T(56, 490, '“sábados até 12h”', 't-small'), 'pop', d=.3)
        o += P('M125 420C125 330 150 260 166 244', 'c-conc grow', m='p-gap0-c', extra=' style="--d:.6s"')
        o += G(R(172, 222, 256, 40, 'w-conc', extra=' stroke="none"') + T(300, 248, 'horário estendido = sábado', 't-small tc-conc', anchor='middle'), 'pop', d=1.0)
        o += G(box(250, 420, 310, 90, 'INTERPRETAÇÃO', 'descobre o que foi combinado', 'conc', ctx='gap'), 'pop', d=1.2)
    else:
        o += G(R(390, 430, 170, 80, 'w-dif ink') + T(406, 462, 'LEI SUPLETIVA', 't-small tc-dif') + T(406, 482, 'quando pagar?', 't-small'), 'pop', d=.3)
        o += P('M475 430C475 330 450 260 434 244', 'c-dif grow', m='p-gap1-d', extra=' style="--d:.6s"')
        o += G(R(172, 222, 256, 40, 'w-dif', extra=' stroke="none"') + T(300, 248, 'regra da lei preenche', 't-small tc-dif', anchor='middle'), 'pop', d=1.0)
        o += G(box(40, 420, 330, 90, 'INTEGRAÇÃO', 'completa o que ninguém combinou', 'dif', ctx='gap'), 'pop', d=1.2)
    o += T(300, 575, ['havia intenção comum, só não escrita', 'não havia: a lei completa'][k], 't-hand', anchor='middle')
    return o

def jul(tone, b, span, corpo, tese):
    return f'<article class="julgado {tone}"><header><b>{b}</b><span>{span}</span></header><div class="corpo">{corpo}</div><div class="tese">{tese}</div></article>'

S = lambda panel, label, h3, body, lcls='': dict(panel=panel, label=label, lcls=lcls, h3=h3, body=body)
b = ''
b += chapter('01', 'c1', 'Regras com gatilho próprio', 'Não existe um “leia sempre contra quem escreveu”. Cada regra especial se aplica numa situação definida, e a primeira tarefa é identificar se ela ocorre.')
b += scrolly('Qual regra especial incide', [(f'p-gt{k}', gates(k), l) for k, l in enumerate(['Art. 114', 'Art. 423', 'CDC 47', 'Em conjunto'])], [
    S('p-gt0', 'Art. 114', 'Gratuidade e renúncia: leitura estrita', '<p>Os negócios jurídicos benéficos, como a doação, e a renúncia interpretam-se estritamente. Quem dá sem receber nada em troca não pode ser obrigado, por dedução, a mais do que declarou.</p><p>A regra vale para esses atos. Ela não manda ler restritivamente todo contrato.</p>', 'conc'),
    S('p-gt1', 'Art. 423', 'Adesão: a dúvida favorece o aderente', '<p>No contrato de adesão, cláusulas ambíguas ou contraditórias se interpretam a favor do aderente. Quem redigiu sozinho responde pela falta de clareza.</p><p>O art. 113, § 1º, IV, vai na mesma direção por outro caminho: favorece quem não redigiu a disposição, desde que se saiba quem redigiu. As duas regras têm pressupostos diferentes e podem atuar juntas.</p>', 'conc'),
    S('p-gt2', 'CDC · art. 47', 'Consumo: todas as cláusulas a favor do consumidor', '<p>No contrato de consumo, as cláusulas se interpretam da maneira mais favorável ao consumidor. Não é preciso ambiguidade nem adesão.</p><p>Antes, confirme que a relação é de consumo. Ser aderente, ou contratar com uma empresa, não responde essa pergunta.</p>', 'dif'),
    S('p-gt3', 'Sobreposição', 'Mais de um gatilho no mesmo caso', '<p>Um consumidor que assina um formulário padrão com uma cláusula contraditória aciona o art. 47 do CDC e o art. 423 do Código Civil ao mesmo tempo. As regras somam razões para o mesmo resultado.</p>'),
])
b += chapter('02', 'c2', 'Interpretar ou integrar?', 'Nem todo silêncio do contrato é lacuna. Às vezes as partes combinaram e não escreveram; às vezes simplesmente não pensaram no assunto.', 'dif')
b += scrolly('O ponto omitido', [('p-gap0', gap(0), 'Interpretação'), ('p-gap1', gap(1), 'Integração')], [
    S('p-gap0', 'Interpretação', 'Havia uma intenção comum', '<p>O contrato fala em atendimento “em horário estendido”. As mensagens da negociação mostram que as partes incluíram sábados até meio-dia. Isso esclarece o sentido do que foi escrito: é interpretação.</p>', 'conc'),
    S('p-gap1', 'Integração', 'Não havia nada a descobrir', '<p>Se nada foi combinado sobre o momento do pagamento, não há intenção escondida a revelar. A lei fornece a regra supletiva, e o contrato é completado. É integração.</p><p>O art. 113, § 2º, também permite às partes criar suas próprias regras de preenchimento de lacunas. E regimes especiais, como o CDC, entram na conta.</p>', 'dif'),
])
b += chapter('03', 'c3', 'Três casos, três limites', 'Um caso só ensina algo quando se sabe o contrato, a pergunta e o que o tribunal de fato decidiu.')
b += wide('<div class="julgados">'
          + jul('conc', 'Doação de terreno', 'REsp 1.938.997/MS · 2021',
                '<p>Uma empresa doou um terreno a outra para a implantação de uma arena cultural. Um instrumento particular mencionava essa finalidade, mas a escritura pública dizia que a doação era pura e simples, e um aditivo também afastava encargo. A doadora pediu a revogação porque a arena não foi construída.</p>',
                'O STJ restabeleceu a improcedência: a escritura não impunha encargo, e a doação, por ser gratuita, recebe interpretação estrita (art. 114). A leitura pelos arts. 112 e 113 levava ao mesmo lugar.')
          + jul('', 'Distrato entre empresas', 'AR 7.296/DF · 2026',
                '<p>Uma fabricante tentou rescindir uma decisão do próprio STJ sobre a indenização prevista num distrato com sua revendedora. Alegou erro de valor e violação das regras de interpretação; o distrato fixava expressamente R$ 271.764,96.</p>',
                'A Segunda Seção julgou a rescisória improcedente. Para rescindir por violação manifesta de norma (CPC, art. 966, V), não basta preferir outra leitura: é preciso uma interpretação juridicamente insustentável. É um limite da ação rescisória, não uma regra de que o texto literal sempre vence.')
          + jul('dif', 'Arranjo empresarial', 'REsp 15.339/RJ · 1994',
                '<p>A estrutura criada para manter o grupo Diários Associados reunia vários elementos, entre eles um condomínio de ações. A dúvida era se a proibição de condomínio perpétuo alcançava a organização inteira.</p>',
                'O STJ tratou o ajuste como contrato atípico misto, em que o condomínio era uma peça e não o objeto todo, e afastou a proibição em relação à continuidade da organização. Antes de aplicar a regra de um elemento, identifique a função do negócio inteiro.')
          + '</div>')
b += chapter('04', 'c4', 'Teste', 'Escolha a regra pelo gatilho e diga por que ele ocorreu.')
b += quiz([
    ('A escritura de doação de um terreno diz “pura e simples”, mas um documento anterior fala em construir um centro cultural. O que decide?', 'Qual instrumento formalizou a doação e se ele impôs o encargo. No REsp 1.938.997/MS, a escritura não o impunha, e a doação gratuita se interpreta estritamente (art. 114).'),
    ('Um formulário de adesão dá prazo de 30 dias numa cláusula e de 60 noutra. Qual vale?', 'O mais favorável ao aderente (art. 423): há adesão e contradição. O art. 113, § 1º, IV, reforça a mesma leitura se for possível identificar quem redigiu.'),
    ('Uma cláusula de um contrato de serviço ao consumidor admite duas leituras razoáveis. Qual regra incide?', 'O art. 47 do CDC: interpreta-se a favor do consumidor. Se o contrato também for de adesão, o art. 423 soma-se a ele.'),
    ('O contrato não diz quem paga a taxa de registro, e nada indica que as partes tenham falado disso. É preciso descobrir a intenção delas?', 'Não há intenção a descobrir. Aplica-se a regra supletiva: é integração, não interpretação.'),
    ('No AR 7.296/DF, o STJ disse que o texto literal sempre prevalece?', 'Não. Disse que uma ação rescisória por violação manifesta de norma exige interpretação insustentável, e que a decisão atacada não chegava a isso.'),
])
page('aula-10.html', '10', 'Interpretação: regras especiais',
     'Regras especiais de interpretação: art. 114, art. 423, CDC art. 47; interpretação e integração; três casos com seus limites.',
     ['Unidade 6 · Interpretação', 'Teoria Geral dos Contratos', 'UFRGS · 2026/2'], 'Regras', 'especiais',
     'A leitura geral dos arts. 112 e 113 vale sempre. <strong class="conc">Gratuidade</strong>, <strong class="conc">adesão</strong> e <strong class="dif">consumo</strong> acrescentam regras próprias, cada uma com seu gatilho.',
     hero, [('Unidade', '6 · Interpretação II'), ('Leitura', '≈ 13 min'), ('Antes', 'Aula 09 · O sentido do acordo'), ('Depois', 'Aula 11 · Desequilíbrio na origem')], b,
     ('aula-09.html', '← Aula 09', 'O sentido do acordo'), ('aula-11.html', 'Aula 11 →', 'Desequilíbrio na formação'), unit='6')
