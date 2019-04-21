from flask import Blueprint, jsonify, request
alunos_app = Blueprint('alunos_app', __name__, template_folder='templates')
alunos_db = []

@alunos_app.route('/alunos', methods=['GET'])
def listar():
    return jsonify(alunos_db)

@alunos_app.route('/alunos/<int:id_aluno>', methods=['GET'])
def localiza(id_aluno):
    for aluno in alunos_db:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)
    return '', 404

@alunos_app.route('/alunos', methods=['POST'])
def novo():
    novo_aluno = request.get_json()
    alunos_db.append(novo_aluno)
    return jsonify(alunos_db)

@alunos_app.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def remover(id_aluno):
    index = 0
    for aluno in alunos_db:
        if aluno['id'] == id_aluno:
            del alunos_db[index]
            return jsonify(aluno)
        index = index + 1
    return '', 404

@alunos_app.route('/alunos/<int:id_aluno>', methods=['PUT'])
def atualiza(id_aluno):
    novo_aluno = request.get_json()
    index = 0
    for aluno in alunos_db:
        if aluno['id'] == id_aluno:
            del alunos_db[index]
            alunos_db.append(novo_aluno)
            return jsonify(aluno)
        index = index + 1
    return '', 404