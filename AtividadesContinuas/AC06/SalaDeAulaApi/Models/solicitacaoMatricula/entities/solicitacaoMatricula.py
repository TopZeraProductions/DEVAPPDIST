import sqlite3
from typing import Dict, Tuple


class SolicitacaoMatricula:
    def __init__(self,
                 id_solicitacao:         int = 0,
                 id_aluno:               int = 0,
                 id_disciplina_ofertada: int = 0,
                 dt_solicitacao:         str = 0,
                 id_coordenador:         int = 0,
                 status:                 str = 0):

        self.id:                     int = id_solicitacao
        self.id_aluno:               int = id_aluno
        self.id_disciplina_ofertada: int = id_disciplina_ofertada
        self.dt_solicitacao:         str = dt_solicitacao
        self.id_coordenador:         int = id_coordenador
        self.status:                 str = status

    def to_dictionary(self) -> Dict[str, str]:
        dictionary = dict()
        dictionary['id']                     = self.id
        dictionary['id_aluno']               = self.id_aluno
        dictionary['id_disciplina_ofertada'] = self.id_disciplina_ofertada
        dictionary['dt_solicitacao']         = self.dt_solicitacao
        dictionary['id_coordenador']         = self.id_coordenador
        dictionary['status']                 = self.status

        return dictionary

    @staticmethod
    def to_tuple(tupla: Tuple[int, int, int, str, int, str]):
        return SolicitacaoMatricula(
            id_solicitacao=tupla[0],
            id_aluno=tupla[1],
            id_disciplina_ofertada=tupla[2],
            dt_solicitacao=tupla[3],
            id_coordenador=tupla[4],
            status=tupla[5],
        )

    @staticmethod
    def create(dados: Dict[str, str]) -> object:
        try:
            id_solicitacao = dados["id"]
            id_aluno = dados["id_aluno"]
            id_disciplina_ofertada = dados["id_disciplina_ofertada"]
            dt_solicitacao = dados["dt_solicitacao"]
            id_coordenador = dados["id_coordenador"]
            status = dados["status"]

            return SolicitacaoMatricula(
                id_solicitacao=int(id_solicitacao),
                id_aluno=int(id_aluno),
                id_disciplina_ofertada=int(id_disciplina_ofertada),
                dt_solicitacao=dt_solicitacao,
                id_coordenador=int(id_coordenador),
                status=status
            )
        except Exception as e:
            print("Problema ao criar novo Solicitacao de matricula! " + e)
            raise ValueError()

    @staticmethod
    def table_name() -> str:
        return "tb_solicitacao_matricula"

    @staticmethod
    def migrate_table() -> int:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {SolicitacaoMatricula.table_name()} ("
                f"      id INTEGER PRIMARY KEY AUTOINCREMENT,"
                f"      id_aluno 			  INT,"
                f"      id_disciplina_ofertada INT,"
                f"      id_coordenador	      INT,"
                f"      dt_solicitacao		  DATETIME,"
                f"      status 				  varchar,"
                f"      FOREIGN KEY (id_aluno) 				REFERENCES tb_aluno(id),"
                f"      FOREIGN KEY (id_coordenador) 	    REFERENCES tb_coordenador(id),"
                f"      FOREIGN KEY (id_disciplina_ofertada) REFERENCES tb_disciplina_ofertada(id)"
                f");"
            )
            conn.commit()

            rows = cursor.fetchall()

        return len(rows)
