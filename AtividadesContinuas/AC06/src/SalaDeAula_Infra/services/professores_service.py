from model.professor import Professor
from infra.professores_log import ProfessorLog

professores_db = []

def listar():
    return professores_db

def localiza(matricula):
    for p in professores_db:
        if p.matricula == matricula:
            return p
    return None

def novo(professor_data):
    professores_db.append(Professor.cria(professor_data))
    return professores_db

def remover(matricula):
    index = 0
    for p in professores_db:
        if p.id == matricula:
            log = ProfessorLog(p)
            del professores_db[index]
            log.atualiza(p)
            p.finaliza_e_imprime()
            return p
        index = index + 1
    return None

def atualiza(matricula, professor_data):
    index = 0
    for p in professores_db:
        if p.matricula == matricula:
            log = ProfessorLog(p)
            p.atualizar(professor_data)
            log.atualiza(p)
            log.finaliza_e_imprime()
            return p
        index = index + 1
    return None