from typing import List, Dict, Any


class UtilRetorno:
    def __init__(self):
        self.error: bool = False
        self.listMessages: List[str] = []
        self.object: object = object

    def add_message(self, value):
        self.listMessages.append(value)

    def to_string(self) -> str:
        ret = str(self.error)
        ret += f" {self.listMessages}"
        ret += f" {self.object}"

        return ret

    def to_dictionary(self) -> Dict[str, Any]:
        d = dict()
        d["error"]        = self.error
        d["listMessages"] = self.listMessages,
        d["object"]       = self.object

        return d
