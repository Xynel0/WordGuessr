# WordGuess

WordGuess é um jogo de adivinhação de palavras inspirado no clássico jogo da forca, mas com foco em diferentes níveis de dificuldade e na personalização da lista de palavras.

## Modos de jogo

O jogo possui cinco modos:

- **Zen:** jogue sem limite de tentativas. Você pode continuar tentando até descobrir a palavra.
- **Fácil:** a quantidade de tentativas é definida de acordo com o número de letras da palavra.
- **Médio:** a quantidade de tentativas é definida de acordo com o número de letras da palavra.
- **Difícil:** a quantidade de tentativas é definida de acordo com o número de letras da palavra.
- **Impossível:** você possui apenas uma única tentativa.

## Lista de palavras

As palavras são escolhidas aleatoriamente a partir de um arquivo `.txt`, permitindo que você personalize facilmente o jogo adicionando ou removendo palavras.

Ao editar o arquivo, siga as seguintes regras:

- Utilize **uma palavra por linha**.
- Não deixe espaços em branco antes ou depois da palavra.
- Não utilize acentos.
- Não utilize caracteres especiais.

Seguindo esse formato, o jogo funcionará corretamente.

## Como executar

Antes de executar o programa, certifique-se de que:

1. Os três arquivos do repositório estão na mesma pasta.
2. Os arquivos mantêm seus nomes originais.
3. O diretório de trabalho utilizado para executar o programa é o mesmo diretório onde os arquivos estão localizados.

Em seguida, execute:

```bash
python main.py
```

> Caso o arquivo principal possua outro nome, substitua `main.py` pelo nome correspondente.

## Estrutura do projeto

```text
.
├── main.py
├── palavras.txt
└── ...
```

## Possíveis melhorias

- Adição de categorias de palavras.
- Sistema de pontuação.
- Ranking de jogadores.
- Interface gráfica.
- Novos modos de jogo.

## Licença

Este projeto foi desenvolvido para fins de estudo e aprendizado.