from flask import Flask, jsonify, request

app = Flask(__name__)

database = {
    "ALUNOS": [
        {
            "id": 1,
            "nome": "Tiago beneteli",
            "idSalaAula": 1
        },
        {
            "id": 2,
            "nome": "Daniel rodrigues",
            "idSalaAula": 1
        },
        {
            "id": 3,
            "nome": "Joao vitor paulino martins",
            "idSalaAula": 1
        },
        {
            "id": 4,
            "nome": "Ramon cavalcanti",
            "idSalaAula": 1
        },
        {
            "id": 5,
            "nome": "Tiago",
            "idSalaAula": 1
        },
        {
            "id": 6,
            "nome": "Adamastor",
            "idSalaAula": 1
        },
        {
            "id": 7,
            "nome": "Felipe azevedo",
            "idSalaAula": 1
        },
        {
            "id": 8,
            "nome": "Rodrigo mota",
            "idSalaAula": 1
        },
        {
            "id": 9,
            "nome": "Rogerio senni",
            "idSalaAula": 1
        },
        {
            "id": 10,
            "nome": "Conect cut",
            "idSalaAula": 1
        },
    ],
    "DISCIPLINAS": [
        {
            "id": 1,
            "nome": "matematica"
        },
        {
            "id": 2,
            "nome": "historia"
        },
        {
            "id": 3,
            "nome": "geografia"
        },
        {
            "id": 4,
            "nome": "biologia"
        },
    ],
    "PROFESSORES": [
        {
            "id": 1,
            "nome": "pr. Jose henrique"
        },
        {
            "id": 2,
            "nome": "dr. joao lacerda "
        },
        {
            "id": 3,
            "nome": "ms. ricardo felipe coutinho"
        },
        {
            "id": 4,
            "nome": "pr. adamstor de souza"
        },
    ],
    "SALA_AULA": [
        {
            "numSala": 12,
            "turma": "B",
            "semestre": "1",
            "idProfessor": 1,
            "idDisciplina": 1
        }
    ]
}


@app.route("/")  # http://localhost:5080/
def all():  # lista geral de alunos
    return jsonify(database)


@app.route("/alunos", methods=['GET'])  # http://localhost:5080/alunos
def listar_aluno():  # Metodo de consulta geral
    return jsonify(database["ALUNOS"])
# OK


@app.route("/alunos/<int:id_aluno>", methods=['GET'])  # http://localhost:5080/alunos/1
def carregar_aluno(id_aluno):  # Metodo de consulta Por id
    for aluno in database['ALUNOS']:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)

    return 'erro, Registro nao encontrado', 404
# OK


@app.route("/alunos", methods=['POST'])  # http://localhost:5080/alunos
def cadastrar_aluno():  # Metodo de Cadastro de novos alunos
    novo_aluno = request.get_json()
    database["ALUNOS"].append(novo_aluno)

    return jsonify(database["ALUNOS"])
# OK


@app.route("/alunos/<int:id_aluno>", methods=['DELETE'])  # http://localhost:5080/alunos/<int:id_aluno>
def deletar_aluno(id_aluno):  # Metodo de exclusao os registro
    for index, aluno in enumerate(database['ALUNOS']):
        print(index, aluno)
        if aluno['id'] == id_aluno:
            database['ALUNOS'].pop(index)

            return jsonify(database["ALUNOS"])

    return 'erro, Registro nao encontrado', 404
# OK


@app.route("/alunos/<int:id_aluno>", methods=['PUT'])  # http://localhost:5080/alunos/1
def atualizar_aluno(id_aluno):  # Metodo de Atualizacao um aluno existente
    update_aluno = request.get_json()

    for index, aluno in enumerate(database['ALUNOS']):
        print(index, aluno)
        if aluno['id'] == id_aluno:
            database['ALUNOS'].pop(index)
            database["ALUNOS"].append(update_aluno)

            return jsonify(database["ALUNOS"])

    return 'erro, Registro nao encontrado', 404

# OK


@app.route("/alunos/relatorio", methods=['GET'])  # http:///alunos/relatorio
def reatorio_alunos():  # Metodo de Atualizacao um aluno existente
    lista_alunos = []

    for aluno in database["ALUNOS"]:
        aluno["sala"] = database["SALA_AULA"][aluno["idSalaAula"]-1]["numSala"]
        database["SALA_AULA"]

        aluno["professor"] = database["PROFESSORES"][]["numSala"]

        lista_alunos.append(aluno)

    return jsonify(lista_alunos), 200

# OK


if __name__ == '__main__':
    app.run(
        port=5080,
        debug=True,
        host="localhost"
    )
