from flask import Flask, render_template, request, redirect

app = Flask(__name__)
contas = [] 

@app.route('/', methods=["GET", "POST"])
def create():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        contas.append({"nome": nome, "email": email})
        return redirect('/')
    return render_template("index.html", contas=contas)

@app.route('/alterar', methods=["POST"])
def update():
    nome = request.form["nome"]
    email = request.form["email"]
    new_name = request.form["new_name"]
    new_email = request.form["new_email"]

    for conta in contas:
        if conta["nome"] == nome and conta["email"] == email:
            conta["nome"] = new_name
            conta["email"] = new_email
            break

    return render_template("alterar.html", contas=contas)

@app.route('/deletar', methods=["POST"])
def delete():
    nome = request.form["name"]
    email = request.form["email"]

    contas[:] = [conta for conta in contas if not (conta["nome"] == nome and conta["email"] == email)]

    return render_template("excluir.html", contas=contas)

if __name__ == "__main__":
    app.run(debug=True)
