from model.professor import Professor
from model.aluno import Aluno
from model.coordenador import Coordenador
from model.curso import Curso
from model.disciplina import Disciplina


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
