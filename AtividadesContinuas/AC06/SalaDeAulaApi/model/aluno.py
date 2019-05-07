from typing import Dict, List, Tuple
import sqlite3


class Aluno:
    def __init__(self, id_aluno: int = 0, nome: str = "", matricula: str = ""):
        self.id = id_aluno
        self.nome = nome
        self.matricula = matricula

    def to_dictionary(self) -> Dict[str, str]:
        d = dict()
        d['id'] = self.id
        d['nome'] = self.nome
        d['matricula'] = self.matricula
        return d

    @staticmethod
    def to_tuple(tupla: Tuple[int, str, str]):
        return Aluno(id_aluno=tupla[0], nome=tupla[1], matricula=tupla[2])

    @staticmethod
    def create(dados: Dict[str, str]) -> object:
        try:
            id = dados["id"]
            nome = dados["nome"]
            matricula = dados["matricula"]
            return Aluno(id_aluno=int(id), nome=nome, matricula=matricula)
        except Exception as e:
            print("Problema ao criar novo professor! " + e)
            raise ValueError()

    @staticmethod
    def table_name() -> str:
        return "tb_aluno"

    @staticmethod
    def migrate_table() -> int:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {Aluno.table_name()} (" +
                "   id INTEGER PRIMARY KEY AUTOINCREMENT,"           +
                "   nome VARCHAR(100),"                              +
                "   matricula VARCHAR(100)"                          +
                ");"
            )
            conn.commit()

            rows = cursor.fetchall()

        return len(rows)
