from flask import Blueprint, jsonify, request
from Services.disciplina.services.disciplina_services import DisciplinaServices

disciplinas_app = Blueprint('disciplinas_app', __name__, template_folder='templates')


@disciplinas_app.route('/disciplinas', methods=['GET'])
def listar():
    post_list = DisciplinaServices.list_all()
    return jsonify(post_list)


@disciplinas_app.route('/disciplinas/<int:id>', methods=['GET'])
def localiza(id: int) -> str:
    obj = DisciplinaServices.find(id)

    return jsonify(obj.to_dictionary())


@disciplinas_app.route('/disciplinas', methods=['POST'])
def novo():
    novo_registro = request.get_json()
    pr_list = []
    if type(novo_registro) is list:
        for element in novo_registro:
            pr_list = DisciplinaServices.new(element)
    else:
        pr_list = DisciplinaServices.new(novo_registro)

    return jsonify(list(map(lambda pr: pr.to_dictionary(), pr_list)))


@disciplinas_app.route('/disciplinas/<int:id>', methods=['DELETE'])
def remover(id):
    post_list = DisciplinaServices.delete(id)

    return jsonify(list(map(lambda x: x.to_dictionary(), post_list)))


@disciplinas_app.route('/disciplinas/<int:id>', methods=['PUT'])
def atualiza(id):
    data = request.get_json()
    data['id'] = id

    post_list = DisciplinaServices.update(data)

    return jsonify(list(map(lambda x: x.to_dictionary(), post_list)))
