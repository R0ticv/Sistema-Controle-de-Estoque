from cadastro import *
from abc import ABC, abstractmethod

class Persistencia(ABC):
    def __init__(self, nome_arquivo):
        self.__nome_arquivo = nome_arquivo

    @abstractmethod
    def salvar(self):
        ...

    @abstractmethod
    def recuperar(self):
        ...

class PersistenciaProduto(Persistencia):

    def salvar(self):
        ...

    def recuperar(self):
        ...
