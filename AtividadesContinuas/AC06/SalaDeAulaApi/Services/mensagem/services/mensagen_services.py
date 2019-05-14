from Models.mensagem.entities.mensagem import Mensagem
from Models.mensagem.dataAccess.mensagem_dao import MensagemDAO
from Infra.util.utilRetorno import UtilRetorno
from typing import List, Dict


class MensagemServices:
    @staticmethod
    def list_all() -> List[Mensagem]:
        return MensagemDAO.list_all()

    @staticmethod
    def find(id: int) -> Mensagem:
        return MensagemDAO.find(id)

    @staticmethod
    def new(novo_registro: Dict[str, str]) -> UtilRetorno:

        ret: UtilRetorno  = UtilRetorno()
        message: Mensagem = Mensagem.create(novo_registro)

        retorno_cadastro = MensagemDAO.new(novo_registro)

        ret.error = False
        ret.add_message("Mensagem Cadastrada com Sucesso!!")
        ret.object = [mensagem.to_dictionary() for mensagem in retorno_cadastro]

        return ret

    @staticmethod
    def update(novo_registro: Dict[str, str]) -> List[Mensagem]:
        return MensagemDAO.update(novo_registro)

    @staticmethod
    def delete(id_registro: int = 0) -> List[Mensagem]:
        return MensagemDAO.delete(id_registro)

