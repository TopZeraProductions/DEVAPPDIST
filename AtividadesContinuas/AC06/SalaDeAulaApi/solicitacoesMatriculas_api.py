from flask import Blueprint, jsonify, request
from services.solicitacoesMatriculas_service import solicitacoesMatriculas_db, \
    listar as service_listar, \
    localiza as service_localiza, \
    novo as service_novo, \
    remover as service_remover, \
    atualiza as service_atualiza

solicitacoesMatriculas_app = Blueprint('solicitacoesMatriculas_app', __name__, template_folder='templates')


@solicitacoesMatriculas_app.route('/solicitacoesMatriculas', methods=['GET'])
def listar():
    pr_list = service_listar()
    return jsonify(list(map(lambda pr: pr.__dict__(), pr_list)))


@solicitacoesMatriculas_app.route('/solicitacoesMatriculas/<int:id>', methods=['GET'])
def localiza(id):
    p = service_localiza(id)
    if p is not None:
        return jsonify(p.__dict__())
    return '', 404


@solicitacoesMatriculas_app.route('/solicitacoesMatriculas', methods=['POST'])
def novo():
    nova_solicitacaoMatricula = request.get_json()
    pr_list = service_novo(nova_solicitacaoMatricula)
    if pr_list is None:
        return 'Esse cadastro já existe', 400
    return jsonify(list(map(lambda pr: pr.__dict__(), pr_list)))


@solicitacoesMatriculas_app.route('/solicitacoesMatriculas/<int:id>', methods=['DELETE'])
def remover(id):
    removido = service_remover(id)
    if removido is not None:
        return jsonify(removido.__dict__())
    return '', 404


@solicitacoesMatriculas_app.route('/solicitacoesMatriculas/<int:id>', methods=['PUT'])
def atualiza(id):
    solicitacaoMatricula_data = request.get_json()
    removido = service_atualiza(id, solicitacaoMatricula_data)
    if removido is not None:
        return jsonify(removido.__dict__())
    return '', 404
