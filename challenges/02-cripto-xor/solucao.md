# Solução — 02 XOR com chave repetida

## Passo a passo

1. Separe os bytes cifrados em 3 grupos pela posição (`i % 3`).
2. Para cada grupo, teste as 256 chaves de 1 byte e veja qual produz só caracteres imprimíveis (letras, espaço, pontuação):

   ```python
   dados = open("cifrado.bin", "rb").read()

   def candidatos(grupo):
       bons = []
       for k in range(256):
           texto = bytes(b ^ k for b in grupo)
           if all(32 <= c < 127 for c in texto):
               bons.append(k)
       return bons

   for pos in range(3):
       grupo = dados[pos::3]
       print(pos, candidatos(grupo))
   ```

3. Cada posição tem só um candidato razoável. A chave encontrada é `b"khe"`.
4. Decifre o arquivo inteiro:

   ```python
   chave = b"khe"
   texto = bytes(b ^ chave[i % 3] for i, b in enumerate(dados))
   print(texto.decode())
   ```

## Flag

```
khoade{xor_nao_e_criptografia_de_verdade}
```

(o texto original só tinha letras minúsculas, então a flag também sai em minúsculas — o verificador não diferencia maiúsculas de minúsculas)
