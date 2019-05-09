from DAL.professor.entities.professor import Professor
from DAL.professor.dataAccess.professores_dao import ProfessorDAO
from typing import List, Dict


class ProfessorServices:
    @staticmethod
    def list_all() -> List[Professor]:
        return ProfessorDAO.list_all()

    @staticmethod
    def find(id: int) -> Professor:
        return ProfessorDAO.find(id)

    @staticmethod
    def new(novo_aluno: Dict[str, str]) -> List[Professor]:
        return ProfessorDAO.new(novo_aluno)

    @staticmethod
    def update(novo_aluno: Dict[str, str]) -> List[Professor]:
        return ProfessorDAO.update(novo_aluno)

    @staticmethod
    def delete(id_aluno: int = 0) -> List[Professor]:
        return ProfessorDAO.delete(id_aluno)
