from flask import Blueprint, jsonify, request
import json
import requests
import random
from random import randrange
from datetime import timedelta, datetime

from Services.person_services import PersonServices, Person

person_app = Blueprint('person_app', __name__, template_folder='templates')


@person_app.route('/person', methods=['GET'])
def get_person():
    lista = [item.to_dictionary() for item in PersonServices.list_all()]

    return jsonify(lista)


@person_app.route('/person', methods=['POST'])
def new_person():
    data = request.get_json()

    retu = PersonServices.new(data)

    dcs = [item.to_dictionary() for item in retu]

    return jsonify(dcs)


@person_app.route('/generate', methods=['GET'])
def new_persons():

    d1 = datetime.strptime('1/1/1998 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('1/1/2012 4:50 AM', '%m/%d/%Y %I:%M %p')

    requestNames = requests.get('http://localhost:5080/names')
    names = requestNames.content
    names_dict = json.loads(names)
    name = names_dict[random.randrange(0, len(names_dict))]['name']

    requestDocuments = requests.get('http://localhost:5080/documents')
    documents = requestDocuments.content
    documents_dict = json.loads(documents)
    document = documents_dict[random.randrange(0, len(documents_dict))]['description']

    requestCep = requests.get('http://localhost:5080/ceps')
    ceps = requestCep.content
    ceps_dict = json.loads(ceps)
    cep = ceps_dict[random.randrange(0, len(ceps_dict))]['description']

    requestEndereco = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    endereco = requestEndereco.content
    endereco_dict = json.loads(endereco)

    newPerson = dict()
    newPerson['name'] = name
    newPerson['document'] = document
    newPerson['birthday'] = str(random_date(d1, d2))
    newPerson['cep'] = cep

    print(newPerson)

    retu = PersonServices.new(newPerson)

    dcs = retu.to_dictionary()
    dcs['endereco'] = endereco_dict

    return jsonify(dcs)


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)
