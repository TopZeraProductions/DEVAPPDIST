from model.aluno import Aluno
from infra.alunos_log import AlunoLog

alunos_db = []

def listar():
    return alunos_db

def localiza(id):
    for p in alunos_db:
        if p.id == id:
            return p
    return None

def novo(aluno_data):
    novo_aluno = localiza(aluno_data["id"])
    if novo_aluno != None:
        return None
    alunos_db.append(Aluno.cria(aluno_data))
    return alunos_db

def remover(id):
    index = 0
    for p in alunos_db:
        if p.id == id:
            log = AlunoLog(p)
            del alunos_db[index]
            log.atualiza(p)
            p.finaliza_e_imprime()
            return p
        index = index + 1
    return None

def atualiza(id, aluno_data):
    index = 0
    for p in alunos_db:
        if p.id == id:
            log = AlunoLog(p)
            p.atualizar(aluno_data)
            log.atualiza(p)
            log.finaliza_e_imprime()
            return p
        index = index + 1
    return None