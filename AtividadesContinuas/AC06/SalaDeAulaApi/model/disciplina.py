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

        self.id:             int = id_disciplina
        self.nome:           str = nome
        self.data:           str = data
        self.status:         str = status
        self.plano_ensino:   str = plano_ensino
        self.carga_horaria:  str = carga_horaria
        self.id_coordenador: int = id_coordenador

    def to_dictionary(self) -> Dict[str, str]:
        dictionary = dict()
        dictionary['id'] = self.id
        dictionary['nome'] = self.nome
        dictionary['data'] = self.data
        dictionary['status'] = self.status
        dictionary['plano_ensino'] = self.plano_ensino
        dictionary['carga_horaria'] = self.carga_horaria
        dictionary['id_coordenador'] = self.id_coordenador
        return dictionary

    @staticmethod
    def to_tuple(tupla: Tuple[int, str, str, str, str, str, int]):
        return Disciplina(
                 id_disciplina=tupla[0],
                 nome=tupla[1],
                 data=tupla[2],
                 status=tupla[3],
                 plano_ensino=tupla[4],
                 carga_horaria=tupla[5],
                 id_coordenador=tupla[6])

    @staticmethod
    def create(dados: Dict[str, str]) -> object:  # typing: Disciplina
        try:
            id:             int = int(dados["id"])
            nome:           str = dados["nome"]
            data:           str = dados['data']
            status:         str = dados['status']
            plano_ensino:   str = dados['plano_ensino']
            carga_horaria:  str = dados['carga_horaria']
            id_coordenador: int = int(dados['id_coordenador'])

            return Disciplina(id, nome, data, status, plano_ensino, carga_horaria, id_coordenador)

        except Exception as e:
            print("Problema ao criar nova Disciplina! " + e)
            raise ValueError()

    @staticmethod
    def table_name() -> str:
        return "tb_disciplina"

    @staticmethod
    def migrate_table() -> int:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {Disciplina.table_name()}(" +
                "    id 			INTEGER PRIMARY KEY AUTOINCREMENT,"   +
                "    nome 		    VARCHAR(100),"                            +
                "    data           DATETIME,"                               +
                "    status         VARCHAR(100),"                           +
                "    plano_ensino   VARCHAR(100),"                           +
                "    carga_horaria  VARCHAR(100),"                           +
                "    id_coordenador INTEGER,"                                +
                "    FOREIGN KEY (id_coordenador) REFERENCES tb_coordenador(id)" +
                ");"
            )

            conn.commit()

            rows = cursor.fetchall()

        return len(rows)
