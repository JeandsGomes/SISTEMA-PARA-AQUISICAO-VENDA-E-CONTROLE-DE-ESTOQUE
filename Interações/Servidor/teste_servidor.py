from cadastrar import Cadastro

cadastro = Cadastro()

#CADASTRO
#cadastro.sqlite_create_fornecedor('Sao_geraldo',1,'Beasil','Rua Maria','089994353256','Maria')
#cadastro.sqlite_create_fornecedor('Corote',3,'Beasil','Rua Maria','089994353256','Maria')
#print(cadastro.sqlite_readSec_fornecedor_todos())
#ATUALIZAÇÃO
#print(cadastro.sqlite_readSec_fornecedor(1))
#cadastro.sqlite_update_fornecedor('Seu_geraldo',1,'Beasil','Rua Maria','089994353256','Maria')
#print(cadastro.sqlite_readSec_fornecedor(1))
#REMOCAO
#cadastro.sqlite_create_fornecedor('Montes',4,'Beasil','Rua Cherindro','089994353256','Maria')
#print(cadastro.sqlite_readSec_fornecedor_todos())
#cadastro.sqlite_remove_fornecedor(4)
#print(cadastro.sqlite_readSec_fornecedor_todos())

#CADASTRO
#cadastro.sqlite_create_cliente('Jeanderson',1,'Av.Maria Lina','07-03-2000','jenander@gmail.com','089994353256')
#cadastro.sqlite_create_cliente('Alfredo',3,'Av.Maria Lina','07-03-2000','jenander@gmail.com','089994353256')
#print(cadastro.sqlite_readSec_cliente_todos())
#ATUALIZACAO
#print(cadastro.sqlite_readSec_cliente(1))
#cadastro.sqlite_update_cliente('Juventos',1,'Av.Maria Lina','07-03-2000','jenander@gmail.com','089994353256')
#print(cadastro.sqlite_readSec_cliente(1))
#REMOCAO
#cadastro.sqlite_create_cliente('Bernardo',5,'Av.Coelho','07-03-2000','jenander@gmail.com','089994353256')
#print(cadastro.sqlite_readSec_cliente_todos())
#cadastro.sqlite_remove_cliente(5)
#print(cadastro.sqlite_readSec_cliente_todos())

#cadastro.sqlite_create_funcionario('jeanderson',1,'2-3-2000','jeands@gmail.com','08999453','vendedor','123')
#cadastro.sqlite_read_funcionario(1,'123')

#CADASTRA
#cadastro.sqlite_create_produto('2','sao_geraldo','3-5-2000','4-5-2002','Em locais pouco Umidos',30,'Ala 4 estante 3',5.00,20.00,1)
#cadastro.sqlite_create_produto('3','montes','3-5-2021','4-5-2021','Em locais pouco Umidos',30,'Ala 4 estante 3',5.00,20.00,1)
#print(cadastro.sqlite_read_produto_todos())
#ATUALIZACAO
#print(cadastro.sqlite_read_produto('2'))
#cadastro.sqlite_update_produto('2','Vinicola','3-5-2000','4-5-2000','Em locais pouco Umidos',30,'Ala 4 estante 3',5.00,20.00,1)
#print(cadastro.sqlite_read_produto('2'))
#REMOCAO
#cadastro.sqlite_create_produto('4','coisa nossa','3-5-2021','4-5-2021','Em locais pouco Umidos',30,'Ala 4 estante 3',5.00,20.00,1)
#print(cadastro.sqlite_read_produto_todos())
#cadastro.sqlite_remove_produto('4')
#print(cadastro.sqlite_read_produto_todos())

#cadastro.sqlite_create_venda('Catao','10-09-2000','2',1,1,'123')
cadastro.sqlite_read_venda_todas()