from typing import Dict, Tuple
import sqlite3


class Cep:
    def __init__(self, id_cep: int = 0, description: str = ""):
        self.id = id_cep
        self.description = description

    def to_dictionary(self):
        retu = dict()
        retu['id'] = self.id
        retu['description'] = self.description

        return retu

    @staticmethod
    def to_tuple(tupla: Tuple[int, str]):
        return Cep(id_cep=tupla[0], description=tupla[1])

    @staticmethod
    def create(dados: Dict[str, str]) -> object:
        try:
            id = dados["id"]
            description = dados["description"]
            return Cep(id_cep=int(id), description=description)
        except Exception as e:
            print("Problema ao criar o novo cep! ")
            raise ValueError()

    @staticmethod
    def table_name() -> str:
        return "tb_cep"

    @staticmethod
    def migrate_table() -> int:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {Cep.table_name()} (" +
                "   id INTEGER PRIMARY KEY AUTOINCREMENT," +
                "   description VARCHAR(100)," +
                "   country VARCHAR(100)" +
                ");"
            )
            conn.commit()

            rows = cursor.fetchall()

        return len(rows)
