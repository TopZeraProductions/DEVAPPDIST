import datetime
from flask import Blueprint, jsonify, request
from Services.mensagem.services.mensagen_services import MensagemServices, Mensagem
from Services.usuario.services.usuarios_services import UsuariosServices
from Infra.Extensions.ListExtensions import MyList
from Infra.util.utilRetorno import UtilRetorno

mensagens_app = Blueprint('mensagens_app', __name__, template_folder='templates')


@mensagens_app.route('/msg', methods=['GET'])
def listar():
    post_list = MensagemServices.list_all()

    response = list(map(lambda x: x.to_dictionary(), post_list))

    return jsonify(response)


@mensagens_app.route('/msg/<int:id>', methods=['GET'])
def listar_mensagens(id: int):
    segredo = request.args.get('segredo')
    inicio = request.args.get('inicio')
    fim = request.args.get('fim')

    usuario = UsuariosServices.find(id)

    if usuario.id <= 0:
        return "Usuario inexistente", 200

    if segredo != usuario.segredo:
        return "Segredo Incorreto", 200

    ml = MyList(MensagemServices.list_all())
    ml = ml.where(lambda item: item.id_destinatario == id) \
           .map(  # Transforma a lista de objetos em uma lista de dicionarios
                lambda item: {
                    "de": item.id_remetente,
                    "para": item.id_destinatario,
                    "datahora": item.data_hora,
                    "texto": item.texto
                }
           )

    d = dict()
    d["mensagens"] = ml
    return jsonify(d)


@mensagens_app.route('/msgdetails/<int:id>', methods=['GET'])
def localizar(id: int, segredo: str) -> str:
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

    remetente = UsuariosServices.find(novo_registro['de'])
    destinatario = UsuariosServices.find(novo_registro['para'])

    if remetente.id <= 0:
        return "Remetente Nao cadastrados no sistema", 200

    if destinatario.id <= 0:
        return "Destinatario Nao cadastrados no sistema", 200

    if novo_registro["segredo"] != remetente.segredo:
        return "Segredo Incorreto", 200

    estrutura = dict()
    estrutura["id_remetente"] = remetente.id
    estrutura["id_destinatario"] = destinatario.id
    estrutura["data_hora"] = datetime.datetime.now()
    estrutura["texto"] = novo_registro["texto"]

    retorno: UtilRetorno = MensagemServices.new(estrutura)

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
