import sqlite3
from DAL.disciplina.entities.disciplina import Disciplina
from typing import Dict, List


class DisciplinaDAO:
    @staticmethod
    def db(where: str = "") -> List[Disciplina]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            query = "SELECT"\
                    "   id, nome, data, status, plano_ensino, carga_horaria, id_coordenador "\
                    f"FROM {Disciplina.table_name()}"
            print(query)

            query += f" WHERE {where} " if where != "" else " WHERE 1 = 1 "

            cursor.execute(query)

            data = [Disciplina.to_tuple(item) for item in cursor.fetchall()]

            conn.commit()

        return data

    @staticmethod
    def list_all() -> List[Disciplina]:
        return DisciplinaDAO.db()

    @staticmethod
    def find(id: int) -> Disciplina:
        data = DisciplinaDAO.db(f" id = {id} ")
        if len(data) > 0:
            return data[0]

        return Disciplina()

    @staticmethod
    def new(novo_registro: Dict[str, str]) -> List[Disciplina]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"INSERT INTO {Disciplina.table_name()} (nome, data, status, plano_ensino, carga_horaria, id_coordenador) "
                f"VALUES(:nome, :data, :status, :plano_ensino, :carga_horaria, :id_coordenador);",
                novo_registro
            )

            conn.commit()

        return DisciplinaDAO.list_all()

    @staticmethod
    def update(novo_registro: Dict[str, str]) -> List[Disciplina]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            query = f" UPDATE {Disciplina.table_name()} "\
                    f" SET nome=:nome, data=:data, status=:status, plano_ensino=:plano_ensino, carga_horaria=:carga_horaria, id_coordenador=:id_coordenador "\
                    f" WHERE id=:id"

            print(novo_registro)

            print(query)
            cursor.execute(
                query,
                novo_registro
            )

            conn.commit()

        return DisciplinaDAO.list_all()

    @staticmethod
    def delete(id_registro: int = 0) -> List[Disciplina]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"DELETE FROM {Disciplina.table_name()} WHERE id == ?",
                [id_registro]
            )

            conn.commit()

        return DisciplinaDAO.list_all()
