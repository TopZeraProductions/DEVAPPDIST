from Models.aluno.entities.aluno import Aluno
from Models.professor.entities.professor import Professor
from Models.coordenador.entities.coordenador import Coordenador
from Models.curso.entities.curso import Curso
from Models.disciplina.entities.disciplina import Disciplina
from Models.disciplinaOfertada.entities.disciplinaOfertada import DisciplinaOfertada
from Models.solicitacaoMatricula.entities.solicitacaoMatricula import SolicitacaoMatricula
from Models.usuario.entities.usuario import Usuario
from Models.mensagem.entities.mensagem import Mensagem


class Migrations:
    def __init__(self):
        pass

    def migrate_all(self):
        print(">>> making Migrations: <<<")
        self.migrate_professor()
        self.migrate_aluno()
        self.migrate_coordenador()
        self.migrate_cursos()
        self.migrate_disciplina()
        self.migrate_disciplina_ofertada()
        self.migrate_solicitacao_matricula()
        self.migrate_usuario()
        self.migrate_mensagem()

    @staticmethod
    def migrate_professor():
        print("\tmake: ", Professor.table_name())
        Professor.migrate_table()

    @staticmethod
    def migrate_cursos():
        print("\tmake: ", Curso.table_name())
        Curso.migrate_table()

    @staticmethod
    def migrate_aluno():
        print("\tmake: ", Aluno.table_name())
        Aluno.migrate_table()

    @staticmethod
    def migrate_coordenador():
        print("\tmake: ", Coordenador.table_name())
        Coordenador.migrate_table()

    @staticmethod
    def migrate_disciplina():
        print("\tmake: ", Disciplina.table_name())
        Disciplina.migrate_table()

    @staticmethod
    def migrate_disciplina_ofertada():
        print("\tmake: ", DisciplinaOfertada.table_name())
        DisciplinaOfertada.migrate_table()

    @staticmethod
    def migrate_solicitacao_matricula():
        print("\tmake: ", SolicitacaoMatricula.table_name())
        SolicitacaoMatricula.migrate_table()

    @staticmethod
    def migrate_usuario():
        print("\tmake: ", Usuario.table_name())
        Usuario.migrate_table()

    @staticmethod
    def migrate_mensagem():
        print("\tmake: ", Mensagem.table_name())
        Mensagem.migrate_table()
