from flask import Flask, request,jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/soma", methods = ["GET"])
def soma():
    valor1 = float(input(request.args.get("valor1",5)))
    valor2 = float(input(request.args.get("valor1",6)))
    resultado = valor1 + valor2
    return jsonify({"continha": "soma", "resultado": resultado})

@app.route("/subtração", methods = ["GET"])
def subtração():
    valor1 = float(input(request.args.get("valor1",5)))
    valor2 = float(input(request.args.get("valor2",6)))
    resultado = valor1 - valor2
    return jsonify({"continha": "subtração", "resultado": resultado})

@app.route("/multiplicação", methods = ["GET"])
def multiplicação():
    valor1 = float(input(request.args.get("valor1",5)))
    valor2 = float(input(request.args.get("valor1",6)))
    resultado = valor1 * valor2
    return jsonify({"continha": "multiplicação", "resultado": resultado})

@app.route("/divisão", methods = ["GET"])
def divisão():
    valor1 = float(input(request.args.get("valor1",5)))
    valor2 = float(input(request.args.get("valor1",6)))
    resultado = valor1 / valor2
    return jsonify({"continha": "divisão", "resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True)