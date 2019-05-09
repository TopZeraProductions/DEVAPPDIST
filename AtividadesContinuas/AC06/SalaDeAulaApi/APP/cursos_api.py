from flask import Blueprint, jsonify, request
from BLL.curso.services.curso_services import CursoServices

cursos_app = Blueprint('cursos_app', __name__, template_folder='templates')


@cursos_app.route('/cursos', methods=['GET'])
def listar():
    post_list = CursoServices.list_all()
    return jsonify(list(map(lambda x: x.to_dictionary(), post_list)))


@cursos_app.route('/cursos/<int:id>', methods=['GET'])
def localiza(id: int) -> str:
    obj = CursoServices.find(id)

    return jsonify(obj.to_dictionary())


@cursos_app.route('/cursos', methods=['POST'])
def novo():
    novo_registro = request.get_json()
    pr_list = []
    if type(novo_registro) is list:
        for element in novo_registro:
            pr_list = CursoServices.new(element)
    else:
        pr_list = CursoServices.new(novo_registro)

    return jsonify(list(map(lambda pr: pr.to_dictionary(), pr_list)))


@cursos_app.route('/cursos/<int:id>', methods=['DELETE'])
def remover(id):
    post_list = CursoServices.delete(id)

    return jsonify(list(map(lambda x: x.to_dictionary(), post_list)))


@cursos_app.route('/cursos/<int:id>', methods=['PUT'])
def atualiza(id):
    data = request.get_json()
    data['id'] = id

    post_list = CursoServices.update(data)

    return jsonify(list(map(lambda x: x.to_dictionary(), post_list)))
