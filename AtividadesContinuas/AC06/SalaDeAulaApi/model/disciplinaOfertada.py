class DisciplinaOfertada:
    def __init__(self, id, id_disciplina, id_professor, ano, semestre, turma):
        self.id = id
        self.id_disciplina = id_disciplina
        self.id_professor = id_professor
        self.ano = ano
        self.semestre = semestre
        self.turma = turma

    def atualizar(self, dados):
        try:
            id = dados["id"]
            id_disciplina = dados["id_disciplina"]
            id_professor = dados["id_professor"]
            ano = dados["ano"]
            semestre = dados["semestre"]
            turma = dados["turma"]
            self.id, self.id_disciplina, self.id_professor, \
            self.ano, self.semestre, self.turma\
            = id, id_disciplina, id_professor, ano, semestre, turma 
            return self
        except Exception as e:
            print("Problema ao criar novo professor!")
            print(e)
            raise ValueError()

    def __dict__(self):
        d = dict()
        d['id'] = self.id
        d["id_disciplina"] = self.id_disciplina
        d["id_professor"] = self.id_professor
        d["ano"] = self.ano
        d["semestre"] = self.semestre
        d["turma"] = self.turma
        return d

    @staticmethod
    def cria(dados):
        try:
            id = dados["id"]
            id_disciplina = dados["id_disciplina"]
            id_professor = dados["id_professor"]
            ano = dados["ano"]
            semestre = dados["semestre"]
            turma = dados["turma"]
            return DisciplinaOfertada(id=id, id_disciplina=id_disciplina, id_professor=id_professor, ano=ano, semestre=semestre, turma=turma)
        except Exception as e:
            print("Problema ao criar novo professor!")
            print(e)
            raise ValueError()