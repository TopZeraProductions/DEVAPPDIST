from Models.solicitacaoMatricula.entities.solicitacaoMatricula import SolicitacaoMatricula
from typing import List, Dict
import sqlite3


class SolicitacaoMatriculaDAO:
    @staticmethod
    def db(where: str = "") -> List[SolicitacaoMatricula]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            query = f" SELECT id, id_aluno, id_disciplina_ofertada, dt_solicitacao, id_coordenador , status " \
                    f" FROM {SolicitacaoMatricula.table_name()} " \

            query += f" WHERE {where} " if where != "" else " WHERE 1 = 1 "

            cursor.execute(query)

            data = [SolicitacaoMatricula.to_tuple(item) for item in cursor.fetchall()]

            conn.commit()

        return data

    @staticmethod
    def list_all() -> List[SolicitacaoMatricula]:
        return SolicitacaoMatriculaDAO.db()

    @staticmethod
    def find(id: int) -> SolicitacaoMatricula:
        data = SolicitacaoMatriculaDAO.db(f" id = {id} ")
        if len(data) > 0:
            return data[0]

        return SolicitacaoMatricula()

    @staticmethod
    def new(novo_registro: Dict[str, str]) -> List[SolicitacaoMatricula]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f" INSERT INTO {SolicitacaoMatricula.table_name()} (id_aluno, id_disciplina_ofertada, id_coordenador, dt_solicitacao, status) "
                f" VALUES(:id_aluno, :id_disciplina_ofertada, :id_coordenador, :dt_solicitacao, :status) ",
                novo_registro
            )

            conn.commit()

        return SolicitacaoMatriculaDAO.list_all()

    @staticmethod
    def update(novo_registro: Dict[str, str]) -> List[SolicitacaoMatricula]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f" UPDATE tb_solicitacao_matricula SET id_aluno=:id_aluno, id_disciplina_ofertada=:id_disciplina_ofertada, id_coordenador=:id_coordenador, dt_solicitacao=:dt_solicitacao, status=:status "
                f" WHERE id=:id ",
                novo_registro
            )

            conn.commit()

        return SolicitacaoMatriculaDAO.list_all()

    @staticmethod
    def delete(id_registro: int = 0) -> List[SolicitacaoMatricula]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f" DELETE FROM {SolicitacaoMatricula.table_name()} WHERE id == ? ",
                [id_registro]
            )

            conn.commit()

        return SolicitacaoMatriculaDAO.list_all()
