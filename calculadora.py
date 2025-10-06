from flask import Flask,request, render_template

app = Flask(__name__)

numeros = [
   {"valor1":5}
   {"valor2":6}
]

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/valores", methods=["GET"])
def get_valores():
    request.args.get("valor1")
