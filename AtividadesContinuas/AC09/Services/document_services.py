from Models.document_model import Document
from Models.document_dao import DocumentDAO

from typing import List, Dict


class DocumentServices:
    @staticmethod
    def list_all() -> List[Document]:
        return DocumentDAO.list_all()

    @staticmethod
    def find(id: int) -> Document:
        return DocumentDAO.find(id)

    @staticmethod
    def new(novo_registro: Dict[str, str]) -> List[Document]:
        return DocumentDAO.new(novo_registro)

    @staticmethod
    def update(novo_registro: Dict[str, str]) -> List[Document]:
        return DocumentDAO.update(novo_registro)

    @staticmethod
    def delete(id_document: int = 0) -> List[Document]:
        return DocumentDAO.delete(id_document)
