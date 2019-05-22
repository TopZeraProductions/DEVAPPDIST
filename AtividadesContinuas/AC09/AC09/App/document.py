from flask import Blueprint, jsonify, request
from Services.document_services import DocumentServices

document_app = Blueprint('document_app', __name__, template_folder='templates')


@document_app.route('/documents', methods=['GET'])
def get_documents():
    docs = [item.to_dictionary() for item in DocumentServices.list_all()]

    return jsonify(docs)


@document_app.route('/documents', methods=['POST'])
def new_documents():
    data = request.get_json()

    retu = DocumentServices.new(data)

    dcs = [item.to_dictionary() for item in retu]

    return jsonify(dcs)
