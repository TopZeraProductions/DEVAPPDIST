from flask import Blueprint, jsonify, request
from services.cursos_service import cursos_db, \
     listar as service_listar, \
     localiza as service_localiza, \
     novo as service_novo, \
     remover as service_remover, \
     atualiza as service_atualiza

cursos_app = Blueprint('cursos_app', __name__, template_folder='templates')


@cursos_app.route('/cursos', methods=['GET'])
def listar():
    pr_list = service_listar()
    return jsonify(list(map(lambda pr: pr.__dict__(), pr_list)))


@cursos_app.route('/cursos/<int:id>', methods=['GET'])
def localiza(id):
    p = service_localiza(id)
    if p is not None:
        return jsonify(p.__dict__())
    return '', 404


@cursos_app.route('/cursos', methods=['POST'])
def novo():
    novo_curso = request.get_json()
    pr_list = service_novo(novo_curso)
    if pr_list is None:
        return 'Esse cadastro já existe', 400
    return jsonify(list(map(lambda pr: pr.__dict__(), pr_list)))


@cursos_app.route('/cursos/<int:id>', methods=['DELETE'])
def remover(id):
    removido = service_remover(id)
    if removido is None:
        return jsonify(removido.__dict__())
    return '', 404


@cursos_app.route('/cursos/<int:id>', methods=['PUT'])
def atualiza(id):
    curso_data = request.get_json()
    removido = service_atualiza(id, curso_data)
    if removido is not None:
        return jsonify(removido.__dict__())
    return '', 404
