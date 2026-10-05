# Deslop pass on Latam Aulas 01 and 02 against the CUFRGS Writing Standard Part D (Claude, 05/10):
# negative parallelism used as flourish (D1), slogans and moral closers (D4), intensifiers (D6), reader address in
# prose (D7), house tics and formulaic connectors (D3/D4). Legal distinctions that carry law in both halves stay.
import sys
D = sys.argv[1].rstrip('/') + '/'
EDITS = {
 'aula-01.html': [
  ('Ela não se mede pela quantidade de anos cobertos, mas pela conexão entre passado e presente.',
   'O que a define é a conexão entre passado e presente, qualquer que seja o número de anos cobertos.'),
  ('Uma análise que não se mede pela quantidade de anos, mas pela conexão entre passado e presente: busca as continuidades, a presença do passado no presente.',
   'Uma análise que procura a conexão entre passado e presente, as continuidades, qualquer que seja o período coberto.'),
  ('Cádiz foi decisiva, mas entrou num continente que já escrevia Constituições.',
   'Quando Cádiz chegou, o continente já escrevia Constituições.'),
  ('Cádiz foi decisiva pela circulação, não pela anterioridade.',
   'O peso de Cádiz vem da circulação que o texto teve, e Cádiz não veio primeiro.'),
  ('esses limites são profundamente marcados pela raça', 'esses limites são marcados pela raça'),
  ('catálogos de direitos generosos ao lado de presidentes muito fortes', 'catálogos de direitos generosos ao lado de presidentes fortes'),
  ('Classifique a combinação e indique o compromisso que a explica.', 'A classificação correta nomeia a combinação e o compromisso que a explica.'),
  ('e limitar de fato o poder da maioria e do Executivo', 'e limitar o poder da maioria e do Executivo'),
  ('Cádiz fez parte da experiência brasileira, não do seu desenho final.', 'A experiência gaditana passou pelo Brasil; o desenho de 1824 seguiu outro caminho.'),
  (' Constituições novas sobre sociedades velhas.', ''),
  ('A questão é simples de formular e difícil de responder: <strong>quem exerce a soberania quando o rei não pode exercê-la?</strong>', 'A questão posta era <strong>quem exerce a soberania quando o rei não pode exercê-la</strong>.'),
  (' É sobre essa superfície que o resto da disciplina acontece.', ''),
  (' Quando uma corte latino-americana decide, decide em cima dessas três veias.', ''),
  ('Importa saber “o que de 1812 continua funcionando hoje?”, e não “o que aconteceu em 1812?”.', 'Interessa saber o que de 1812 continua funcionando hoje.'),
  (' A constitucionalização dos direitos mudou também o papel dos juízes.', ''),
  ('O peso de Cádiz vem da circulação que o texto teve, e Cádiz não veio primeiro.', 'O peso de Cádiz vem da circulação que o texto teve.'),

 ],
 'aula-02.html': [
  ('suas instituições judiciais nasceram de uma matriz muito parecida', 'suas instituições judiciais nasceram de uma matriz parecida'),
  ('seguiram trajetórias nitidamente diferentes', 'seguiram trajetórias diferentes'),
  ('A regra de nomeação explica pouco; a pergunta é o que explica o resto.', 'A regra de nomeação explica pouco. O resto da explicação está na história de cada corte.'),
  ('Para analisar um caso, identifique primeiro qual pergunta está sendo respondida e que evidência serve a ela.',
   'A análise de um caso começa por saber qual pergunta está sendo respondida e que evidência serve a ela.'),
  ('ou muito protagonismo sem proteger direitos', 'ou protagonismo intenso sem proteger direitos'),
  ('<p class="lede">Não pelas decisões, mas pelas pessoas que as tomam.</p>', '<p class="lede">Um retrato das pessoas que decidem, de onde vêm e como chegaram.</p>'),
  ('A profissionalização começou, paradoxalmente, sob Vargas,', 'A profissionalização começou sob Vargas, apesar das restrições do governo à independência judicial,'),
  ('Para os autores, o que separa o Brasil da Argentina não é a regra de nomeação, que é a mesma, mas a estabilidade institucional e a preocupação das elites políticas com a legitimação jurídica de suas decisões.',
   'Com a mesma regra de nomeação, o que separa o Brasil da Argentina, para os autores, é a estabilidade institucional e a preocupação das elites políticas com a legitimação jurídica de suas decisões.'),
  ('Um quadro das cortes constitucionais latino-americanas responde a outra pergunta: não como as cortes conquistaram autonomia, mas que desenho cada país deu ao controle de constitucionalidade, tal como o quadro o registra, sem indicar ano-base.',
   'Um quadro das cortes constitucionais latino-americanas responde a outra pergunta, a do desenho: que forma cada país deu ao controle de constitucionalidade, tal como o quadro o registra, sem indicar ano-base.'),
  ('Ao comparar países, descreva cada eixo sem converter', 'A comparação entre países descreve cada eixo sem converter'),
  ('Use-a para comparar o desenho tal como apresentado, sem afirmar que as composições e competências continuam iguais hoje.',
   'Ela serve para comparar o desenho tal como apresentado; afirmar que composições e competências continuam iguais exigiria uma fonte datada.'),
  ('<p class="lede">O estudo não responde com um sim; mostra por que a pergunta é ambivalente.</p>', '<p class="lede">O estudo mostra por que a resposta é ambivalente.</p>'),
  ('Nesse sentido, expansão de competência e de ações de tutela pode reforçar a proteção de direitos.', 'Assim, a expansão de competência e de ações de tutela pode reforçar a proteção de direitos.'),
  (' É o caso que mostra com mais nitidez a distância entre a regra escrita e a prática.', ''),
  (' Protagonismo, portanto, não é sinônimo de proteção de direitos.', ''),
  (' Numa região de presidentes fortes, isso importa.', ''),
  (' A diferença de universo e tempo é parte da resposta, não uma falha a preencher com suposição.', ''),

 ],
}
for f, pairs in EDITS.items():
    s = open(D + f).read()
    for a, b in pairs:
        n = s.count(a)
        if n != 1: print('!!', f, n, a[:60])
        s = s.replace(a, b)
    open(D + f, 'w').write(s)
print('done')
