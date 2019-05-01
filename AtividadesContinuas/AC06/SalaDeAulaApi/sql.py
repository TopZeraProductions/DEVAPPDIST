import sqlite3

with sqlite3.connect('DATABASE') as conn:
    cursor = conn.cursor()

    cursor.execute("DROP TABLE cliente")
    cursor.execute("CREATE TABLE cliente ( id INTEGER, nome VARCHAR(100))")
    cursor.execute("INSERT INTO cliente(id, nome) VALUES(1, 'joao')")
    cursor.execute("INSERT INTO cliente(id, nome) VALUES(2, 'jose')")
    cursor.execute("INSERT INTO cliente(id, nome) VALUES(3, 'maria')")
    cursor.execute("INSERT INTO cliente(id, nome) VALUES(4, 'joaquim')")
    cursor.execute("INSERT INTO cliente(id, nome) VALUES(5, 'etelvina')")
    cursor.execute("INSERT INTO cliente(id, nome) VALUES(6, 'lorenzo')")

    inp = input("nome: ")

    cursor.execute("INSERT INTO cliente(id, nome) VALUES (6, ?)", [inp])
    cursor.execute("insert into cliente(id, nome) values (0, ?)", ("Joe",))
    cursor.execute("SELECT id, nome FROM cliente")

    rows = cursor.fetchall()
    conn.commit()

print(rows)
