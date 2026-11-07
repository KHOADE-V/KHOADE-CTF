"""Confere se a flag enviada é a flag certa de um desafio.

Uso: python3 scripts/verificar_flag.py <pasta-do-desafio> "KHOADE{...}"
Exemplo: python3 scripts/verificar_flag.py 01-cripto-cesar "KHOADE{cesar_e_so_o_comeco}"
"""

import sys

FLAGS = {
    "01-cripto-cesar": "KHOADE{cesar_e_so_o_comeco}",
    "02-cripto-xor": "khoade{xor_nao_e_criptografia_de_verdade}",
    "03-web-login-fraco": "KHOADE{comparar_senha_char_a_char_vaza_tempo}",
    "04-esteganografia": "KHOADE{quem_olha_so_ve_um_poema_comum}",
}


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 1
    desafio, flag_enviada = argv[1], argv[2]
    if desafio not in FLAGS:
        print(f"desafio desconhecido: {desafio}")
        print("desafios disponíveis:", ", ".join(sorted(FLAGS)))
        return 1
    if flag_enviada.strip().lower() == FLAGS[desafio].lower():
        print("Flag correta! 🚩")
        return 0
    print("Flag incorreta. Tente de novo.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
