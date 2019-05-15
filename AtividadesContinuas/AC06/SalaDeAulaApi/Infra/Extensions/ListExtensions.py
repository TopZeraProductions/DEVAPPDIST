class MyList(list):
    def __init__(self, lista: list = list()):
        super().__init__()
        self.extend(lista)

    def foreach(self, expr) -> None:
        for index, element in enumerate(self):
            expr(element)

    def map(self, expr):
        what = MyList()
        for index, element in enumerate(self):
            what.append(expr(element))

        return what

    def any(self, expr) -> bool:
        for index, element in enumerate(self):
            if expr(element):
                return True

        return False

    def where(self, expr):
        list = MyList()
        for index, element in enumerate(self):
            if expr(element):
                list.append(element)

        return list


lista_teste = MyList()
lista_teste.append({"Nome": "Joao", "idade": 80})
lista_teste.append({"Nome": "maria", "idade": 25})
lista_teste.append({"Nome": "Jose", "idade": 14})
lista_teste.append({"Nome": "adamastor", "idade": 18})
lista_teste.append({"Nome": "sergio", "idade": 20})

list2 = []
lista_teste.foreach(
     lambda c:
        list2.append(c["Nome"])
)

print(
    lista_teste.any(
        lambda c: c["Nome"] == "jose"
    )
)

list_where = lista_teste.where(
    lambda c: (c["Nome"] == "maria" or c["idade"] > 20)
)

list_map = lista_teste.map(
    lambda c: {"nome_pessoa": c["Nome"] + ", " + str(c["idade"])}
)


print(list_where)
print(list2)
print(list_map)
