from flask import Flask, request
import random

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>" \
           "    <strong>Hello World<strong>" \
           "</h1>"


@app.route("/auth/login", methods=['GET', 'POST'])
def login_page():
    html = "<label>Seu nome arrombot.</label><br />"
    html += "<input type=\"text\" placeholder=\"Digite seu login fdp\" /><br />"
    html += "<label>Agora a senha viado.</label><br />"
    html += "<input type=\"password\" placeholder=\"Digite seu login fdp\" /><br />"
    html += "<button>Envia essa porra agora</button> <br />"

    return html


@app.route("/calculadoradeviadage", methods=['GET', 'POST'])
def calculadora_viadage():
    num = random.randint(0, 100)

    html = f"<h1>Voce eh {num}% boiola</h1><br />"

    return html


@app.route("/calculadoradeviadagenome/<string:nome>", methods=['GET', 'POST'])
def calculadora_viadagep(nome):
    num = random.randint(0, 100)

    html = f"<h1>O {nome} eh {num}% boiola</h1><br />"

    return html


@app.route("/calculadora/<int:num1>&<int:num2>", methods=['GET', 'POST'])
def calculadora(num1, num2):
    html = f"<h1>{num1} + {num2} = {num1 + num2} </h1><br />"

    return html


@app.route('/calculadoramulti', methods=['GET', 'POST'])
def calculadora_multi():
    num1 = int(request.args.get('num1'))
    html = ""
    for i in range(0, 11):
        html += f"<strong>{num1} + {i} = {num1 * i} <strong><br />"

    return html


if __name__ == '__main__':
    app.run(
        port=5080,
        debug=True,
        host="localhost"
    )
