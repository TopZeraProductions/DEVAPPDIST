from flask import Blueprint, jsonify, request
from services.disciplinasOfertadas_service import disciplinasOfertadas_db, \
     listar as service_listar, \
     localiza as service_localiza, \
     novo as service_novo, \
     remover as service_remover, \
     atualiza as service_atualiza

disciplinasOfertadas_app = Blueprint('disciplinasOfertadas_app', __name__, template_folder='templates')


@disciplinasOfertadas_app.route('/disciplinasOfertadas', methods=['GET'])
def listar():
    pr_list = service_listar()
    return jsonify(list(map(lambda pr: pr.__dict__(), pr_list)))


@disciplinasOfertadas_app.route('/disciplinasOfertadas/<int:id>', methods=['GET'])
def localiza(id):
    p = service_localiza(id)
    if p is not None:
        return jsonify(p.__dict__())
    return '', 404


@disciplinasOfertadas_app.route('/disciplinasOfertadas', methods=['POST'])
def novo():
    nova_disciplinaOfertada = request.get_json()
    pr_list = service_novo(nova_disciplinaOfertada)
    if pr_list is None:
        return 'Esse cadastro já existe', 400
    return jsonify(list(map(lambda pr: pr.__dict__(), pr_list)))


@disciplinasOfertadas_app.route('/disciplinasOfertadas/<int:id>', methods=['DELETE'])
def remover(id):
    removido = service_remover(id)
    if removido is not None:
        return jsonify(removido.__dict__())
    return '', 404


@disciplinasOfertadas_app.route('/disciplinasOfertadas/<int:id>', methods=['PUT'])
def atualiza(id):
    disciplinaOfertada_data = request.get_json()
    removido = service_atualiza(id, disciplinaOfertada_data)
    if removido is not None:
        return jsonify(removido.__dict__())
    return '', 404