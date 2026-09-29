from common import *
from maps import latam_map, map_defs, xy, inset

TL = [(80, '1986', 'Lei 15.848', 'Ley de Caducidad', 'ink'),
      (240, '1989', 'Referendo', 'a lei é mantida', 'ink'),
      (400, '2009', 'Plebiscito', 'a anulação não passa', 'ink'),
      (580, '2011', 'Corte IDH', 'Gelman: sem efeitos', 'conc'),
      (760, '2011', 'Lei 18.831', 'reabre a persecução', 'dif'),
      (940, '2013', 'SCJ 20/2013', 'arts. 2 e 3 caem', 'dif')]
hero = '<path class="draw" d="M50 70H1030" style="fill:none;stroke:var(--ink);stroke-width:3"/>'
for i, (x, y, a, b_, tone) in enumerate(TL):
    col = {'ink': 'var(--ink)', 'dif': 'var(--dif)', 'conc': 'var(--conc)'}[tone]
    hero += (f'<g class="pop" style="--d:{.2 + i * .2:.1f}s;font:12px var(--mono);letter-spacing:1px">'
             f'<circle cx="{x}" cy="70" r="7" style="fill:{col}"/>'
             f'<text x="{x}" y="46" text-anchor="middle" style="fill:{col}">{y}</text>'
             f'<text x="{x}" y="100" text-anchor="middle" style="fill:var(--ink)">{a}</text>'
             f'<text x="{x}" y="118" text-anchor="middle" style="fill:var(--ink-2);font-size:11px">{b_}</text></g>')

# ---- Fig: Gargarella's democratic gradient
AM = [('ARGENTINA · BIGNONE', 'autoanistia da ditadura, no fim do regime', 'extremo da ilegitimidade'),
      ('PERU · FUJIMORI', 'Congresso pós-autogolpe, liberdades restritas', 'legitimidade muito baixa'),
      ('ARGENTINA · ALFONSÍN', 'Congresso democrático, sob pressão militar', 'legítima, mas golpeada'),
      ('URUGUAI · CADUCIDAD', 'Congresso democrático + duas consultas populares', 'legitimidade significativa')]
GPIN = [(-58.4, -34.6, 'Bignone · 83', 'middle', 0, 22), None, (-58.4, -34.6, 'Alfonsín · 86–87', 'middle', 0, 38), (-56.2, -34.9, 'Caducidad · 86', 'end', 4, -14)]
GISO = ['ARG', 'PER', 'ARG', 'URY']
def gradient(k):
    fills = {}
    for i in range(k + 1):
        fills[GISO[i]] = 'conc' if i < 2 else 'dif'
    if k >= 2: fills['ARG'] = 'mix'
    pins = [(-77.0, -12.05, 'Fujimori · 1995', 'end', -10, 4)] if k >= 1 else []
    o = latam_map(fills, ['PER'] if k >= 1 else [], pins=pins, title='QUATRO ANISTIAS, QUATRO GRAUS', skip_seas=('OCEANO ATLÂNTICO', 'OCEANO PACÍFICO'))
    ipins = [GPIN[i] for i in range(k + 1) if GPIN[i]] + [(-58.4, -34.6, '', 'start', 0, 0)]
    o += inset(f'ins-gr{k}', -62.5, -52.5, -37.5, -30.5, 396, 330, 196, fills, ipins[:-1], 'Rio da Prata')
    # the gradient scale, in the Pacific
    o += T(24, 404, 'LEGITIMIDADE DEMOCRÁTICA', 't-small', style='letter-spacing:.08em')
    for i, (a, s_, v) in enumerate(AM):
        x = 24 + i * 44
        h = 14 + i * 12
        on = i <= k
        tone = 'conc' if i < 2 else 'dif'
        o += G(R(x, 480 - h, 36, h, f'w-{tone} ink' if on else 'f-paper ink', style='' if on else 'opacity:.35'), extra=' ' + go(f'p-gr{i}', a))
    o += P('M24 486H196', 'ink') + T(24, 502, 'menos', 't-small') + T(196, 502, 'mais', 't-small', anchor='end')
    a, s_, v = AM[k]
    l1, _, l2 = s_.partition(', ') if ', ' in s_ else s_.partition(' + ')
    o += G(T(24, 524, a, 't-mid') + T(24, 542, l1 + (',' if ', ' in s_ else ' +'), 't-small') + T(24, 557, l2, 't-small')
           + T(24, 574, v, 't-small tc-' + ('conc' if k < 2 else 'dif')), 'fade', d=.2)
    return o

# ---- Fig: argument map of the Gelman debate
REAS = [(40, '§ 226', 'impede ouvir as', 'vítimas (8 e 25)'),
        (220, '§ 229', 'vale a ratio legis,', 'não a origem da lei'),
        (400, '§§ 238–239', 'o voto não basta:', 'limite às maiorias')]
OBJ = [(220, 'GARGARELLA', 'gradação', 'democrática', [(300, 310), (480, 310)]),
       (40, 'GARGARELLA', 'reproche não é só', 'castigo penal', [(120, 310)]),
       (400, 'SCJ 20/2013', 'irretroatividade;', 'a CF é dela', None)]
def node(x, y, w, h, t1, t2, t3, tone, on=True):
    return (R(x, y, w, h, f'w-{tone} ink' if on else 'f-paper ink', style='' if on else 'opacity:.3')
            + T(x + 12, y + 30, t1, 't-small tc-' + tone if on else 't-small', style='letter-spacing:.06em' + ('' if on else ';opacity:.4'))
            + T(x + 12, y + 58, t2, 't-small', style='' if on else 'opacity:.4') + T(x + 12, y + 78, t3, 't-small', style='' if on else 'opacity:.4'))
def amap(k):
    o = T(40, 40, 'O DEBATE EM UM MAPA', 't-small', style='letter-spacing:.1em')
    o += G(node(40, 56, 520, 96, 'CORTE IDH · CONCLUSÃO', 'a Lei de Caducidade não tem efeitos jurídicos', 'e não pode impedir investigar e punir', 'dif'), 'pop' if k == 0 else '', d=.1, extra=go('p-am0', 'Conclusão'))
    for i, (x, t1, t2, t3) in enumerate(REAS):
        o += G(node(x, 210, 160, 100, t1, t2, t3, 'dif') + P(f'M{x+80} 210V152', 'c-dif'), 'pop' if k == 0 else '', d=.3 + i * .15)
    for j, (x, t1, t2, t3, targets) in enumerate(OBJ):
        on = j + 1 <= k
        g = node(x, 400, 160, 100, t1, t2, t3, 'conc', on)
        if on:
            if targets:
                for tx, ty in targets:
                    g += P(f'M{x+80} 400L{tx} {ty}', 'c-conc', style='stroke-dasharray:6 5')
                    g += C((x + 80 + tx) / 2, (400 + ty) / 2, 9, 'f-paper ink') + T((x + 80 + tx) / 2, (400 + ty) / 2 + 5, '×', 't-small tc-conc', anchor='middle')
            else:
                g += P(f'M{x+160} 450C590 450 590 104 560 104', 'c-conc', style='stroke-dasharray:6 5')
                g += C(585, 280, 9, 'f-paper ink') + T(585, 285, '×', 't-small tc-conc', anchor='middle')
        o += G(g, 'pop' if j + 1 == k else '', d=.2, extra=go(f'p-am{j+1}', t1))
    o += G(T(40, 560, 'azul: a decisão e suas razões · vermelho: o que ataca cada razão', 't-hand'), 'fade', d=.6)
    return o

b = map_defs()
b += chapter('01', 'c1', 'Os fatos do caso Gelman', 'Um desaparecimento da Operação Condor e uma lei aprovada, e duas vezes confirmada, pela democracia uruguaia.', 'dif')
b += longform(
    '<p>María Claudia García Iruretagoyena, argentina de 19 anos, estudante de Filosofia e Letras, foi detida em Buenos Aires em 24 de agosto de 1976, grávida de cerca de sete meses, com o marido Marcelo Gelman, filho do poeta Juan Gelman, por comandos militares uruguaios e argentinos. Foi levada ao Uruguai, onde deu à luz uma menina, entregue a uma família uruguaia. María Claudia continua desaparecida. A filha, María Macarena Gelman, só recuperou sua identidade anos depois. Os fatos se inserem na <strong>Operação Condor</strong>, a aliança secreta de repressão entre as ditaduras do Cone Sul.</p>',
    '<p>O obstáculo à investigação foi uma lei da democracia. Em 1986, o governo eleito do Uruguai promulgou a <strong>Lei 15.848, de Caducidade da Pretensão Punitiva do Estado</strong>: o Estado renunciava a punir os crimes cometidos até 1º de março de 1985 por militares e policiais, por motivos políticos ou em cumprimento de ordens. A lei foi submetida duas vezes ao voto popular. Em 1989, um <strong>referendo</strong> a manteve. Em 25 de outubro de 2009, um <strong>plebiscito</strong> sobre uma reforma constitucional que declararia nulos os arts. 1 a 4 não obteve os votos necessários.</p>',
    '<p>A Comissão Interamericana levou o caso à Corte em janeiro de 2010. A Corte julgou em <strong>24 de fevereiro de 2011</strong>.</p>')

b += bet('Uma lei aprovada pelo Parlamento de uma democracia e confirmada duas vezes pelo voto popular impede investigar desaparecimentos forçados. Um tribunal internacional pode declarar que ela não tem efeitos?', [
    ('Sim: direitos humanos são um limite que nenhuma maioria ultrapassa.', '*Corte IDH, Gelman (2011)'),
    ('Não sem mais: é preciso distinguir essa lei de uma autoanistia e pesar sua legitimidade democrática.', 'Gargarella (crítica acadêmica)'),
], '<p>A Corte IDH decidiu que sim, sem distinguir leis democráticas de autoanistias (§§ 229, 238 e 239). A segunda resposta é a crítica de Roberto Gargarella, que você verá no capítulo 04.</p>')
b += chapter('02', 'c2', 'O que a Corte Interamericana decidiu', 'As anistias para graves violações não têm efeito jurídico, venham de onde vierem.')
b += longform(
    '<p>A Corte reafirmou a linha que vinha desde <em>Barrios Altos vs. Peru</em> (2001): são inadmissíveis anistias, prescrições e excludentes de responsabilidade que impeçam a investigação e a punição de graves violações, como tortura, execuções e desaparecimentos forçados (§ 225). Essas leis violam os arts. 1.1 e 2 da Convenção, porque impedem que as vítimas sejam ouvidas por um juiz (art. 8.1) e recebam proteção judicial (art. 25), e por isso "carecem de efeitos jurídicos" (§ 226).</p>',
    '<p>Dois passos da sentença são novos e são o centro da aula de 31/08. O primeiro está no § 229: a incompatibilidade não se restringe às <strong>autoanistias</strong>. O que importa não é o processo de adoção nem a autoridade que editou a lei, mas a sua <em>ratio legis</em>, isto é, deixar impunes graves violações. A incompatibilidade é material, não formal.</p>',
    lex('Corte IDH, Gelman vs. Uruguai, § 238', 'El hecho de que la Ley de Caducidad haya sido aprobada en un régimen democrático y aún ratificada o respaldada por la ciudadanía en dos ocasiones no le concede, automáticamente ni por sí sola, legitimidad ante el Derecho Internacional.', 'conc'),
    '<p>O segundo passo responde exatamente ao que distinguia o caso uruguaio: a lei não era uma autoanistia de ditadura, e o povo a confirmou duas vezes. Para a Corte, as consultas populares são atos atribuíveis ao Estado e, portanto, também geram responsabilidade internacional (§ 238). E no § 239 formula o princípio:</p>',
    lex('Corte IDH, Gelman vs. Uruguai, § 239', 'La sola existencia de un régimen democrático no garantiza, per se, el permanente respeto del Derecho Internacional [...]. La legitimación democrática de determinados hechos o actos en una sociedad está limitada por las normas y obligaciones internacionales de protección de los derechos humanos [...], la protección de los derechos humanos constituye un límite infranqueable a la regla de mayorías, es decir, a la esfera de lo "susceptible de ser decidido" por parte de las mayorías.', 'conc'),
    '<p>Nos pontos resolutivos, a Corte declarou o Uruguai responsável pelo desaparecimento forçado de María Claudia, pela supressão da identidade de Macarena e pela falta de investigação, e determinou que o Estado garantisse que a Lei de Caducidade, por carecer de efeitos, não voltasse a representar obstáculo para investigar este e outros casos de graves violações.</p>')

b += chapter('03', 'c3', 'A reação uruguaia', 'O Legislativo cumpriu a sentença; a Suprema Corte derrubou parte do cumprimento.', 'dif')
b += longform(
    '<p>Em 2011, o Parlamento aprovou a <strong>Lei 18.831</strong>, para restabelecer a pretensão punitiva do Estado. O art. 1º restaurou a possibilidade de processar os crimes cobertos pela Lei de Caducidade; o art. 2º determinou que não se computasse prazo algum de prescrição ou caducidade entre 22 de dezembro de 1986 e a vigência da nova lei; o art. 3º declarou esses delitos crimes de lesa-humanidade, conforme os tratados de que o Uruguai é parte.</p>',
    '<p>Militares investigados opuseram exceção de inconstitucionalidade. Na <strong>Sentencia 20/2013</strong>, de 22 de fevereiro de 2013, a Suprema Corte de Justiça acolheu parcialmente a exceção e declarou <strong>inconstitucionais e inaplicáveis aos excepcionantes os arts. 2 e 3</strong> da Lei 18.831. O fundamento foi a irretroatividade da lei penal mais grave, que decorre dos princípios de liberdade e legalidade da Constituição uruguaia (arts. 10 e 72): suspender retroativamente a prescrição e requalificar retroativamente os crimes agravava a situação de quem já havia adquirido o direito à prescrição.</p>',
    '<p>O acórdão enfrenta a sentença de Gelman sem negá-la de frente. A maioria afirma que o caso não trata de cumprir ou descumprir a Corte IDH, mas de exercer o controle de constitucionalidade, que é irrenunciável: se a Corte IDH é a intérprete última da Convenção, a Suprema Corte é a intérprete última da Constituição uruguaia. Cita ainda a crítica de Néstor Sagüés ao controle de convencionalidade: Estados passam a ficar vinculados por jurisprudência formada em processos dos quais não foram parte.</p>',
    '<p>Ricardo Pérez Manrique ficou vencido. Para ele, os tratados de direitos humanos integram um bloco de constitucionalidade, e a imprescritibilidade dos crimes de lesa-humanidade já era norma de direito internacional consuetudinário (<em>jus cogens</em>) quando os fatos ocorreram. A lei nova não criaria nada, apenas reconheceria o que já vigorava, e não haveria retroatividade. A Corte IDH respondeu à Sentencia 20/2013 na resolução de supervisão de cumprimento de 2013 que o programa da disciplina indica.</p>')

b += chapter('04', 'c4', 'A crítica de Gargarella', 'Nem toda anistia é igual: a legitimidade democrática tem graus.')
b += scrolly('A gradação democrática', [(f'p-gr{k}', gradient(k), AM[k][0]) for k in range(4)], [
    S('p-gr0', 'Grau 1', 'A autoanistia da ditadura argentina', '<p>Roberto Gargarella aceita que as anistias da região foram muitas e diversas, e critica a Corte por tratá-las todas do mesmo modo. No extremo inferior está a anistia editada pelo general Bignone a favor dos próprios militares, antes de deixar o poder, no pior momento de popularidade do regime: um caso-limite de falta de legitimidade.</p>', 'conc'),
    S('p-gr1', 'Grau 2', 'A lei de Fujimori', '<p>Em seguida, a anistia peruana aprovada em 1995 pelo Congresso que se seguiu ao autogolpe de 1992, num contexto de fortes restrições às liberdades civis e políticas. A presunção de validade é muito baixa.</p>', 'conc'),
    S('p-gr2', 'Grau 3', 'As leis de perdão de Alfonsín', '<p>As leis de perdão do governo Alfonsín foram aprovadas por um Congresso democrático, com amplas liberdades, mobilização nas ruas e debate público, e depois mantidas pela Corte Suprema argentina. Mas surgiram sob pressão militar ilegítima, que culminou no levante da Semana Santa. São, em princípio, legítimas, mas golpeadas em sua legitimidade.</p>', 'dif'),
    S('p-gr3', 'Grau 4', 'A Lei de Caducidade uruguaia', '<p>No topo está a lei uruguaia: aprovada em plena democracia, afetada por medos e por pressões militares, mas reforçada por duas consultas populares, que Gargarella considera a expressão máxima da soberania popular. Ele lembra que, em 1980, sob a ditadura, os uruguaios já tinham rejeitado por mais de 57% um plebiscito convocado pelos militares: o eleitorado sabia dizer não. Para ele, a Corte IDH deveria ter feito um esforço argumentativo especial para distinguir esta lei da autoanistia de Bignone, e desautorizou a decisão democrática "em menos de dez linhas".</p>', 'dif'),
])
b += longform(
    '<p>Gargarella acrescenta uma segunda crítica. A Corte confunde <strong>reproche, sanção e castigo</strong>: trata a prisão como a única forma de expressar a máxima reprovação social. Uma comunidade democrática pode escolher outras formas de responder a crimes massivos: comissões de verdade (Chile, El Salvador, a Comissão de Paz uruguaia, a Comissão da Verdade brasileira), reparações, pedidos públicos de perdão, memoriais, "juízos pela verdade". Sua conclusão é que a Corte perdeu a oportunidade de construir uma teoria mais rica em termos democráticos e menos punitivista, e ofereceu uma visão marcada pela desconfiança em relação à cidadania.</p>',
    '<p>Uma ressalva do próprio Gargarella evita a leitura caricata: há boas razões de igualdade para não dar tratamento especial justamente aos autores dos piores crimes da história da região. O que ele recusa é que isso justifique, sem discussão, o modelo punitivo como única resposta possível.</p>')

b += scrolly('O mapa do debate', [(f'p-am{k}', amap(k), ['Decisão', 'Gradação', 'Castigo', 'SCJ'][k]) for k in range(4)], [
    S('p-am0', 'A decisão', 'Uma conclusão, três razões', '<p>A Corte IDH chega à conclusão por três caminhos que se reforçam: a anistia impede que as vítimas sejam ouvidas e protegidas (§ 226); o que conta é o efeito da lei, não sua origem (§ 229); e o voto popular não dá à lei legitimidade perante o direito internacional, porque os direitos humanos limitam as maiorias (§§ 238–239).</p>', 'dif'),
    S('p-am1', 'Primeira objeção', 'A gradação democrática ataca duas razões', '<p>A crítica de Gargarella não nega o § 226. Ela ataca o § 229 e os §§ 238–239: tratar da mesma forma uma autoanistia de ditadura e uma lei confirmada por plebiscito ignora diferenças de legitimidade que importam.</p>', 'conc'),
    S('p-am2', 'Segunda objeção', 'Reproche não é só castigo', '<p>A segunda crítica ataca a premissa de que investigar e responder a graves violações exige, sempre, punição penal. Há outras formas de reprovação social, como comissões de verdade, reparações e memória.</p>', 'conc'),
    S('p-am3', 'Terceira objeção', 'A Suprema Corte uruguaia e a execução', '<p>A SCJ não discute a sentença de Gelman em si. Ataca a forma de cumpri-la: a Lei 18.831 não pode retroagir para suspender prescrições ou requalificar crimes, e a última palavra sobre a Constituição uruguaia é dela.</p><p>Um mapa assim é um bom roteiro para a atividade escrita: identifique a conclusão, as razões e qual objeção atinge qual razão.</p>', 'conc'),
])
b += chapter('05', 'c5', 'O eixo da aula', 'Pode uma decisão majoritária afastar direitos protegidos constitucional e internacionalmente?', 'dif')
b += longform(
    eixo('Pode uma decisão majoritária afastar direitos protegidos constitucional e internacionalmente? Quais são os limites da soberania popular?'),
    '<p>O caso Gelman oferece três respostas para comparar. Para a <strong>Corte IDH</strong>, não pode: os direitos humanos são um limite intransponível para as maiorias, e a origem democrática de uma lei não a torna compatível com a Convenção. Para a <strong>Suprema Corte uruguaia</strong>, a pergunta se desloca: mesmo quando o Estado decide cumprir a obrigação internacional, garantias constitucionais do acusado, como a irretroatividade penal, também limitam o que as maiorias podem fazer. Para <strong>Gargarella</strong>, a resposta depende do grau de legitimidade democrática da decisão e do tipo de resposta que ela dá aos crimes; tratar um plebiscito livre como uma autoanistia empobrece a própria ideia de democracia.</p>',
    '<p>A aula continua com o caso inverso na Aula 06: na Bolívia, um tribunal usou a Convenção Americana para <em>ampliar</em> o que a maioria havia recusado no voto.</p>')

b += deep_chapter('05', '06', ('Legitimidade democrática',))
b += chapter('07', 'c7', 'Teste', 'Responda antes de abrir.')
b += quiz([
    ('Por que a Lei de Caducidade não era uma "autoanistia"?', 'Porque foi promulgada por um governo democrático em 1986 e depois mantida pelo voto popular duas vezes (referendo de 1989 e plebiscito de 2009). Não foi editada pelo regime em favor de si próprio.'),
    ('O que diz o § 229 de Gelman e por que ele importa?', 'Que a incompatibilidade das anistias com a Convenção não depende do processo de adoção nem da autoridade que as editou, mas da ratio legis de deixar impunes graves violações. Por isso vale também para leis democráticas, e não só para autoanistias.'),
    ('Qual o fundamento da Sentencia 20/2013 para derrubar os arts. 2 e 3 da Lei 18.831?', 'A irretroatividade da lei penal mais grave (arts. 10 e 72 da Constituição uruguaia): suspender retroativamente a prescrição e requalificar retroativamente os delitos como lesa-humanidade prejudicava os acusados.'),
    ('Qual o argumento do voto vencido de Pérez Manrique?', 'Os tratados de direitos humanos integram o bloco de constitucionalidade e a imprescritibilidade dos crimes de lesa-humanidade já era jus cogens na época dos fatos; a lei apenas a reconheceu, então não haveria retroatividade.'),
    ('O que é a "gradação democrática" de Gargarella?', 'A ideia de que anistias diferem em legitimidade democrática, conforme a inclusão e o debate que as cercaram: da autoanistia de Bignone à lei de Fujimori, às leis de perdão de Alfonsín e, no topo, à lei uruguaia confirmada por duas consultas populares. A Corte IDH deveria tê-las distinguido.'),
])

lesson('05', 'aula-05.html', 'Soberania popular e direitos: o caso Gelman',
       'Corte IDH, Gelman vs. Uruguai (2011): a Lei de Caducidade, o limite dos direitos humanos às maiorias (§§ 229, 238, 239), a Lei 18.831, a Sentencia 20/2013 da Suprema Corte uruguaia e a crítica de Gargarella.',
       'A maioria e', 'os direitos',
       'O Uruguai confirmou duas vezes, pelo voto, uma lei que impedia punir os crimes da ditadura. A Corte Interamericana disse que o voto <strong class="conc">não basta</strong>. Gargarella perguntou se todo voto <strong class="dif">vale o mesmo</strong>.',
       hero, [('Aula', '31/08 · Soberania popular'), ('Leitura', '≈ 22 min'), ('Antes', 'Aula 04 · Colômbia'), ('Depois', 'Aula 06 · Bolívia e OC-28')], b,
       ('aula-04.html', '← Aula 04', 'Justiça de transição na Colômbia'), ('aula-06.html', 'Aula 06 →', 'Reeleição e direitos políticos'), '31/08')
