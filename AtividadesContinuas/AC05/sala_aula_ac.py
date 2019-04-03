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
    ]
}


@app.route("/")  # Root
def all():
    return jsonify(database)


@app.route("/alunos", methods=['GET'])  # Metodo de consulta geral
def listar_aluno():
    return jsonify(database["ALUNOS"])
# OK


@app.route("/alunos/<int:id_aluno>", methods=['GET'])  # Metodo de consulta Por id
def carregar_aluno(id_aluno):
    for aluno in database['ALUNOS']:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)

    return 'erro, Registro nao encontrado', 404
# OK


@app.route("/alunos", methods=['POST'])  # Metodo de Cadastro de novos alunos
def cadastrar_aluno():
    novo_aluno = request.get_json()
    database["ALUNOS"].append(novo_aluno)

    return jsonify(database["ALUNOS"])
# OK


@app.route("/alunos/<int:id_aluno>", methods=['DELETE'])  # Metodo de exclusao os registro
def deletar_aluno(id_aluno):
    for index, aluno in enumerate(database['ALUNOS']):
        print(index, aluno)
        if aluno['id'] == id_aluno:
            database['ALUNOS'].pop(index)

            return jsonify(database["ALUNOS"])

    return 'erro, Registro nao encontrado', 404
# OK


@app.route("/alunos/<int:id_aluno>", methods=['PUT'])  # Metodo de Atualizacao um aluno existente
def atualizar_aluno(id_aluno):
    update_aluno = request.get_json()

    for index, aluno in enumerate(database['ALUNOS']):
        print(index, aluno)
        if aluno['id'] == id_aluno:
            database['ALUNOS'].pop(index)
            database["ALUNOS"].append(update_aluno)

            return jsonify(database["ALUNOS"])

    return 'erro, Registro nao encontrado', 404

# OK


if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True,
        host="localhost"
    )
