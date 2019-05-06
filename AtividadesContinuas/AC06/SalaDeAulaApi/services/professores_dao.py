import sqlite3
from model.professor import Professor


def db(where=""):
    with sqlite3.connect('DATABASE') as conn:
        cursor = conn.cursor()

        query = "SELECT id, nome, matricula FROM professor"
        query += f" WHERE {where}" if where != "" else " 1=1 "

        cursor.execute(query)

        db = [Professor.to_tuple(item) for item in cursor.fetchall()]

        print(db)
        conn.commit()

        return db


def listar():
    return db()


def find(id):
    return db(f" id == {id} ")


def novo(novo_professor):
    with sqlite3.connect('DATABASE') as conn:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO professor (nome, matricula) VALUES (:nome, :matricula)",
            novo_professor
        )

        conn.commit()
        return listar()
