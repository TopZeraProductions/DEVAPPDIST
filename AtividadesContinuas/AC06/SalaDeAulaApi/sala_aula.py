from flask import Flask, jsonify, request
from alunos_api import alunos_app, alunos_db
from professores_api import professores_app, professores_db
from disciplinas_api import disciplinas_app, disciplinas_db
from coordenadores_api import coordenadores_app, coordenadores_db
from cursos_api import cursos_app, cursos_db
from disciplinasOfertadas_api import disciplinasOfertadas_app, disciplinasOfertadas_db
from solicitacoesMatriculas_api import solicitacoesMatriculas_app, solicitacoesMatriculas_db

database = {
    "ALUNOS" : alunos_db,
    "PROFESSORES" : professores_db,
    "COORDENADORES" : coordenadores_db,
    "CURSOS" : cursos_db,
    "DISCIPLINAS_OFERTADAS" : disciplinasOfertadas_db,
    "DISCIPLINAS" : disciplinas_db,
    "SOLICITACOES_MATRICULAS" : solicitacoesMatriculas_db,
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


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
