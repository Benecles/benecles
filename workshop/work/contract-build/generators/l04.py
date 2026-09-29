from kit import *

hero = ('<path class="draw" d="M20 90H1060" style="stroke:var(--ink);stroke-width:2;fill:none"/>'
        + ''.join(f'<g class="pop" style="--d:{.3+i*.25}s"><circle cx="{80+i*230}" cy="90" r="10" style="fill:{c}"/>'
                  f'<text x="{80+i*230}" y="130" text-anchor="middle" style="font:12px var(--mono);fill:var(--ink)">{t}</text></g>'
                  for i, (t, c) in enumerate([('TRATATIVAS', 'var(--conc)'), ('PROPOSTA', 'var(--ink)'), ('ACEITAÇÃO', 'var(--ink)'), ('EXECUÇÃO', 'var(--dif)'), ('EXTINÇÃO', 'var(--dif)')]))
        + '<g class="pop" style="--d:1.7s"><path d="M150 60l14 18-12 4 16 20" style="stroke:var(--conc);stroke-width:3;fill:none"/>'
        '<text x="180" y="50" style="font:12px var(--mono);fill:var(--conc)">RUPTURA ABUSIVA · ART. 187</text></g>')

phases = [('TRATATIVAS', 'conversas · minutas · estudos', 'conc'), ('PROPOSTA', 'declaração séria e completa', 'grey'),
          ('ACEITAÇÃO', 'o contrato se forma', 'grey'), ('EXECUÇÃO', 'prestações e cooperação', 'dif'), ('EXTINÇÃO', 'pagamento · prazo · outra causa', 'dif')]
notes = [['qualquer parte', 'pode parar, mas', 'com lealdade'], ['vincula quem', 'a faz · 427-429'],
         ['agora há contrato', 'e deveres de', 'prestação'], ['boa-fé em toda', 'a execução', '(art. 422)']]
def track(k):
    o = P('M80 70V540', 'ink', style='stroke-width:2')
    for i, (t, s, tone) in enumerate(phases):
        y = 90 + i * 110
        on = (i == k) or (k == 3 and i == 4)
        o += C(80, y, 12 if on else 8, 'f-ink' if on else 'f-paper ink', style=f'fill:var(--{tone if tone != "grey" else "ink"})' if on else '')
        o += G(box(110, y - 38, 250, 76, t, s, tone if on else 'grey', ctx='track'), 'pop' if on else '', d=.1, extra='' if on else ' opacity=".35"')
    y0 = 90 + k * 110
    for j, n in enumerate(notes[k]):
        o += G(T(385, y0 - 20 + j * 28, n, 't-hand'), 'fade', d=.5 + .2 * j)
    return o
trk = [(f'p-ph{k}', track(k), phases[k][0]) for k in range(4)]

reqs = [('EXPECTATIVA LEGÍTIMA', 'confiança objetiva de que sairia'), ('RUPTURA ABUSIVA', 'desistência sem motivo, desleal'),
        ('DANO', 'despesas feitas por confiar'), ('NEXO CAUSAL', 'o dano vem da ruptura')]
rq = T(40, 64, 'OS QUATRO REQUISITOS', 't-small', style='letter-spacing:.1em')
for i, (a, b) in enumerate(reqs):
    y = 96 + i * 104
    rq += G(box(90, y, 470, 84, a, b, 'conc', ctx='rq') + R(40, y + 26, 32, 32, 'f-paper ink') + check(56, y + 43), 'pop', d=.2 + .3 * i)
rq += G(R(40, 530, 520, 46, 'f-ink') + T(300, 559, 'FALTOU UM? NÃO HÁ INDENIZAÇÃO', 't-small t-light', anchor='middle'), 'pop', d=1.5)
ab = (T(60, 90, 'DIREITO DE NÃO CONTRATAR', 't-small', style='letter-spacing:.1em')
      + R(60, 110, 480, 56, 'f-paper ink')
      + G(R(60, 110, 320, 56, 'w-dif', extra=' stroke="none"') + T(80, 145, 'DESISTIR É LEGÍTIMO', 't-small tc-dif'), 'pop', d=.2)
      + G(R(380, 110, 160, 56, 'w-conc', extra=' stroke="none"') + T(394, 145, 'ABUSO', 't-small tc-conc'), 'pop', d=.8)
      + P('M380 90V200', 'c-conc', style='stroke-width:3;stroke-dasharray:6 4') + T(380, 222, 'LIMITE DA BOA-FÉ', 't-small tc-conc', anchor='middle')
      + G(box(60, 270, 480, 110, 'ART. 187', 'exercer um direito excedendo manifestamente', 'conc', ctx='ab', sub2='os limites da boa-fé é ato ilícito'), 'pop', d=1.1)
      + G(box(60, 400, 480, 80, 'CONSEQUÊNCIA', 'indenizar o dano; nunca obrigar a contratar', 'ink', ctx='ab'), 'pop', d=1.4)
      + T(300, 540, 'o art. 422 reforça', 't-hand', anchor='middle'))
bank = T(40, 64, 'PARCERIA SUPERMERCADO × BANCO', 't-small', style='letter-spacing:.1em')
steps_b = [('MINUTAS', 'trocadas'), ('CAMPANHA', 'material produzido'), ('GASTOS', 'conhecidos do banco')]
for i, (a, b) in enumerate(steps_b):
    bank += G(box(40 + i * 180, 110, 160, 90, a, b, 'dif', ctx='bank'), 'pop', d=.2 + .3 * i)
    if i < 2: bank += P(f'M{200+i*180} 155H{218+i*180}', 'ink', m='p-bank-i')
bank += P('M120 200C120 280 300 250 300 300', 'c-dif grow', m='p-bank-d', extra=' style="--d:.9s"')
bank += G(T(300, 300, '', '') + C(300, 320, 26, 'w-conc ink') + check(300, 320, False) + T(300, 372, 'RUPTURA SEM MOTIVO', 't-small tc-conc', anchor='middle'), 'pop', d=1.2)
bank += G(R(100, 420, 400, 70, 'f-ink') + T(300, 452, 'DANO E NEXO RECONHECIDOS', 't-small t-light', anchor='middle') + T(300, 474, 'condenação mantida no STJ', 't-small t-light', anchor='middle'), 'pop', d=1.6)

S = lambda panel, label, h3, body, lcls='': dict(panel=panel, label=label, lcls=lcls, h3=h3, body=body)
b = ''
b += chapter('01', 'c1', 'As fases do contrato', 'O contrato é um processo. Antes de existir, já há uma relação entre as partes, e ela tem regras.')
b += scrolly('O contrato como processo', trk, [
    S('p-ph0', 'Fase 1', 'Tratativas', '<p>As partes trocam informações, avaliam condições, fazem minutas. Nada disso, por si só, cria contrato ou obrigação de contratar. Em regra, qualquer parte pode parar.</p><p>Mesmo sem contrato, há deveres de lealdade, informação e cuidado com a confiança do outro. É preciso ser claro sobre os passos dados.</p>', 'conc'),
    S('p-ph1', 'Fase 2', 'Proposta', '<p>Uma declaração séria e completa vincula quem a faz (arts. 427 a 429). A diferença para as tratativas é que a proposta já contém tudo o que é preciso para que um simples \"aceito\" forme o contrato. Os detalhes estão na Aula 05.</p>'),
    S('p-ph2', 'Fase 3', 'Aceitação e conclusão', '<p>Quando a aceitação encontra a proposta, o contrato se forma e passam a existir os deveres de prestação.</p>'),
    S('p-ph3', 'Fases 4 e 5', 'Execução e extinção', '<p>O contrato é cumprido e se extingue pelo pagamento, pelo prazo ou por outra causa. Em toda a execução, vale a boa-fé (art. 422).</p>', 'dif'),
])
b += chapter('02', 'c2', 'Responsabilidade pré-contratual', 'Não importa quantas reuniões houve. Importa haver confiança legítima, ruptura abusiva e dano causado por ela.', 'conc')
b += scrolly('Quando a ruptura gera responsabilidade', [('p-rq', rq, 'Os requisitos'), ('p-ab', ab, 'Abuso do direito'), ('p-bank', bank, 'O caso do banco')], [
    S('p-rq', 'Os requisitos', 'O que precisa estar presente', '<p><strong>Expectativa legítima:</strong> a confiança precisa ser objetiva, considerando o estágio do negócio, o que foi dito e as ressalvas feitas. Otimismo de um lado só não basta.</p><p><strong>Ruptura abusiva:</strong> induzir gastos sabendo que não há intenção de fechar, esconder uma decisão já tomada, encerrar de repente depois de sinais firmes de fechamento.</p><p><strong>Dano e nexo:</strong> despesas feitas por causa da confiança, ou investimentos que perderam a utilidade. Lucros esperados não se presumem, e gastos que a parte faria de qualquer jeito não entram.</p>', 'conc'),
    S('p-ab', 'O fundamento', 'Abuso do direito de não contratar', '<p>O fundamento é o <strong>art. 187</strong> do Código Civil. A liberdade de não contratar é um direito, mas quem o exerce depois de criar expectativa legítima, excedendo manifestamente os limites da boa-fé, comete abuso do direito e deve indenizar. O art. 422 reforça a ideia, embora seu texto fale só da conclusão e da execução.</p><p>Isso não torna ilícita toda ruptura: desistir continua permitido. E a consequência é indenizar, nunca obrigar a contratar.</p>', 'conc'),
    S('p-bank', 'Na jurisprudência', 'Supermercado × banco', '<p>Numa parceria entre uma rede de supermercados e um banco, as tratativas estavam avançadas: havia minutas, material de campanha produzido e usado, e o banco sabia dos investimentos feitos. Depois, rompeu as negociações.</p><p>O tribunal estadual reconheceu o dano e o nexo, e a condenação ficou de pé no STJ, que não reexamina provas.</p>'),
])
b += wide('<div class="julgados">'
          '<article class="julgado dif"><header><b>Evento</b><span>despesas indenizadas</span></header><div class="corpo"><p>Uma varejista negociava com uma empresa a organização de um evento. As conversas criaram a expectativa firme de contratação; perto da data, a empresa de eventos já tinha assumido compromissos com terceiros e feito despesas, que se perderam com a ruptura.</p></div><div class="tese">Indenização das despesas comprovadas; lucros cessantes estimados ficaram de fora.</div></article>'
          '<article class="julgado"><header><b>Bilhete</b><span>sem vínculo</span></header><div class="corpo"><p>Discutiu-se um bilhete escrito à mão, numa viagem, sobre uma futura participação societária. A Justiça entendeu que o texto era vago e programático, sem os elementos de uma proposta.</p></div><div class="tese">Sem proposta, não havia vínculo. O que se escreve informalmente, sem conteúdo definido, não obriga.</div></article>'
          '</div>')
b += chapter('03', 'c3', 'Tratativas × contrato preliminar', 'O contrato preliminar já é um contrato, que obriga a celebrar outro. As negociações preliminares são a fase em que ainda se decide se haverá contrato.')
b += wide(table(['', 'Tratativas', 'Contrato preliminar'], [
    ['O que há', 'Conversas preparatórias, sem obrigação de fechar o acordo.', 'Obrigação de celebrar o definitivo. Deve ter todos os requisitos essenciais dele, exceto a forma (art. 462).'],
    ['Pode desistir?', 'Sim. Só se indeniza a ruptura abusiva.', 'Sem cláusula de arrependimento, a outra parte pode exigir o definitivo, e o juiz supre a vontade (arts. 463 e 464); ou pedir perdas e danos (art. 465).'],
    ['O que provar', 'Confiança legítima, ruptura abusiva, dano e nexo.', 'Que o preliminar tem os requisitos do definitivo e que a outra parte se recusou a celebrá-lo.'],
], hcls=['', 'conc', 'dif']) + '<p class="note">Minutas, cartas de intenção e memorandos podem não obrigar a nada, obrigar em parte (sigilo, exclusividade, divisão de custos) ou ser verdadeiros contratos preliminares. Leia o que cada cláusula assume.</p>')
b += chapter('04', 'c4', 'Teste')
b += quiz([
    ('Depois de meses de negociação, uma parte desiste porque nunca houve acordo sobre o preço. Há indenização?', 'Não. O preço sempre esteve em aberto, e não chegar a um acordo sobre ele é desistência legítima.'),
    ('Uma empresa diz à outra que "o contrato está fechado", sabe que ela está produzindo material caro para a campanha e depois encerra as conversas sem motivo. O que se deve verificar?', 'Estão presentes a expectativa legítima, os gastos conhecidos e a ruptura sem motivo. Falta verificar o dano concreto e se as despesas poderiam ter sido evitadas.'),
    ('Um documento se chama "memorando de entendimentos". É contrato preliminar?', 'Não necessariamente. Vale o conteúdo, não o título: há obrigação de contratar? Estão presentes os elementos essenciais?'),
    ('No caso do banco, qual foi o fundamento da condenação?', 'A ruptura abusiva de tratativas avançadas: abuso do direito de não contratar (art. 187), com apoio na boa-fé.'),
])
page('aula-04.html', '04', 'Tratativas e responsabilidade pré-contratual',
     'O contrato como processo: fases, tratativas e responsabilidade pré-contratual (art. 187).',
     ['Unidade 3 · Formação', 'Teoria Geral dos Contratos', 'UFRGS · 2026/2'], 'O contrato', 'como processo',
     'Negociar é livre, mas é preciso negociar com lealdade. Qualquer parte pode desistir das <strong class="conc">tratativas</strong>; quem desiste depois de criar expectativa legítima, e causa prejuízo com isso, responde.',
     hero, [('Unidade', '3 · Formação I'), ('Leitura', '≈ 12 min'), ('Antes', 'Aula 03 · Princípios II'), ('Depois', 'Aula 05 · Proposta e aceitação')], b,
     ('aula-03.html', '← Aula 03', 'Função social, boa-fé e equilíbrio'), ('aula-05.html', 'Aula 05 →', 'Proposta e aceitação'), unit='3')
