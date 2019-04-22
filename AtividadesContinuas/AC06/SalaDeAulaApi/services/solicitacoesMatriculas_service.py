from model.solicitacaoMatricula import SolicitacaoMatricula
from infra.solicitacoesMatriculas_log import SolicitacaoMatriculaLog

solicitacoesMatriculas_db = []

def listar():
    return solicitacoesMatriculas_db

def localiza(id):
    for p in solicitacoesMatriculas_db:
        if p.id == id:
            return p
    return None

def novo(solicitacaoMatricula_data):
    nova_solicitacaoMatricula = localiza(solicitacaoMatricula_data["id"])
    if nova_solicitacaoMatricula != None:
        return None
    solicitacoesMatriculas_db.append(SolicitacaoMatricula.cria(solicitacaoMatricula_data))
    return solicitacoesMatriculas_db

def remover(id):
    index = 0
    for p in solicitacoesMatriculas_db:
        if p.id == id:
            log = SolicitacaoMatriculaLog(p)
            del solicitacoesMatriculas_db[index]
            log.atualiza(p)
            p.finaliza_e_imprime()
            return p
        index = index + 1
    return None

def atualiza(id, solicitacaoMatricula_data):
    index = 0
    for p in solicitacoesMatriculas_db:
        if p.id == id:
            log = SolicitacaoMatriculaLog(p)
            p.atualizar(solicitacaoMatricula_data)
            log.atualiza(p)
            log.finaliza_e_imprime()
            return p
        index = index + 1
    return None