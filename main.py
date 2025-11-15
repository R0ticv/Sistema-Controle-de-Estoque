from persistencia import *


p = Produto('Nome', 'Categoria,' 'preco_compra','preco_venda', 'qtd_inicial', 'fornecedor' )
persistencia = PersistenciaProduto()
persistencia.adicionar(p)