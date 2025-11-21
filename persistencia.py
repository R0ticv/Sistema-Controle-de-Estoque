from cadastro import *
import json
import os
class ProdutoRepetidoException(Exception):
    ...

class CnpjRepetidoException(Exception):
    ...

class TelefoneRepetidoException(Exception):
    ...

class EmailRepetidoException(Exception):
    ...

class PersistenciaProduto:
    def __init__(self, arquivo = 'produto.json' ):
        self.__arquivo = arquivo
        if not os.path.exists(self.__arquivo):
            with open(self.__arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump([], arquivo, ensure_ascii=False, indent=4)
        
        try:
            with open(self.__arquivo, 'r', encoding='utf-8') as f_json:
                self.dados = json.load(f_json)

        except (json.JSONDecodeError, FileNotFoundError):
            self.dados = []
            with open(self.__arquivo, 'w', encoding='utf-8') as f_json:
                json.dump([], f_json, ensure_ascii=False,indent=4)

    def ler(self):
        with open(self.__arquivo,'r', encoding='utf-8') as arquivo_json:
            return json.load(arquivo_json)

    def salvar(self, dados):
        with open(self.__arquivo, 'w',encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, ensure_ascii=False,indent=4,)

    def adicionar(self, produto : Produto):
        dados = self.ler()

        nome_novo = ((produto.nome).strip()).capitalize()
        categoria_nova = ((produto.categoria).strip()).capitalize()
        fornecedor_novo = ((produto.fornecedor).strip()).capitalize()

        for item in dados:
            if (item['nome'].strip().capitalize() == nome_novo and item['categoria'].strip().capitalize() == categoria_nova and item['fornecedor'].strip().capitalize() == fornecedor_novo):
                raise ProdutoRepetidoException(f"O produto: '{nome_novo}', da categoria: '{categoria_nova}', do fornecedor: '{fornecedor_novo}' já existe")
            
        dados.append(produto.para_dict())
        self.salvar(dados)

    def atualizar(self, id : Produto):
        dados = self.ler()

    def remover(self, id_produto: str):
        dados = self.ler()
        encontrar = False
        for item in dados[:]:
            if item['id'] == id_produto:
                dados.remove(item)
                encontrar = True
                break   
        if not encontrar:
            raise ValueError(f"Produto com ID '{id_produto}' não encontrado.")

        self.salvar(dados)

class PersistenciaFornecedores:
    def __init__(self, arquivo = 'fornecedor.json' ):
        self.__arquivo = arquivo
        if not os.path.exists(self.__arquivo):
            with open(self.__arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump([], arquivo, ensure_ascii=False,indent=4)
        
        try:
            with open(self.__arquivo, 'r', encoding='utf-8') as f_json:
                self.dados = json.load(f_json)

        except (json.JSONDecodeError, FileNotFoundError):
            self.dados = []
            with open(self.__arquivo, 'w',encoding='utf-8') as f_json:
                json.dump([], f_json, ensure_ascii=False,indent=4)

    def ler(self):
        with open(self.__arquivo,'r', encoding='utf-8') as arquivo_json:
            return json.load(arquivo_json)

    def salvar(self, dados):
        with open(self.__arquivo, 'w',encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, ensure_ascii=False, indent=4,)

    def adicionar(self, fornecedor : Fornecedores):
        dados = self.ler()


        cnpj_novo = (fornecedor.cnpj).strip()
        telefone_novo = (fornecedor.telefone).strip()
        email_novo = (fornecedor.email).strip()

        for item in dados:
            if (item['cnpj'].strip() == cnpj_novo):
                raise CnpjRepetidoException(f"O cnpj: '{fornecedor.cnpj}' já está cadastrado.")
            if(item['telefone'].strip() == telefone_novo):
                raise TelefoneRepetidoException(f"O telefone: '{fornecedor.telefone}' já está cadastrado")
            if(item['email'].strip() == email_novo):
                raise EmailRepetidoException(f"O email: '{fornecedor.email}' já está cadastrado")

        dados.append(fornecedor.para_dict())
        self.salvar(dados)

        #Os itens serão mostrados na tabela/Interface
    def editar(self, cnpj : Fornecedores):
        dados = self.ler()
    
    def remover(self, cnpj : Fornecedores):
        dados = self.ler()
        for item in dados:
            if (item['cnpj'] == cnpj.cnpj):
                dados.remove(item)
                self.salvar(dados)