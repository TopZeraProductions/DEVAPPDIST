import sqlite3
from Models.names_model import Name
from typing import Dict, List


class NameDAO:
    @staticmethod
    def db(where: str = "") -> List[Name]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            query = f" SELECT id, name, gender FROM  {Name.table_name()}"
            query += f" WHERE {where} " if where != "" else " WHERE 1 = 1 "

            cursor.execute(query)

            data = [Name.to_tuple(item) for item in cursor.fetchall()]

            conn.commit()

        return data

    @staticmethod
    def list_all() -> List[Name]:
        return NameDAO.db()

    @staticmethod
    def find(id: int) -> Name:
        data = NameDAO.db(f" id = {id} ")
        if len(data) > 0:
            return data[0]

        return Name()

    @staticmethod
    def new(novo_registro: Dict[str, str]) -> List[Name]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"INSERT INTO {Name.table_name()} (name, gender) VALUES (:name, :gender)",
                novo_registro
            )

            conn.commit()

        return NameDAO.list_all()

    @staticmethod
    def update(novo_registro: Dict[str, str]) -> List[Name]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"UPDATE {Name.table_name()} SET name = :name, gender = :gender WHERE id == :id ",
                novo_registro
            )

            conn.commit()

        return NameDAO.list_all()

    @staticmethod
    def delete(id_name: int = 0) -> List[Name]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"DELETE FROM {Name.table_name()} WHERE id == ?",
                [id_name]
            )

            conn.commit()

        return NameDAO.list_all()
