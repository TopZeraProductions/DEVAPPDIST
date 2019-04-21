from model.professor import Professor

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
            del professores_db[index]
            return p
        index = index + 1
    return None

def atualiza(matricula, professor_data):
    index = 0
    for p in professores_db:
        if p.matricula == matricula:
            p.atualizar(professor_data)
            return p
        index = index + 1
    return None