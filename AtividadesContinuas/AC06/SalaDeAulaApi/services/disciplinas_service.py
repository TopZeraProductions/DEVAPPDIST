from model.disciplina import Disciplina
from infra.disciplinas_log import DisciplinaLog

disciplinas_db = []

def listar():
    return disciplinas_db

def localiza(id):
    for p in disciplinas_db:
        if p.id == id:
            return p
    return None

def novo(disciplina_data):
    nova_disciplina = localiza(disciplina_data["id"])
    if nova_disciplina != None:
        return None
    disciplinas_db.append(Disciplina.cria(disciplina_data))
    return disciplinas_db

def remover(id):
    index = 0
    for p in disciplinas_db:
        if p.id == id:
            log = DisciplinaLog(p)
            del disciplinas_db[index]
            log.atualiza(p)
            p.finaliza_e_imprime()
            return p
        index = index + 1
    return None

def atualiza(id, disciplina_data):
    index = 0
    for p in disciplinas_db:
        if p.id == id:
            log = DisciplinaLog(p)
            p.atualizar(disciplina_data)
            log.atualiza(p)
            log.finaliza_e_imprime()
            return p
        index = index + 1
    return None