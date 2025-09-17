from flask import Flask, render_template, request, redirect, url_for
from controller import BibliotecaController

app = Flask(__name__)
controller = BibliotecaController()

@app.route("/")
def index():
    disponiveis = controller.obter_disponiveis()
    emprestados = controller.obter_emprestados()
    return render_template("index.html", disponiveis=disponiveis, emprestados=emprestados)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    nome = request.form["nome"]
    autor = request.form["autor"]
    edicao = request.form["edicao"]
    categoria = request.form["categoria"]
    controller.adicionar_item(categoria, nome, autor, edicao)  # corrigido
    return redirect(url_for("index"))

@app.route("/remover/<int:indice>", methods=["POST"])
def remover(indice):
    controller.remover_item(indice)
    return redirect(url_for("index"))

@app.route("/emprestar/<int:indice>", methods=["POST"])
def emprestar(indice):
    dias = int(request.form.get("dias", 7))
    controller.emprestar_item(indice, dias)
    return redirect(url_for("index"))

@app.route("/devolver/<int:indice>", methods=["POST"])
def devolver(indice):
    controller.devolver_item(indice)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
