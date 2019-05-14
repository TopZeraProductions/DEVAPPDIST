from Models.disciplina.dataAccess.disciplinas_dao import DisciplinaDAO
from Models.professor.dataAccess.professores_dao import ProfessorDAO
from Models.disciplinaOfertada.dataAccess.disciplinas_ofertadas_dao import DisciplinaOfertadaDAO
from Models.disciplinaOfertada.entities.disciplinaOfertada import DisciplinaOfertada
from typing import List, Dict


class DisciplinaOfertadaServices:
    @staticmethod
    def list_all() -> List[Dict[str, str]]:
        lista = []
        for disciplinaOfertada in DisciplinaOfertadaDAO.list_all():
            di = disciplinaOfertada.to_dictionary()
            di["professor"] = ProfessorDAO.find(disciplinaOfertada.id_professor).to_dictionary()
            di["disciplina"] = DisciplinaDAO.find(disciplinaOfertada.id_disciplina).to_dictionary()
            lista.append(di)

        return lista

    @staticmethod
    def find(id: int) -> DisciplinaOfertada:
        return DisciplinaOfertadaDAO.find(id)

    @staticmethod
    def new(novo_registro: Dict[str, str]) -> List[DisciplinaOfertada]:
        return DisciplinaOfertadaDAO.new(novo_registro)

    @staticmethod
    def update(novo_registro: Dict[str, str]) -> List[DisciplinaOfertada]:
        return DisciplinaOfertadaDAO.update(novo_registro)

    @staticmethod
    def delete(id_referencia: int = 0) -> List[DisciplinaOfertada]:
        return DisciplinaOfertadaDAO.delete(id_referencia)
