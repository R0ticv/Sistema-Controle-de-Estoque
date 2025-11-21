from persistencia import *
from cadastro import *

p = Produto('Outro Nome','Categoria', 16.8, 22.8, 10, 'Fornecedor')
persistencia = PersistenciaProduto()
#persistencia.adicionar(p)
persistencia.remover('')
""" fornecedor = Fornecedores('Nome','02.234.567/0001-89','telefone','email','endereço')
f = PersistenciaFornecedores()
f.adicionar(fornecedor) """