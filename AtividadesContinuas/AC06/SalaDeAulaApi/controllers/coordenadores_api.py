from flask import Blueprint, jsonify, request
from services.coordenadores_service import coordenadores_db, \
     listar as service_listar, \
     localiza as service_localiza, \
     novo as service_novo, \
     remover as service_remover, \
     atualiza as service_atualiza

coordenadores_app = Blueprint('coordenadores_app', __name__, template_folder='templates')


@coordenadores_app.route('/coordenadores', methods=['GET'])
def listar():
    pr_list = service_listar()
    return jsonify(list(map(lambda pr: pr.__dict__(), pr_list)))


@coordenadores_app.route('/coordenadores/<int:id>', methods=['GET'])
def localiza(id):
    p = service_localiza(id)
    if p is not None:
        return jsonify(p.__dict__())
    return '', 404


@coordenadores_app.route('/coordenadores', methods=['POST'])
def novo():
    novo_coordenador = request.get_json()
    pr_list = service_novo(novo_coordenador)
    if pr_list is None:
        return 'Esse cadastro já existe', 400
    return jsonify(list(map(lambda pr: pr.__dict__(), pr_list)))


@coordenadores_app.route('/coordenadores/<int:id>', methods=['DELETE'])
def remover(id):
    removido = service_remover(id)
    if removido is not None:
        return jsonify(removido.__dict__())
    return '', 404


@coordenadores_app.route('/coordenadores/<int:id>', methods=['PUT'])
def atualiza(id):
    coordenador_data = request.get_json()
    removido = service_atualiza(id, coordenador_data)
    if removido is not None:
        return jsonify(removido.__dict__())
    return '', 404
