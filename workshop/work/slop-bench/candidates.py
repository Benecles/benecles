"""Candidate rules from SlopDetector, tropes.fyi and Antislop discovery, ported to Portuguese (CEO 06/10).
Each is backtested by eval_candidates.py; only survivors move into protocols/tools/slop_lint.py."""
C = {
 # SlopDetector: chatbot leftovers (language-agnostic or PT)
 'tool-artifact': r'(?:citeturn\d|contentReference\[oaicite|oai_citation|utm_source=(?:chatgpt|openai|claude|perplexity|copilot)|\[attached_file:\d)',
 'placeholder': r'\[(?:inserir|insira|seu nome|nome|data|fonte|link|citação|referência|preencher|completar)[^\]]{0,40}\]|\bXX/XX/XXXX\b|(?-i:\bTODO\b)|\blorem ipsum\b',
 'chat-scaffolding': r'\b(?:espero que (?:isso|este|esta) (?:ajude|tenha ajudado)|se (?:quiser|preferir|desejar), posso|fico à disposição|ótima pergunta|claro! |certamente! |posso ajudar (?:com|em) mais)',
 'ai-self-reference': r'\b(?:como (?:um )?modelo de linguagem|como (?:uma )?(?:IA|inteligência artificial),|até (?:a data|o momento) do meu (?:conhecimento|treinamento)|não tenho acesso (?:a|à) (?:internet|dados em tempo real))',
 'ritual-conclusion': r'(?m)(?:^|(?<=[.!?]\s))(?:Em suma|Em síntese|Em resumo|Resumindo|Para concluir|Em conclusão|Concluindo),',
 'challenges-future': r'\b(?:apesar dos (?:desafios|obstáculos)|desafios e perspectivas|resta saber se|o futuro dirá|só o tempo dirá|ainda há um longo caminho|permanece(?:m)? (?:como )?(?:um )?desafio)',
 'copula-avoidance': r'\b(?:configura-se como|constitui-se (?:como|em)|apresenta-se como|revela-se (?:como )?(?:um|uma|essencial|fundamental|crucial|decisivo)|figura como|afigura-se|erige-se (?:como|em))\b',
 'evaluative-tail': r',\s*o que (?:evidencia|demonstra|reforça|revela|ressalta|sublinha|mostra|confirma|ilustra|reflete|denota|atesta)\b',
 'ai-vocab-pt': r'\b(?:crucial|cruciais|fundamental|fundamentais|essencial|essenciais|robust[oa]s?|abrangente|notável|nuances?|panorama|multifacetad[oa]|intrínsec[oa]|salientar|primordial|imprescindível)\b',
 # tropes.fyi
 'count-announce': r'(?:^|(?<=[.!?]\s))(?:(?:Há|Existem|São) )?(?:Duas|Três|Quatro|Cinco|duas|três|quatro|cinco) (?:razões|coisas|perguntas|condições|camadas|lições|diferenças|movimentos|etapas|ideias|pontos|leituras|respostas|problemas)\b',
 'familiarity-appeal': r'\b(?:como (?:se sabe|é sabido|todos sabem|é notório)|é sabido que|notoriamente|célebre|clássic[oa] exemplo)\b',
 'analogy-coach': r'\b(?:pense (?:em|n[oa]s?) [^.]{1,40} como (?:um|uma)|imagine um mundo|imagine uma sociedade)\b',
 'where-it-lives': r'\b(?:é aí que (?:mora|reside|está)|onde (?:mora|reside) (?:de fato|realmente|o verdadeiro|a verdadeira))\b',
 'invented-label': r'\b(?:o|a|no|na|do|da|um|uma) (?:paradoxo|armadilha|dilema|ilusão|miragem|vácuo|inversão) d[aoe]s? [a-záéíóúçãõ]+\b',
 'stakes-inflation': r'\b(?:muda(?:m)? tudo|redefine(?:m)? (?:o|a)s? |sem precedentes|marco histórico|revolucion(?:a|ou|ário))\b',
}
