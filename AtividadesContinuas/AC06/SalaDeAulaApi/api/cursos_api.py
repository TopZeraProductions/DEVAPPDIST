from flask import Blueprint, jsonify, request
from services.cursos_dao import CursosServices

cursos_app = Blueprint('cursos_app', __name__, template_folder='templates')


@cursos_app.route('/cursos', methods=['GET'])
def listar():
    post_list = CursosServices.list_all()
    return jsonify(list(map(lambda x: x.to_dictionary(), post_list)))


@cursos_app.route('/cursos/<int:id>', methods=['GET'])
def localiza(id: int) -> str:
    obj = CursosServices.find(id)

    return jsonify(obj.to_dictionary())


@cursos_app.route('/cursos', methods=['POST'])
def novo():
    novo_registro = request.get_json()

    post_list = CursosServices.new(novo_registro)

    return jsonify(list(map(lambda x: x.to_dictionary(), post_list)))


@cursos_app.route('/cursos/<int:id>', methods=['DELETE'])
def remover(id):
    post_list = CursosServices.delete(id)

    return jsonify(list(map(lambda x: x.to_dictionary(), post_list)))


@cursos_app.route('/cursos/<int:id>', methods=['PUT'])
def atualiza(id):
    data = request.get_json()
    data['id'] = id

    post_list = CursosServices.update(data)

    return jsonify(list(map(lambda x: x.to_dictionary(), post_list)))
