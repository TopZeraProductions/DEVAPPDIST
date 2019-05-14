from flask import Blueprint, jsonify, request
from Services.usuario.services.usuarios_services import UsuariosServices
from Infra.util.utilRetorno import UtilRetorno

usuarios_app = Blueprint('usuarios_app', __name__, template_folder='templates')


@usuarios_app.route('/usr', methods=['GET'])
def listar():
    post_list = UsuariosServices.list_all()

    response = dict()
    response["usr"] = list(map(lambda x: x.to_dictionary(), post_list))

    return jsonify(response)


@usuarios_app.route('/usr/<int:id>', methods=['GET'])
def localiza(id: int) -> str:
    obj = UsuariosServices.find(id)

    return jsonify(obj.to_dictionary())


@usuarios_app.route('/usr', methods=['POST'])
def novo():
    novo_registro = request.get_json()

    retorno: UtilRetorno = UtilRetorno()

    list_usuarios = UsuariosServices.list_all();
    ls = list()
    for usuario in list_usuarios:
        if novo_registro['nome'] == usuario.nome:
            ls.append(usuario)

    if len(ls) > 0:
        return "Usuario ja existente no sistema", 409

    retorno = UsuariosServices.new(novo_registro)

    return jsonify(retorno.object)


@usuarios_app.route('/usr/<int:id>', methods=['DELETE'])
def remover(id):
    post_list = UsuariosServices.delete(id)

    return jsonify(list(map(lambda x: x.to_dictionary(), post_list)))


@usuarios_app.route('/usr/<int:id>', methods=['PUT'])
def atualiza(id):
    data = request.get_json()
    data['id'] = id

    post_list = UsuariosServices.update(data)

    return jsonify(list(map(lambda x: x.to_dictionary(), post_list)))
