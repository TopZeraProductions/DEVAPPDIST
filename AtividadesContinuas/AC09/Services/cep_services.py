from Models.cep_dao import CepDAO
from Models.cep_model import Cep

from typing import List, Dict


class CepServices:
    @staticmethod
    def list_all() -> List[Cep]:
        return CepDAO.list_all()

    @staticmethod
    def find(id: int) -> Cep:
        return CepDAO.find(id)

    @staticmethod
    def new(novo_registro: Dict[str, str]) -> List[Cep]:
        return CepDAO.new(novo_registro)

    @staticmethod
    def update(novo_registro: Dict[str, str]) -> List[Cep]:
        return CepDAO.update(novo_registro)

    @staticmethod
    def delete(id_name: int = 0) -> List[Cep]:
        return CepDAO.delete(id_name)
