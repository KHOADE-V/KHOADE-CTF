# 03 — Login fraco

**Categoria:** Segurança web · **Dificuldade:** Intermediário

## História

Uma aplicação interna de exemplo tem uma tela de login. O código tem uma falha comum de implementação — o tipo de erro que aparece em sistemas reais quando a verificação de senha é feita de um jeito ingênuo.

## Subindo o alvo

Este desafio roda **só na sua máquina**, em `127.0.0.1`. Não é uma ferramenta de ataque e não deve ser exposto na internet.

```bash
cd challenges/03-web-login-fraco
python3 -m venv .venv && source .venv/bin/activate
pip install flask
python3 app.py
```

Acesse `http://127.0.0.1:5050`.

## Sua missão

Faça login como o usuário `admin` **sem saber a senha dele** e pegue a flag que aparece na página após o login.

## Dicas

<details>
<summary>Dica 1</summary>

Olhe como a aplicação decide se a senha está certa. Ela não usa hash — compara a senha enviada com a senha certa caractere por caractere, parando no primeiro que for diferente.
</details>

<details>
<summary>Dica 2</summary>

Esse tipo de comparação vaza informação pelo **tempo de resposta**: quanto mais caracteres do começo você acertar, mais tempo a comparação leva para falhar. É um ataque de "timing".
</details>

<details>
<summary>Dica 3</summary>

Escreva um script que testa cada posição da senha, um caractere de cada vez, medindo o tempo de resposta de várias tentativas e ficando com o caractere que demora mais. Repita até formar a senha inteira.
</details>
