from flask import Blueprint, jsonify, request
from Services.mensagem.services.mensagen_services import MensagemServices
from Services.usuario.services.usuarios_services import UsuariosServices
from Models.usuario.entities.usuario import Usuario

from Infra.util.utilRetorno import UtilRetorno

mensagens_app = Blueprint('mensagens_app', __name__, template_folder='templates')


@mensagens_app.route('/msg', methods=['GET'])
def listar():
    post_list = MensagemServices.list_all()

    response = list(map(lambda x: x.to_dictionary(), post_list))

    return jsonify(response)


@mensagens_app.route('/msg/<int:id>', methods=['GET'])
def localiza(id: int) -> str:
    obj = MensagemServices.find(id)

    return jsonify(obj.to_dictionary())


@mensagens_app.route('/msg', methods=['POST'])
def novo():
    novo_registro = request.get_json()
    # {
    #   "de": <int>,
    #   "para": <int>,
    #   "segredo": <str>,
    #   "texto": <str>
    # }

    remetente = UsuariosServices.query(f" nome = '{novo_registro['de']}' ")

    print(remetente[0])
    exit(0)

    retorno: UtilRetorno = UtilRetorno()
    retorno = MensagemServices.new(novo_registro)

    return jsonify(retorno.to_dictionary())


@mensagens_app.route('/msg/<int:id>', methods=['DELETE'])
def remover(id):
    post_list = MensagemServices.delete(id)

    return jsonify(list(map(lambda x: x.to_dictionary(), post_list)))


@mensagens_app.route('/msg/<int:id>', methods=['PUT'])
def atualiza(id):
    data = request.get_json()
    data['id'] = id

    post_list = MensagemServices.update(data)

    return jsonify(list(map(lambda x: x.to_dictionary(), post_list)))
