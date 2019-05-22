from flask import Blueprint, jsonify, request
from Services.cep_services import CepServices

cep_app = Blueprint('cep_app', __name__, template_folder='templates')


@cep_app.route('/ceps', methods=['GET'])
def get_ceps():
    ceps = [item.to_dictionary() for item in CepServices.list_all()]

    return jsonify(ceps)


@cep_app.route('/ceps', methods=['POST'])
def new_cep():
    data = request.get_json()
    retu = CepServices.new(data)
    names = [item.to_dictionary() for item in retu]

    return jsonify(names)
