from flask import Blueprint, jsonify, request

from Services.person_services import PersonServices, Person
from Services.api_services import *

person_app = Blueprint('person_app', __name__, template_folder='templates')


@person_app.route('/person', methods=['GET'])
def get_person():
    lista = [item.to_dictionary() for item in PersonServices.list_all()]

    list2 = list()
    for item in lista:
        endereco_dict = get_from_via_cep(item["cep"])
        item['street'] = endereco_dict["logradouro"]
        item['neighborhood'] = endereco_dict["bairro"]
        item['city'] = endereco_dict["localidade"]
        list2.append(item)

    return jsonify(list2)


@person_app.route('/generate', methods=['GET'])
def new_persons():
    name          = get_name()
    document      = get_document()
    cep           = get_cep()
    endereco_dict = get_from_via_cep(cep)
    birthday      = get_birthday()

    newPerson = dict()
    newPerson['name'] = name
    newPerson['document'] = document
    newPerson['birthday'] = birthday
    newPerson['cep'] = cep

    retu = PersonServices.new(newPerson)

    dcs = retu.to_dictionary()
    dcs['street']       = endereco_dict["logradouro"]
    dcs['neighborhood'] = endereco_dict["bairro"]
    dcs['city']         = endereco_dict["localidade"]

    return jsonify(dcs)
