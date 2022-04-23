#import sqlite3
# Instale a biblioteca caso o modulo myql não exista: 
# pip install mysql-connector-python
import mysql.connector as mysql
from mysql.connector import Error

class Cadastro:
    '''
        O objetivo da class Cadastro conter as contas criadas.
        Todos as informações do objeto são inicializados e deixados vazios até ser adicionado informações.
    '''
    def __init__(self):

        self.forecedor = []
        self.cliente = []
        self.fucionario = []
        self.produto = []
        self.vendas = []


        #Cria tabela fornecedor
        try:
            #self._conta_cache = Banco()
            conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
            cursor = conexao.cursor()

            sql = """CREATE TABLE IF NOT EXISTS `mydb_2`.`Fornecedor` (
  `idFornecedor` INT NOT NULL AUTO_INCREMENT,
  `razao_social` VARCHAR(100) NOT NULL,
  `CNPJ` VARCHAR(100) NOT NULL,
  `nacionalidade` VARCHAR(100) NOT NULL,
  `endereco` VARCHAR(100) NOT NULL,
  `telefone` VARCHAR(100) NOT NULL,
  `pessoa_de_contato` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idFornecedor`),
  UNIQUE INDEX `CNPJ_UNIQUE` (`CNPJ` ASC),
  UNIQUE INDEX `idFornecedor_UNIQUE` (`idFornecedor` ASC))
ENGINE = InnoDB;"""

            cursor.execute(sql)

            conexao.commit()
            conexao.close()
        except Error as erro:
            print("Falha ao criar tabela fornecedor no Banco adega_do_povo: {}".format(erro))
        
        #Cria tabela produto
        try:
            #self._conta_cache = Banco()
            conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
            cursor = conexao.cursor()

            sql = """CREATE TABLE IF NOT EXISTS `mydb_2`.`Produto` (
  `idProduto` INT NOT NULL AUTO_INCREMENT,
  `nome_da_bebida` VARCHAR(100) NOT NULL,
  `numero_do_lote` INT NOT NULL,
  `data_de_fabricacao` VARCHAR(100) NOT NULL,
  `data_validade` VARCHAR(100) NOT NULL,
  `condicoes_de_armazenamento` VARCHAR(100) NOT NULL,
  `quantidade` INT NOT NULL,
  `local_armazenado` VARCHAR(100) NOT NULL,
  `valor_de_compra_UN` FLOAT NOT NULL,
  `valor_revenda_UN` FLOAT NOT NULL,
  `Fornecedor_idFornecedor` INT NOT NULL,
  PRIMARY KEY (`idProduto`, `Fornecedor_idFornecedor`),
  INDEX `fk_Produto_Fornecedor1_idx` (`Fornecedor_idFornecedor` ASC),
  UNIQUE INDEX `idProduto_UNIQUE` (`idProduto` ASC),
  CONSTRAINT `fk_Produto_Fornecedor1`
    FOREIGN KEY (`Fornecedor_idFornecedor`)
    REFERENCES `mydb_2`.`Fornecedor` (`idFornecedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;"""

            cursor.execute(sql)

            conexao.commit()
            conexao.close()
        except Error as erro:
            print("Falha ao criar tabela produto no Banco adega_do_povo: {}".format(erro))

        #Cria tabela clietne
        try:
            #self._conta_cache = Banco()
            conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
            cursor = conexao.cursor()

            sql = """CREATE TABLE IF NOT EXISTS `mydb_2`.`Cliente` (
  `idCliente` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `CPF` VARCHAR(100) NOT NULL,
  `endereco` VARCHAR(100) NOT NULL,
  `data_de_nascimento` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `telefone` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idCliente`),
  UNIQUE INDEX `idCliente_UNIQUE` (`idCliente` ASC),
  UNIQUE INDEX `CPF_UNIQUE` (`CPF` ASC))
ENGINE = InnoDB
COMMENT = '	';"""

            cursor.execute(sql)

            conexao.commit()
            conexao.close()
        except Error as erro:
            print("Falha ao criar tabela cliente no Banco adega_do_povo: {}".format(erro))
        
        #Cria tabela funcionario
        try:
            #self._conta_cache = Banco()
            conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
            cursor = conexao.cursor()

            sql = """CREATE TABLE IF NOT EXISTS `mydb_2`.`Funcionario` (
  `idFuncionario` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `CPF` VARCHAR(100) NOT NULL,
  `data_de_nascimento` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `telefone` VARCHAR(100) NOT NULL,
  `cargo` VARCHAR(100) NOT NULL,
  `senha` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idFuncionario`),
  UNIQUE INDEX `idFuncionario_UNIQUE` (`idFuncionario` ASC),
  UNIQUE INDEX `CPF_UNIQUE` (`CPF` ASC))
ENGINE = InnoDB;"""

            cursor.execute(sql)

            conexao.commit()
            conexao.close()
        except Error as erro:
            print("Falha ao criar tabela funcionario no Banco adega_do_povo: {}".format(erro))

        #Cria tabela vendas
        try:
            #self._conta_cache = Banco()
            conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
            cursor = conexao.cursor()

            sql = """CREATE TABLE IF NOT EXISTS `mydb_2`.`Vendas` (
  `idVendas` INT NOT NULL AUTO_INCREMENT,
  `forma_de_pagamento` VARCHAR(100) NOT NULL,
  `data_da_venda` VARCHAR(100) NOT NULL,
  `valor` FLOAT NOT NULL,
  `Cliente_idCliente` INT NOT NULL,
  `Funcionario_idFuncionario` INT NOT NULL,
  `Produto_idProduto` INT NOT NULL,
  PRIMARY KEY (`idVendas`, `Cliente_idCliente`, `Funcionario_idFuncionario`, `Produto_idProduto`),
  INDEX `fk_Vendas_Cliente_idx` (`Cliente_idCliente` ASC),
  INDEX `fk_Vendas_Funcionario1_idx` (`Funcionario_idFuncionario` ASC),
  INDEX `fk_Vendas_Produto1_idx` (`Produto_idProduto` ASC),
  UNIQUE INDEX `idVendas_UNIQUE` (`idVendas` ASC),
  CONSTRAINT `fk_Vendas_Cliente`
    FOREIGN KEY (`Cliente_idCliente`)
    REFERENCES `mydb_2`.`Cliente` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Vendas_Funcionario1`
    FOREIGN KEY (`Funcionario_idFuncionario`)
    REFERENCES `mydb_2`.`Funcionario` (`idFuncionario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Vendas_Produto1`
    FOREIGN KEY (`Produto_idProduto`)
    REFERENCES `mydb_2`.`Produto` (`idProduto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;"""

            cursor.execute(sql)

            conexao.commit()
            conexao.close()
        except Error as erro:
            print("Falha ao criar tabela vendas no Banco adega_do_povo: {}".format(erro))


    def sqlite_create_fornecedor(self,razao_social,CNPJ,nacionalidade,endereco,telefone,passoa_contato):
        
        try:
            if(True):

                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()

                bd_razao_social = str(razao_social)
                bd_CNPJ = str(CNPJ)
                bd_nacionalidade = str(nacionalidade)
                bd_endereco = str(endereco)
                bd_telefone = str(telefone)
                bd_passoa_contato = str(passoa_contato)

                #transacoes = banco._historico.transacoes
                #print(transacoes)
                #data_abertura = str(banco.historico.data_abertura)
                #pega=''
                #for i in transacoes:
                #    if (transacoes!=[]):
                #        pega= pega+i+'\n'

                #cursor.execute(sql)
                cursor.execute('INSERT INTO Fornecedor (razao_social,CNPJ,nacionalidade,endereco,telefone,pessoa_de_contato) VALUES (%s,%s,%s,%s,%s,%s)' , (bd_razao_social,bd_CNPJ,bd_nacionalidade,bd_endereco,bd_telefone,bd_passoa_contato))

                conexao.commit()
                conexao.close()

                return True
        except Error as erro:
            print("Falha ao inserir dados na tabela fornecedores: {}".format(erro))
            return False

    def sqlite_create_cliente(self,nome,cpf,edereco,data_de_nascimento,email,telefone):
        
        try:
            if(True):

                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()

                bd_nome = str(nome)
                bd_cpf = str(cpf)
                bd_edereco = str(edereco)
                bd_data_de_nascimento = str(data_de_nascimento)
                bd_email = str(email)
                bd_telefone = str(telefone)


                #transacoes = banco._historico.transacoes
                #print(transacoes)
                #data_abertura = str(banco.historico.data_abertura)
                #pega=''
                #for i in transacoes:
                #    if (transacoes!=[]):
                #        pega= pega+i+'\n'

                #cursor.execute(sql)
                cursor.execute('INSERT INTO Cliente (nome,CPF,endereco,data_de_nascimento,email,telefone) VALUES (%s,%s,%s,%s,%s,%s)' , (bd_nome,bd_cpf,bd_edereco,bd_data_de_nascimento,bd_email,bd_telefone))

                conexao.commit()
                conexao.close()

                return True
        except Error as erro:
            print("Falha ao inserir dados na tabela cliente: {}".format(erro))
            return False

    def sqlite_create_funcionario(self,nome,CPF,data_de_ascimento,email,telefone,Cargo,senha):
        
        try:
            if(True):

                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()

                bd_nome = str(nome)
                bd_CPF = str(CPF)
                bd_data_de_ascimento = str(data_de_ascimento)
                bd_email = str(email)
                bd_telefone = str(telefone)
                bd_Cargo = str(Cargo)
                bd_senha = str(senha)


                #transacoes = banco._historico.transacoes
                #print(transacoes)
                #data_abertura = str(banco.historico.data_abertura)
                #pega=''
                #for i in transacoes:
                #    if (transacoes!=[]):
                #        pega= pega+i+'\n'

                #cursor.execute(sql)
                cursor.execute('INSERT INTO Funcionario (nome,CPF,data_de_nascimento,email,telefone,Cargo,senha) VALUES (%s,%s,%s,%s,%s,%s,MD5(%s))' , (bd_nome,bd_CPF,bd_data_de_ascimento,bd_email,bd_telefone,bd_Cargo,bd_senha))

                conexao.commit()
                conexao.close()

                return True
        except Error as erro:
            print("Falha ao inserir dados na tabela funcionario: {}".format(erro))
            return False


    def sqlite_readSec_fornecedor(self,cpf):
        try:
            if(True):
                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()
                cursor.execute('SELECT * FROM `fornecedor` WHERE CNPJ= %s'%cpf)
                usuario = cursor.fetchall()
                
                if (usuario!=[]):
                    #print(usuario)
                    #print(usuario)
                    #cliente_novo = Cliente(usuario[0][2],usuario[0][3],cpf)
                    #banco_novo = Banco(int(usuario[0][1]),cliente_novo,float(usuario[0][5]),float(usuario[0][6]),usuario[0][8])
                        
                    #usuario[0][7].split('--')
                           
                    #banco_novo.historico.transacoes.append (usuario[0][7])
                    #banco_novo.historico.data_abertura = usuario[0][8]
                    conexao.commit()
                    conexao.close()

                    return usuario
                
                conexao.commit()
                conexao.close()
                return False

        except Error as erro:
            print("Falha ao buscar fornecedor: {}".format(erro))
            return False

    def sqlite_readSec_fornecedor_id(self,cpf):
        try:
            if(True):
                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()
                cursor.execute('SELECT * FROM `Fornecedor` WHERE idFornecedor= %s'%int(cpf))
                usuario = cursor.fetchall()
                print('usuario')
                print(usuario)
                
                if (usuario!=[]):
                    #print(usuario)
                    #print(usuario)
                    #cliente_novo = Cliente(usuario[0][2],usuario[0][3],cpf)
                    #banco_novo = Banco(int(usuario[0][1]),cliente_novo,float(usuario[0][5]),float(usuario[0][6]),usuario[0][8])
                        
                    #usuario[0][7].split('--')
                           
                    #banco_novo.historico.transacoes.append (usuario[0][7])
                    #banco_novo.historico.data_abertura = usuario[0][8]
                    conexao.commit()
                    conexao.close()

                    return usuario
                
                conexao.commit()
                conexao.close()
                return False

        except Error as erro:
            print("Falha ao buscar fornecedor: {}".format(erro))
            return False

    def sqlite_readSec_fornecedor_todos(self):
        try:
            if(True):
                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()
                cursor.execute('SELECT * FROM `fornecedor`')
                usuario = cursor.fetchall()
                
                if (usuario!=[]):
                    #print(usuario)
                    #print(usuario)
                    #cliente_novo = Cliente(usuario[0][2],usuario[0][3],cpf)
                    #banco_novo = Banco(int(usuario[0][1]),cliente_novo,float(usuario[0][5]),float(usuario[0][6]),usuario[0][8])
                        
                    #usuario[0][7].split('--')
                           
                    #banco_novo.historico.transacoes.append (usuario[0][7])
                    #banco_novo.historico.data_abertura = usuario[0][8]
                    conexao.commit()
                    conexao.close()

                    return usuario
                
                conexao.commit()
                conexao.close()
                return False

        except Error as erro:
            print("Falha ao buscar fornecedor: {}".format(erro))
            return False

    def sqlite_readSec_cliente(self,cpf):
        try:
            if(True):
                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()
                cursor.execute('SELECT * FROM `Cliente` WHERE CPF= %s'%cpf)
                usuario = cursor.fetchall()
                
                if (usuario!=[]):
                    #print(usuario)
                    #print(usuario)

                    conexao.commit()
                    conexao.close()

                    return usuario
                
                conexao.commit()
                conexao.close()
                return False

        except Error as erro:
            print("Falha ao buscar cliente: {}".format(erro))
            return False

    def sqlite_readSec_cliente_todos(self):
        try:
            if(True):
                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()
                cursor.execute('SELECT * FROM `Cliente`')
                usuario = cursor.fetchall()
                
                if (usuario!=[]):
                    #print(usuario)
                    #print(usuario)

                    conexao.commit()
                    conexao.close()

                    return usuario
                
                conexao.commit()
                conexao.close()
                return False

        except Error as erro:
            print("Falha ao buscar cliente: {}".format(erro))
            return False


    def sqlite_read_funcionario(self,cpf,senha):
        try:
            if(True):
                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()

                cursor.execute("SELECT * FROM `funcionario` WHERE CPF=%s AND senha= MD5('%s')" %(cpf,senha))
                usuario = cursor.fetchall()
                
               
                
                if (usuario!=[]):

                    #print(usuario)

                    conexao.commit()
                    conexao.close()
                   
                    return usuario

                conexao.commit()
                conexao.close()
                return False

        except Error as erro:
            print("Falha ao buscar funcionario: {}".format(erro))
            return False

    def sqlite_read_funcionario_cpf(self,cpf):
        try:
            if(True):
                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()

                cursor.execute("SELECT * FROM `funcionario` WHERE CPF=%s" %(cpf))
                usuario = cursor.fetchall()
                
               
                
                if (usuario!=[]):

                    #print(usuario)

                    conexao.commit()
                    conexao.close()
                   
                    return usuario

                conexao.commit()
                conexao.close()
                return False

        except Error as erro:
            print("Falha ao buscar funcionario: {}".format(erro))
            return False


    def sqlite_create_produto(self,n_bebida,nome_da_bebida,data_de_fabricacao,data_de_validade,condicoes_de_armazenamento,quantidades,local_armazenado,valor_de_compra_UN,valor_revenda_UN,cnpj_fornecedor):
        
        try:
            bd_n_bebida = str(n_bebida)
            bd_nome_da_bebida = str(nome_da_bebida)
            bd_data_de_fabricacao = str(data_de_fabricacao)
            bd_data_de_validade = str(data_de_validade)
            bd_condicoes_de_armazenamento = str(condicoes_de_armazenamento)
            bd_quantidades = str(quantidades)
            bd_local_armazenado = str(local_armazenado)
            bd_valor_de_compra_UN = str(valor_de_compra_UN)
            bd_valor_revenda_UN = str(valor_revenda_UN)
            fornecedor = self.sqlite_readSec_fornecedor(cnpj_fornecedor)          

            if(fornecedor != False):

                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()

                cursor.execute('INSERT INTO Produto (numero_do_lote,nome_da_bebida,data_de_fabricacao,data_validade,condicoes_de_armazenamento,quantidade,local_armazenado,valor_de_compra_UN,valor_revenda_UN,Fornecedor_idFornecedor) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' , (bd_n_bebida,bd_nome_da_bebida,bd_data_de_fabricacao,bd_data_de_validade,bd_condicoes_de_armazenamento,bd_quantidades,bd_local_armazenado,bd_valor_de_compra_UN,bd_valor_revenda_UN,fornecedor[0][0]))

                conexao.commit()
                conexao.close()

                return True
            else:
                print("Não foi possivel cadastrar, Fornecedor nao cadastrado.")
                return False

        except Error as erro:
            print("Falha ao inserir dados na tabela produto: {}".format(erro))
            return False

    def sqlite_read_produto_todos(self):
        try:
            if(True):
                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()

                cursor.execute("SELECT * FROM `produto`")
                usuario = cursor.fetchall()
                
                if (usuario!=[]):

                    #print(usuario)

                    conexao.commit()
                    conexao.close()
                   
                    return usuario

                conexao.commit()
                conexao.close()
                return False
                

        except Error as erro:
            print("Falha ao buscar produto: {}".format(erro))
            return False

    def sqlite_read_produto(self,n_bebida):
        try:
            if(True):
                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()

                cursor.execute("SELECT * FROM `produto` WHERE numero_do_lote= %s" %(n_bebida))
                usuario = cursor.fetchall()
                
                if (usuario!=[]):

                    #print(usuario)

                    conexao.commit()
                    conexao.close()
                   
                    return usuario

                conexao.commit()
                conexao.close()
                return False
                

        except Error as erro:
            print("Falha ao buscar produto: {}".format(erro))
            return False




    def sqlite_create_venda(self,forma_de_pagamento,data_da_venda,n_bebida,cpf_cliente,cpf_funcionario,senha_funcionario):
        
        try:

            bd_forma_de_pagamento = str(forma_de_pagamento)
            bd_data_da_venda = str(data_da_venda)
            produto = self.sqlite_read_produto(n_bebida)
            print('PRODUTO:',produto)
            cliente = self.sqlite_readSec_cliente(cpf_cliente)
            print(cliente)
            funcioanrio = self.sqlite_read_funcionario(cpf_funcionario,senha_funcionario)
            print(funcioanrio)
            

            if(cliente != False and funcioanrio != False and produto != False and int(produto[0][6]) >= 1):

                valor_da_compra = float(produto[0][9])
                print(valor_da_compra)

                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()

                print(cliente[0][0])
                print(funcioanrio[0][0])
                cursor.execute('INSERT INTO Vendas (forma_de_pagamento,data_da_venda,valor,Cliente_idCliente,Funcionario_idFuncionario,Produto_idProduto) VALUES (%s,%s,%s,%s,%s,%s)' , (bd_forma_de_pagamento,bd_data_da_venda,produto[0][9],cliente[0][0],funcioanrio[0][0],produto[0][0]))

                conexao.commit()
                conexao.close()

                nova_quantidade = int(produto[0][6]) - 1
                self.sqlite_update_produto_crinado_venda(n_bebida,nova_quantidade)

                return True

            else:
                print('Não foi possivel cadastrar a venda pois o cliente, ou produto informado não estao cadastrado')
                return False

        except Error as erro:
            print("Falha ao inserir dados na tabela vendas: {}".format(erro))
            return False

    def sqlite_read_venda_todas(self):
        try:
            if(True):
                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()

                cursor.execute("SELECT * FROM `vendas`")
                usuario = cursor.fetchall()
                
                if (usuario!=[]):

                    print(usuario)

                    conexao.commit()
                    conexao.close()
                   
                    return usuario

                conexao.commit()
                conexao.close()
                return False

        except Error as erro:
            print("Falha ao buscar vendas: {}".format(erro))
            return False

    def sqlite_read_venda_cliente(self,id_cliente):
        try:
            if(True):
                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()

                cursor.execute("SELECT * FROM `vendas` WHERE Cliete_idCliete = %s" %(id_cliente))
                usuario = cursor.fetchall()
                
                if (usuario!=[]):

                    print(usuario)

                    conexao.commit()
                    conexao.close()
                   
                    return usuario

                conexao.commit()
                conexao.close()
                return False

        except Error as erro:
            print("Falha ao buscar vendas: {}".format(erro))
            return False

    def sqlite_read_venda_funcionario(self,id_funcionario):
        try:
            if(True):
                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()

                cursor.execute("SELECT * FROM `vendas` WHERE Funcionari_idFuncionari = %s" %(id_funcionario))
                usuario = cursor.fetchall()
                
                if (usuario!=[]):

                    print(usuario)

                    conexao.commit()
                    conexao.close()
                   
                    return usuario

                conexao.commit()
                conexao.close()
                return False

        except Error as erro:
            print("Falha ao buscar vendas: {}".format(erro))
            return False


    def sqlite_update_produto_crinado_venda(self,n_bebida,nova_quantidade):
        try:

            #produto = self.sqlite_read_produto(nome_produto)

            if(True):

                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()
                #print(lista)
                cursor.execute('UPDATE `produto` SET quantidade="%s" WHERE numero_do_lote = %s' % (str(nova_quantidade),n_bebida))
                conexao.commit()
                conexao.close()

                return True

        except Error as erro:
            print("Falha ao fazer update da quantidade do produto: {}".format(erro))
            return False

    def sqlite_update_produto(self,n_bebida,nome_da_bebida,data_de_fabricacao,data_de_validade,condicoes_de_armazenamento,quantidades,local_armazenado,valor_de_compra_UN,valor_revenda_UN,cnpj_fornecedor):
        try:

            #produto = self.sqlite_read_produto(nome_produto)

            bd_n_bebida = str(n_bebida)
            bd_nome_da_bebida = str(nome_da_bebida)
            bd_data_de_fabricacao = str(data_de_fabricacao)
            bd_data_de_validade = str(data_de_validade)
            bd_condicoes_de_armazenamento = str(condicoes_de_armazenamento)
            bd_quantidades = str(quantidades)
            bd_local_armazenado = str(local_armazenado)
            bd_valor_de_compra_UN = str(valor_de_compra_UN)
            bd_valor_revenda_UN = str(valor_revenda_UN)
            fornecedor = self.sqlite_readSec_fornecedor_id(cnpj_fornecedor)
            print('Fornecedor')
            print(self.produto)

            if(fornecedor):

                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()
                #print(lista)
                cursor.execute('UPDATE `produto` SET nome_da_bebida="%s",data_de_fabricacao = "%s",data_validade = "%s", condicoes_de_armazenamento = "%s",quantidade="%s", local_armazenado = "%s",valor_de_compra_UN = "%s",valor_revenda_UN = "%s", Fornecedor_idFornecedor = "%s" WHERE numero_do_lote = %s' % (bd_nome_da_bebida,bd_data_de_fabricacao,bd_data_de_validade,bd_condicoes_de_armazenamento,bd_quantidades,bd_local_armazenado,bd_valor_de_compra_UN,bd_valor_revenda_UN,fornecedor[0][0],bd_n_bebida))
                conexao.commit()
                conexao.close()

                return True
            else:
                print('Fornecedor informado não encontrado.')
                return False

        except Error as erro:
            print("Falha ao fazer update da tabela produto: {}".format(erro))
            return False


    def sqlite_update_cliente(self,nome,cpf,edereco,data_de_nascimento,email,telefone):
        try:

            #produto = self.sqlite_read_produto(nome_produto)

            bd_nome = str(nome)
            bd_cpf = str(cpf)
            bd_edereco = str(edereco)
            bd_data_de_nascimento = str(data_de_nascimento)
            bd_email = str(email)
            bd_telefone = str(telefone)        

            if(True):

                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()
                #print(lista)
                cursor.execute('UPDATE Cliete SET nome = "%s",endereco = "%s",data_de_nascimento = "%s",email = "%s",telefone = "%s" WHERE cpf = %s' % (bd_nome,bd_edereco,bd_data_de_nascimento,bd_email,bd_telefone,bd_cpf))
                conexao.commit()
                conexao.close()

                return True


        except Error as erro:
            print("Falha ao fazer update da tabela cliente: {}".format(erro))
            return False

    def sqlite_update_fornecedor(self,razao_social,CNPJ,nacionalidade,endereco,telefone,passoa_contato):
        try:

            #produto = self.sqlite_read_produto(nome_produto)

            bd_razao_social = str(razao_social)
            bd_CNPJ = str(CNPJ)
            bd_nacionalidade = str(nacionalidade)
            bd_endereco = str(endereco)
            bd_telefone = str(telefone)
            bd_passoa_contato = str(passoa_contato)        

            if(True):

                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()
                #print(lista)
                cursor.execute('UPDATE Fornecedor SET razao_social = "%s",nacionalidade = "%s",endereco = "%s",telefone = "%s",pessoa_de_contato = "%s" WHERE CNPJ = %s' % (bd_razao_social,bd_nacionalidade,bd_endereco,bd_telefone,bd_passoa_contato,bd_CNPJ))
                conexao.commit()
                conexao.close()

                return True


        except Error as erro:
            print("Falha ao fazer update da tabela fornecedor: {}".format(erro))
            return False


    def sqlite_update_cliente(self,nome,cpf,edereco,data_de_nascimento,email,telefone):
        try:

            #produto = self.sqlite_read_produto(nome_produto)

            bd_nome = str(nome)
            bd_cpf = str(cpf)
            bd_edereco = str(edereco)
            bd_data_de_nascimento = str(data_de_nascimento)
            bd_email = str(email)
            bd_telefone = str(telefone)        

            if(True):

                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()
                #print(lista)
                cursor.execute('UPDATE Cliente SET nome = "%s",endereco = "%s",data_de_nascimento = "%s",email = "%s",telefone = "%s" WHERE cpf = %s' % (bd_nome,bd_edereco,bd_data_de_nascimento,bd_email,bd_telefone,bd_cpf))
                conexao.commit()
                conexao.close()

                return True


        except Error as erro:
            print("Falha ao fazer update da tabela cliente: {}".format(erro))
            return False

    def sqlite_remove_fornecedor(self,cnpj):
        try:
            print('Verificando se não existe produto com Fornecedor Informado:')
            conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
            cursor = conexao.cursor()
            cursor.execute('SELECT * FROM `Fornecedor` WHERE CNPJ= %s'%int(cnpj))
            fornecedor = cursor.fetchall()
            print(fornecedor)  
            cursor.execute('SELECT * FROM `Produto` WHERE Fornecedor_idFornecedor= %s'%int(fornecedor[0][0]))
            produto = cursor.fetchall()          

            if(produto == []):
                #print(lista)
                cursor.execute('DELETE FROM `mydb_2`.`Fornecedor` WHERE CNPJ = %s' % (str(cnpj)))
                conexao.commit()
                conexao.close()

                return True

            else:
                print('Falha ao remover funcionario: Existe produto cadastrado com esse fornecedor.')
                return False


        except Error as erro:
            print("Falha ao remover fornecedor: {}".format(erro))
            return False

    def sqlite_remove_cliente(self,cpf):
        try:      
            if(True):

                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()
                #print(lista)
                print('cpf:',cpf)
                cliente = self.sqlite_readSec_cliente(cpf)
                if cliente:
                    print('cliente[0][0]:',cliente[0][0])
                    cursor.execute('SELECT * FROM `Vendas` WHERE Cliente_idCliente= %s'%cliente[0][0])
                    venda = cursor.fetchall()
                    print('Venda:',venda)
                    if venda:
                        print("Falha ao remover cliente: Registro de venda feita por esse cliente.")
                        return False
                    else:
                        cursor.execute('DELETE FROM `mydb_2`.`cliente` WHERE CPF = %s' % (str(cpf)))
                        conexao.commit()
                        conexao.close()
                        return True
                else:
                    print('Falha ao remover cliente: Registro de cliente não encontrado.')
                    return False


        except Error as erro:
            print("Falha ao remover cliente: {}".format(erro))
            return False

    def sqlite_remove_produto(self,n_bebida):
        try:      
            if(True):

                conexao = mysql.connect(host = 'localhost',db='mydb_2',user='root')
                cursor = conexao.cursor()
                #print(lista)
                cursor.execute('DELETE FROM `mydb_2`.`produto` WHERE numero_do_lote = %s' %(str(n_bebida)))
                conexao.commit()
                conexao.close()

                return True


        except Error as erro:
            print("Falha ao remover produto: {}".format(erro))
            return False

    