from flask import Blueprint, jsonify, request
from services.alunos_service import alunos_db, \
    listar as service_listar, \
    localiza as service_localiza, \
    novo as service_novo, \
    remover as service_remover, \
    atualiza as service_atualiza

alunos_app = Blueprint('alunos_app', __name__, template_folder='templates')


@alunos_app.route('/alunos', methods=['GET'])
def listar():
    pr_list = service_listar()
    return jsonify(list(map(lambda pr: pr.__dict__(), pr_list)))


@alunos_app.route('/alunos/<int:id>', methods=['GET'])
def localiza(id):
    p = service_localiza(id)
    if(p != None):
        return jsonify(p.__dict__())
    return '', 404


@alunos_app.route('/alunos', methods=['POST'])
def novo():
    novo_aluno = request.get_json()
    pr_list = service_novo(novo_aluno)
    if pr_list == None:
        return 'Esse cadastro já existe', 400
    return jsonify(list(map(lambda pr: pr.__dict__(), pr_list)))


@alunos_app.route('/alunos/<int:id>', methods=['DELETE'])
def remover(id):
    removido = service_remover(id)
    if removido != None:
        return jsonify(removido.__dict__())
    return '', 404


@alunos_app.route('/alunos/<int:id>', methods=['PUT'])
def atualiza(id):
    aluno_data = request.get_json()
    removido = service_atualiza(id, aluno_data)
    if removido != None:
        return jsonify(removido.__dict__())
    return '', 404
