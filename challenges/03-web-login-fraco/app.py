"""Alvo do desafio 03: uma tela de login com uma falha de propósito.

Roda só em 127.0.0.1, para fins didáticos. Não exponha na internet.

A falha: a senha é comparada caractere por caractere com `==`, parando no
primeiro que for diferente. Isso faz a resposta demorar um pouco mais quanto
mais caracteres do início estiverem corretos — um "ataque de timing" clássico.
Uma implementação correta usa `hmac.compare_digest`, que sempre leva o mesmo
tempo, não importa onde a senha esteja errada.
"""

import time

from flask import Flask, redirect, render_template_string, request, url_for

app = Flask(__name__)

USUARIOS = {"admin": "tr0p1c0-s3gur0"}
ATRASO_POR_ACERTO = 0.03  # segundos "gastos" a mais por caractere certo

PAGINA_LOGIN = """
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Login fraco</title></head><body style="font-family: sans-serif; max-width: 420px; margin: 60px auto;">
<h1>Área interna</h1>
<form method="post">
  <label>Usuário<br><input name="usuario" value="admin"></label><br><br>
  <label>Senha<br><input name="senha" type="password"></label><br><br>
  <button type="submit">Entrar</button>
</form>
{% if erro %}<p style="color:#b00">{{ erro }}</p>{% endif %}
</body></html>
"""

PAGINA_SUCESSO = """
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Bem-vindo</title></head><body style="font-family: sans-serif; max-width: 420px; margin: 60px auto;">
<h1>Bem-vindo, admin!</h1>
<p>Você entrou. A flag é:</p>
<p style="font-family: monospace; font-size: 1.1rem;">KHOADE{comparar_senha_char_a_char_vaza_tempo}</p>
<p><a href="/">Sair</a></p>
</body></html>
"""


def senha_confere_de_forma_insegura(enviada, correta):
    """Comparação propositalmente fraca: vulnerável a ataque de timing."""
    if len(enviada) != len(correta):
        return False
    for a, b in zip(enviada, correta):
        if a != b:
            return False
        time.sleep(ATRASO_POR_ACERTO)  # simula um custo real por caractere certo
    return True


@app.route("/", methods=["GET", "POST"])
def login():
    erro = None
    if request.method == "POST":
        usuario = request.form.get("usuario", "")
        senha = request.form.get("senha", "")
        correta = USUARIOS.get(usuario)
        if correta is not None and senha_confere_de_forma_insegura(senha, correta):
            return redirect(url_for("sucesso"))
        erro = "Usuário ou senha incorretos."
    return render_template_string(PAGINA_LOGIN, erro=erro)


@app.route("/sucesso")
def sucesso():
    return render_template_string(PAGINA_SUCESSO)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050)
