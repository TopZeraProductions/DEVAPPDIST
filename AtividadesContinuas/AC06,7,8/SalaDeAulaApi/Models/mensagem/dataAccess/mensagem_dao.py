import sqlite3
from typing import Dict, List
from Models.mensagem.entities.mensagem import Mensagem


class MensagemDAO:

    @staticmethod
    def db(where: str = "") -> List[Mensagem]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            query = f" SELECT id, id_remetente, id_destinatario, data_hora, texto FROM  {Mensagem.table_name()}"
            query += f" WHERE {where} " if where != "" else " WHERE 1 = 1 "

            cursor.execute(query)

            data = [Mensagem.to_tuple(item) for item in cursor.fetchall()]

            conn.commit()

        return data

    @staticmethod
    def list_all() -> List[Mensagem]:
        return MensagemDAO.db()

    @staticmethod
    def find(id: int) -> Mensagem:
        data = MensagemDAO.db(f" id = {id} ")
        if len(data) > 0:
            return data[0]

        return Mensagem()

    @staticmethod
    def new(novo_registro: Dict[str, str]) -> List[Mensagem]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"INSERT INTO {Mensagem.table_name()} (id_remetente, id_destinatario, data_hora, texto ) "
                f"VALUES (:id_remetente, :id_destinatario, :data_hora, :texto )",
                novo_registro
            )

            conn.commit()

        return MensagemDAO.list_all()

    @staticmethod
    def update(novo_registro: Dict[str, str]) -> List[Mensagem]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"UPDATE {MensagemDAO.table_name()} "
                f"SET id_remetente=:id_remetente, id_destinatario=:id_destinatario, data_hora=:data_hora, texto=:texto  "
                f"WHERE id == :id ",
                novo_registro
            )

            conn.commit()

        return MensagemDAO.list_all()

    @staticmethod
    def delete(id_aluno: int = 0) -> List[Mensagem]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"DELETE FROM {Mensagem.table_name()} WHERE id == ?",
                [id_aluno]
            )

            conn.commit()

        return MensagemDAO.list_all()
