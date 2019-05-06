from flask import Flask, jsonify
from controllers.alunos_api import alunos_app, alunos_db
from controllers.professores_api import professores_app, professores_db
from controllers.disciplinas_api import disciplinas_app, disciplinas_db
from controllers.coordenadores_api import coordenadores_app, coordenadores_db
from controllers.cursos_api import cursos_app, cursos_db
from controllers.disciplinasOfertadas_api import disciplinasOfertadas_app, disciplinasOfertadas_db
from controllers.solicitacoesMatriculas_api import solicitacoesMatriculas_app, solicitacoesMatriculas_db
import sqlite3


database = {
    "ALUNOS": alunos_db,
    "PROFESSORES": professores_db,
    "COORDENADORES": coordenadores_db,
    "CURSOS": cursos_db,
    "DISCIPLINAS_OFERTADAS": disciplinasOfertadas_db,
    "DISCIPLINAS": disciplinas_db,
    "SOLICITACOES_MATRICULAS": solicitacoesMatriculas_db,
}

app = Flask(__name__)

app.register_blueprint(alunos_app)
app.register_blueprint(professores_app)
app.register_blueprint(coordenadores_app)
app.register_blueprint(cursos_app)
app.register_blueprint(disciplinasOfertadas_app)
app.register_blueprint(disciplinas_app)
app.register_blueprint(solicitacoesMatriculas_app)


@app.route('/')
def all():
    return jsonify(database)


'''
if input("deseja criar o bd? S/N: ") == "S":
    with sqlite3.connect('DATABASE') as conn:
        cursor = conn.cursor()

        cursor.execute("CREATE TABLE professor (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), matricula VARCHAR(100))")
        conn.commit()

        rows = cursor.fetchall()
'''

app.run(host='localhost', port=5080, debug=True)

