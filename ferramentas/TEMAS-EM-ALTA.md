# Motor Stories — Temas em alta (instruções da tarefa diária)

Quem executa: o Claude, numa tarefa agendada todo dia às 6h (horário de Brasília). Resultado: **3 sequências de stories prontas**, cada uma sobre um tema em alta, num único link para o Daniel importar no Motor Stories vermelho.

## 1. Achar os temas (web)
- Pesquisar o que está em alta **nas últimas 24 a 48 horas** nestas frentes: marcas e marketing; IA e tecnologia; redes sociais (Instagram, TikTok, YouTube, virais); assunto do dia no Brasil.
- Escolher **3 temas de frentes diferentes**. Bons temas: uma marca fez algo que todo mundo comentou; uma mudança em rede social que afeta quem posta; um lançamento de IA que muda o trabalho de quem cria; um viral com lição de comunicação.
- **Nunca:** política brasileira, eleições, partidos, religião, Exército, tragédia, crime, morte, doença, fofoca de celebridade sem lição de marca.
- Para cada tema, abrir **pelo menos uma fonte confiável** (veículo de notícia, site oficial, blog da empresa) e confirmar os fatos: o que aconteceu, quando, números. Nada de fato que não esteja na fonte.
- Não repetir tema das últimas sequências (ver histórico em `ferramentas/historico-temas.txt` se existir).

## 2. Escrever cada sequência

COMO ESCREVER: ESTRUTURA DO LADEIRA, VOZ DO ELTON, ZERO CARA DE IA
A entrada do Daniel é MATÉRIA-PRIMA, nunca o texto final. Não resuma nem adapte o texto dele: reescreva do zero, mantendo só os fatos e a ideia, com a estrutura e a voz abaixo. Se o texto final ficar parecido com a entrada, você errou.

ESTRUTURA (marketing de premissas do Leandro Ladeira, Light Copy e Stories 10x). Cada sequência segue esta ordem:
1. Premissa de abertura: uma cena ou um fato concreto que a pessoa não consegue contestar. Despretensiosa (não cheira a venda), incontestável e simples (uma frase, uma ideia). Gancho forte = curiosidade, frase que engasga, desabafo ou argumento incontestável. Proibido abrir com conceito, imperativo, promessa ou pergunta retórica.
2. Escalada de atenção: cada story acrescenta uma premissa nova (premissa 1 + premissa 2 + premissa 3) e termina abrindo a porta do próximo. Nunca repetir a ideia com outras palavras. O story seguinte sempre é mais forte que o anterior.
3. Virada super sincera: o que todo mundo pensa e ninguém fala, ou uma antítese seca. É aqui que entra a opinião do Daniel.
4. Conclusão que a pessoa tira sozinha: não explique a moral. No máximo uma âncora "sempre que…" ligada ao cotidiano.
5. Fecho pelo "quadro na parede", nunca pela "furadeira": a interação fala do resultado que a pessoa quer, não do esforço.
Recursos do Ladeira (2 ou 3 por sequência, sem empilhar): super sincero, crônica (detalhe do detalhe), sentir na pele, sempre que, metáfora, antítese, criação de personagem, ironia leve.

VOZ (forma de falar do Elton Luiz; não copie frases dele):
- Como quem manda áudio pra um amigo contando o que aconteceu hoje. Primeira pessoa. Frases curtas, algumas bem curtas ("Voltei pro zero."), uma mais longa quando a emoção pede.
- Detalhe concreto da entrada: o objeto, o número, a hora, o que alguém disse. Nada genérico.
- Pode começar frase com "E" ou "Mas". Pode usar "cara", "sei lá", "olha", "sabe?" (no máximo uma vez cada por sequência). Sem palavrão, salvo se estiver na entrada.

ANTI-IA (o texto não pode parecer escrito por IA):
- Proibido travessão (—) e meia-risca (–) no texto. Use ponto.
- Proibido "não é X, é Y" mais de uma vez na sequência. Proibido trio de adjetivos ou lista de três coisas em sequência ("rápido, simples e eficaz").
- Proibidas estas palavras e expressões: jornada, potencializar, desbloquear, mergulhar, navegar, cenário, ecossistema, alavancar, escalar, estratégia, framework, robusto, crucial, fundamental, essencial, transformar, impactar, "no fim do dia", "vale lembrar", "em resumo", "afinal", "isso muda tudo", "o segredo", "a verdade é que", "e o melhor", "spoiler", "plot twist", "bora", "simples assim".
- Sem emoji, sem exclamação, sem dois-pontos dramático antes da revelação, sem frase de efeito simétrica em todo story. Varie o tamanho das frases. Nada de pergunta retórica em série.
- Prefira palavra do dia a dia à palavra bonita. Se uma frase parece legenda de banco de imagem, reescreva.

PALAVRAS PROIBIDAS DE VENDEDOR: exclusivo, único, promocional, não perca, infalível, imperdível, garantido, revolucionário, "agora" como urgência, descubra, você sabia que, vamos falar sobre, game changer, confira, dica de ouro, vou te ensinar.
Sem engagement bait: nada de "compartilha", "marca um amigo", "manda pra alguém", "me segue", "comenta X", "curte se concorda".

Posicionamento v4: bio "Quem é lembrado é chamado. Quem some, não."; público: quem vive do próprio trabalho e trava no conteúdo; **nunca** chamar o Daniel de designer; **sem ofertas**.

Estrutura (4 a 6 stories):
1. Gancho: o fato, concreto, com nome da marca ou plataforma (visual `nativo` ou `anuncio`).
2. O que aconteceu, em 1 ou 2 stories (só fatos da fonte; números exatos).
3. A leitura do Daniel: por que isso foi (ou vai ser) lembrado. É opinião: vai em `conferir`.
4. O que a pessoa que vive do próprio trabalho faz com isso (1 ação simples).
5. Interação: caixinha ou enquete com pergunta real ligada ao tema.

Escrita: fragmentar, ponto-final, 1 a 3 palavras em `**negrito**` por story, até 40 palavras por story, sem palavra fraca (talvez, meio que, acho que, um pouco, basicamente, na verdade).

## 3. Formato (JSON)
```json
{"sequencias":[{
  "id":"alta-AAAAMMDD-1",
  "data":"AAAA-MM-DD",
  "titulo":"Em alta: até 40 caracteres",
  "gatilho":"alta",
  "dispositivos":["escalada de atenção","super sincero"],
  "stories":[
    {"tipo":"texto","visual":"imagem|vidro|nativo|manchete|papel|nota|conversa|anuncio","texto":"...","imgBusca":"busca de foto em inglês (só para vidro)","fundo":"#0F0F10 (opcional)",
     "sticker":{"tipo":"nenhum|caixinha|enquete|quiz|slider","texto":"pergunta curta","opcoes":["Sim","Não"]}}
  ],
  "respostasModelo":[],
  "conferir":["Fonte: Veículo, DD/MM/AAAA — link","Story 3 é opinião sua."]
}]}
```
- `id`: `alta-` + data sem traços + número do tema (1, 2, 3). `data`: o dia da execução.
- Alterne visual `imagem` (só a foto em tela cheia com o texto por cima, até 25 palavras) e `vidro` (painel de vidro líquido com texto em serifa sobre a foto) na maioria dos stories de texto, inclusive o último com adesivo. Todo `imagem` e `vidro` leva `imgBusca`: 2 a 5 palavras em inglês, assunto + cor + lugar ("red umbrella gray street"), um assunto só, com contraste, sem clichê (escada, estrada, lâmpada, quebra-cabeça, xadrez, engrenagem, alvo, montanha, foguete, cérebro, aperto de mão, notebook, post-its, gráfico); cada story com uma foto diferente. O Motor vermelho busca a foto sozinho; `anuncio` para o título grande (1º parágrafo; depois de uma linha em branco, o texto).
- Toda fonte usada entra em `conferir` com veículo, data e link.

## 4. Gerar o link e entregar
```bash
git clone --depth 1 https://github.com/danielsoaresbarboza-debug/motor-storiesV2 /tmp/ms
python3 /tmp/ms/ferramentas/gerar_link.py temas.json
```
A mensagem final para o Daniel (é a notificação dele) tem:
1. Uma linha por tema: título + por que está em alta (até 15 palavras).
2. O link gerado, sozinho numa linha.
3. "Copie o link, abra o Motor Stories vermelho e toque em Colar do Motor azul."
4. As fontes.
