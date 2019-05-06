import sqlite3
from model.professor import Professor


def listar():
    with sqlite3.connect('DATABASE') as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT id, nome, matricula FROM professor")

        professores_db = [Professor.to_tupla(item) for item in cursor.fetchall()]

        print(professores_db)

        conn.commit()

    return professores_db


def novo(novo_professor):
    with sqlite3.connect('DATABASE') as conn:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO professor (nome, matricula) VALUES (:nome, :matricula)",
            novo_professor
        )

        conn.commit()
        return listar()
