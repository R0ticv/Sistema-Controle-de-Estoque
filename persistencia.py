from cadastro import *
import json
import os
from abc import ABC, abstractmethod

class Persistencia(ABC):
    @abstractmethod
    def salvar(self):
        ...

    @abstractmethod
    def recuperar(self):
        ...

class PersistenciaProduto(Persistencia):
    def __init__(self, arquivo = 'produto.json' ):
        self.__nome_arquivo = arquivo
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, "w") as p:
                json.dump([], p)
        
    def salvar(self):
        ...

    def recuperar(self):
        ...
