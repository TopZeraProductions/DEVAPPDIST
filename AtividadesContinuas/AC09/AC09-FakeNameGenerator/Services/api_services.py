import json
import requests
import random
from random import randrange
from datetime import timedelta, datetime


def get_from_via_cep(cep: str = ""):
    requestEndereco = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    endereco = requestEndereco.content
    endereco_dict = json.loads(endereco)
    if "erro" in endereco_dict:
        endereco_dict["logradouro"] = "Nao definido"
        endereco_dict["bairro"] = "Nao definido"
        endereco_dict["localidade"] = "Nao definido"

    return endereco_dict


def get_name():
    requestNames = requests.get('http://localhost:5080/names')
    names = requestNames.content
    names_dict = json.loads(names)
    name = names_dict[random.randrange(0, len(names_dict))]['name']
    return name


def get_document():
    requestDocuments = requests.get('http://localhost:5080/documents')
    documents = requestDocuments.content
    documents_dict = json.loads(documents)
    document = documents_dict[random.randrange(0, len(documents_dict))]['description']
    return document


def get_cep():
    requestCep = requests.get('http://localhost:5080/ceps')
    ceps = requestCep.content
    ceps_dict = json.loads(ceps)
    cep = ceps_dict[random.randrange(0, len(ceps_dict))]['description']
    return cep


def get_birthday():
    d1 = datetime.strptime('1/1/1998 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('1/1/2012 4:50 AM', '%m/%d/%Y %I:%M %p')

    return str(random_date(d1, d2))


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)
