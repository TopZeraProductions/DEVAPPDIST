from flask import Flask, jsonify

from api.alunos_api import alunos_app
from api.disciplinas_api import disciplinas_app, disciplinas_db
from api.coordenadores_api import coordenadores_app
from api.cursos_api import cursos_app, cursos_db
from api.disciplinasOfertadas_api import disciplinasOfertadas_app, disciplinasOfertadas_db
from api.solicitacoesMatriculas_api import solicitacoesMatriculas_app, solicitacoesMatriculas_db
from api.professores_api import professores_app

from migrates import Migrations

database = {
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


@app.route('/migrate')
def migrate():
    return jsonify(database)


Mig = Migrations()

Mig.migrate_all()

app.run(
    host='localhost',
    port=5080,
    debug=True
)

