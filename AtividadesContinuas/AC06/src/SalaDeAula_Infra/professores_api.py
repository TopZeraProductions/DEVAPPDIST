from flask import Blueprint, jsonify, request
from services.professores_service import professores_db, \
    listar as service_listar, \
    localiza as service_localiza, \
    novo as service_novo, \
    remover as service_remover, \
    atualiza as service_atualiza

professores_app = Blueprint('professores_app', __name__, template_folder='templates')

@professores_app.route('/professores', methods=['GET'])
def listar():
    pr_list = service_listar()
    return jsonify(list(map(lambda pr: pr.__dict__(), pr_list)))

@professores_app.route('/professores/<int:matricula>', methods=['GET'])
def localiza(matricula):
    p = service_localiza(matricula)
    if(p != None):
        return jsonify(p.__dict__())
    return '', 404

@professores_app.route('/professores', methods=['POST'])
def novo():
    novo_professor = request.get_json()
    pr_list = service_novo(novo_professor)
    return jsonify(list(map(lambda pr: pr.__dict__(), pr_list)))

@professores_app.route('/professores/<int:matricula>', methods=['DELETE'])
def remover(matricula):
    removido = service_remover(matricula)
    if removido != None:
        return jsonify(removido.__dict__())
    return '', 404

@professores_app.route('/professores/<int:matricula>', methods=['PUT'])
def atualiza(matricula):
    professor_data = request.get_json()
    removido = service_atualiza(matricula, professor_data)
    if removido != None:
        return jsonify(removido.__dict__())
    return '', 404