from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacao = request.form["operacao"]

            if operacao == "/" and num2 == 0:
                resultado = "Erro: Divisão por zero!"
            else:
                resultado = eval(f"{num1} {operacao} {num2}")

        except ValueError:
            resultado = "Erro: Entrada inválida!"

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)