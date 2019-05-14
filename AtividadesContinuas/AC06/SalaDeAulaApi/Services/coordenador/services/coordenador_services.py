from Models.coordenador.entities.coordenador import Coordenador
from Models.coordenador.dataAccess.coordenadores_dao import CoordenadorDAO
from typing import List, Dict


class CoordenadorServices:
    @staticmethod
    def list_all() -> List[Coordenador]:
        return CoordenadorDAO.list_all()

    @staticmethod
    def find(id: int) -> Coordenador:
        return CoordenadorDAO.find(id)

    @staticmethod
    def new(novo_aluno: Dict[str, str]) -> List[Coordenador]:
        return CoordenadorDAO.new(novo_aluno)

    @staticmethod
    def update(novo_aluno: Dict[str, str]) -> List[Coordenador]:
        return CoordenadorDAO.update(novo_aluno)

    @staticmethod
    def delete(id_aluno: int = 0) -> List[Coordenador]:
        return CoordenadorDAO.delete(id_aluno)
