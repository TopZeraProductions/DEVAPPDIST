from typing import Dict, Tuple
import sqlite3


class Coordenador:
    def __init__(self, id_coordenador: int = 0, nome: str = ""):
        self.id = id_coordenador
        self.nome = nome

    def to_dictionary(self) -> Dict[str, str]:
        d = dict()
        d['id'] = self.id
        d['nome'] = self.nome
        return d

    @staticmethod
    def to_tuple(tupla: Tuple[int, str]):
        return Coordenador(id_coordenador=tupla[0], nome=tupla[1])

    @staticmethod
    def create(dados: Dict[str, str]) -> object:
        try:
            id = dados["id"]
            nome = dados["nome"]
            return Coordenador(id_coordenador=int(id), nome=nome)
        except Exception as e:
            print("Problema ao criar novo coordenador! " + e)
            raise ValueError()

    @staticmethod
    def table_name() -> str:
        return "tb_coordenador"

    @staticmethod
    def migrate_table() -> int:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {Coordenador.table_name()} (" +
                f"   id INTEGER PRIMARY KEY AUTOINCREMENT,"                 +
                f"   nome VARCHAR(100)"                                     +
                f");"
            )
            conn.commit()

            rows = cursor.fetchall()

        return len(rows)
