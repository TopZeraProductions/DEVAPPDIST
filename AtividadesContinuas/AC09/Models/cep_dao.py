import sqlite3
from Models.cep_model import Cep
from typing import Dict, List


class CepDAO:
    @staticmethod
    def db(where: str = "") -> List[Cep]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            query = f" SELECT id, description FROM  {Cep.table_name()}"
            query += f" WHERE {where} " if where != "" else " WHERE 1 = 1 "

            cursor.execute(query)

            data = [Cep.to_tuple(item) for item in cursor.fetchall()]

            conn.commit()

        return data

    @staticmethod
    def list_all() -> List[Cep]:
        return CepDAO.db()

    @staticmethod
    def find(id: int) -> Cep:
        data = CepDAO.db(f" id = {id} ")
        if len(data) > 0:
            return data[0]

        return Cep()

    @staticmethod
    def new(novo_registro: Dict[str, str]) -> List[Cep]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"INSERT INTO {Cep.table_name()} (description) VALUES (:description)",
                novo_registro
            )

            conn.commit()

        return CepDAO.list_all()

    @staticmethod
    def update(novo_registro: Dict[str, str]) -> List[Cep]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"UPDATE {Cep.table_name()} SET description = :description WHERE id == :id ",
                novo_registro
            )

            conn.commit()

        return CepDAO.list_all()

    @staticmethod
    def delete(id_name: int = 0) -> List[Cep]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"DELETE FROM {Cep.table_name()} WHERE id == ?",
                [id_name]
            )

            conn.commit()

        return CepDAO.list_all()
