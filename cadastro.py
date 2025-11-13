import uuid

class PrecoCompraNaoFloatExcpetion(Exception):
    ...

class PrecoVendaNaoFloatExcpetion(Exception):
    ...

class QtdNaoIntException(Exception):
    ...
    
class Produto:
    def __init__(self, nome, categoria, preco_compra, preco_venda, qtd_inicial):
        self.__id = str(uuid.uuid4())
        self.__nome = nome
        self.__categoria = categoria
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.qtd_inicial = qtd_inicial

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
    
    # Quantidade Inicial

    @property
    def qtd_inicial(self):
        return self.__qtd_inical
    
    @qtd_inicial.setter
    def qtd_inicial(self, qi):
        if not isinstance(qi, int):
            raise QtdNaoIntException('Valor Quantidade Inválido')
        self.__qtd_inical = qi

    def __repr__(self):
        return f'Nome: {self.nome}\nID: {self.id}\nCategoria: {self.categoria}\nPreço Compra R${self.preco_compra}\nPreço Venda: R${self.preco_venda}\nQuantidade Inicial: {self.qtd_inicial}'
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "categoria": self.categoria,
            "preco_compra": self.preco_compra,
            "preco_venda": self.preco_venda,
            "qtd_inicial": self.qtd_inicial
        }


class Fornecedores:
    def __init__(self, nome, cnpj, telefone, email, endereco):
        self.__nome = nome
        self.__cnpj = cnpj
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
        self.__cnpj = c
    
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, t):
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

""" try:
    p = Produto('Carne', 'Comida', 50 ,50, 15.2)
except PrecoCompraNaoFloatExcpetion as e:
    print(e)
except PrecoVendaNaoFloatExcpetion as e:
    print(e)
except QtdNaoIntException as e:
    print(e)

f = Fornecedores('Vitarella', '12323283', '83 984330946', 'emailmuitolegal@gmail.com', 'Rua Comerciante Incrível, 29\n') 
"""

