class Coordenador:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def atualizar(self, dados):
        try:
            id = dados["id"]
            nome = dados["nome"]
            self.id, self.nome = id, nome
            return self
        except Exception as e:
            print("Problema ao criar novo coordenador!")
            print(e)
            raise ValueError()

    def __dict__(self):
        d = dict()
        d['id'] = self.id
        d['nome'] = self.nome
        return d

    @staticmethod
    def cria(dados):
        try:
            id = dados["id"]
            nome = dados["nome"]
            return Coordenador(id=id, nome=nome)
        except Exception as e:
            print("Problema ao criar novo coordenador!")
            print(e)
            raise ValueError()