from Models.person_model import Person
from Models.person_dao import PersonDAO

from typing import List, Dict


class PersonServices:
    @staticmethod
    def list_all() -> List[Person]:
        return PersonDAO.list_all()

    @staticmethod
    def find(id: int) -> Person:
        return PersonDAO.find(id)

    @staticmethod
    def new(novo_registro: Dict[str, str]) -> Person:
        return PersonDAO.new(novo_registro)

    @staticmethod
    def update(novo_registro: Dict[str, str]) -> List[Person]:
        return PersonDAO.update(novo_registro)

    @staticmethod
    def delete(id_document: int = 0) -> List[Person]:
        return PersonDAO.delete(id_document)
