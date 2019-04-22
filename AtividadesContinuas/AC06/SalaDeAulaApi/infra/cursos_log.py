from datetime import datetime
class CursoLog():
    def __init__(self, curso):
        self.original_data = curso.__dict__()
        self.ultima_atualizacao = curso.__dict__()
        self.start_time = datetime.now()

    def atualiza(self, curso):
        self.ultima_atualizacao = curso.__dict__()

    def finaliza_e_imprime(self):
        print(f'Mudanças iniciaram em {self.start_time}')
        print(f'Valor original:')
        print(self.original_data)
        print(f'Valor final:')
        print(self.ultima_atualizacao)
        print(f'Mudanças finalizaram em {datetime.now()}')
