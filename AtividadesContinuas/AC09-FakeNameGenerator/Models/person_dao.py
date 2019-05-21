import sqlite3
from Models.person_model import Person
from typing import Dict, List


class PersonDAO:
    @staticmethod
    def db(where: str = "") -> List[Person]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            query = f" SELECT id, name, document, birthday, cep FROM  {Person.table_name()}"
            query += f" WHERE {where} " if where != "" else " WHERE 1 = 1 "

            cursor.execute(query)

            data = [Person.to_tuple(item) for item in cursor.fetchall()]

            conn.commit()

        return data

    @staticmethod
    def list_all() -> List[Person]:
        return PersonDAO.db()

    @staticmethod
    def find(id: int) -> Person:
        data = PersonDAO.db(f" id = {id} ")
        if len(data) > 0:
            return data[0]

        return Person()

    @staticmethod
    def new(novo_registro: Dict[str, str]) -> Person:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"INSERT INTO {Person.table_name()} (name, document, birthday, cep) VALUES (:name, :document, :birthday, :cep )",
                novo_registro
            )

            conn.commit()

        return PersonDAO.list_all()[len(PersonDAO.list_all()) - 1]

    @staticmethod
    def update(novo_registro: Dict[str, str]) -> List[Person]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"UPDATE {Person.table_name()} SET name = :name, document = :document, birthday = :birthday , cep = :cep  WHERE id == :id ",
                novo_registro
            )

            conn.commit()

        return PersonDAO.list_all()

    @staticmethod
    def delete(id_name: int = 0) -> List[Person]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"DELETE FROM {Person.table_name()} WHERE id == ?",
                [id_name]
            )

            conn.commit()

        return PersonDAO.list_all()
