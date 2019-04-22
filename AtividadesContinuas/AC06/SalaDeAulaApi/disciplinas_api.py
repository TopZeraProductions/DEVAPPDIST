from flask import Blueprint, jsonify, request
from services.disciplinas_service import disciplinas_db, \
     listar as service_listar, \
     localiza as service_localiza, \
     novo as service_novo, \
     remover as service_remover, \
     atualiza as service_atualiza

disciplinas_app = Blueprint('disciplinas_app', __name__, template_folder='templates')


@disciplinas_app.route('/disciplinas', methods=['GET'])
def listar():
    pr_list = service_listar()
    return jsonify(list(map(lambda pr: pr.__dict__(), pr_list)))


@disciplinas_app.route('/disciplinas/<int:id>', methods=['GET'])
def localiza(id):
    p = service_localiza(id)
    if p is not None:
        return jsonify(p.__dict__())
    return '', 404


@disciplinas_app.route('/disciplinas', methods=['POST'])
def novo():
    nova_disciplina = request.get_json()
    pr_list = service_novo(nova_disciplina)
    if pr_list is None:
        return 'Esse cadastro já existe', 400
    return jsonify(list(map(lambda pr: pr.__dict__(), pr_list)))


@disciplinas_app.route('/disciplinas/<int:id>', methods=['DELETE'])
def remover(id):
    removido = service_remover(id)
    if removido is not None:
        return jsonify(removido.__dict__())
    return '', 404


@disciplinas_app.route('/disciplinas/<int:id>', methods=['PUT'])
def atualiza(id):
    disciplina_data = request.get_json()
    removido = service_atualiza(id, disciplina_data)
    if removido is not None:
        return jsonify(removido.__dict__())
    return '', 404
