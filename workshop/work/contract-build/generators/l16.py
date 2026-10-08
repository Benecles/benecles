from kit import *

# hero: left half, two lines converge (distrato); right half, one line + envelope (denúncia)
hero = ('<path class="draw" d="M40 40C200 40 260 90 380 90" style="stroke:var(--dif);stroke-width:2.5;fill:none"/>'
        '<path class="draw" d="M40 130C200 130 260 90 380 90" style="stroke:var(--dif);stroke-width:2.5;fill:none"/>'
        '<g class="pop" style="--d:1.1s"><circle cx="390" cy="90" r="10" style="fill:var(--dif)"/></g>'
        '<path class="draw" style="--d:.5s;stroke:var(--conc);stroke-width:2.5;fill:none" d="M640 90H900"/>'
        '<g class="pop" style="--d:1.2s"><rect x="904" y="68" width="64" height="44" style="fill:var(--conc-wash);stroke:var(--conc);stroke-width:2"/><path d="M904 68l32 22l32-22" style="stroke:var(--conc);stroke-width:2;fill:none"/></g>'
        '<g class="pop" style="--d:1.5s;font:12px var(--mono);letter-spacing:1px"><text x="40" y="162" style="fill:var(--dif)">DISTRATO · AS DUAS PARTES</text>'
        '<text x="640" y="150" style="fill:var(--conc)">DENÚNCIA · UMA PARTE, AUTORIZADA, AVISA</text></g>')

def node(cx, cy, l, tone='conc', label=None, r=30):
    o = C(cx, cy, r, f'w-{tone} c-{tone}', extra=' stroke-width="2"') + T(cx, cy + 8, l, f't-mid tc-{tone}', anchor='middle')
    if label: o += T(cx, cy + r + 22, label, 't-small', anchor='middle')
    return o

# ---- Fig 1: agreement vs unilateral exit
dis = (T(40, 60, 'DISTRATO · UM NOVO ACORDO PARA ENCERRAR', 't-small', style='letter-spacing:.1em')
       + node(120, 160, 'A', 'dif') + node(480, 160, 'B', 'dif')
       + P('M150 160H240', 'c-dif grow') + P('M450 160H360', 'c-dif grow')
       + G(doc(240, 100, 120, 130, None, 'w-dif ink', lines=4) + P('M256 200h40M304 200h40', 'ink'), 'pop', d=.6)
       + T(300, 256, 'as duas assinam', 't-small tc-dif', anchor='middle')
       + T(40, 310, 'ESCREVA', 't-small', style='letter-spacing:.1em')
       + ''.join(G(R(40, 324 + j * 44, 26, 26, 'f-paper ink') + check(53, 337 + j * 44) + T(78, 342 + j * 44, t, 't-serif'), 'pop', d=.9 + .12 * j)
                 for j, t in enumerate(['quais obrigações terminam', 'o que se devolve ou ainda se paga', 'garantias e data de eficácia', 'efeito só para o futuro, ou também para trás?'])))
den = (T(40, 60, 'DENÚNCIA · SAÍDA UNILATERAL (ART. 473)', 't-small', style='letter-spacing:.1em')
       + ''.join(G(box(40 + i * 180, 100, 160, 120, a, s, tone, tcls='t-small', ctx='den', sub2=s2), 'pop', d=.2 + .3 * i)
                 for i, (a, s, s2, tone) in enumerate([('1 · AUTORIZAÇÃO', 'lei ou contrato', 'permitem sair', 'grey'),
                                                        ('2 · AVISO', 'notificação que', 'chega ao outro', 'conc'),
                                                        ('3 · EFICÁCIA', 'quando o aviso', 'e o prazo operam', 'dif')]))
       + P('M200 160H220M380 160H400', 'ink')
       + G(box(40, 270, 520, 100, 'O AVISO NÃO CRIA O DIREITO', 'só comunica o exercício de um direito que já existe', 'conc', ctx='den'), 'pop', d=1.2)
       + G(T(300, 430, 'motivada (“cheia”) ou sem causa (“vazia”),', 't-hand', anchor='middle') + T(300, 460, 'nos limites da lei e do contrato', 't-hand', anchor='middle'), 'fade', d=1.4)
       + T(300, 520, 'não é remédio para o inadimplemento do outro', 't-small', anchor='middle'))

# ---- Fig 2: REsp 1.040.606 — the unsigned distrato
unsigned = (T(40, 60, 'REsp 1.040.606/ES · LOCAÇÃO DE LOJA', 't-small', style='letter-spacing:.1em')
            + P('M60 170H540', 'ink', style='stroke-width:2')
            + ''.join(G(C(x, 170, 9, 'f-ink', style=st) + T(x, 206, a, 't-small' + c, anchor='middle') + T(x, 224, s, 't-small', anchor='middle'), 'pop', d=d)
                      for x, a, s, st, c, d in [(90, 'ACORDO', 'fim + reembolso', 'fill:var(--dif)', ' tc-dif', .1), (250, 'MINUTA', 'preparada', '', '', .3),
                                                (410, 'RECUSA', 'de assinar', 'fill:var(--conc)', ' tc-conc', .5)])
            + G(doc(420, 250, 120, 150, None, lines=4) + P('M436 370h88', 'ink') + P('M440 350l30 30M470 350l-30 30', 'c-conc', style='stroke-width:3'), 'pop', d=.7)
            + G(R(40, 260, 350, 70, 'w-conc ink') + T(56, 290, 'A LOCADORA ALEGA:', 't-small tc-conc') + T(56, 312, '“faltou a forma escrita”', 't-serif'), 'pop', d=.9)
            + G(box(40, 440, 520, 110, 'STJ · RECURSO NÃO PROVIDO', 'quem impediu a assinatura não pode usar a falta', 'dif', ctx='uns', sub2='do documento para negar o acordo provado'), 'pop', d=1.2))

# ---- Fig 3: art. 473 sole paragraph
def invest(k):
    o = T(40, 60, 'ART. 473, PARÁGRAFO ÚNICO', 't-small', style='letter-spacing:.1em')
    o += P('M60 300H540', 'ink', style='stroke-width:2')
    o += G(R(80, 180, 60, 120, 'w-dif ink') + R(150, 140, 60, 160, 'w-dif ink') + T(145, 330, 'INVESTIMENTOS', 't-small tc-dif', anchor='middle') + T(145, 348, 'consideráveis', 't-small', anchor='middle'), 'pop', d=.1)
    o += G(C(260, 300, 10, 'f-ink', style='fill:var(--conc)') + T(260, 330, 'AVISO', 't-small tc-conc', anchor='middle'), 'pop', d=.4)
    if k == 0:
        o += G(C(262, 300, 16, 'f-paper ink', style='fill:none;stroke-dasharray:4 3'), 'pulse')
        o += G(T(380, 240, 'sem investimento relevante:', 't-hand', anchor='middle') + T(380, 270, 'efeito com o aviso', 't-hand', anchor='middle'), 'fade', d=.8)
    else:
        o += G(R(262, 288, 220, 24, 'w-conc', extra=' stroke="none"'), 'pop', d=.7) + T(372, 280, 'PRAZO COMPATÍVEL', 't-small tc-conc', anchor='middle')
        o += G(C(490, 300, 12, 'f-ink') + T(490, 330, 'EFICÁCIA', 't-small', anchor='middle'), 'pop', d=1.0)
        o += G(box(40, 400, 520, 110, 'SEM NÚMERO FIXO', 'o prazo se mede pela natureza do contrato', 'dif', ctx='inv', sub2='e pelo vulto dos investimentos'), 'pop', d=1.2)
    return o

# ---- Fig 4: AMBEV timeline
def ambev(k):
    o = T(40, 60, 'REsp 1.112.796/PR · DISTRIBUIÇÃO DE BEBIDAS', 't-small', style='letter-spacing:.1em')
    o += P('M50 200H550', 'ink', style='stroke-width:2')
    pts = [(70, '1984', 'início'), (220, '1995', 'programa de'), (380, '03/06/1998', 'notificação'), (520, '25/01/1999', 'fim do prazo')]
    for i, (x, a, s) in enumerate(pts):
        o += G(C(x, 200, 8, 'f-ink') + T(x, 176, a, 't-small', anchor='middle') + T(x, 230, s, 't-small', anchor='middle'), 'pop', d=.1 * i)
    o += T(220, 248, 'investimentos', 't-small', anchor='middle')
    o += G(R(380, 190, 140, 20, 'w-conc', extra=' stroke="none"') + T(450, 272, 'mais de 7 meses', 't-small tc-conc', anchor='middle'), 'pop', d=.5)
    o += G(R(380, 290, 30, 14, 'w-grey ink') + T(418, 302, 'cláusula: 60 dias', 't-small'), 'pop', d=.6)
    if k == 0:
        o += G(box(40, 360, 520, 150, 'MAIORIA · RESULTADO DO RECURSO', 'havia cláusula de denúncia, e o aviso superou', 'dif', ctx='amb', sub2='os 60 dias: indenizações afastadas, sentença') + T(54, 490, 'de improcedência restabelecida', 't-small'), 'pop', d=.9)
    else:
        o += G(box(40, 360, 520, 150, 'VOTO VENCIDO · RELATOR', 'relação longa, confiança e investimentos', 'grey', ctx='amb', sub2='podiam gerar expectativa de continuidade') + T(54, 490, 'argumento que não prevaleceu', 't-small'), 'pop', d=.9)
    return o

def jul(tone, b, span, corpo, tese):
    return f'<article class="julgado {tone}"><header><b>{b}</b><span>{span}</span></header><div class="corpo">{corpo}</div><div class="tese">{tese}</div></article>'

S = lambda panel, label, h3, body, lcls='': dict(panel=panel, label=label, lcls=lcls, h3=h3, body=body)
b = ''
b += chapter('01', 'c1', 'Acordo ou saída de uma só parte', 'Quem manifesta a vontade, e o que autoriza essa vontade a produzir efeito?', 'dif')
b += scrolly('Duas formas de sair', [('p-dis', dis, 'Distrato'), ('p-den', den, 'Denúncia')], [
    S('p-dis', 'Art. 472', 'Distrato', '<p>O distrato é um novo acordo, entre as mesmas partes, para encerrar o vínculo anterior. Faz-se pela mesma forma exigida para o contrato (art. 472).</p><p>Ele não apaga o contrato que existiu. As partes decidem quais obrigações terminam, o que se devolve, o destino das garantias e a data de eficácia. Não se presume que todo distrato desfaça retroativamente tudo o que aconteceu. Dizer só “o contrato está cancelado” deixa abertas exatamente as perguntas que o acordo deveria responder.</p>', 'dif'),
    S('p-den', 'Art. 473', 'Denúncia', '<p>A resilição unilateral opera por denúncia notificada à outra parte, <strong>nos casos em que a lei expressa ou implicitamente o permita</strong> (art. 473). A declaração de vontade não basta em qualquer contrato: é preciso encontrar a autorização na lei ou no contrato.</p><p>Contratos por prazo indeterminado costumam admitir denúncia; o contrato pode prever saída motivada ou, nos limites permitidos, sem motivo. E a denúncia não é remédio para o inadimplemento da outra parte: para isso existe a resolução (Aula 17).</p>', 'conc'),
])
b += scrolly('O distrato que não foi assinado', [('p-uns', unsigned, 'REsp 1.040.606')], [
    S('p-uns', 'REsp 1.040.606/ES · 4ª Turma · 2012', 'A forma que uma parte impediu', '<p>A locatária já tinha deixado a loja. As partes combinaram o distrato e o reembolso de parte dos valores; o instrumento foi preparado, mas a locadora se recusou a assiná-lo. A locatária pediu o reconhecimento da extinção e a devolução; a locadora respondeu que faltava a forma escrita.</p><p>A 4ª Turma negou provimento ao recurso da locadora, por unanimidade: quem frustrou a assinatura não pode usar a falta do documento para tratar o contrato como vigente e fugir da devolução combinada. O resultado depende da prova do acordo e da conduta contraditória; não elimina, em geral, a exigência de forma do art. 472.</p>', 'dif'),
])
b += chapter('02', 'c2', 'Revogação', 'Revogar é retirar um poder ou uma manifestação anterior, nos casos em que a lei permite. Não é uma permissão geral para desfazer contratos.')
b += wide(table(['', 'Quem decide', 'Onde está a autorização'], [
    ['Distrato', 'As duas partes, de comum acordo.', 'Na própria autonomia das partes, com a forma do art. 472.'],
    ['Denúncia', 'Uma parte, com aviso à outra.', 'Na lei ou no contrato (art. 473).'],
    ['Revogação', 'Uma parte, retirando um poder ou ato.', 'Em regras específicas: a revogação do mandato está entre as causas de cessação do art. 682; a doação pode ser revogada nos casos do art. 555.'],
], hcls=['', 'dif', 'conc']) + '<p class="note">O efeito da revogação também não é sempre retroativo. Depende do tipo de ato, dos terceiros envolvidos e da regra que a autoriza.</p>')
b += chapter('03', 'c3', 'O aviso e o investimento', 'Quem investiu pesado para executar o contrato tem direito a um tempo antes que a denúncia produza efeito.', 'conc')
b += scrolly('Art. 473, parágrafo único', [('p-inv0', invest(0), 'Aviso'), ('p-inv1', invest(1), 'Prazo compatível')], [
    S('p-inv0', 'A regra', 'Normalmente, o aviso basta', '<p>Havendo autorização, a denúncia notificada encerra o contrato no marco que o aviso e o contrato definem. Deveres já vencidos continuam devidos.</p>'),
    S('p-inv1', 'A exceção', 'Quando houve investimento considerável', '<p>Se, pela natureza do contrato, uma das partes fez investimentos consideráveis para executá-lo, a denúncia só produz efeito depois de transcorrido prazo compatível com a natureza e o vulto desses investimentos.</p><p>O Código não fixa meses. O prazo se avalia no caso concreto.</p>', 'conc'),
])
b += chapter('04', 'c4', 'O aviso foi suficiente? O caso AMBEV', 'Uma relação de mais de vinte anos, um programa de investimentos e uma denúncia no fim do prazo. A Turma se dividiu.', 'dif')
b += scrolly('Maioria e voto vencido', [('p-amb0', ambev(0), 'Maioria'), ('p-amb1', ambev(1), 'Voto vencido')], [
    S('p-amb0', 'REsp 1.112.796/PR · 4ª Turma · 2010', 'O que a maioria decidiu', '<p>Uma distribuidora tinha relação exclusiva com a fornecedora desde 1984. O contrato permitia a qualquer parte denunciar com ao menos 60 dias de antecedência. Em 3 de junho de 1998, a fornecedora avisou que encerraria o vínculo ao fim do prazo contratual, em 25 de janeiro de 1999: mais de sete meses de aviso. A distribuidora alegou que um programa de investimentos de 1995 criara expectativa de continuidade, e o tribunal estadual lhe deu indenizações.</p><p>Por maioria, a 4ª Turma deu provimento em parte ao recurso da fornecedora e restabeleceu a sentença de improcedência: havia cláusula de denúncia, e o aviso superou com folga o prazo pactuado.</p>', 'dif'),
    S('p-amb1', 'Voto vencido', 'O argumento que perdeu', '<p>O relator, vencido, destacou a relação duradoura, a confiança e os investimentos ligados ao programa da fornecedora, e entendeu que isso podia gerar expectativa de continuidade por tempo razoável para recuperar o investimento.</p><p>Os fatos são anteriores ao Código Civil de 2002, então o caso não decidiu a aplicação do parágrafo único do art. 473 a um contrato atual. Use-o para separar o que a maioria resolveu (cláusula, prazo, aviso concreto) do argumento vencido.</p>'),
])
b += '<div class="wide"><p class="note"><strong>Sobre os nomes.</strong> O art. 473 chama de “resilição unilateral” a saída autorizada por denúncia; o art. 475 usa “resolução” para o inadimplemento, e o art. 478 para a onerosidade excessiva. Outra classificação doutrinária usa resilição e resolução conforme a duração e os efeitos. Para não confundir, nomeie primeiro o fundamento (acordo, vontade unilateral autorizada, inadimplemento) e só depois os efeitos.</p></div>\n'
b += chapter('05', 'c5', 'Teste')
b += quiz([
    ('As partes combinaram encerrar a locação e devolver parte do preço. Uma delas se recusa a assinar o documento que prometeu. O que o REsp 1.040.606 discutiu?', 'Se quem causou a falta de assinatura podia invocar esse defeito de forma para negar o distrato provado. O STJ não admitiu essa conduta, naquele quadro de fatos.'),
    ('O contrato permite denúncia com 60 dias de antecedência. O aviso chega sete meses antes do fim do prazo. O que decidiu o REsp 1.112.796?', 'Por maioria, que a denúncia no termo, com aviso maior que o pactuado, era válida, e afastou as indenizações. O voto vencido defendia outro resultado com base em confiança e investimento.'),
    ('Uma parte quer sair de um contrato, mas não há autorização legal nem contratual. Basta notificar?', 'Não. O art. 473 exige que a lei, expressa ou implicitamente, permita a resilição unilateral. A notificação comunica um direito; não o cria.'),
    ('O contrato permite denúncia, e a outra parte fez investimentos consideráveis para executá-lo. A notificação encerra tudo no mesmo dia?', 'Não necessariamente. O parágrafo único do art. 473 adia o efeito até correr prazo compatível com a natureza do contrato e o vulto dos investimentos.'),
    ('A outra parte atrasou pagamentos. Posso “denunciar” o contrato por isso?', 'O remédio para o inadimplemento é a resolução (art. 475), com seus requisitos. A denúncia é saída autorizada, independente de falta do outro.'),
])
page('aula-16.html', '16', 'Extinção: saída por vontade',
     'Extinção dos contratos II: distrato (art. 472), denúncia e resilição unilateral (art. 473), revogação e os casos REsp 1.040.606 e REsp 1.112.796.',
     ['Unidade 9 · Extinção', 'Teoria Geral dos Contratos', 'UFRGS · 2026/2'], 'Saída', 'por vontade',
     'Uma saída depende de <strong class="dif">acordo</strong>; a outra, de <strong class="conc">autorização e aviso</strong>. Distrato, denúncia e revogação encerram vínculos por caminhos diferentes.',
     hero, [('Unidade', '9 · Extinção II'), ('Leitura', '≈ 16 min'), ('Antes', 'Aula 15 · Impossibilidade'), ('Depois', 'Aula 17 · Inadimplemento')], b,
     ('aula-15.html', '← Aula 15', 'Qual evento extingue o quê?'), ('aula-17.html', 'Aula 17 →', 'Quando o descumprimento permite resolver'), unit='9')
