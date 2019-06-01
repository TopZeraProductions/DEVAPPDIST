import requests
import json

host = "http://localhost:5000/"


def main():
    while 1:
        print("--------------interface----------------")
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
            cadastrar_mensagem()
        else:
            break


def listar_usuarios():
    r = requests.get(host+"usr")
    print(r.content)


def cadastrar_usuario():
    usu = input("Digite o usuário: ")
    data = json.dumps({"nome": str(usu)})

    response = requests.post(url=host+"usr",
                             data=data,
                             headers={'Content-type': 'application/json', 'Accept': 'text/plain'})

    retorno_api = str(response.content)

    print(type(retorno_api))

    if retorno_api is dict:
        print("Seu novo ID:" + retorno_api["nome"] + " sua nova KEY: " + retorno_api["segredo"])
    else:
        print(retorno_api)


def listar_mensagem():
    usuario = input("Digite seu ID")
    segredo = input("Digite seu segredo")

    r = requests.get(host+"msg/"+usuario+"?segredo="+segredo)
    print(r.content)


def cadastrar_mensagem():
    de = int(input("Digite o usuário: "))
    para = int(input("Digite o usuário: "))
    texto = input("Digite a mensagem: ")
    segredo = input("Digite a mensagem: ")
    data = {"de": int(de), "para": int(para), "segredo": str(segredo), "texto": str(texto)}
    js = json.dumps(data)
    print(js)


if __name__ == '__main__':
    main()
