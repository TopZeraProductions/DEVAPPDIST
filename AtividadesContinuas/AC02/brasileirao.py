import json

def datas_de_jogo(dados):
    return dados["fases"]["2700"]["jogos"]["data"].keys()

def data_de_um_jogo(dados,
                    id_jogo):
    try:
        return dados["fases"]["2700"]["jogos"]["id"][str(id_jogo)]["data"]

    except:

        return "nao encontrado"

def ids_dos_times_de_um_jogo(dados,id_jogo):
    time1 = dados["fases"]["2700"]["jogos"]["id"][str(id_jogo)]["time1"]
    time2 = dados["fases"]["2700"]["jogos"]["id"][str(id_jogo)]["time1"]

    return time1, time2 #assim a gente retorna as duas respostas em um unico return

def nome_do_time(dados, id_time):

    return dados["equipes"][str(id_time)]["nome-comum"]

def nomes_dos_times_de_um_jogo(dados, id_jogo):

    id_time1, id_time2 = ids_dos_times_de_um_jogo(dados, id_jogo)

    nome1 = dados["equipes"][str(id_time1)]["nome-comum"]
    nome2 = dados["equipes"][str(id_time2)]["nome-comum"]

    return nome1, nome2


def id_do_time(dados,
               nome_time):

    for key, value in dados["equipes"].items():
        if(value["nome-comum"] == nome_time):
            return key

    return "nao encontrado"

def busca_imprecisa_por_nome_de_time(dados, nome_time):
    results = []
    for key, value in dados["equipes"].items():
        if  (nome_time in value["nome-comum"]) or \
            (nome_time in value["nome-slug"]) or \
            (nome_time in value["sigla"]) or \
            (nome_time in value["nome"]) :

            results.append(key)

    return results


def ids_de_jogos_de_um_time(dados,time_id):
    results=[]
    for key, value in dados["fases"]["2700"]["jogos"]["id"].items():
        if (value["time1"] == time_id or value["time2"] == time_id):
            results.append(key)

    return results


def datas_de_jogos_de_um_time(dados,nome_time):
    ids = busca_imprecisa_por_nome_de_time(dados, nome_time)

    datas = []
    for id_jogo, jogo in dados["fases"]["2700"]["jogos"]["id"].items():
        if (jogo["time1"] == ids[0] or jogo["time2"] == ids[0]):
            datas.append(jogo["data"])

    return datas


def dicionario_de_gols(dados):

    dicionario_time_gols = {}
    for id_jogo, jogo in dados["fases"]["2700"]["jogos"]["id"].items():

        dicionario_time_gols[jogo["time1"]] = dicionario_time_gols.get(jogo["time1"], 0) + int(jogo["placar1"])

        dicionario_time_gols[jogo["time2"]] = dicionario_time_gols.get(jogo["time2"], 0) + int(jogo["placar2"])


    return dicionario_time_gols

def time_que_fez_mais_gols(dados):
    dict = dicionario_de_gols(dados)

    rank = [0, 0]
    for i, v in dict.items():
        if int(v) > rank[1]:
            rank[1] = int(v)
            rank[0] = i

    return rank[0]

def dicionario_id_estadio_e_nro_jogos(dados):
    dicionario_jogos_estadio = {}
    for id_jogo, jogo in dados["fases"]["2700"]["jogos"]["id"].items():

        dicionario_jogos_estadio[jogo["estadio_id"]] = dicionario_jogos_estadio.get(jogo["estadio_id"], 0) + 1

    return dicionario_jogos_estadio


def qtos_libertadores(dados):
    return int(dados["fases"]["2700"]["faixas-classificacao"]["classifica1"]["faixa"].split("-")[1])

def qtos_brasileirao(dados):
    zona = dados["fases"]["2700"]["faixas-classificacao"]["classifica3"]["faixa"].split("-")
    z1 , z2 = zona[0], zona[1]
    return int(z2) - int(z1)

def ids_dos_melhor_classificados(dados, numero):
    melhores = []
    for index in range(0, numero):
        melhores.append(dados["fases"]["2700"]["classificacao"]["grupo"]["Único"][index])

    return melhores

def classificados_libertadores(dados):
    return ids_dos_melhor_classificados(dados, qtos_libertadores(dados))

def rebaixados(dados):
    rebaixados = []
    for index in range(len(dados["fases"]["2700"]["classificacao"]["grupo"]["Único"])):
        rebaixados.append(dados["fases"]["2700"]["classificacao"]["grupo"]["Único"][index])

    return rebaixados[len(rebaixados) - (qtos_brasileirao(dados) + 1) : len(rebaixados)]

def classificacao_do_time_por_id(dados, time_id):
    for index, id in enumerate(dados["fases"]["2700"]["classificacao"]["grupo"]["Único"]):
        if id == time_id:
            return index + 1

    return "nao encontrado"


import unittest

class TestClientes(unittest.TestCase):
    def test_01_datas_de_jogo(self):
        dados = pega_dados()
        datas = datas_de_jogo(dados)
        self.assertEqual(len(datas), 107)
        self.assertTrue('2018-04-14' in datas)
        self.assertTrue('2018-07-26' in datas)
        self.assertTrue('2018-10-26' in datas)

    def test_02_datas_de_jogo(self):
        dados = pega_dados()
        del dados['fases']['2700']['jogos']['data']['2018-04-14']
        datas = datas_de_jogo(dados)
        self.assertEqual(len(datas), 106)
        self.assertFalse('2018-04-14' in datas)
        self.assertTrue('2018-07-26' in datas)
        self.assertTrue('2018-10-26' in datas)

    def test_03_data_de_um_jogo(self):
        dados = pega_dados()
        self.assertEqual(data_de_um_jogo(dados,'102132'),'2018-05-06')
        self.assertEqual(data_de_um_jogo(dados,'102187'),'2018-06-06')
        self.assertEqual(data_de_um_jogo(dados,'102540'),'nao encontrado')

    def test_04_ids_dos_times_de_um_jogo(self):
        dados = pega_dados()
        t1,t2 = ids_dos_times_de_um_jogo(dados,'102099')
        self.assertTrue(t1 in ['5','17'])
        self.assertTrue(t2 in ['5','17'])
        t1,t2 = ids_dos_times_de_um_jogo(dados,'102109')
        self.assertTrue(t1 in ['1','26'])
        self.assertTrue(t2 in ['1','26'])
    
    def test_05_nome_do_time(self):
        dados = pega_dados()
        self.assertEqual(nome_do_time(dados,'1'),'Flamengo')
        self.assertEqual(nome_do_time(dados,'695'),'Chapecoense')
    
    def test_06_nomes_dos_times_de_um_jogo(self):
        dados = pega_dados()
        t1,t2 = nomes_dos_times_de_um_jogo(dados,'102099')
        self.assertTrue(t1 in ['Botafogo','Palmeiras'])
        self.assertTrue(t2 in ['Botafogo','Palmeiras'])
        t1,t2 = nomes_dos_times_de_um_jogo(dados,'102109')
        self.assertTrue(t1 in ['Flamengo','América-MG'])
        self.assertTrue(t2 in ['Flamengo','América-MG'])

    def test_07_id_do_time(self):
        dados = pega_dados()
        self.assertEqual(id_do_time(dados,'Cruzeiro'),'9')
        self.assertEqual(id_do_time(dados,'Athletico'),'3')

    def test_08_busca_imprecisa_por_nome_de_time(self):
        dados = pega_dados()
        ids_times = busca_imprecisa_por_nome_de_time(dados,'Paulo')
        self.assertTrue('24' in ids_times)
        ids_times = busca_imprecisa_por_nome_de_time(dados,'SPA')
        self.assertTrue('24' in ids_times)
        ids_times = busca_imprecisa_por_nome_de_time(dados,'anto')
        self.assertTrue('22' in ids_times)
    
    def test_09_ids_de_jogos_de_um_time(self):
        dados = pega_dados()
        jogos_chapeco = ids_de_jogos_de_um_time(dados,'695')
        self.assertEqual(len(jogos_chapeco),38)
        self.assertTrue('102330' in jogos_chapeco)
        self.assertTrue('102422' in jogos_chapeco)
        jogos_santos = ids_de_jogos_de_um_time(dados,'22')
        self.assertEqual(len(jogos_santos),38)
        self.assertTrue('102208' in jogos_santos)
        self.assertTrue('102259' in jogos_santos)
    
    def test_10_datas_de_jogos_de_um_time(self):
        dados = pega_dados()
        datas_santos = datas_de_jogos_de_um_time(dados,'Santos')
        self.assertEqual(len(datas_santos),38)
        self.assertTrue('2018-04-21' in datas_santos)
        self.assertTrue('2018-10-13' in datas_santos)
        datas_chapeco = datas_de_jogos_de_um_time(dados,'Chapecoense')
        self.assertEqual(len(datas_chapeco),38)
        self.assertTrue('2018-11-25' in datas_chapeco)
        self.assertTrue('2018-12-02' in datas_chapeco)
    
    def test_11_dicionario_de_gols(self):
        dados = pega_dados()
        dic_gols = dicionario_de_gols(dados)

        self.assertEqual(dic_gols['695'],34)
        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['jogos']['id']['102330']['placar2']=1
        dic_gols = dicionario_de_gols(dados)
        self.assertEqual(dic_gols['695'],35)
        dados['fases']['2700']['jogos']['id']['102422']['placar2']=2
        dic_gols = dicionario_de_gols(dados)
        self.assertEqual(dic_gols['695'],36)
        dados['fases']['2700']['jogos']['id']['102422']['placar2']=12
        dic_gols = dicionario_de_gols(dados)
        self.assertEqual(dic_gols['695'],46)
    
    def test_12_time_que_fez_mais_gols(self):
        dados = pega_dados()
        time = time_que_fez_mais_gols(dados)
        self.assertEqual(time,'17')
        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['jogos']['id']['102422']['placar2']=120
        time = time_que_fez_mais_gols(dados)
        self.assertEqual(time,'695')

    def test_13_dicionario_id_estadio_e_nro_jogos(self):
        dados = pega_dados()
        estadios = dicionario_id_estadio_e_nro_jogos(dados)
        self.assertEqual(estadios['72'],16)
        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['jogos']['id']['102097']['estadio_id']='72'
        estadios = dicionario_id_estadio_e_nro_jogos(dados)
        self.assertEqual(estadios['72'],17)

    def test_14_qtos_libertadores(self):
        dados = pega_dados()
        self.assertEqual(qtos_libertadores(dados),6)
        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['faixas-classificacao']['classifica1']['faixa']='1-8'
        self.assertEqual(qtos_libertadores(dados),8)


    def test_15_ids_dos_melhor_classificados(self):
        dados = pega_dados()
        self.assertEqual(ids_dos_melhor_classificados(dados,10),["17","1","15","13","24","4","3","9","5","22"])
        self.assertEqual(ids_dos_melhor_classificados(dados,5),["17","1","15","13","24"])
        self.assertEqual(ids_dos_melhor_classificados(dados,3),["17","1","15"])

    def test_16_classificados_libertadores(self):
        dados = pega_dados()
        self.assertEqual(classificados_libertadores(dados),["17","1","15","13","24","4"])
        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['faixas-classificacao']['classifica1']['faixa']='1-8'
        self.assertEqual(classificados_libertadores(dados),["17","1","15","13","24","4","3","9"])
    
    def test_17_rebaixados(self):
        dados = pega_dados()
        self.assertEqual(rebaixados(dados),['76', '26', '21', '18'])
        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['faixas-classificacao']['classifica3']['faixa']='15-20'
        self.assertEqual(rebaixados(dados),['33','25','76', '26', '21', '18'])

    def test_18_classificacao_do_time_por_id(self):
        dados = pega_dados()
        self.assertEqual(classificacao_do_time_por_id(dados,'17'),1)
        self.assertEqual(classificacao_do_time_por_id(dados,'30'),11)
        self.assertEqual(classificacao_do_time_por_id(dados,'695'),14)
        self.assertEqual(classificacao_do_time_por_id(dados,'1313'),'nao encontrado')



def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestClientes)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

def pega_dados():
    with open('ano2018.json') as f:
        dados = json.load(f)

    return dados

dados2018 = pega_dados()

if __name__ == '__main__':
    runTests()
    # print(data_de_um_jogo(dados2018, 102540))