import random

from Models.usuario.entities.usuario import Usuario
from Models.usuario.dataAccess.usuario_dao import UsuarioDAO
from Infra.util.utilRetorno import UtilRetorno

from typing import List, Dict


class UsuariosServices:
    @staticmethod
    def query(where_clause: str = "") -> List[Usuario]:
        return UsuarioDAO.db(where_clause)

    @staticmethod
    def list_all() -> List[Usuario]:
        return UsuarioDAO.list_all()

    @staticmethod
    def find(id: int) -> Usuario:
        return UsuarioDAO.find(id)

    @staticmethod
    def new(novo_registro: Dict[str, str]) -> UtilRetorno:
        ret: UtilRetorno = UtilRetorno()
        if "segredo" in novo_registro:
            novo_registro["segredo"] = novo_registro["segredo"]
        else:
            novo_registro["segredo"] = str(random.getrandbits(128))

        user: Usuario    = Usuario.create(novo_registro)

        if user.segredo == "":
            ret.error = True
            ret.listMessages.append("Senha nao podera entrar Vazia")
            return ret

        if user.nome == "":
            ret.error = True
            ret.listMessages.append("Nome nao pode estar Vazio")
            return ret

        retorno_cadastro = UsuarioDAO.new(novo_registro)

        ret.error = False
        ret.add_message("Usuario Cadastrado com Sucesso!!")
        ret.object = [user.to_dictionary() for user in retorno_cadastro]
        ret.object = ret.object[len(ret.object) - 1]

        return ret

    @staticmethod
    def update(novo_registro: Dict[str, str]) -> List[Usuario]:
        return UsuarioDAO.update(novo_registro)

    @staticmethod
    def delete(id_registro: int = 0) -> List[Usuario]:
        return UsuarioDAO.delete(id_registro)


