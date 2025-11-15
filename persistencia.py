from cadastro import *
import json
import os
class ProdutoRepetidoException(Exception):
    ...

class PersistenciaProduto:
    def __init__(self, arquivo = 'produto.json' ):
        self.__arquivo = arquivo
        if not os.path.exists(self.__arquivo):
            with open(self.__arquivo, "w") as arquivo:
                json.dump([], arquivo)
        
        try:
            with open(self.__arquivo, "r") as f_json:
                self.dados = json.load(f_json)

        except json.JSONDecodeError:
            self.dados = []
            with open(self.__arquivo, "w") as f_json:
                json.dump([], f_json, indent=4)

    def ler(self):
        with open(self.__arquivo,'r') as arquivo_json:
            return json.load(arquivo_json)

    def salvar(self, dados):
        with open(self.__arquivo, 'w',encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, indent=4,ensure_ascii=False)

    def adicionar(self, produto : Produto):
        dados = self.ler()

        nome_novo = ((produto.nome).strip()).capitalize()
        categoria_nova = ((produto.categoria).strip()).capitalize()
        fornecedor_novo = ((produto.fornecedor).strip()).capitalize()

        for item in dados:
            if (item["nome"].strip().capitalize() == nome_novo and item["categoria"].strip().capitalize() == categoria_nova and item["fornecedor"].strip().capitalize() == fornecedor_novo):
                raise ProdutoRepetidoException("O produto: '{nome_novo}', da categoria: '{categoria_nova}', do fornecedor: '{fornecedor_novo}' já existe")
            
        dados.append(produto.para_dict())
        self.salvar(dados)

        #Os itens serão mostrados na tabela/Interface
    def atualizar(self):
        dados = self.ler()

    def remover(self):
        ...