from persistencia import *
from cadastro import *

nome = input('Nome: ')
categoria = input('Categoria: ')
qtd = int(input('Quantidade: '))
preco_venda = float(input('Preco venda: '))
preco_compra = float(input('Preco compra: '))
fornecedor = input('Fornecedor: ')
estoque_minimo = int(input('Etoque mínimo: '))

p = Produto(nome, categoria,preco_venda, preco_compra, qtd, fornecedor, estoque_minimo)
persistencia = PersistenciaProduto()
persistencia.adicionar(p)

#fornecedor = Fornecedores('Nome','02.234.67/0001-89','telefone','email','endereço')
#f = PersistenciaFornecedores()
#f.adicionar(fornecedor)