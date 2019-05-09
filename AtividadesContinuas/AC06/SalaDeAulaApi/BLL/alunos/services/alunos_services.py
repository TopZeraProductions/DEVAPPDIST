from DAL.aluno.entities.aluno import Aluno
from DAL.aluno.dataAccess.alunos_dao import AlunoDAO
from typing import List, Dict


class AlunoServices:
    @staticmethod
    def list_all() -> List[Aluno]:
        return AlunoDAO.list_all()

    @staticmethod
    def find(id: int) -> Aluno:
        return AlunoDAO.find(id)

    @staticmethod
    def new(novo_aluno: Dict[str, str]) -> List[Aluno]:
        return AlunoDAO.new(novo_aluno)

    @staticmethod
    def update(novo_aluno: Dict[str, str]) -> List[Aluno]:
        return AlunoDAO.update(novo_aluno)

    @staticmethod
    def delete(id_aluno: int = 0) -> List[Aluno]:
        return AlunoDAO.delete(id_aluno)


