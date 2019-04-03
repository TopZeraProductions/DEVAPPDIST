from flask import Flask, jsonify, request

app = Flask(__name__)

database = {
    "ALUNOS": [
        {
            "id": 1,
            "nome": "Tiago beneteli"
        },
        {
            "id": 2,
            "nome": "Daniel rodrigues"
        },
        {
            "id": 3,
            "nome": "Joao vitor paulino martins"
        },
        {
            "id": 4,
            "nome": "Ramon cavalcanti"
        },
    ],
    "PROFESSORES": [
        {
            "nome": "Tiago",
            "matricula": 123456
        },
        {
            "matricula": 123456,
            "nome": "Daniel"
        },
        {
            "matricula": 123456,
            "nome": "Joao"
        },
        {
            "matricula": 123456,
            "nome": "Ramon "
        },
    ]
}


@app.route("/")
def all():
    return jsonify(database)


@app.route("/alunos")
def listar_alunos():
    return jsonify(database["ALUNOS"])


@app.route("/alunos", methods=['POST'])
def novo_aluno():
    novo_aluno = request.get_json()
    database["ALUNOS"].append(novo_aluno)

    return jsonify(database["ALUNOS"])


@app.route("/alunos/<int:id_aluno>", methods=['GET'])
def localiza_aluno(id_aluno):
    for aluno in database['ALUNOS']:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)

    return 'erro', 404


@app.route("/professor")
def listar_professores():
    return jsonify(database["PROFESSORES"])


if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True,
        host="localhost"
    )
