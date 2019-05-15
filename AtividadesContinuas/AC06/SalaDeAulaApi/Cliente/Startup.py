import json
import requests 


def main():
    while 1:
        print("Ola seja bem vindo!!")
        print("Digite a opçao desejada!!")
        print("1 ==> cadastrar usuario")
        print("2 ==> visualizar mensagens")
        print("3 ==> enviar nova mensagem")
        print("outro ==> sair")

        option = int(input())

        if option == 1:
            cadastrar_usuario()
        elif option == 2:
            listar_mensagem()
        elif option == 3:
            listar_mensagem()
        else:
            break


def listar_usuarios():
    r = requests.get("http://localhost:5080/usr")
    print(r.content)


def cadastrar_usuario():
    usu = input("Digite o usuário: ")
    data = json.dumps({"nome": str(usu)})

    response = requests.post(url="http://localhost:5080/usr",
                             data=data,
                             headers={'Content-type': 'application/json', 'Accept': 'text/plain'})
    print(response.content)


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
