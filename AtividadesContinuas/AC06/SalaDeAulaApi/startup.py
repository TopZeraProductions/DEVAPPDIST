from flask import Flask, jsonify

from App.alunos_api import alunos_app
from App.disciplinas_api import disciplinas_app
from App.coordenadores_api import coordenadores_app
from App.cursos_api import cursos_app
from App.disciplinasOfertadas_api import disciplinasOfertadas_app
from App.solicitacoesMatriculas_api import solicitacoesMatriculas_app
from App.professores_api import professores_app
from App.usuario_api import usuarios_app
from App.mensagem_api import mensagens_app

from Models.migrates import Migrations

database = {}

app = Flask(__name__)

app.register_blueprint(alunos_app)
app.register_blueprint(professores_app)
app.register_blueprint(coordenadores_app)
app.register_blueprint(cursos_app)
app.register_blueprint(disciplinasOfertadas_app)
app.register_blueprint(disciplinas_app)
app.register_blueprint(solicitacoesMatriculas_app)
app.register_blueprint(usuarios_app)
app.register_blueprint(mensagens_app)


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

