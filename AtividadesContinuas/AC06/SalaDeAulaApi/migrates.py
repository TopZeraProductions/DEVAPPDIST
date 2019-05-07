from model.professor import Professor
from model.aluno import Aluno
from model.coordenador import Coordenador
from model.curso import Curso


class Migrations:
    def __init__(self):
        pass

    def migrate_all(self):
        print(">>> making Migrations: <<<")
        self.migrate_professor()
        self.migrate_aluno()
        self.migrate_coordenador()
        self.migrate_cursos()

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
