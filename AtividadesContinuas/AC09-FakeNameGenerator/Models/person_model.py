from typing import Dict, Tuple
import sqlite3


class Person:
    def __init__(self,
                 id_person: int = 0,
                 name:      str = "",
                 document:  str = "",
                 birthday:  str = "",
                 cep:       str = ""):

        self.id = id_person
        self.name = name
        self.document = document
        self.birthday = birthday
        self.cep = cep

    def to_dictionary(self):
        retu = dict()
        retu['id'] = self.id
        retu['name'] = self.name
        retu['document'] = self.document
        retu['birthday'] = self.birthday
        retu['cep'] = self.cep

        return retu

    @staticmethod
    def to_tuple(tupla: Tuple[int, str, str, str, str]):
        return Person(id_person=tupla[0], name=tupla[1], document=tupla[2], birthday=tupla[3], cep=tupla[4])

    @staticmethod
    def create(dados: Dict[str, str]) -> object:
        try:
            id = dados["id"]
            name = dados["name"]
            document = dados["document"]
            birthday = dados["birthday"]
            cep = dados["cep"]
            return Person(int(id), name, document, birthday, cep)
        except Exception as e:
            print("Problema ao criar o novo nome! ")
            raise ValueError()

    @staticmethod
    def table_name() -> str:
        return "tb_person"

    @staticmethod
    def migrate_table() -> int:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {Person.table_name()} (" +
                "   id INTEGER PRIMARY KEY AUTOINCREMENT," +
                "   name VARCHAR(100)," +
                "   document VARCHAR(100)," +
                "   birthday VARCHAR(100)," +
                "   cep VARCHAR(100)" +
                ");"
            )
            conn.commit()

            rows = cursor.fetchall()

        return len(rows)
