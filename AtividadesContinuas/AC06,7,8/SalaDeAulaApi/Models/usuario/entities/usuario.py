from typing import Dict, Tuple
import sqlite3
import random


class Usuario:
    def __init__(self, id_usuario: int = 0, nome: str = "", segredo: str = ""):
        self.id = id_usuario
        self.nome = nome
        self.segredo = segredo

    def to_dictionary(self) -> Dict[str, str]:
        d = dict()
        d['id'] = self.id
        d['nome'] = self.nome
        d['segredo'] = self.segredo
        return d

    @staticmethod
    def to_tuple(tupla: Tuple[int, str, str]):
        return Usuario(id_usuario=tupla[0], nome=tupla[1], segredo=tupla[2])

    @staticmethod
    def create(dados: Dict[str, str]) -> object:
        try:
            nome = dados["nome"]
            segredo = dados["segredo"]
            return Usuario(nome=nome, segredo=segredo)
        except Exception as e:
            print("Problema ao criar novo professor! " + e)
            raise ValueError()

    @staticmethod
    def table_name() -> str:
        return "tb_usuario"

    @staticmethod
    def migrate_table() -> int:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {Usuario.table_name()} (" +
                "   id INTEGER PRIMARY KEY AUTOINCREMENT," +
                "   nome VARCHAR(100)," +
                "   segredo VARCHAR(100)" +
                ");"
            )
            conn.commit()

            rows = cursor.fetchall()

        return len(rows)
