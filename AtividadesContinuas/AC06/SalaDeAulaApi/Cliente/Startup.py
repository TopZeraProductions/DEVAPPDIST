import json
import requests 

def listar_usuarios():
    r = requests.get("http://localhost:5080/usr")
    print(r.content)

def cadastrar_usuario():
    usu = input("Digite o usuário: ")
    data = {"nome": str(usu)}
    js = json.dumps(data)
    print(js)

    r = requests.post(url="http://localhost:5080/usr", data=js, headers={'Content-type': 'application/json', 'Accept': 'text/plain'}) 
    print (r.content)

cadastrar_usuario()
exit(0)

def listar_mensagem():
    r = requests.get("http://localhost:5080/msg")
    print(r.content)


def cadastrar_mensagem():    
    de = int(input("Digite o usuário: "))
    para = int(input("Digite o usuário: "))
    texto = input("Digite a mensagem: ")
    segredo = input("Digite a mensagem: ")
    data = {"de": int(de), "para": int(para), "segredo": str(segredo), "texto": str(texto)}
    js = json.dumps(data)
    print(js)


r = requests.post(url="http://localhost:5080/msg", data=js, headers={'Content-type': 'application/json', 'Accept': 'text/plain'}) 
print (r.content)


cadastrar_mensagem()