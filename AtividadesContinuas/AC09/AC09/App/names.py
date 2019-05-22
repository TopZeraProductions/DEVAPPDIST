from flask import Blueprint, jsonify, request
from Services.names_services import NameServices

name_app = Blueprint('name_app', __name__, template_folder='templates')


@name_app.route('/names', methods=['GET'])
def get_names():
    names = [item.to_dictionary() for item in NameServices.list_all()]

    return jsonify(names)


@name_app.route('/names', methods=['POST'])
def new_name():
    data = request.get_json()

    retu = NameServices.new(data)

    names = [item.to_dictionary() for item in retu]

    return jsonify(names)
