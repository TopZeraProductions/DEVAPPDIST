import sqlite3
from typing import Dict, Tuple


class DisciplinaOfertada:
    def __init__(self,
                 id_ofertada:   int = 0,
                 id_disciplina: int = 0,
                 id_professor:  int = 0,
                 ano:           str = "",
                 semestre:      int = 0,
                 turma:         int = 0):
        self.id:            int = id_ofertada
        self.id_disciplina: int = id_disciplina
        self.id_professor:  int = id_professor
        self.ano:           str = ano
        self.semestre:      int = semestre
        self.turma:         int = turma

    def to_dictionary(self) -> Dict[str, str]:
        dictionary = dict()
        dictionary['id'] = self.id
        dictionary['id_disciplina'] = self.id_disciplina
        dictionary['id_professor'] = self.id_professor
        dictionary['ano'] = self.ano
        dictionary['semestre'] = self.semestre
        dictionary['turma'] = self.turma

        return dictionary

    @staticmethod
    def to_tuple(tupla: Tuple[int, int, int, str, int, int]):
        return DisciplinaOfertada(
            id_ofertada=tupla[0],
            id_disciplina=tupla[1],
            id_professor=tupla[2],
            ano=tupla[3],
            semestre=tupla[4],
            turma=tupla[5])

    @staticmethod
    def create(dados: Dict[str, str]) -> object:  # typing: DisciplinaOfertada
        try:
            id:            int = int(dados["id"])
            id_disciplina: int = int(dados["id_disciplina"])
            id_professor:  int = int(dados["id_professor"])
            ano:           str = dados["ano"]
            semestre:      int = int(dados["semestre"])
            turma:         int = int(dados["turma"])

            return DisciplinaOfertada(id_ofertada=id,
                                      id_disciplina=id_disciplina,
                                      id_professor=id_professor,
                                      ano=ano,
                                      semestre=semestre,
                                      turma=turma)

        except Exception as e:
            print("Problema ao criar nova DisciplinaOfertada! " + e)
            raise ValueError()

    @staticmethod
    def table_name() -> str:
        return "tb_disciplina_ofertada"

    @staticmethod
    def migrate_table() -> int:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {DisciplinaOfertada.table_name()}(" +
                f"   id 			INTEGER PRIMARY KEY AUTOINCREMENT," +
                f"   id_disciplina  INTEGER," +
                f"   id_professor   INTEGER," +
                f"   ano            VARCHAR(100)," +
                f"   semestre       INT," +
                f"   turma          INT," +
                f"   FOREIGN KEY (id_disciplina) REFERENCES tb_disciplina(id)," +
                f"   FOREIGN KEY (id_professor) REFERENCES tb_professor(id)" +
                f");"
            )

            conn.commit()

            rows = cursor.fetchall()

        return len(rows)
