import sqlite3

connection = sqlite3.connect('banco_dados')
cursor = connection.cursor()

cursor.execute("create table cliente ( id integer, nome varchar(100) )")
cursor.execute("insert into cliente(id, nome) values (1, 'zezinho')")

cursor.execute("select id, nome from cliente")
rows = cursor.fetchall()

cursor.close()

print(rows)