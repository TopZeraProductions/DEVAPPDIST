import sqlite3
from model.aluno import Aluno
from typing import Dict, List


class AlunoServices:
    @staticmethod
    def db(where: str = "") -> List[Aluno]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            query = f" SELECT id, nome, matricula FROM  {Aluno.table_name()}"
            query += f" WHERE {where} " if where != "" else " WHERE 1 = 1 "

            cursor.execute(query)

            data = [Aluno.to_tuple(item) for item in cursor.fetchall()]

            conn.commit()

        return data


    @staticmethod
    def list_all() -> List[Aluno]:
        return AlunoServices.db()

    @staticmethod
    def find(id: int) -> Aluno:
        data = AlunoServices.db(f" id = {id} ")
        if len(data) > 0:
            return data[0]

        return Aluno()

    @staticmethod
    def new(novo_aluno: Dict[str, str]) -> List[Aluno]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"INSERT INTO {Aluno.table_name()} (nome, matricula) VALUES (:nome, :matricula)",
                novo_aluno
            )

            conn.commit()

        return AlunoServices.list_all()

    @staticmethod
    def update(novo_aluno: Dict[str, str]) -> List[Aluno]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"UPDATE {Aluno.table_name()} SET nome = :nome, matricula = :matricula WHERE id == :id ",
                novo_aluno
            )

            conn.commit()

        return AlunoServices.list_all()

    @staticmethod
    def delete(id_aluno: int = 0) -> List[Aluno]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"DELETE FROM {Aluno.table_name()} WHERE id == ?",
                [id_aluno]
            )

            conn.commit()

        return AlunoServices.list_all()
