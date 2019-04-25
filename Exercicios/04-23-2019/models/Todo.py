class Todo:
    def __init__(self, text_arg, situacao_arg="pendente"):
        self.__texto = text_arg
        self.__situacao = situacao_arg

    def to_list(self):
        result = dict()
        result['texto'] = self.__texto
        result['situacao'] = self.__situacao
        return result
