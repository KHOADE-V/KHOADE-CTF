"""Testes que garantem que cada desafio é resolvível com a solução documentada."""

import importlib.util
import string
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from verificar_flag import FLAGS, main as verificar_main  # noqa: E402


class CesarTests(unittest.TestCase):
    def test_decifra_e_encontra_flag(self):
        alfabeto = string.ascii_lowercase
        texto = (ROOT / "challenges/01-cripto-cesar/cifrado.txt").read_text(encoding="utf-8")

        def decifrar(texto, deslocamento):
            resultado = []
            for ch in texto:
                if ch.lower() in alfabeto:
                    i = alfabeto.index(ch.lower())
                    nova = alfabeto[(i - deslocamento) % 26]
                    resultado.append(nova.upper() if ch.isupper() else nova)
                else:
                    resultado.append(ch)
            return "".join(resultado)

        decifrado = decifrar(texto, 7)
        self.assertIn(FLAGS["01-cripto-cesar"], decifrado)


class XorTests(unittest.TestCase):
    def test_decifra_com_a_chave_documentada(self):
        dados = (ROOT / "challenges/02-cripto-xor/cifrado.bin").read_bytes()
        chave = b"khe"
        texto = bytes(b ^ chave[i % 3] for i, b in enumerate(dados)).decode("ascii")
        self.assertIn(FLAGS["02-cripto-xor"], texto)


class SteganografiaTests(unittest.TestCase):
    def test_extrai_mensagem_escondida(self):
        linhas = (ROOT / "challenges/04-esteganografia/poema.txt").read_bytes().split(b"\n")
        mensagem = []
        for linha in linhas:
            marcador = bytes(b for b in linha if b in (0x20, 0x09))[-8:]
            if len(marcador) != 8:
                continue
            bits = "".join("1" if b == 0x09 else "0" for b in marcador)
            mensagem.append(chr(int(bits, 2)))
        self.assertIn(FLAGS["04-esteganografia"], "".join(mensagem))


class VerificadorTests(unittest.TestCase):
    def test_aceita_flag_certa(self):
        self.assertEqual(
            verificar_main(["_", "01-cripto-cesar", FLAGS["01-cripto-cesar"]]), 0
        )

    def test_rejeita_flag_errada(self):
        self.assertEqual(verificar_main(["_", "01-cripto-cesar", "KHOADE{errado}"]), 1)

    def test_desafio_desconhecido(self):
        self.assertEqual(verificar_main(["_", "99-nao-existe", "KHOADE{x}"]), 1)

    def test_aceita_sem_diferenciar_maiusculas(self):
        self.assertEqual(
            verificar_main(["_", "02-cripto-xor", FLAGS["02-cripto-xor"].upper()]), 0
        )


if __name__ == "__main__":
    unittest.main()
