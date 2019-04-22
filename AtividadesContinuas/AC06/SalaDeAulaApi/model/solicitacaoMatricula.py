class SolicitacaoMatricula:
    def __init__(self, id, id_aluno, id_disciplina_ofertada, dt_solicitacao, id_coordenador, status):
        self.id = id
        self.id_aluno = id_aluno
        self.id_disciplina_ofertada = id_disciplina_ofertada
        self.dt_solicitacao = dt_solicitacao
        self.id_coordenador = id_coordenador
        self.status = status

    def atualizar(self, dados):
        try:
            id = dados["id"]
            id_aluno = dados["id_aluno"]
            id_disciplina_ofertada = dados["id_disciplina_ofertada"]
            dt_solicitacao = dados["dt_solicitacao"]
            id_coordenador = dados["id_coordenador"]
            status = dados["status"]
            self.id, self.id_aluno, self.id_disciplina_ofertada, \
            self.dt_disciplina, self.id_coordenador, self.status \
            = id, id_aluno, id_disciplina_ofertada, dt_solicitacao, id_coordenador, status
            return self
        except Exception as e:
            print("Problema ao criar nova solicitacao de matricula!")
            print(e)
            raise ValueError()

    def __dict__(self):
        d = dict()
        d['id'] = self.id
        d["id_aluno"] = self.id_aluno
        d["id_disciplina_ofertada"] = self.id_disciplina_ofertada
        d["dt_solicitacao"] = self.dt_solicitacao
        d["id_coordenador"] = self.id_coordenador
        d["status"] = self.status
        return d

    @staticmethod
    def cria(dados):
        try:
            id = dados["id"]
            id_aluno = dados["id_aluno"]
            id_disciplina_ofertada = dados["id_disciplina_ofertada"]
            dt_solicitacao = dados["dt_solicitacao"]
            id_coordenador = dados["id_coordenador"]
            status = dados["status"]
            return SolicitacaoMatricula(id=id, id_aluno=id_aluno, id_disciplina_ofertada=id_disciplina_ofertada,  dt_solicitacao=dt_solicitacao, id_coordenador=id_coordenador, status=status)
        except Exception as e:
            print("Problema ao criar nova solicitacao de matricula!")
            print(e)
            raise ValueError()