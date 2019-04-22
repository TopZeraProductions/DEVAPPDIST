from model.curso import Curso
from infra.cursos_log import CursoLog

cursos_db = []

def listar():
    return cursos_db

def localiza(id):
    for p in cursos_db:
        if p.id == id:
            return p
    return None

def novo(curso_data):
    novo_curso = localiza(curso_data["id"])
    if novo_curso != None:
        return None
    cursos_db.append(Curso.cria(curso_data))
    return cursos_db

def remover(id):
    index = 0
    for p in cursos_db:
        if p.id == id:
            log = CursoLog(p)
            del cursos_db[index]
            log.atualiza(p)
            p.finaliza_e_imprime()
            return p
        index = index + 1
    return None

def atualiza(id, curso_data):
    index = 0
    for p in cursos_db:
        if p.id == id:
            log = CursoLog(p)
            p.atualizar(curso_data)
            log.atualiza(p)
            log.finaliza_e_imprime()
            return p
        index = index + 1
    return None