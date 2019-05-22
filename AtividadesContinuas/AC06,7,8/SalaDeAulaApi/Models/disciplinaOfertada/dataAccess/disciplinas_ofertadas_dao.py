import sqlite3
from Models.disciplinaOfertada.entities.disciplinaOfertada import DisciplinaOfertada
from typing import Dict, List


class DisciplinaOfertadaDAO:
    @staticmethod
    def db(where: str = "") -> List[DisciplinaOfertada]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            query = f" SELECT id, id_disciplina, id_professor, ano, semestre, turma " \
                    f" FROM {DisciplinaOfertada.table_name()} "

            query += f" WHERE {where} " if where != "" else " WHERE 1 = 1 "

            print(query)

            cursor.execute(query)

            data = [DisciplinaOfertada.to_tuple(item) for item in cursor.fetchall()]

            conn.commit()

        return data

    @staticmethod
    def list_all() -> List[DisciplinaOfertada]:
        return DisciplinaOfertadaDAO.db()

    @staticmethod
    def find(id: int) -> DisciplinaOfertada:
        data = DisciplinaOfertadaDAO.db(f" id = {id} ")
        if len(data) > 0:
            return data[0]

        return DisciplinaOfertada()

    @staticmethod
    def new(novo_registro: Dict[str, str]) -> List[DisciplinaOfertada]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            print(novo_registro)

            cursor.execute(
                f"INSERT INTO {DisciplinaOfertada.table_name()} (id_disciplina, id_professor, ano, semestre, turma) "
                f"VALUES(:id_disciplina, :id_professor, :ano, :semestre, :turma);",
                novo_registro
            )

            conn.commit()

        return DisciplinaOfertadaDAO.list_all()

    @staticmethod
    def update(novo_registro: Dict[str, str]) -> List[DisciplinaOfertada]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f" UPDATE {DisciplinaOfertada.table_name()} SET id_disciplina=:id_disciplina, id_professor=:id_professor, ano=:ano, semestre=:semestre, turma=:turma"
                f" WHERE id=:id",
                novo_registro
            )

            conn.commit()

        return DisciplinaOfertadaDAO.list_all()

    @staticmethod
    def delete(id_registro: int = 0) -> List[DisciplinaOfertada]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"DELETE FROM {DisciplinaOfertada.table_name()} WHERE id == ?",
                [id_registro]
            )

            conn.commit()

        return DisciplinaOfertadaDAO.list_all()
