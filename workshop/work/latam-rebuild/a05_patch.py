# LAT-1 · Aula 05 (Gelman): rebuild on the live page (Claude, 05/10).
# Keeps ch. 01, the hero and Fig. 1 verbatim; restructures 02–07 so each fact is said once (F-021),
# adds Vio Grossi's concurrence, § 241, the 2011 compliance steps, the 2013 supervision as its own chapter,
# replaces the text-in-cells Fig. 2 with the glossed judgment page (F-026), and closes with eixo questions.
import re, sys
sys.path.insert(0, '/Users/benecles/Developer/ordenacoes-filipinas-workshop/work/latam-rebuild')
from a05_fig2 import FIG2

P = sys.argv[1]
s = open(P).read()

def chapter(n, title, lede, tone=''):
    return (f'<section class="chapter" aria-labelledby="c{n}"><span class="num {tone}" aria-hidden="true">{n:02d}</span>'
            f'<h2 id="c{n}">{title}</h2><p class="lede">{lede}</p></section>\n')
def longform(*paras): return '<div class="longform"><div>' + ''.join(paras) + '</div></div>\n'
def p(t): return f'<p>{t}</p>'
def h3(t): return f'<h3>{t}</h3>'
def lex(label, text, tone='conc'): return f'<p class="lex {tone}"><b>{label}</b>{text}</p>'

# ---- pieces kept verbatim from the live page
i_c2 = s.index('<section class="chapter" aria-labelledby="c2"')
i_c3 = s.index('<section class="chapter" aria-labelledby="c3"')
i_c4 = s.index('<section class="chapter" aria-labelledby="c4"')
scrollies = [m.start() for m in re.finditer(r'<div class="scrolly">', s)]
fig1 = s[scrollies[0]:s.index('<div class="longform">', scrollies[0])]
i_end = s.index('<nav class="endnav"')
quiz_start = s.index('<div class="quiz">')
quiz_end = s.index('</div>', s.rindex('</details>', 0, i_end)) + len('</div>')
old_quiz = s[quiz_start:quiz_end]
old_items = re.findall(r'<details>.*?</details>', old_quiz, re.S)
assert len(old_items) == 5, len(old_items)

# ---- 02 · the Court (edited in place: two sentences of backstage out, three facts in)
c2 = s[i_c2:i_c3]
c2 = c2.replace('Dois passos da sentença são novos e são o centro da aula de 31/08. O primeiro',
                'Dois passos da sentença vão além dessa linha. O primeiro')
c2 = c2.replace('Para a Corte, as consultas populares são atos atribuíveis ao Estado e, portanto, também geram responsabilidade internacional (§ 238).',
                'Para a Corte, o referendo de 1989 (art. 79 da Constituição uruguaia) e o plebiscito de 2009 (art. 331) são atos atribuíveis ao Estado e, portanto, também geram responsabilidade internacional (§ 238).')
old_res = re.search(r'<p>Nos pontos resolutivos,.*?</p>', c2, re.S).group(0)
new_tail = (
    p('O caso tinha uma particularidade que a Corte registrou sem se deixar desviar por ela. Desde 23 de junho de 2005, o Executivo uruguaio entendia que o caso Gelman estava fora do alcance da Lei de Caducidade, e a investigação havia sido reaberta. Mesmo assim, o principal obstáculo às investigações tinha sido a vigência e a aplicação da própria lei (§ 241). Por isso a condenação não se limita ao caso: o Uruguai descumpriu o dever de adequar seu direito interno à Convenção (art. 2º), pela interpretação e aplicação que deu à Lei de Caducidade em graves violações.')
    + p('Nos pontos resolutivos, todos votados por <strong>unanimidade</strong>, a Corte declarou o Uruguai responsável pelo desaparecimento forçado de María Claudia, pela supressão e substituição da identidade de Macarena, tratada como forma de desaparecimento forçado, e pela falta de investigação. Mandou conduzir a investigação, determinar responsabilidades e aplicar as sanções cabíveis (ponto 9), continuar a busca por María Claudia (ponto 10) e garantir que a Lei de Caducidade, por carecer de efeitos, não volte a obstruir a investigação deste e de outros casos de graves violações (ponto 11).')
    + h3('O voto de Vio Grossi: por que o eleitorado responde pelo Estado')
    + p('Ninguém divergiu, mas o juiz Eduardo Vio Grossi juntou um voto concorrente que explica o passo mais ousado da sentença: imputar ao Estado o resultado de uma votação popular. Pelas regras de responsabilidade internacional codificadas pela Comissão de Direito Internacional da ONU, é ato do Estado o comportamento de qualquer de seus órgãos, exerça ele funções legislativas, executivas, judiciais ou “de outra índole”. Quando o eleitorado aprova ou ratifica uma lei, exerce função legislativa, ou ao menos uma função de outra índole, a da democracia direta. Logo, a cidadania inteira pode violar uma norma internacional e comprometer a responsabilidade do Estado. A qualificação de um ato como ilícito pelo direito internacional não depende do que diz o direito interno.')
    + p('Vio Grossi apoia a frase do § 239 na Carta Democrática Interamericana: ela faz do respeito aos direitos humanos elemento essencial da democracia (art. 3º) e, no art. 8º, garante a quem se considere violado o acesso ao sistema interamericano de petições, e não aos órgãos políticos da OEA. O mesmo voto traz uma advertência que reaparecerá em Montevidéu: a jurisprudência da Corte é fonte auxiliar do direito internacional. Ela interpreta o tratado, o costume ou o princípio vigente para o Estado; não cria direito novo.')
)
c2 = c2.replace(old_res, new_tail)

# ---- 03 · Uruguay complies, and its Supreme Court strikes part of the compliance
c3 = chapter(3, 'A reação uruguaia', 'O Legislativo cumpriu a sentença; a Suprema Corte derrubou parte do cumprimento.') + longform(
    p('O Uruguai começou a cumprir. O Decreto 323, de 30 de junho de 2011, e a Lei 18.831, de 27 de outubro de 2011, foram passos que a própria Corte IDH depois reconheceria como concretos. A lei restabeleceu a pretensão punitiva do Estado, e seus três artigos fazem coisas diferentes: o art. 1º restaura a possibilidade de processar os crimes cobertos pela Lei de Caducidade; o art. 2º manda não computar prazo algum de prescrição ou caducidade entre 22 de dezembro de 1986 e a vigência da nova lei; o art. 3º declara esses delitos crimes de lesa-humanidade, conforme os tratados de que o Uruguai é parte.'),
    p('Investigados opuseram exceção de inconstitucionalidade contra os três artigos. Na <strong>Sentencia 20/2013</strong>, de 22 de fevereiro de 2013, a Suprema Corte de Justiça acolheu a exceção só em parte: declarou inconstitucionais e inaplicáveis aos excepcionantes os arts. 2º e 3º e rejeitou o resto, de modo que o art. 1º ficou de pé. O fundamento foi a irretroatividade da lei penal mais grave, que decorre dos princípios de liberdade e legalidade da Constituição uruguaia (arts. 10 e 72): suspender retroativamente a prescrição e requalificar retroativamente os crimes agravava a situação de quem já havia adquirido o direito à prescrição.'),
    p('O acórdão enfrenta Gelman sem negá-lo de frente. A maioria afirma que o caso não trata de cumprir ou descumprir a Corte IDH, mas de exercer o controle de constitucionalidade, que é irrenunciável: se a Corte IDH é a intérprete última da Convenção, a Suprema Corte é a intérprete última da Constituição uruguaia. Cita ainda a crítica de Néstor Sagüés ao controle de convencionalidade: Estados passam a ficar vinculados por jurisprudência formada em processos dos quais não foram parte. A objeção tem parentesco com a advertência de Vio Grossi sobre a jurisprudência como fonte auxiliar, levada a uma conclusão que ele não tirou.'),
    p('Formalmente, a decisão vale só para os excepcionantes daquele processo. O problema está no raciocínio, que pode ser repetido em cada caso análogo e conduzir à prescrição de todos eles.'),
    p('Ricardo Pérez Manrique ficou vencido, por três razões. Os arts. 2º e 3º nem se aplicavam ao caso concreto. Também não inovavam: os tratados de direitos humanos têm raiz constitucional no Uruguai, e os crimes contra a humanidade são imprescritíveis por integrarem o <em>jus cogens</em> desde Nuremberg; a convenção sobre imprescritibilidade apenas declara obrigações preexistentes. Por fim, o art. 3º admite interpretação conforme à Constituição: nem todo delito coberto pela Lei de Caducidade é de lesa-humanidade, e cabe ao juiz do mérito qualificar cada conduta. Onde a maioria dá peso à data em que o regime legal foi positivado, Pérez Manrique dá peso ao caráter inderrogável da proibição internacional.'),
    p('A Sentencia 65/2014 da mesma Suprema Corte, de 17 de março de 2014, julga outra matéria: uma exceção contra o art. 365 do Código Penal, na redação da Lei 19.120, que trata de faltas como a falta de respeito à autoridade. Não trata de Gelman nem da Lei 18.831.'),
)

# ---- 04 · the Court answers: the 2013 supervision resolution
c4 = chapter(4, 'A resposta da Corte em 2013', 'A supervisão não anula a decisão uruguaia; chama-a de obstáculo.') + longform(
    p('Um mês depois, em 20 de março de 2013, a Corte IDH emitiu resolução de supervisão de cumprimento. Não funcionou como recurso contra a Sentencia 20/2013 nem declarou seus efeitos anulados. A pergunta era outra: depois da sentença de 2011, o Estado tinha tomado as medidas necessárias para que a Lei de Caducidade e obstáculos semelhantes não bloqueassem a investigação?'),
    lex('Corte IDH, supervisão Gelman (2013), considerando 102', 'La obligación del Estado de dar pronto cumplimiento a las decisiones de la Corte […] vincula a todos sus poderes y órganos, incluidos sus jueces […], por lo cual no puede invocar disposiciones del derecho constitucional u otros aspectos del derecho interno para justificar una falta de cumplimiento de la Sentencia.', 'dif'),
    p('Em português: a obrigação de cumprir vincula todos os poderes e órgãos, inclusive os juízes, e o Estado não pode invocar a própria Constituição para justificar o descumprimento. A Corte acrescentou que seria contraditório usar o controle de convencionalidade, um instrumento para aplicar o direito internacional, como justificativa para deixar de cumprir a sentença.'),
    p('No considerando 103, a Corte reconheceu os passos concretos do Uruguai, o Decreto 323 e a Lei 18.831, e disse que a decisão de 22 de fevereiro de 2013 não estava em consonância com a evolução do direito interamericano e universal dos direitos humanos. Mesmo contendo reflexões dirigidas a cumprir a sentença, pela maneira como estavam expostas constituíam um <strong>obstáculo ao pleno cumprimento</strong>, que poderia quebrar o acesso das vítimas à justiça e perpetuar a impunidade. A resolução registrou a tese uruguaia de que a decisão só produzia efeito no processo concreto, e respondeu com o raciocínio: a fundamentação podia ser reiterada em casos análogos. No considerando 104, afirmou que a sentença de 2011 é coisa julgada internacional, vinculante em sua integralidade, nas partes considerativas e dispositivas, para todos os órgãos uruguaios.'),
    p('A Corte enfrentou também a objeção de irretroatividade. O desaparecimento forçado é uma violação continuada: enquanto não se conhece o destino da pessoa, o delito continua. Aplicar a tipificação uruguaia de desaparecimento forçado, em vigor desde 2006, a um desaparecimento ainda em curso não é aplicar retroativamente uma lei nova a um fato encerrado. A supervisão manteve abertas as obrigações de investigar, buscar María Claudia, remover obstáculos, formar agentes e garantir acesso a arquivos.'),
    p('As duas cortes, portanto, não se contradizem no mesmo plano. A Suprema Corte decidiu o dever doméstico de cada juiz naquele processo, à luz da Constituição. A Corte IDH decidiu o dever internacional do Uruguai, como Estado, de cumprir uma sentença em caso do qual foi parte. O conflito real está no efeito prático: se o raciocínio da Sentencia 20/2013 se repete, a ordem do ponto 11 deixa de ser cumprida.'),
)

# ---- 05 · Gargarella: Fig. 1 kept, his arguments said once, Fig. 2 = the glossed judgment
steps2 = (
    '<div class="step" data-panel="p-am0"><div class="card"><span class="label dif">A sentença</span><h3>Três razões, uma ordem</h3><p>A conclusão da Corte se apoia em três razões que se reforçam: a anistia impede que as vítimas sejam ouvidas e protegidas (§ 226); o que conta é o efeito da lei, não sua origem (§ 229); e o voto popular não dá à lei legitimidade perante o direito internacional (§§ 238–239). Delas sai o ponto 11: a lei não pode obstruir a investigação.</p></div></div>'
    '<div class="step" data-panel="p-am1"><div class="card"><span class="label conc">Primeira objeção</span><h3>A gradação ataca duas razões</h3><p>Gargarella não nega o § 226. Ataca o § 229 e os §§ 238–239: tratar da mesma forma uma autoanistia de ditadura e uma lei confirmada por plebiscito ignora diferenças de legitimidade que importam.</p></div></div>'
    '<div class="step" data-panel="p-am2"><div class="card"><span class="label conc">Segunda objeção</span><h3>Reproche não é só castigo</h3><p>A segunda crítica mira a premissa por trás do ponto 9: que responder a graves violações exige, sempre, investigação e sanção penal. Verdade, reparação e memória também são formas de reprovação.</p></div></div>'
    '<div class="step" data-panel="p-am3"><div class="card"><span class="label conc">A objeção de Montevidéu</span><h3>A sentença fica; a execução cai</h3><p>A Sentencia 20/2013 não toca nenhuma razão da Corte. Derruba os arts. 2º e 3º da lei que cumpria a sentença, e mantém o art. 1º. É por isso que a supervisão de 2013 a chama de obstáculo, e não de afronta.</p></div></div>'
)
fig2 = ('<div class="scrolly">\n <div class="stage" aria-hidden="true"><figure>' + FIG2 +
        '<figcaption><span>Fig. 2 · A sentença e suas objeções</span><span class="stage-step">1 / 4</span></figcaption></figure></div>\n'
        ' <div class="steps">\n' + steps2 + '\n </div>\n</div>\n')
c5 = chapter(5, 'A crítica de Gargarella', 'Nem toda anistia é igual: a legitimidade democrática tem graus.') + fig1 + longform(
    p('Gargarella acrescenta uma segunda crítica. A Corte confunde reproche, sanção e castigo: trata a prisão como a única forma de expressar a máxima reprovação social. Uma comunidade democrática pode escolher outras formas de responder a crimes massivos: comissões de verdade (Chile, El Salvador, a Comissão para a Paz uruguaia, a Comissão Nacional da Verdade brasileira), reparações, pedidos públicos de perdão, memoriais, arquivos, “juízos pela verdade”. Ele não sustenta que essas alternativas sejam superiores nem pede impunidade. Seu ponto é mais estreito: antes de concluir que a Convenção exige o castigo penal como única resposta, a Corte precisava justificar essa leitura.'),
    p('A disputa aparece no art. 1.1 da Convenção. A Corte lê o dever de respeitar e garantir direitos como fundamento para prevenir, investigar, sancionar e reparar; Gargarella observa que a redação do artigo não enumera essa sequência e questiona a passagem que converte o dever de garantia em obrigação de sancionar penalmente. A crítica não demonstra que a Corte esteja errada. Identifica o passo que ela precisa justificar.'),
    p('Víctor Abramovich, ex-vice-presidente da Comissão Interamericana, objeta que o Uruguai também aderiu democraticamente ao sistema interamericano e ratificou a Convenção: há pedigree democrático na autoridade regional. Gargarella responde que aceitar um tribunal abre, em vez de encerrar, a discussão sobre o alcance de sua autoridade. E lembra que juízes também discordam sobre o conteúdo dos direitos e resolvem o desacordo votando: a regra majoritária não desaparece quando a decisão é judicial, muda de foro e de composição.'),
    p('Uma ressalva do próprio Gargarella evita a leitura caricata: há boas razões de igualdade para não dar tratamento especial justamente aos autores dos piores crimes da história da região. O que ele recusa é que isso justifique, sem discussão, o modelo punitivo como única resposta possível. Na prática, a diferença é verificável: memorial, reparação e pedido de perdão, sem investigar o desaparecimento, não satisfazem a ordem concreta de Gelman. Mas reconhecer o dever de investigar não resolve sozinho qual sanção é devida em cada processo.'),
) + fig2

# ---- 06 · the eixo, answered with the cases
c6 = chapter(6, 'O eixo da aula', 'Pode uma decisão majoritária afastar direitos protegidos constitucional e internacionalmente?', 'dif') + longform(
    '<p class="eixo"><b>Eixo de discussão da aula</b>Pode uma decisão majoritária afastar direitos protegidos constitucional e internacionalmente? Quais são os limites da soberania popular?</p>',
    p('O caso Gelman oferece três respostas para comparar. Para a <strong>Corte IDH</strong> (2011, unânime), não pode: a proteção dos direitos humanos é limite intransponível à regra da maioria, e o voto popular, por ser ato do Estado, gera responsabilidade como qualquer lei. Para a <strong>Suprema Corte uruguaia</strong> (2013, com o voto vencido de Pérez Manrique), a pergunta se desloca: mesmo quando o Estado decide cumprir a obrigação internacional, garantias constitucionais do acusado, como a irretroatividade penal, também limitam o que as maiorias podem fazer. Para <strong>Gargarella</strong>, a resposta depende do grau de legitimidade democrática da decisão e do tipo de resposta que ela dá aos crimes; tratar um plebiscito livre como uma autoanistia empobrece a própria ideia de democracia.'),
    h3('Como montar a resposta'),
    '<ol><li><strong>Tese.</strong> Diga se a maioria pode, e com qual limite.</li><li><strong>Casos.</strong> Para cada um: tribunal, ano, o que decidiu, por quê. Gelman (§§ 229, 238–239, ponto 11); Sentencia 20/2013 (arts. 2º e 3º caem, art. 1º fica); supervisão de 2013 (considerandos 102–104).</li><li><strong>Divergência.</strong> Quem discordou e como: Pérez Manrique contra a maioria uruguaia; Gargarella contra a Corte IDH; Vio Grossi concorda, mas por um fundamento próprio.</li><li><strong>Posição.</strong> Separe o plano internacional (o dever do Estado) do doméstico (o dever de cada juiz) antes de concluir.</li></ol>',
    h3('Três situações para testar'),
    p('Se uma lei nova apenas reabre a pretensão punitiva e mexe em prazos para fatos passados, a objeção de legalidade da Sentencia 20/2013 está diretamente em jogo. Se a investigação apura um desaparecimento que continuou depois de o tipo penal entrar em vigor, a razão da Corte IDH sobre crime continuado precisa ser enfrentada. E se alguém disser que a Sentencia 20/2013 anulou Gelman, a resposta é não: são decisões de planos diferentes, e a sentença internacional continua vinculando o Uruguai.'),
    p('O caso inverso vem na Aula 06: na Bolívia, um tribunal usou a Convenção Americana para <em>ampliar</em> o que a maioria havia recusado no voto.'),
)

# ---- 07 · test: the five old items kept, four new ones, the last an eixo question
def item(q, a): return f'<details><summary>{q}</summary><p>{a}</p></details>'
new_items = [
    item('Quem divergiu em Gelman vs. Uruguai?', 'Ninguém: os pontos resolutivos foram votados por unanimidade. O juiz Vio Grossi juntou voto concorrente, não divergente, explicando por que um voto popular é ato do Estado.'),
    item('Por que um plebiscito pode gerar responsabilidade internacional do Estado?', 'Porque o comportamento de qualquer órgão do Estado, em função legislativa ou de outra índole, é ato do Estado; o eleitorado que aprova ou ratifica uma lei exerce essa função (§ 238; voto de Vio Grossi). A legitimação democrática é limitada pelas obrigações de direitos humanos (§ 239).'),
    item('A Sentencia 20/2013 anulou Gelman? O que a Corte IDH disse dela?', 'Não. Ela declarou inaplicáveis aos excepcionantes os arts. 2º e 3º da Lei 18.831. Na supervisão de 20/03/2013, a Corte IDH chamou a decisão de obstáculo ao pleno cumprimento, porque seu raciocínio podia ser reiterado em casos análogos, e reafirmou que a sentença vincula todos os órgãos uruguaios, inclusive os juízes (considerandos 102–104).'),
    item('Eixo: um país aprova em referendo uma lei que extingue a punibilidade de desaparecimentos forçados cometidos sob a ditadura. A maioria pode fazer isso?', 'Pela Corte IDH, não: Gelman (2011) diz que a origem democrática não dá à lei legitimidade internacional (§ 238) e que os direitos humanos limitam as maiorias (§ 239); o efeito, não a origem, decide (§ 229). Divergências a registrar: Gargarella pediria distinguir o grau de legitimidade do referendo e discutir se a resposta tem de ser penal; e, se o Estado depois reabrir os casos, a Sentencia 20/2013 mostra que a irretroatividade penal limita como fazê-lo, enquanto a Corte IDH responde com o crime continuado.'),
]
c7 = chapter(7, 'Teste', 'Responda antes de abrir.') + '<div class="wide">\n<div class="quiz">' + ''.join(old_items + new_items) + '</div>\n</div>\n'

s = s[:i_c2] + c2 + c3 + c4 + c5 + c6 + c7 + s[i_end:]
open(P, 'w').write(s)
print('ok')
