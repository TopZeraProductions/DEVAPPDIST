from flask import Blueprint, jsonify, request

from Services.alunos.services.alunos_services import AlunoServices

alunos_app = Blueprint('alunos_app', __name__, template_folder='templates')


@alunos_app.route('/alunos', methods=['GET'])
def listar():
    al_list = AlunoServices.list_all()
    return jsonify(list(map(lambda pr: pr.to_dictionary(), al_list)))


@alunos_app.route('/alunos/<int:id>', methods=['GET'])
def localiza(id: int) -> str:
    aluno = AlunoServices.find(id)

    return jsonify(aluno.to_dictionary())


@alunos_app.route('/alunos', methods=['POST'])
def novo():
    novo_registro = request.get_json()
    pr_list = []
    if type(novo_registro) is list:
        for element in novo_registro:
            pr_list = AlunoServices.new(element)
    else:
        pr_list = AlunoServices.new(novo_registro)

    return jsonify(list(map(lambda pr: pr.to_dictionary(), pr_list)))


@alunos_app.route('/alunos/<int:id>', methods=['DELETE'])
def remover(id):
    post_list = AlunoServices.delete(id)

    return jsonify(list(map(lambda pr: pr.to_dictionary(), post_list)))


@alunos_app.route('/alunos/<int:id>', methods=['PUT'])
def atualiza(id):
    aluno_data = request.get_json()
    aluno_data['id'] = id

    post_list = AlunoServices.update(aluno_data)

    return jsonify(list(map(lambda pr: pr.to_dictionary(), post_list)))
