class Professor:
    def __init__(self, id, nome, matricula):
        self.id = id
        self.nome = nome
        self.matricula = matricula

    def atualizar(self, dados):
        try:
            id = dados["id"]
            nome = dados["nome"]
            matricula = dados["matricula"]
            self.id, self.nome, self.matricula = id, nome, matricula
            return self
        except Exception as e:
            print("Problema ao criar novo professor!")
            print(e)
            raise ValueError()

    def __dict__(self):
        d = dict()
        d['id'] = self.id
        d['nome'] = self.nome
        d['matricula'] = self.matricula
        return d

    def to_dictionary(self):
        d = dict()
        d['id'] = self.id
        d['nome'] = self.nome
        d['matricula'] = self.matricula
        return d

    @staticmethod
    def to_tupla(tupla):
        return Professor(id=tupla[0], nome=tupla[1], matricula=tupla[2])

    @staticmethod
    def cria(dados):
        try:
            id = dados["id"]
            nome = dados["nome"]
            matricula = dados["matricula"]
            return Professor(id=id, nome=nome, matricula=matricula)
        except Exception as e:
            print("Problema ao criar novo professor!")
            print(e)
            raise ValueError()