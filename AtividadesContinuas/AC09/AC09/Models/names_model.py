from typing import Dict, Tuple
import sqlite3


class Name:
    def __init__(self, id_name: int = 0, name: str = "", gender: str = "male"):
        self.id = id_name
        self.name = name
        self.gender = gender

    def to_dictionary(self):
        retu = dict()
        retu['id'] = self.id
        retu['name'] = self.name
        retu['gender'] = self.gender

        return retu

    @staticmethod
    def to_tuple(tupla: Tuple[int, str, str]):
        return Name(id_name=tupla[0], name=tupla[1], gender=tupla[2])

    @staticmethod
    def create(dados: Dict[str, str]) -> object:
        try:
            id = dados["id"]
            name = dados["name"]
            gender = dados["gender"]
            return Name(id_name=int(id), name=name, gender=gender)
        except Exception as e:
            print("Problema ao criar o novo nome! ")
            raise ValueError()

    @staticmethod
    def table_name() -> str:
        return "tb_name"

    @staticmethod
    def migrate_table() -> int:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {Name.table_name()} (" +
                "   id INTEGER PRIMARY KEY AUTOINCREMENT," +
                "   name VARCHAR(100)," +
                "   gender VARCHAR(100)" +
                ");"
            )
            conn.commit()

            rows = cursor.fetchall()

        return len(rows)
