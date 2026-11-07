# Solução — 04 Esteganografia em texto

## A técnica

Cada linha do poema termina com uma sequência de 8 caracteres invisíveis: espaço (`0x20`) para o bit `0` e tab (`0x09`) para o bit `1`. Essa sequência de 8 bits forma um byte — um caractere da mensagem escondida. Uma linha, um caractere.

## Extraindo a mensagem

```python
linhas = open("poema.txt", "rb").read().split(b"\n")

mensagem = []
for linha in linhas:
    marcador = bytes(b for b in linha if b in (0x20, 0x09))
    # pega só os últimos 8 marcadores de cada linha (o resto são espaços do texto normal)
    marcador = marcador[-8:]
    if len(marcador) != 8:
        continue
    bits = "".join("1" if b == 0x09 else "0" for b in marcador)
    mensagem.append(chr(int(bits, 2)))

print("".join(mensagem))
```

## Flag

```
KHOADE{quem_olha_so_ve_um_poema_comum}
```
