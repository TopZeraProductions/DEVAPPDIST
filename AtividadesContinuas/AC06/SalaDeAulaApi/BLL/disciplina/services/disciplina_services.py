from DAL.disciplina.entities.disciplina import Disciplina
from DAL.disciplina.dataAccess.disciplinas_dao import DisciplinaDAO
from DAL.coordenador.dataAccess.coordenadores_dao import CoordenadorDAO
from typing import List, Dict


class DisciplinaServices:
    @staticmethod
    def list_all() -> List[Dict[str, str]]:
        lista = []
        for disciplina in DisciplinaDAO.list_all():
            di = disciplina.to_dictionary()
            di["coordenador"] = CoordenadorDAO.find(disciplina.id_coordenador).to_dictionary()
            lista.append(di)

        return lista

    @staticmethod
    def find(id: int) -> Disciplina:
        return DisciplinaDAO.find(id)

    @staticmethod
    def new(novo_registro: Dict[str, str]) -> List[Disciplina]:
        return DisciplinaDAO.new(novo_registro)

    @staticmethod
    def update(novo_registro: Dict[str, str]) -> List[Disciplina]:
        return DisciplinaDAO.update(novo_registro)

    @staticmethod
    def delete(id_referencia: int = 0) -> List[Disciplina]:
        return DisciplinaDAO.delete(id_referencia)
