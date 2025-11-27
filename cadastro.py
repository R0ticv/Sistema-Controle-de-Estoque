import uuid
import re

class PrecoCompraNaoFloatExcpetion(Exception):
    ...

class PrecoVendaNaoFloatExcpetion(Exception):
    ...

class QtdNaoIntException(Exception):
    ...

class CnpjFormatoInvalidoException(Exception):
    ...

class Produto:
    def __init__(self, nome, categoria, preco_compra, preco_venda, qtd, fornecedor, estoque_minimo):
        self.__id = str(uuid.uuid4())
        self.__nome = nome
        self.__categoria = categoria
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.qtd = qtd
        self.__fornecedor = fornecedor
        self.estoque_minimo = estoque_minimo

    #Nome
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, n):
        self.__nome = n
    
    #ID
    @property
    def id(self):
        return self.__id
    
    #Categoria
    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, c):
        self.__categoria = c

    #Preço Compra
    @property
    def preco_compra(self):
        return self.__preco_compra
    
    @preco_compra.setter
    def preco_compra(self, pc):
        if isinstance(pc, int):
            pc = float(pc)
        if not isinstance(pc, float):
            raise PrecoCompraNaoFloatExcpetion('Valor Preço Compra Inválido')
        self.__preco_compra = pc

    # Preço Venda
    @property
    def preco_venda(self):
        return self.__preco_venda
    
    @preco_venda.setter
    def preco_venda(self, pv):
        if isinstance(pv, int):
            pv = float(pv)
        if not isinstance(pv, float):
            raise PrecoVendaNaoFloatExcpetion('Valor Preço Venda Inválido')
        self.__preco_venda = pv
    

    @property
    def qtd(self):
        return self.__qtd
    
    @qtd.setter
    def qtd(self, qi):
        if not isinstance(qi, int):
            raise QtdNaoIntException('Valor Quantidade Inválido')
        self.__qtd = qi

    @property
    def fornecedor(self):
        return self.__fornecedor
    
    def __repr__(self):
        return f'Nome: {self.nome}\nID: {self.id}\nCategoria: {self.categoria}\nPreço Compra R${self.preco_compra}\nPreço Venda: R${self.preco_venda}\nQuantidade Inicial: {self.qtdl}'
    
    def para_dict(self):
        return {
            "id": self.id,
            "nome": ((self.nome).strip()).capitalize(),
            "categoria": ((self.categoria).strip()).capitalize(),
            "preco_compra": self.preco_compra,
            "preco_venda": self.preco_venda,
            "qtd": self.qtd,
            "estoque_minimo": self.estoque_minimo,
            "fornecedor": self.fornecedor
        }

class Fornecedores:
    def __init__(self, nome, cnpj, telefone, email, endereco):
        self.__nome = nome
        self.cnpj = cnpj
        self.__telefone = telefone
        self.__email = email
        self.__endereco = endereco

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, n):
        self.__nome = n

    @property
    def cnpj(self):
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, c):
        match = re.search(r"[0-9]{2}.[0-9]{3}.[0-9]{3}/[0]{3}[1]{1}-[0-9]{2}", c)
        if not match:
            raise CnpjFormatoInvalidoException('CNPJ Formato Inválido')
        else:
            self.__cnpj = c
    
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, t):
        #Match, telefone
        self.__telefone = t

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, s):
        self.__email = s

    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, e):
        self.__endereco = e
    
    def __repr__(self):
        return f'Nome: {self.nome}\nCNPJ: {self.cnpj}\nTelefone: {self.telefone}\nEmail: {self.email}\nEndereço: {self.endereco}\n'
    
    def para_dict(self):
        return {
            "nome": ((self.nome).strip()).capitalize(),
            "cnpj": self.cnpj,
            "telefone": self.telefone,
            "email": self.email,
            "endereço": self.endereco,
        }
    