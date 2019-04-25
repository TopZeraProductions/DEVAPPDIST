from models.Todo import Todo


class TodoServices:
    def __init__(self):
        self.__database = []

    def list(self):
        return self.__database

    def create_todo(self, todo):
        self.__database.append(todo)

