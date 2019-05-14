from flask import Blueprint, jsonify, request
from Services.disciplinaOfertada.services.disciplinaOfertada_services import DisciplinaOfertadaServices

disciplinasOfertadas_app = Blueprint('disciplinasOfertadas_app', __name__, template_folder='templates')


@disciplinasOfertadas_app.route('/disciplinasofertadas', methods=['GET'])
def listar():
    post_list = DisciplinaOfertadaServices.list_all()
    return jsonify(post_list)


@disciplinasOfertadas_app.route('/disciplinasofertadas/<int:id>', methods=['GET'])
def localiza(id: int) -> str:
    obj = DisciplinaOfertadaServices.find(id)

    return jsonify(obj.to_dictionary())


@disciplinasOfertadas_app.route('/disciplinasofertadas', methods=['POST'])
def novo():
    novo_registro = request.get_json()
    pr_list = []
    if type(novo_registro) is list:
        for element in novo_registro:
            pr_list = DisciplinaOfertadaServices.new(element)
    else:
        pr_list = DisciplinaOfertadaServices.new(novo_registro)

    return jsonify(list(map(lambda pr: pr.to_dictionary(), pr_list)))


@disciplinasOfertadas_app.route('/disciplinasofertadas/<int:id>', methods=['DELETE'])
def remover(id):
    post_list = DisciplinaOfertadaServices.delete(id)

    return jsonify(list(map(lambda x: x.to_dictionary(), post_list)))


@disciplinasOfertadas_app.route('/disciplinasofertadas/<int:id>', methods=['PUT'])
def atualiza(id):
    data = request.get_json()
    data['id'] = id

    post_list = DisciplinaOfertadaServices.update(data)

    return jsonify(list(map(lambda x: x.to_dictionary(), post_list)))
