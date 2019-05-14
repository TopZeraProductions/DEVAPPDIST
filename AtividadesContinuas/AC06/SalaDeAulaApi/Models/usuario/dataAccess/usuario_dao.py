import sqlite3
from typing import Dict, List
from Models.usuario.entities.usuario import Usuario


class UsuarioDAO:

    @staticmethod
    def db(where: str = "") -> List[Usuario]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            query = f" SELECT id, nome, segredo FROM  {Usuario.table_name()}"
            query += f" WHERE {where} " if where != "" else " WHERE 1 = 1 "

            print(">>>>>  ", query)

            cursor.execute(query)

            data = [Usuario.to_tuple(item) for item in cursor.fetchall()]

            conn.commit()

        return data

    @staticmethod
    def list_all() -> List[Usuario]:
        return UsuarioDAO.db()

    @staticmethod
    def find(id: int) -> Usuario:
        data = UsuarioDAO.db(f" id = {id} ")
        if len(data) > 0:
            return data[0]

        return Usuario()

    @staticmethod
    def new(novo_registro: Dict[str, str]) -> List[Usuario]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"INSERT INTO {Usuario.table_name()} (nome, segredo) VALUES (:nome, :segredo)",
                novo_registro
            )

            conn.commit()

        return UsuarioDAO.list_all()

    @staticmethod
    def update(novo_registro: Dict[str, str]) -> List[Usuario]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"UPDATE {Usuario.table_name()} SET nome = :nome, segredo = :segredo WHERE id == :id ",
                novo_registro
            )

            conn.commit()

        return UsuarioDAO.list_all()

    @staticmethod
    def delete(id_aluno: int = 0) -> List[Usuario]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"DELETE FROM {Usuario.table_name()} WHERE id == ?",
                [id_aluno]
            )

            conn.commit()

        return UsuarioDAO.list_all()
