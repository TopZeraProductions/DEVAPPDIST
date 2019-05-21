from typing import Dict, Tuple
import sqlite3


class Document:
    def __init__(self, id_document: int = 0, description: str = "", country: str = ""):
        self.id = id_document
        self.description = description
        self.country = country

    def to_dictionary(self):
        retu = dict()
        retu['id'] = self.id
        retu['description'] = self.description
        retu['country'] = self.country

        return retu

    @staticmethod
    def to_tuple(tupla: Tuple[int, str, str]):
        return Document(id_document=tupla[0], description=tupla[1], country=tupla[2])

    @staticmethod
    def create(dados: Dict[str, str]) -> object:
        try:
            id = dados["id"]
            description = dados["description"]
            country = dados["country"]
            return Document(id_document=int(id), description=description, country=country)
        except Exception as e:
            print("Problema ao criar o novo nome! ")
            raise ValueError()

    @staticmethod
    def table_name() -> str:
        return "tb_document"

    @staticmethod
    def migrate_table() -> int:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {Document.table_name()} (" +
                "   id INTEGER PRIMARY KEY AUTOINCREMENT," +
                "   description VARCHAR(100)," +
                "   country VARCHAR(100)" +
                ");"
            )
            conn.commit()

            rows = cursor.fetchall()

        return len(rows)
