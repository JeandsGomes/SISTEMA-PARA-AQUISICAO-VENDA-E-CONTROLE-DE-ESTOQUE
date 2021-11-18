from usuario import plataforma_funcionario

plataforma = plataforma_funcionario()
print(plataforma.cadastro_funcionario('Jeanderson',1,'07-03-2000','jeands@gmail.com','089994353256','Gerente','123'))
print(plataforma.login_funcionario(1,'123'))

#Cliente
#Cadastro
print(plataforma.cadastrar_cliente('Pedro Lucas',2,'AV.Maria Lina','10-20-2000','pedro@gmail.com','899932349'))
print(plataforma.cadastrar_cliente('Gabriel',1,'AV.Maria Lina','10-20-2000','pedro@gmail.com','899932349'))
print(plataforma.cadastrar_cliente('Jeremias',4,'AV.Maria Lina','10-20-2000','pedro@gmail.com','899932349'))
print(plataforma.cadastrar_cliente('Sthefany',3,'Morada nova','10-20-2000','pedro@gmail.com','899932349'))
print(plataforma.cadastrar_cliente('Alencar',5,'AV.Maria Lina','10-20-2000','pedro@gmail.com','899932349'))
print(plataforma.cadastrar_cliente('Celsios',6,'AV.Maria Lina','10-20-2000','pedro@gmail.com','899932349'))
print(plataforma.cadastrar_cliente('Brunildo',7,'AV.Maria Lina','10-20-2000','pedro@gmail.com','899932349'))
print(plataforma.cadastrar_cliente('Filipo',8,'Morada nova','10-20-2000','pedro@gmail.com','899932349'))

#Buscar
#print(plataforma.buscar_clente(1))
#print(plataforma.cliete)
#print(plataforma.buscar_clente(3))
#print(plataforma.cliete)

#Buscar Todos
#print(plataforma.buscar_todos_clientes())
#print(plataforma.cliente_todos)
#print(plataforma.buscar_todos_clientes())
#print(plataforma.cliente_todos)

#Atualizar
#plataforma.atualiza_cliente('Bolinha',2,'AV.Maria Lina','10-20-2000','pedro@gmail.com','899932349')
#print(plataforma.buscar_clente(2))
#print(plataforma.cliete)

#Remoção
#plataforma.remover_cliente(2)
#print(plataforma.buscar_todos_clientes())
#print(plataforma.cliente_todos)

#Fornecedor
#Cadastrar e Busca
plataforma.cadastra_fornecedor('Corote',1,'Brasil','AV. Braz','899945332154','Karel')
plataforma.cadastra_fornecedor('Virote',2,'Brasil','AV. Braz','899945332154','Karel')
plataforma.cadastra_fornecedor('Sao_Bras',3,'Brasil','AV. Braz','899945332154','Karel')
plataforma.cadastra_fornecedor('Visima',4,'Brasil','AV. Braz','899945332154','Karel')
plataforma.cadastra_fornecedor('With_Wolf',5,'Brasil','AV. Braz','899945332154','Karel')
plataforma.cadastra_fornecedor('Skeliguer',6,'Brasil','AV. Braz','899945332154','Karel')
plataforma.cadastra_fornecedor('Shurima',7,'Brasil','AV. Braz','899945332154','Karel')
plataforma.cadastra_fornecedor('Tusan',8,'Brasil','AV. Braz','899945332154','Karel')
#plataforma.buscar_fornecedor(1)
#print(plataforma.fornecedor)

#Buscar Todos fornecedores
#plataforma.buscar_todos_fornecedores()
#print(plataforma.fornecedor_todos)
#plataforma.buscar_todos_fornecedores()
#print(plataforma.fornecedor_todos)

#Atualzar
#plataforma.atualziar_fornecedor('Jorel',8,'Brasil','AV. Braz','899945332154','Karel')
#plataforma.buscar_todos_fornecedores()
#plataforma.buscar_todos_fornecedores()
#print(plataforma.fornecedor_todos)

#Remoção
#plataforma.remover_fornecedor(1)
#plataforma.buscar_todos_fornecedores()
#print(plataforma.fornecedor_todos)

#Produto
#Cadastrar e Busca
plataforma.cadastra_produto(1,'Sao_Jorge','10-10-2000','10-10-2010','Clima_nao_humido','10','10-20',20.10,30.10,2)
plataforma.cadastra_produto(2,'Bilada','10-10-2000','10-10-2010','Clima_nao_humido','10','10-20',20.10,30.10,2)
plataforma.cadastra_produto(3,'Seldon','10-10-2000','10-10-2010','Clima_nao_humido','10','10-20',20.10,30.10,2)
plataforma.cadastra_produto(4,'Shurima','10-10-2000','10-10-2010','Clima_nao_humido','10','10-20',20.10,30.10,2)
plataforma.cadastra_produto(5,'Gideon','10-10-2000','10-10-2010','Clima_nao_humido','10','10-20',20.10,30.10,2)
plataforma.cadastra_produto(6,'Cascane','10-10-2000','10-10-2010','Clima_nao_humido','10','10-20',20.10,30.10,2)
plataforma.cadastra_produto(7,'Belivenet','10-10-2000','10-10-2010','Clima_nao_humido','10','10-20',20.10,30.10,2)
plataforma.cadastra_produto(8,'Sedrico','10-10-2000','10-10-2010','Clima_nao_humido','10','10-20',20.10,30.10,2)
#plataforma.buscar_produto(1)
#print(plataforma.prdotos)

#Buscar todos os produtos
#plataforma.buscar_produto_todos()
#print(plataforma.prdotos_todas)
#plataforma.buscar_produto_todos()
#print(plataforma.prdotos_todas)

#Atualizar
#plataforma.atualizar_produto(1,'Piladinha','10-10-2000','10-10-2010','Clima_nao_humido','10','10-20',20.10,30.10,2)
#plataforma.buscar_produto(1)
#print(plataforma.prdotos)

#Remocao
#plataforma.remover_produto(1)
#plataforma.buscar_produto_todos()
#print(plataforma.prdotos_todas)

#Vendas
#Cadastrar
#forma_de_pagamento,data_da_venda,n_bebida,cpf_cliente,cpf_funcionario,senha_funcionario
plataforma.cadastrar_venda('CC','10-10-2021',2,1,1,'123')
plataforma.cadastrar_venda('CD','10-10-2021',2,1,1,'123')
plataforma.cadastrar_venda('Dinheiro','10-10-2021',2,1,1,'123')
plataforma.cadastrar_venda('CC','10-10-2021',2,1,1,'123')
plataforma.cadastrar_venda('CD','10-10-2021',2,1,1,'123')
plataforma.cadastrar_venda('Dinheiro','10-10-2021',2,1,1,'123')
plataforma.cadastrar_venda('Dinheiro','10-10-2021',2,1,1,'123')
plataforma.cadastrar_venda('CC','10-10-2021',2,1,1,'123')
plataforma.cadastrar_venda('CD','10-10-2021',2,1,1,'123')

#Buscar Todos
plataforma.buscar_vendas_todas()
print(plataforma.vendas_todas)
plataforma.buscar_vendas_todas()
print(plataforma.vendas_todas)