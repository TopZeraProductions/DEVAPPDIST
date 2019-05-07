import sqlite3
from typing import Dict, Tuple


class Disciplina:
    def __init__(self,
                 id_disciplina:  int = 0,
                 nome:           str = "",
                 data:           str = "",
                 status:         str = "",
                 plano_ensino:   str = "",
                 carga_horaria:  str = "",
                 id_coordenador: int = 0):

        self.id = id_disciplina
        self.nome = nome
        self.data = data
        self.status = status
        self.plano_ensino = plano_ensino
        self.carga_horaria = carga_horaria
        self.id_coordenador = id_coordenador

    def to_dictionary(self) -> Dict[str, str]:
        d = dict()
        d['id'] = self.id
        d['nome'] = self.nome
        return d

    @staticmethod
    def to_tuple(tupla: Tuple[int, str]):
        return Curso(id_curso=tupla[0], nome=tupla[1])

    @staticmethod
    def create(dados: Dict[str, str]) -> object:
        try:
            id = dados["id"]
            nome = dados["nome"]
            return Curso(id_curso=int(id), nome=nome)
        except Exception as e:
            print("Problema ao criar novo Curso! " + e)
            raise ValueError()

    @staticmethod
    def table_name() -> str:
        return "tb_curso"

    @staticmethod
    def migrate_table() -> int:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {Curso.table_name()} (" +
                "   id INTEGER PRIMARY KEY AUTOINCREMENT,"                 +
                "   nome VARCHAR(100)"                                     +
                ");"
            )
            conn.commit()

            rows = cursor.fetchall()

        return len(rows)
