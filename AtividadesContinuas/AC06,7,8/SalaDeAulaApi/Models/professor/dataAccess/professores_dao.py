import sqlite3
from Models.professor.entities.professor import Professor
from typing import Dict, List


class ProfessorDAO:
    @staticmethod
    def db(where: str = "") -> List[Professor]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            query = " SELECT id, nome, matricula FROM tb_professor "
            query += f" WHERE {where} " if where != "" else " WHERE 1 = 1 "

            cursor.execute(query)

            data = [Professor.to_tuple(item) for item in cursor.fetchall()]

            conn.commit()

        return data

    @staticmethod
    def list_all() -> List[Professor]:
        return ProfessorDAO.db()

    @staticmethod
    def find(id: int) -> Professor:
        data = ProfessorDAO.db(f" id = {id} ")
        if len(data) > 0:
            return data[0]

        return Professor()

    @staticmethod
    def new(novo_professor: Dict[str, str]) -> List[Professor]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"INSERT INTO {Professor.table_name()} (nome, matricula) VALUES (:nome, :matricula)",
                novo_professor
            )

            conn.commit()

        return ProfessorDAO.list_all()

    @staticmethod
    def update(novo_professor: Dict[str, str]) -> List[Professor]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"UPDATE {Professor.table_name()} SET nome = :nome, matricula = :matricula WHERE id == :id ",
                novo_professor
            )

            conn.commit()

        return ProfessorDAO.list_all()

    @staticmethod
    def delete(id_professor: int = 0) -> List[Professor]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"DELETE FROM {Professor.table_name()} WHERE id == ?",
                [id_professor]
            )

            conn.commit()

        return ProfessorDAO.list_all()
