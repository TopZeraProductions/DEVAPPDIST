class Disciplina:
    def __init__(self, id, nome, data, status, plano_ensino, carga_horaria, id_coordenador):
        self.id = id
        self.nome = nome
        self.data = data
        self.status = status
        self.plano_ensino = plano_ensino
        self.carga_horaria = carga_horaria
        self.id_coordenador = id_coordenador

    def atualizar(self, dados):
        try:
            id = dados["id"]
            nome = dados["nome"]
            data = dados["data"]
            status = dados["status"]
            plano_ensino = dados["plano_ensino"]
            carga_horaria = dados["carga_horaria"]
            id_coordenador = dados["id_coordenador"]
            self.id, self.nome, self.data, self.status, \
            self.plano_ensino, self.carga_horaria, self.id_coordenador \
            = id, nome, data, status, plano_ensino, carga_horaria, id_coordenador
            return self
        except Exception as e:
            print("Problema ao criar novo professor!")
            print(e)
            raise ValueError()

    def __dict__(self):
        d = dict()
        d['id'] = self.id
        d['nome'] = self.nome
        d["data"] = self.data
        d["status"] = self.status
        d["plano_ensino"] = self.plano_ensino
        d["carga_horaria"] = self.carga_horaria
        d["id_coordenador"] = self.id_coordenador
        return d

    @staticmethod
    def cria(dados):
        try:
            id = dados["id"]
            nome = dados["nome"]
            data = dados["data"]
            status = dados["status"]
            plano_ensino = dados["plano_ensino"]
            carga_horaria = dados["carga_horaria"]
            id_coordenador = dados["id_coordenador"]
            return Disciplina(id=id, nome=nome, data=data, status=status, plano_ensino=plano_ensino, carga_horaria=carga_horaria, id_coordenador=id_coordenador)
        except Exception as e:
            print("Problema ao criar novo professor!")
            print(e)
            raise ValueError()