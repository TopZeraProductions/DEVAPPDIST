from model.disciplinaOfertada import DisciplinaOfertada
from infra.disciplinasOfertadas_log import DisciplinaOfertadaLog

disciplinasOfertadas_db = []

def listar():
    return disciplinasOfertadas_db

def localiza(id):
    for p in disciplinasOfertadas_db:
        if p.id == id:
            return p
    return None

def novo(disciplinaOfertada_data):
    nova_disciplinaOfertada = localiza(disciplinaOfertada_data["id"])
    if nova_disciplinaOfertada != None:
        return None
    disciplinasOfertadas_db.append(DisciplinaOfertada.cria(disciplinaOfertada_data))
    return disciplinasOfertadas_db

def remover(id):
    index = 0
    for p in disciplinasOfertadas_db:
        if p.id == id:
            log = DisciplinaOfertadaLog(p)
            del disciplinasOfertadas_db[index]
            log.atualiza(p)
            p.finaliza_e_imprime()
            return p
        index = index + 1
    return None

def atualiza(id, disciplinaOfertada_data):
    index = 0
    for p in disciplinasOfertadas_db:
        if p.id == id:
            log = DisciplinaOfertadaLog(p)
            p.atualizar(disciplinaOfertada_data)
            log.atualiza(p)
            log.finaliza_e_imprime()
            return p
        index = index + 1
    return None