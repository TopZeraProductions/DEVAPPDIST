from flask import Blueprint, jsonify, request
from Services.solicitacaoMatricula.services.solicitacaoMatricula_services import SolicitacaoMatriculaServices

solicitacoesMatriculas_app = Blueprint('solicitacoesMatriculas_app', __name__, template_folder='templates')


@solicitacoesMatriculas_app.route('/solicitacoesMatriculas', methods=['GET'])
def listar():
    post_list = SolicitacaoMatriculaServices.list_all()
    return jsonify(post_list)


@solicitacoesMatriculas_app.route('/solicitacoesMatriculas/<int:id>', methods=['GET'])
def localiza(id: int) -> str:
    obj = SolicitacaoMatriculaServices.find(id)

    return jsonify(obj.to_dictionary())


@solicitacoesMatriculas_app.route('/solicitacoesMatriculas', methods=['POST'])
def novo():
    novo_registro = request.get_json()
    pr_list = []
    if type(novo_registro) is list:
        for element in novo_registro:
            pr_list = SolicitacaoMatriculaServices.new(element)
    else:
        pr_list = SolicitacaoMatriculaServices.new(novo_registro)

    return jsonify(list(map(lambda pr: pr.to_dictionary(), pr_list)))


@solicitacoesMatriculas_app.route('/solicitacoesMatriculas/<int:id>', methods=['DELETE'])
def remover(id):
    post_list = SolicitacaoMatriculaServices.delete(id)

    return jsonify(list(map(lambda x: x.to_dictionary(), post_list)))


@solicitacoesMatriculas_app.route('/solicitacoesMatriculas/<int:id>', methods=['PUT'])
def atualiza(id):
    data = request.get_json()
    data['id'] = id

    post_list = SolicitacaoMatriculaServices.update(data)

    return jsonify(list(map(lambda x: x.to_dictionary(), post_list)))
