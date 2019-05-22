from Models.names_dao import NameDAO
from Models.names_model import Name

from typing import List, Dict


class NameServices:
    @staticmethod
    def list_all() -> List[Name]:
        return NameDAO.list_all()

    @staticmethod
    def find(id: int) -> Name:
        return NameDAO.find(id)

    @staticmethod
    def new(novo_registro: Dict[str, str]) -> List[Name]:
        return NameDAO.new(novo_registro)

    @staticmethod
    def update(novo_aluno: Dict[str, str]) -> List[Name]:
        return NameDAO.update(novo_aluno)

    @staticmethod
    def delete(id_name: int = 0) -> List[Name]:
        return NameDAO.delete(id_name)
