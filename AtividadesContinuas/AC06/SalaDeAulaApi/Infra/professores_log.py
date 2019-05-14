from datetime import datetime
class ProfessorLog():
    def __init__(self, professor):
        self.original_data = professor.__dict__()
        self.ultima_atualizacao = professor.__dict__()
        self.start_time = datetime.now()

    def atualiza(self, professor):
        self.ultima_atualizacao = professor.__dict__()

    def finaliza_e_imprime(self):
        print(f'Mudanças iniciaram em {self.start_time}')
        print(f'Valor original:')
        print(self.original_data)
        print(f'Valor final:')
        print(self.ultima_atualizacao)
        print(f'Mudanças finalizaram em {datetime.now()}')
