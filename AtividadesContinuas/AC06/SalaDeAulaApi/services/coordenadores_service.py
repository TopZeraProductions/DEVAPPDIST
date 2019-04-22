from model.coordenador import Coordenador
from infra.coordenadores_log import CoordenadorLog

coordenadores_db = []

def listar():
    return coordenadores_db

def localiza(id):
    for p in coordenadores_db:
        if p.id == id:
            return p
    return None

def novo(coordenador_data):
    novo_coordenador = localiza(coordenador_data["id"])
    if novo_coordenador != None:
        return None
    coordenadores_db.append(Coordenador.cria(coordenador_data))
    return coordenadores_db

def remover(id):
    index = 0
    for p in coordenadores_db:
        if p.id == id:
            log = CoordenadorLog(p)
            del coordenadores_db[index]
            log.atualiza(p)
            p.finaliza_e_imprime()
            return p
        index = index + 1
    return None

def atualiza(id, coordenador_data):
    index = 0
    for p in coordenadores_db:
        if p.id == id:
            log = CoordenadorLog(p)
            p.atualizar(coordenador_data)
            log.atualiza(p)
            log.finaliza_e_imprime()
            return p
        index = index + 1
    return None