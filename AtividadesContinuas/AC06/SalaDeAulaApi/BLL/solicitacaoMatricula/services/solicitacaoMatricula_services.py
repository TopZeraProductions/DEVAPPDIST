from DAL.solicitacaoMatricula.entities.solicitacaoMatricula import SolicitacaoMatricula
from DAL.solicitacaoMatricula.dataAccess.solicitacoesMatriculas_dao import SolicitacaoMatriculaDAO

from DAL.disciplinaOfertada.dataAccess.disciplinas_ofertadas_dao import DisciplinaOfertadaDAO
from DAL.coordenador.dataAccess.coordenadores_dao import CoordenadorDAO
from DAL.aluno.dataAccess.alunos_dao import AlunoDAO

from typing import List, Dict


class SolicitacaoMatriculaServices:
    @staticmethod
    def list_all() -> List[Dict[str, str]]:
        lista = []
        for SolMat in SolicitacaoMatriculaDAO.list_all():
            di = SolMat.to_dictionary()
            di["coordenador"] = CoordenadorDAO.find(SolMat.id_coordenador).to_dictionary()
            di["aluno"] = AlunoDAO.find(SolMat.id_aluno).to_dictionary()
            di["disciplina_ofertada"] = DisciplinaOfertadaDAO.find(SolMat.id_disciplina_ofertada).to_dictionary()
            lista.append(di)

        return lista

    @staticmethod
    def find(id: int) -> SolicitacaoMatricula:
        return SolicitacaoMatriculaDAO.find(id)

    @staticmethod
    def new(novo_aluno: Dict[str, str]) -> List[SolicitacaoMatricula]:
        return SolicitacaoMatriculaDAO.new(novo_aluno)

    @staticmethod
    def update(novo_aluno: Dict[str, str]) -> List[SolicitacaoMatricula]:
        return SolicitacaoMatriculaDAO.update(novo_aluno)

    @staticmethod
    def delete(id_aluno: int = 0) -> List[SolicitacaoMatricula]:
        return SolicitacaoMatriculaDAO.delete(id_aluno)
