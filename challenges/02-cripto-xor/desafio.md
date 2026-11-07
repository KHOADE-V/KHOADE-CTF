# 02 — XOR com chave repetida

**Categoria:** Criptografia · **Dificuldade:** Iniciante

## História

Dessa vez a mensagem foi cifrada com XOR usando uma chave curta que se repete até cobrir todo o texto. É um esquema fraco (na prática, uma versão simplificada da cifra de Vernam), mas ótimo para entender como o XOR funciona.

## O arquivo

Arquivo: [`cifrado.bin`](cifrado.bin) — bytes brutos, não é texto.

## O que você sabe

- A chave tem exatamente **3 bytes**.
- O texto original é em português, só com letras minúsculas, espaços e pontuação comum (sem acentos).
- A flag está no texto, no formato `KHOADE{...}`.

## Sua missão

Descubra a chave de 3 bytes e recupere o texto original.

## Dicas

<details>
<summary>Dica 1</summary>

Se `C = P XOR K`, então `P = C XOR K`. Como a chave se repete, o byte na posição `i` do texto cifrado usou o byte `i % 3` da chave.
</details>

<details>
<summary>Dica 2</summary>

Agrupe os bytes cifrados por posição na chave (posição 0, 1 e 2) e tente, para cada grupo, cada um dos 256 valores possíveis de byte, verificando qual produz só caracteres imprimíveis.
</details>

<details>
<summary>Dica 3</summary>

Em Python, leia o arquivo com `open("cifrado.bin", "rb").read()` e use `bytes(c ^ k for c, k in zip(dados, chave_repetida))` para decifrar.
</details>
