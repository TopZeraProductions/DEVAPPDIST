from flask import Blueprint, jsonify, request

from services.professores_service import professores_db
from services.professores_service import listar as service_listar
from services.professores_service import localiza as service_localiza
from services.professores_service import novo as service_novo
from services.professores_service import remover as service_remover
from services.professores_service import atualiza as service_atualiza

from services.professores_dao import listar as dao_listar
from services.professores_dao import novo as dao_novo
from services.professores_dao import find as dao_find

professores_app = Blueprint('professores_app', __name__, template_folder='templates')


@professores_app.route('/professores', methods=['GET'])
def listar():
    pr_list = dao_listar()
    return jsonify(list(map(lambda pr: pr.__dict__(), pr_list)))


@professores_app.route('/professores/<int:id>', methods=['GET'])
def localiza(id):
    professor = dao_find(id)
    return jsonify(professor.__dict__())

    # p = service_localiza(id)
    # if p is not None:
    #     return jsonify(p.__dict__())
    # return '', 404


'''
@professores_app.route('/professores', methods=['POST'])
def novo():
    novo_professor = request.get_json()
    pr_list = service_novo(novo_professor)
    if pr_list is None:
        return 'Esse cadastro já existe', 400
    return jsonify(list(map(lambda pr: pr.__dict__(), pr_list)))
'''


@professores_app.route('/professores', methods=['POST'])
def novo():
    novo_professor = request.get_json()
    # pr_list = service_novo(novo_professor)
    pr_list = dao_novo(novo_professor)

    if pr_list is None:
        return 'Esse cadastro já existe', 400

    return jsonify(list(map(lambda pr: pr.__dict__(), pr_list)))


@professores_app.route('/professores/<int:id>', methods=['DELETE'])
def remover(id):
    removido = service_remover(id)
    if removido is not None:
        return jsonify(removido.__dict__())
    return '', 404


@professores_app.route('/professores/<int:id>', methods=['PUT'])
def atualiza(id):
    professor_data = request.get_json()
    removido = service_atualiza(id, professor_data)
    if removido is not None:
        return jsonify(removido.__dict__())
    return '', 404
