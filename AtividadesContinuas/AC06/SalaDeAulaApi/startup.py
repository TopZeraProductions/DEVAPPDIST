from flask import Flask, jsonify

from APP.alunos_api import alunos_app
from APP.disciplinas_api import disciplinas_app
from APP.coordenadores_api import coordenadores_app
from APP.cursos_api import cursos_app
from APP.disciplinasOfertadas_api import disciplinasOfertadas_app
from APP.solicitacoesMatriculas_api import solicitacoesMatriculas_app
from APP.professores_api import professores_app

from DAL.migrates import Migrations

database = {}

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

