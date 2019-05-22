from typing import Dict, Tuple
import sqlite3


class Mensagem:
    def __init__(self, id_mensagem: int = 0, id_remetente: int = 0, id_destinatario: int = 0, data_hora: str = "", texto: str = ""):
        self.id = id_mensagem
        self.id_remetente = id_remetente
        self.id_destinatario = id_destinatario
        self.data_hora = data_hora
        self.texto = texto

    def to_dictionary(self) -> Dict[str, str]:
        dic = dict()
        dic['id'] = self.id
        dic['id_remetente'] = self.id_remetente
        dic['id_destinatario'] = self.id_destinatario
        dic['data_hora'] = self.data_hora
        dic['texto'] = self.texto
        return dic

    @staticmethod
    def to_tuple(tupla: Tuple[int, int, int, str, str]):
        return Mensagem(id_mensagem=tupla[0],
                        id_remetente=tupla[1],
                        id_destinatario=tupla[2],
                        data_hora=tupla[3],
                        texto=tupla[4])

    @staticmethod
    def create(dados: Dict[str, str]) -> object:
        try:
            return Mensagem(id_remetente=int(dados["id_remetente"]),
                            id_destinatario=int(dados["id_destinatario"]),
                            data_hora=dados["data_hora"],
                            texto=dados["texto"])
        except Exception as e:
            print("Problema ao criar nova Mensagem! " + e)
            raise ValueError()

    @staticmethod
    def table_name() -> str:
        return "tb_mensagem"

    @staticmethod
    def migrate_table() -> int:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {Mensagem.table_name()}(" +
                f"   id 			INTEGER PRIMARY KEY AUTOINCREMENT," +
                f"   id_destinatario INTEGER," +
                f"   id_remetente   INTEGER," +
                f"   data_hora      DATETIME," +
                f"   texto          VARCHAR(250)," +
                f"   FOREIGN KEY (id_destinatario) REFERENCES tb_usuario(id)," +
                f"   FOREIGN KEY (id_remetente) REFERENCES tb_usuario(id)" +
                f");"
            )
            conn.commit()

            rows = cursor.fetchall()

        return len(rows)
