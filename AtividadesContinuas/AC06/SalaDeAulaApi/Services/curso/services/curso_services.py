from Models.curso.entities.curso import Curso
from Models.curso.dataAccess.cursos_dao import CursosDAO
from typing import List, Dict


class CursoServices:
    @staticmethod
    def list_all() -> List[Curso]:
        return CursosDAO.list_all()

    @staticmethod
    def find(id: int) -> Curso:
        return CursosDAO.find(id)

    @staticmethod
    def new(novo_aluno: Dict[str, str]) -> List[Curso]:
        return CursosDAO.new(novo_aluno)

    @staticmethod
    def update(novo_aluno: Dict[str, str]) -> List[Curso]:
        return CursosDAO.update(novo_aluno)

    @staticmethod
    def delete(id_aluno: int = 0) -> List[Curso]:
        return CursosDAO.delete(id_aluno)
