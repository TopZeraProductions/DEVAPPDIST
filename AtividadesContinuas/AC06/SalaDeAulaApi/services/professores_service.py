from model.professor import Professor
from infra.professores_log import ProfessorLog

professores_db = []


def listar():
    return professores_db


def localiza(id):
    for p in professores_db:
        if p.id == id:
            return p
    return None


def novo(professor_data):
    novo_professor = localiza(professor_data["id"])
    if novo_professor != None:
        return None
    professores_db.append(Professor.cria(professor_data))
    return professores_db


def remover(id):
    index = 0
    for p in professores_db:
        if p.id == id:
            log = ProfessorLog(p)
            del professores_db[index]
            log.atualiza(p)
            p.finaliza_e_imprime()
            return p
        index = index + 1
    return None


def atualiza(id, professor_data):
    index = 0
    for p in professores_db:
        if p.id == id:
            log = ProfessorLog(p)
            p.atualizar(professor_data)
            log.atualiza(p)
            log.finaliza_e_imprime()
            return p
        index = index + 1
    return None