# 01 — Cifra de César

**Categoria:** Criptografia · **Dificuldade:** Iniciante

## História

Um bilhete foi interceptado. Quem escreveu só deslocou cada letra do alfabeto sempre pelo mesmo número de posições — a cifra mais antiga que se tem notícia, usada por Júlio César para mensagens militares.

## O bilhete

Arquivo: [`cifrado.txt`](cifrado.txt)

## Sua missão

Descubra o deslocamento usado e decifre a mensagem. A flag está escondida dentro do texto decifrado, no formato `KHOADE{...}`.

## Dicas

<details>
<summary>Dica 1</summary>

Na cifra de César, cada letra é trocada por outra que está N posições à frente no alfabeto (voltando ao "A" depois do "Z"). Decifrar é só deslocar na direção contrária.
</details>

<details>
<summary>Dica 2</summary>

Como só existem 25 deslocamentos possíveis (1 a 25), dá pra testar todos com um script e ver qual produz texto que faz sentido em português.
</details>

<details>
<summary>Dica 3</summary>

Em Python, `string.ascii_lowercase` e o operador `%` ajudam a "dar a volta" no alfabeto.
</details>
