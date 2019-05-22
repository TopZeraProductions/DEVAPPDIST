import sqlite3
from Models.document_model import Document
from typing import Dict, List


class DocumentDAO:
    @staticmethod
    def db(where: str = "") -> List[Document]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            query = f" SELECT id, description, country FROM  {Document.table_name()}"
            query += f" WHERE {where} " if where != "" else " WHERE 1 = 1 "

            cursor.execute(query)

            data = [Document.to_tuple(item) for item in cursor.fetchall()]

            conn.commit()

        return data

    @staticmethod
    def list_all() -> List[Document]:
        return DocumentDAO.db()

    @staticmethod
    def find(id: int) -> Document:
        data = DocumentDAO.db(f" id = {id} ")
        if len(data) > 0:
            return data[0]

        return Document()

    @staticmethod
    def new(novo_registro: Dict[str, str]) -> List[Document]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"INSERT INTO {Document.table_name()} (description, country) VALUES (:description, :country)",
                novo_registro
            )

            conn.commit()

        return DocumentDAO.list_all()

    @staticmethod
    def update(novo_registro: Dict[str, str]) -> List[Document]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"UPDATE {Document.table_name()} SET description = :description, country = :country WHERE id == :id ",
                novo_registro
            )

            conn.commit()

        return DocumentDAO.list_all()

    @staticmethod
    def delete(id_name: int = 0) -> List[Document]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"DELETE FROM {Document.table_name()} WHERE id == ?",
                [id_name]
            )

            conn.commit()

        return DocumentDAO.list_all()
