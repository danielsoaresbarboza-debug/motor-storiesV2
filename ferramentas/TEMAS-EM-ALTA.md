# Motor Stories — Temas em alta (instruções da tarefa diária)

Quem executa: o Claude, numa tarefa agendada todo dia às 6h (horário de Brasília). Resultado: **3 sequências de stories prontas**, cada uma sobre um tema em alta, num único link para o Daniel importar no Motor Stories vermelho.

## 1. Achar os temas (web)
- Pesquisar o que está em alta **nas últimas 24 a 48 horas** nestas frentes: marcas e marketing; IA e tecnologia; redes sociais (Instagram, TikTok, YouTube, virais); assunto do dia no Brasil.
- Escolher **3 temas de frentes diferentes**. Bons temas: uma marca fez algo que todo mundo comentou; uma mudança em rede social que afeta quem posta; um lançamento de IA que muda o trabalho de quem cria; um viral com lição de comunicação.
- **Nunca:** política brasileira, eleições, partidos, religião, Exército, tragédia, crime, morte, doença, fofoca de celebridade sem lição de marca.
- Para cada tema, abrir **pelo menos uma fonte confiável** (veículo de notícia, site oficial, blog da empresa) e confirmar os fatos: o que aconteceu, quando, números. Nada de fato que não esteja na fonte.
- Não repetir tema das últimas sequências (ver histórico em `ferramentas/historico-temas.txt` se existir).

## 2. Escrever cada sequência
Quem é o Daniel e as regras de voz: **conversa do Elton Luiz** (frases curtas, uma ideia por story, como quem conta para um amigo) + **método do Ladeira** (premissa em vez de promessa, escalada de atenção, super sincero, antítese; sem palavras de vendedor) + posicionamento v4:
- Bio: "Quem é lembrado é chamado. Quem some, não." Pergunta-guia: "Por que isso foi lembrado — e o que você faz com isso?"
- Público: quem vive do próprio trabalho e trava no conteúdo. **Nunca** chamar o Daniel de designer.
- **Sem ofertas** (nada de preço, vagas, palavra-chave, "responda com X"). Sem pedido de compartilhar, marcar ou seguir.

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
    {"tipo":"texto","visual":"vidro|nativo|manchete|papel|nota|conversa|anuncio","texto":"...","fundo":"#0F0F10 (opcional)",
     "sticker":{"tipo":"nenhum|caixinha|enquete|quiz|slider","texto":"pergunta curta","opcoes":["Sim","Não"]}}
  ],
  "respostasModelo":[],
  "conferir":["Fonte: Veículo, DD/MM/AAAA — link","Story 3 é opinião sua."]
}]}
```
- `id`: `alta-` + data sem traços + número do tema (1, 2, 3). `data`: o dia da execução.
- Visual `vidro` (o mais elegante, painel de vidro líquido com texto em serifa) na maioria dos stories de texto; `anuncio` para o título grande (1º parágrafo; depois de uma linha em branco, o texto).
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
