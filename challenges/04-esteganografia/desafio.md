# 04 — Esteganografia em texto

**Categoria:** Esteganografia · **Dificuldade:** Iniciante

## História

Esteganografia é esconder uma mensagem dentro de outra, de um jeito que não chame atenção. Aqui, alguém escondeu uma mensagem dentro de um arquivo de texto comum, usando espaços e tabulações no final de cada linha — invisíveis para quem só olha o texto.

## O arquivo

Arquivo: [`poema.txt`](poema.txt). Parece só um poema qualquer.

## Sua missão

Encontre a mensagem escondida. A flag está no formato `KHOADE{...}`.

## Dicas

<details>
<summary>Dica 1</summary>

A maioria dos editores de texto esconde espaços e tabs no fim da linha. Abra o arquivo em modo binário para ver o que realmente tem lá.
</details>

<details>
<summary>Dica 2</summary>

Em Python: `linhas = open("poema.txt", "rb").read().split(b"\n")`. Olhe o que sobra depois do último caractere visível de cada linha.
</details>

<details>
<summary>Dica 3</summary>

Se cada linha termina com uma sequência de espaços (`0x20`) e tabs (`0x09`), pense neles como 0 e 1 — ou tab e espaço como os dois símbolos de um código binário de 8 bits por linha, formando um byte (um caractere) por linha.
</details>
