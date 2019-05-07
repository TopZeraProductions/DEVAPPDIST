import sqlite3
from model.coordenador import Coordenador
from typing import Dict, List


class CoordenadorServices:
    @staticmethod
    def db(where: str = "") -> List[Coordenador]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            query = f" SELECT id, nome FROM  {Coordenador.table_name()}"
            query += f" WHERE {where} " if where != "" else " WHERE 1 = 1 "

            cursor.execute(query)

            data = [Coordenador.to_tuple(item) for item in cursor.fetchall()]

            conn.commit()

        return data

    @staticmethod
    def list_all() -> List[Coordenador]:
        return CoordenadorServices.db()

    @staticmethod
    def find(id: int) -> Coordenador:
        data = CoordenadorServices.db(f" id = {id} ")
        if len(data) > 0:
            return data[0]

        return Coordenador()

    @staticmethod
    def new(novo_coordenador: Dict[str, str]) -> List[Coordenador]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"INSERT INTO {Coordenador.table_name()} (nome) VALUES (:nome)",
                novo_coordenador
            )

            conn.commit()

        return CoordenadorServices.list_all()

    @staticmethod
    def update(novo_coordenador: Dict[str, str]) -> List[Coordenador]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"UPDATE {Coordenador.table_name()} SET nome = :nome WHERE id == :id ",
                novo_coordenador
            )

            conn.commit()

        return CoordenadorServices.list_all()

    @staticmethod
    def delete(id_aluno: int = 0) -> List[Coordenador]:
        with sqlite3.connect('DATABASE') as conn:
            cursor = conn.cursor()

            cursor.execute(
                f"DELETE FROM {Coordenador.table_name()} WHERE id == ?",
                [id_aluno]
            )

            conn.commit()

        return CoordenadorServices.list_all()
