# KHOADE CTF

Desafios de segurança da informação para estudar na prática, no estilo CTF (*Capture The Flag*). Cada desafio é independente, autocontido e roda só na sua máquina — nenhum deles ataca serviços reais.

## Como jogar

1. Entre na pasta do desafio e leia o `desafio.md`.
2. Resolva e encontre a *flag*, sempre no formato `KHOADE{...}`.
3. Confira sua resposta:

   ```bash
   python3 scripts/verificar_flag.py 01-cripto-cesar "KHOADE{sua_resposta}"
   ```

4. Travou? Cada pasta tem um `solucao.md` com o passo a passo. Tente sem olhar primeiro — é mais divertido.

## Desafios

| Pasta | Categoria | Dificuldade |
| --- | --- | --- |
| [01-cripto-cesar](challenges/01-cripto-cesar/desafio.md) | Criptografia | Iniciante |
| [02-cripto-xor](challenges/02-cripto-xor/desafio.md) | Criptografia | Iniciante |
| [03-web-login-fraco](challenges/03-web-login-fraco/desafio.md) | Segurança web | Intermediário |
| [04-esteganografia](challenges/04-esteganografia/desafio.md) | Esteganografia | Iniciante |

## Sobre o desafio web

O `03-web-login-fraco` sobe um servidor Flask **só na sua máquina** (`127.0.0.1`), criado para este desafio. Ele contém de propósito uma falha comum de autenticação, para você encontrar e entender — não é uma ferramenta de ataque, e não deve ser exposto na internet.

## Licença

Conteúdo e código sob MIT — veja `LICENSE`.
