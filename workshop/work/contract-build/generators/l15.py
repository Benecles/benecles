from kit import *

# hero: one road with five exits
EX = [('CUMPRIMENTO', 'ink'), ('IMPOSSIBILIDADE', 'conc'), ('DISTRATO', 'dif'), ('DENÚNCIA', 'dif'), ('INADIMPLEMENTO', 'conc')]
hero = '<path class="draw" d="M30 50H1050" style="stroke:var(--ink);stroke-width:3;fill:none"/><g style="font:12px var(--mono);letter-spacing:1px">'
for i, (lab, tone) in enumerate(EX):
    x = 110 + i * 205
    hero += (f'<path class="draw" style="--d:{.5+.15*i}s;stroke:var(--{tone});stroke-width:2;fill:none" d="M{x} 50C{x} 90 {x+30} 100 {x+30} 120"/>'
             f'<g class="pop" style="--d:{1+.15*i}s"><circle cx="{x+30}" cy="124" r="6" style="fill:var(--{tone})"/>'
             f'<text x="{x+30}" y="156" text-anchor="middle" style="fill:var(--{tone})">{lab}</text></g>')
hero += '</g>'

# ---- Fig 1: event → rule → lesson
MAP = [('CUMPRIMENTO', 'as prestações foram feitas', 'esta aula', 'grey'), ('IMPOSSIBILIDADE', 'uma prestação não pode mais ser feita', 'esta aula', 'conc'),
       ('ACORDO / DENÚNCIA', 'as partes, ou uma delas, decidem sair', 'Aula 16', 'dif'), ('INADIMPLEMENTO', 'uma parte não cumpriu', 'Aula 17', 'conc')]
def emap(k):
    o = G(R(40, 60, 170, 480, 'f-ink') + T(125, 290, 'O QUE', 't-small t-light', anchor='middle') + T(125, 310, 'ACONTECEU?', 't-small t-light', anchor='middle'), 'pop', d=0)
    for i, (a, s, where, tone) in enumerate(MAP):
        y = 70 + i * 120
        on = k == 4 or i == k
        o += P(f'M210 {y+45}H250', 'ink' if on else 'thin')
        o += G(R(250, y, 310, 90, f'w-{tone} ink' if on else 'f-paper ink', style='' if on else 'opacity:.4')
               + T(266, y + 32, a, 't-small' + (f' tc-{tone}' if on and tone != 'grey' else ''), style='' if on else 'opacity:.5')
               + T(266, y + 54, s, 't-small', style='' if on else 'opacity:.5') + T(266, y + 74, '→ ' + where, 't-small', style='' if on else 'opacity:.5'), 'pop' if on else '', d=.1 * i)
    return o
def rent(k):
    o = T(40, 60, 'LOCAÇÃO · CADA ALUGUEL É UMA DÍVIDA', 't-small', style='letter-spacing:.1em')
    o += P('M60 230H540', 'ink', style='stroke-width:2')
    for i in range(12):
        x = 80 + i * 40
        paid = i < 7
        o += G(R(x - 14, 196, 28, 28, 'w-dif ink' if paid else 'f-paper ink') + (check(x, 210, True, .7) if paid else ''), 'pop' if paid else '', d=.08 * i)
    o += T(200, 270, 'dívidas mensais extintas', 't-small tc-dif', anchor='middle') + T(460, 270, 'ainda por vir', 't-small', anchor='middle')
    o += G(box(40, 330, 520, 110, 'O CONTRATO CONTINUA', 'cada pagamento extingue aquela dívida;', 'dif', ctx='rent', sub2='o vínculo segue enquanto houver períodos'), 'pop', d=1.0)
    o += G(T(300, 510, 'o pagamento extingue uma obrigação, não o contrato inteiro', 't-hand', anchor='middle'), 'fade', d=1.3)
    return o

# ---- Fig 2: impossibility
art = (T(40, 60, 'COISA CERTA · ART. 234', 't-small', style='letter-spacing:.1em')
       + G(R(90, 100, 160, 200, 'f-paper ink') + R(106, 116, 128, 168, 'w-grey ink') + P('M120 250l30-50l30 30l20-20l20 40', 'ink'), 'pop', d=.1)
       + G(P('M130 300c10-40 30-20 40-60c10 30 30 20 20 60z', 'c-conc', style='fill:var(--conc-wash)'), 'pop', d=.5)
       + T(170, 330, 'PEÇA ÚNICA · INCÊNDIO', 't-small tc-conc', anchor='middle')
       + P('M280 200H330', 'ink')
       + G(box(340, 100, 220, 100, 'SEM CULPA', 'resolve-se para', 'dif', ctx='art', sub2='ambas as partes'), 'pop', d=.8)
       + G(box(340, 220, 220, 100, 'COM CULPA', 'equivalente +', 'conc', ctx='art', sub2='perdas e danos'), 'pop', d=1.0)
       + G(T(300, 420, 'antes da tradição, sem culpa,', 't-hand', anchor='middle') + T(300, 450, 'a coisa perece para o dono', 't-hand', anchor='middle'), 'fade', d=1.2))
genus = (T(40, 60, 'COISA INCERTA · GÊNERO', 't-small', style='letter-spacing:.1em')
         + G(R(60, 100, 200, 140, 'f-paper ink', style='stroke-dasharray:6 4') + T(160, 170, 'SAFRA DA FAZENDA', 't-small', anchor='middle') + T(160, 192, 'perdida', 't-small tc-conc', anchor='middle'), 'pop', d=.1)
         + G(R(340, 100, 200, 140, 'w-dif ink') + T(440, 160, 'MERCADO', 't-small tc-dif', anchor='middle') + T(440, 182, 'arroz equivalente', 't-small', anchor='middle') + T(440, 200, 'disponível', 't-small', anchor='middle'), 'pop', d=.4)
         + P('M262 170H336', 'c-dif grow', m='p-genus-d', style='--d:.6s')
         + G(box(40, 300, 520, 110, '100 SACAS DE ARROZ', 'a fonte específica falhou, mas a prestação', 'dif', ctx='genus', sub2='continua possível: o gênero não perece'), 'pop', d=.9)
         + G(T(300, 490, 'antes da escolha, não se alega perda (art. 246)', 't-hand', anchor='middle'), 'fade', d=1.2))
mora = (T(40, 60, 'IMPOSSIBILIDADE DURANTE A MORA · ART. 399', 't-small', style='letter-spacing:.1em')
        + P('M60 160H540', 'ink', style='stroke-width:2')
        + G(C(120, 160, 9, 'f-ink') + T(120, 196, 'VENCIMENTO', 't-small', anchor='middle'), 'pop', d=.1)
        + G(R(120, 150, 260, 20, 'w-conc', extra=' stroke="none"') + T(250, 138, 'EM MORA', 't-small tc-conc', anchor='middle'), 'pop', d=.3)
        + G(C(380, 160, 11, 'f-ink', style='fill:var(--conc)') + T(380, 196, 'FORTUITO', 't-small tc-conc', anchor='middle'), 'pop', d=.6)
        + G(box(40, 250, 520, 90, 'O DEVEDOR RESPONDE', 'mesmo por caso fortuito ou força maior', 'conc', ctx='mora'), 'pop', d=.9)
        + T(40, 390, 'SALVO SE PROVAR', 't-small', style='letter-spacing:.1em')
        + G(box(40, 406, 250, 100, 'SEM CULPA', 'no atraso', 'dif', ctx='mora'), 'pop', d=1.1)
        + G(box(310, 406, 250, 100, 'DANO IGUAL', 'ocorreria mesmo com', 'dif', ctx='mora', sub2='cumprimento pontual'), 'pop', d=1.3))

# ---- Fig 3: closed mall vs empty till
def mall(k):
    o = T(40, 60, 'LOJA EM SHOPPING · FECHAMENTO TEMPORÁRIO', 't-small', style='letter-spacing:.1em')
    o += P('M300 90V520', 'thin', style='stroke-dasharray:6 5')
    o += T(170, 110, 'PRESTAÇÃO DO SHOPPING', 't-small', anchor='middle') + T(430, 110, 'PRESTAÇÃO DO LOJISTA', 't-small', anchor='middle')
    on0, on1 = k in (0, 2), k in (1, 2)
    o += G(R(80, 140, 180, 150, 'w-conc ink' if on0 else 'f-paper ink', style='' if on0 else 'opacity:.4') + P('M110 290V190l60-30l60 30V290', 'ink', style='' if on0 else 'opacity:.4')
           + P('M150 290V240h40v50', 'c-conc' if on0 else 'thin') + P('M140 230l60 60M200 230l-60 60', 'c-conc' if on0 else 'thin', style='stroke-width:3'), 'pop' if on0 else '', d=.1)
    o += G(R(340, 140, 180, 150, 'w-dif ink' if on1 else 'f-paper ink', style='' if on1 else 'opacity:.4')
           + coin(400, 215, 22) + T(470, 222, 'R$', 't-mid', anchor='middle', style='opacity:.4'), 'pop' if on1 else '', d=.1)
    if on0:
        o += G(box(40, 330, 250, 150, 'ACESSO FECHADO', 'pode haver impossibilidade', 'conc', ctx='mall', sub2='temporária de uma prestação') + T(54, 462, 'delimite serviço e período', 't-small'), 'pop', d=.5)
    if on1:
        o += G(box(310, 330, 250, 150, 'CAIXA BAIXO', 'pagar dinheiro continua', 'dif', ctx='mall', sub2='possível') + T(324, 462, 'onerosidade é outra rota', 't-small'), 'pop', d=.7)
    return o

S = lambda panel, label, h3, body, lcls='': dict(panel=panel, label=label, lcls=lcls, h3=h3, body=body)
b = ''
b += chapter('01', 'c1', 'Caminhos diferentes para o fim', 'O motivo da extinção decide qual regra entra em cena e quais efeitos ela produz.')
b += scrolly('O evento escolhe a regra', [(f'p-em{k}', emap(k), MAP[k][0] if k < 4 else 'Mapa') for k in [4, 0, 1, 2, 3]] + [('p-rent', rent(0), 'Locação')], [
    S('p-em4', 'O mapa', 'Quatro perguntas antes de dizer “acabou”', '<p>Se as prestações foram feitas e o objetivo alcançado, o cumprimento encerra o vínculo. Se o contrato termina sem isso, pergunte o que aconteceu: uma prestação ficou impossível? As partes combinaram sair? Uma delas exerceu uma faculdade de saída? Houve descumprimento?</p>'),
    S('p-em0', 'Cumprimento', 'O fim natural', '<p>Numa compra simples, entregar o bem e pagar o preço satisfaz as prestações principais, e o contrato cumpriu seu programa.</p>'),
    S('p-em1', 'Impossibilidade', 'Uma prestação não pode mais ser feita', '<p>É o outro tema desta aula. A impossibilidade atinge uma prestação específica, e a primeira tarefa é dizer qual.</p>', 'conc'),
    S('p-em2', 'Aula 16', 'Saída por vontade', '<p>Distrato (acordo das partes), denúncia (saída unilateral autorizada) e revogação ficam para a próxima aula.</p>', 'dif'),
    S('p-em3', 'Aula 17', 'Descumprimento', '<p>Mora, inadimplemento definitivo e resolução ficam para a Aula 17. Nem todo atraso torna a prestação inútil.</p>', 'conc'),
    S('p-rent', 'Contratos continuados', 'Um pagamento, uma dívida', '<p>Numa locação, cada aluguel pago extingue aquela dívida mensal, mas não o contrato: o vínculo segue enquanto houver períodos por cumprir. Identifique qual obrigação foi satisfeita antes de dizer que o contrato acabou.</p>', 'dif'),
])
b += '<div class="wide"><p class="note"><strong>Sobre os nomes.</strong> A doutrina usa resolução, resilição e rescisão com sentidos que variam de autor para autor. Este curso segue o Código atual: <em>resilição</em> é a saída por vontade autorizada (art. 473); <em>resolução</em> aparece para o inadimplemento (art. 475) e para a onerosidade excessiva (art. 478). A duração do contrato, sozinha, não escolhe o nome nem os efeitos.</p></div>\n'
b += chapter('02', 'c2', 'Impossibilidade: qual prestação não pode mais ser feita?', 'Uma prestação pode se tornar impossível depois de contratada. Isso ainda não diz quem suporta o risco nem se o contrato inteiro termina.', 'conc')
b += scrolly('Impossibilidade superveniente', [('p-art', art, 'Coisa certa'), ('p-genus', genus, 'Gênero'), ('p-mora', mora, 'Mora')], [
    S('p-art', 'Art. 234', 'A obra de arte que pegou fogo', '<p>Antes da entrega, um incêndio fortuito destrói uma peça única. Na obrigação de dar coisa certa, a perda antes da tradição, sem culpa do devedor, deixa a obrigação resolvida para ambas as partes: ninguém entrega, ninguém paga; com culpa, ele responde pelo equivalente mais perdas e danos (art. 234). Os arts. 234 a 242 distribuem os efeitos conforme perda ou deterioração, culpa e momento da tradição.</p>', 'conc'),
    S('p-genus', 'Gênero', 'O arroz que ainda existe', '<p>Outro vendedor prometeu cem sacas de arroz, e a safra da própria fazenda se perdeu. Mas há arroz equivalente no mercado. A prestação não ficou impossível só porque aquela fonte falhou: antes da escolha, o devedor de coisa incerta não pode alegar perda ou deterioração, nem por força maior (art. 246).</p>', 'dif'),
    S('p-mora', 'Art. 399', 'Se o devedor já estava atrasado', '<p>O devedor em mora responde pela impossibilidade da prestação, mesmo que resulte de caso fortuito ou força maior. Escapa só se provar que não teve culpa no atraso, ou que o dano aconteceria mesmo com o cumprimento pontual.</p><p>Sem mora e sem culpa, olhe para o regime da obrigação e para quem assumiu aquele risco.</p>'),
])
b += chapter('03', 'c3', 'Shopping fechado não é caixa vazio', 'A impossibilidade recai sobre uma prestação. Queda de faturamento pode pesar no pagamento sem tornar o pagamento impossível.', 'dif')
b += scrolly('Duas prestações, duas análises', [(f'p-mall{k}', mall(k), l) for k, l in enumerate(['Shopping', 'Lojista', 'Juntas'])], [
    S('p-mall0', 'A prestação do shopping', 'O acesso fechou', '<p>Durante um fechamento imposto por autoridade pública, o funcionamento organizado do centro e o acesso que permite o comércio podem ficar interrompidos. Isso pede exame da prestação do shopping: qual serviço parou, por quanto tempo, e como isso repercute nas parcelas devidas.</p>', 'conc'),
    S('p-mall1', 'A prestação do lojista', 'O caixa esvaziou', '<p>O lojista deve dinheiro, e pagar dinheiro continua possível. Menos clientes não tornam o pagamento impossível. Podem, conforme o contrato, abrir uma discussão diferente sobre onerosidade (arts. 317 e 478), com os requisitos próprios dessas regras.</p>', 'dif'),
    S('p-mall2', 'A pergunta certa', 'Qual prestação o fato afetou?', '<p>Não pergunte só “houve um fato imprevisível?”. Pergunte qual prestação ele atingiu e que consequência a lei ou o contrato ligam a isso. Um mesmo fato coletivo pode ter efeitos diferentes em prestações diferentes, e o fechamento não cancela automaticamente todo o aluguel.</p>'),
])
b += chapter('04', 'c4', 'Teste')
b += quiz([
    ('Uma locatária teve queda de faturamento e parou de pagar o aluguel. A prestação de pagar ficou impossível?', 'Não. Pagar dinheiro continua possível. Eventual onerosidade se analisa pelos requisitos próprios.'),
    ('Uma peça única se perdeu num incêndio fortuito antes da entrega, sem culpa do vendedor. O que acontece com a obrigação de entregar?', 'Fica resolvida para ambas as partes (art. 234): a perda foi antes da tradição e sem culpa, então o vendedor não entrega e o comprador não paga. Se houvesse culpa, o vendedor responderia pelo equivalente e por perdas e danos.'),
    ('O devedor já estava em mora quando um evento fortuito tornou a prestação impossível. Muda algo?', 'Sim. Pelo art. 399, ele responde mesmo pelo fortuito, salvo se provar que não teve culpa no atraso ou que o dano ocorreria de qualquer forma.'),
    ('O vendedor de cem sacas de arroz perdeu a safra da própria fazenda. Pode alegar impossibilidade?', 'Em regra, não: a obrigação é de gênero, e há arroz equivalente no mercado. Antes da escolha, não se alega perda da coisa (art. 246).'),
    ('O shopping fechou por ordem pública durante um mês. O aluguel do lojista se extinguiu automaticamente?', 'Não. É preciso identificar qual prestação do shopping foi impedida, por quanto tempo, como o aluguel está estruturado e quem assumiu esse risco.'),
])
page('aula-15.html', '15', 'Extinção: cumprimento e impossibilidade',
     'Extinção dos contratos I: os modos de extinção, cumprimento, impossibilidade superveniente (arts. 234, 246, 399) e o caso do shopping fechado.',
     ['Unidade 9 · Extinção', 'Teoria Geral dos Contratos', 'UFRGS · 2026/2'], 'Qual evento', 'extingue o quê?',
     'Uma enchente fecha o shopping onde funciona uma loja. A loja também perde vendas. As duas coisas encerram o contrato? Primeiro descubra <strong class="conc">qual prestação</strong> ficou impossível, e <strong class="dif">por quê</strong>.',
     hero, [('Unidade', '9 · Extinção I'), ('Leitura', '≈ 14 min'), ('Antes', 'Aula 14 · Cessão'), ('Depois', 'Aula 16 · Saída por vontade')], b,
     ('aula-14.html', '← Aula 14', 'Cessão da posição contratual'), ('aula-16.html', 'Aula 16 →', 'Quando as partes decidem sair'), unit='9')
