# Solução — 01 Cifra de César

## Passo a passo

1. Força bruta nos 25 deslocamentos possíveis:

   ```python
   import string

   texto = open("cifrado.txt", encoding="utf-8").read()
   alfabeto = string.ascii_lowercase

   def decifrar(texto, deslocamento):
       resultado = []
       for char in texto:
           if char.lower() in alfabeto:
               indice = alfabeto.index(char.lower())
               nova = alfabeto[(indice - deslocamento) % 26]
               resultado.append(nova.upper() if char.isupper() else nova)
           else:
               resultado.append(char)
       return "".join(resultado)

   for d in range(1, 26):
       print(d, decifrar(texto, d)[:60])
   ```

2. O deslocamento **7** produz um texto legível em português.

## Flag

```
KHOADE{cesar_e_so_o_comeco}
```
