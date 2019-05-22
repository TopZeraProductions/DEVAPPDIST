import sqlite3
from Models.curso.entities.curso import Curso
from typing import Dict, List


class CursosDAO:
    @staticmethod
    def db(where: str = "") -> List[Curso]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            query = f" SELECT id, nome FROM  {Curso.table_name()}"
            query += f" WHERE {where} " if where != "" else " WHERE 1 = 1 "

            cursor.execute(query)

            data = [Curso.to_tuple(item) for item in cursor.fetchall()]

            conn.commit()

        return data

    @staticmethod
    def list_all() -> List[Curso]:
        return CursosDAO.db()

    @staticmethod
    def find(id: int) -> Curso:
        data = CursosDAO.db(f" id = {id} ")
        if len(data) > 0:
            return data[0]

        return Curso()

    @staticmethod
    def new(novo_curso: Dict[str, str]) -> List[Curso]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"INSERT INTO {Curso.table_name()} (nome) VALUES (:nome)",
                novo_curso
            )

            conn.commit()

        return CursosDAO.list_all()

    @staticmethod
    def update(novo_aluno: Dict[str, str]) -> List[Curso]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"UPDATE {Curso.table_name()} SET nome = :nome WHERE id == :id ",
                novo_aluno
            )

            conn.commit()

        return CursosDAO.list_all()

    @staticmethod
    def delete(id_curso: int = 0) -> List[Curso]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"DELETE FROM {Curso.table_name()} WHERE id == ?",
                [id_curso]
            )

            conn.commit()

        return CursosDAO.list_all()
