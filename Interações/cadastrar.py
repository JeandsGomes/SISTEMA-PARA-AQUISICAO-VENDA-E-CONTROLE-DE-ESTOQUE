#import sqlite3
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
            conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
            cursor = conexao.cursor()

            sql = """CREATE TABLE IF NOT EXISTS `mydb`.`Fornecedor` (
  `idFornecedor` INT NOT NULL AUTO_INCREMENT,
  `razao_social` VARCHAR(100) NOT NULL,
  `CNPJ` VARCHAR(100) NOT NULL,
  `nacionalidade` VARCHAR(100) NOT NULL,
  `endereco` VARCHAR(100) NOT NULL,
  `telefone` VARCHAR(100) NOT NULL,
  `pessoa_de_contato` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idFornecedor`))
ENGINE = InnoDB;"""

            cursor.execute(sql)

            conexao.commit()
            conexao.close()
        except Error as erro:
            print("Falha ao criar tabela fornecedor no Banco adega_do_povo: {}".format(erro))
        
        #Cria tabela produto
        try:
            #self._conta_cache = Banco()
            conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
            cursor = conexao.cursor()

            sql = """CREATE TABLE IF NOT EXISTS `mydb`.`Produto` (
  `idproduto` INT NOT NULL AUTO_INCREMENT,
  `n_bebida` VARCHAR(45) NOT NULL,
  `nome_da_bebida` VARCHAR(100) NOT NULL,
  `data_de_fabricacao` VARCHAR(100) NOT NULL,
  `data_validade` VARCHAR(100) NOT NULL,
  `condicoes_de_armazenamento` VARCHAR(100) NOT NULL,
  `quantidades` VARCHAR(100) NOT NULL,
  `local_armazenado` VARCHAR(100) NOT NULL,
  `valor_de_compra_UN` VARCHAR(100) NOT NULL,
  `valor_revenda_UN` VARCHAR(100) NOT NULL,
  `Fornecedor_idFornecedor` INT NOT NULL,
  PRIMARY KEY (`idproduto`, `Fornecedor_idFornecedor`),
  INDEX `fk_Produto_Fornecedor1_idx` (`Fornecedor_idFornecedor` ASC),
  CONSTRAINT `fk_Produto_Fornecedor1`
    FOREIGN KEY (`Fornecedor_idFornecedor`)
    REFERENCES `mydb`.`Fornecedor` (`idFornecedor`)
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
            conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
            cursor = conexao.cursor()

            sql = """CREATE TABLE IF NOT EXISTS `mydb`.`Cliete` (
  `idCliete` INT NOT NULL,
  `nome` VARCHAR(100) NOT NULL,
  `CPF` VARCHAR(100) NOT NULL,
  `endereco` VARCHAR(100) NOT NULL,
  `data_de_nascimento` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `telefone` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idCliete`))
ENGINE = InnoDB;"""

            cursor.execute(sql)

            conexao.commit()
            conexao.close()
        except Error as erro:
            print("Falha ao criar tabela cliente no Banco adega_do_povo: {}".format(erro))
        
        #Cria tabela funcionario
        try:
            #self._conta_cache = Banco()
            conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
            cursor = conexao.cursor()

            sql = """CREATE TABLE IF NOT EXISTS `mydb`.`Funcionari` (
  `idFuncionari` INT NOT NULL,
  `nome` VARCHAR(100) NOT NULL,
  `CPF` VARCHAR(100) NOT NULL,
  `data_de_nascimento` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `telefone` VARCHAR(100) NOT NULL,
  `Cargo` VARCHAR(100) NOT NULL,
  `senha` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idFuncionari`))
ENGINE = InnoDB;"""

            cursor.execute(sql)

            conexao.commit()
            conexao.close()
        except Error as erro:
            print("Falha ao criar tabela funcionario no Banco adega_do_povo: {}".format(erro))

        #Cria tabela vendas
        try:
            #self._conta_cache = Banco()
            conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
            cursor = conexao.cursor()

            sql = """CREATE TABLE IF NOT EXISTS `mydb`.`Vendas` (
  `idVendas` INT NOT NULL,
  `forma_de_pagamento` VARCHAR(100) NOT NULL,
  `data_da_venda` VARCHAR(100) NOT NULL,
  `Produto_idproduto` INT NOT NULL,
  `Cliete_idCliete` INT NOT NULL,
  `Funcionari_idFuncionari` INT NOT NULL,
  PRIMARY KEY (`idVendas`, `Produto_idproduto`, `Cliete_idCliete`, `Funcionari_idFuncionari`),
  INDEX `fk_Vendas_Produto_idx` (`Produto_idproduto` ASC),
  INDEX `fk_Vendas_Cliete1_idx` (`Cliete_idCliete` ASC),
  INDEX `fk_Vendas_Funcionari1_idx` (`Funcionari_idFuncionari` ASC),
  CONSTRAINT `fk_Vendas_Produto`
    FOREIGN KEY (`Produto_idproduto`)
    REFERENCES `mydb`.`Produto` (`idproduto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Vendas_Cliete1`
    FOREIGN KEY (`Cliete_idCliete`)
    REFERENCES `mydb`.`Cliete` (`idCliete`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Vendas_Funcionari1`
    FOREIGN KEY (`Funcionari_idFuncionari`)
    REFERENCES `mydb`.`Funcionari` (`idFuncionari`)
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

                conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
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

                conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
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
                cursor.execute('INSERT INTO Cliete (nome,CPF,endereco,data_de_nascimento,email,telefone) VALUES (%s,%s,%s,%s,%s,%s)' , (bd_nome,bd_cpf,bd_edereco,bd_data_de_nascimento,bd_email,bd_telefone))

                conexao.commit()
                conexao.close()

                return True
        except Error as erro:
            print("Falha ao inserir dados na tabela cliete: {}".format(erro))
            return False

    def sqlite_create_funcionario(self,nome,CPF,data_de_ascimento,email,telefone,Cargo,senha):
        
        try:
            if(True):

                conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
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
                cursor.execute('INSERT INTO Funcionari (nome,CPF,data_de_nascimento,email,telefone,Cargo,senha) VALUES (%s,%s,%s,%s,%s,%s,MD5(%s))' , (bd_nome,bd_CPF,bd_data_de_ascimento,bd_email,bd_telefone,bd_Cargo,bd_senha))

                conexao.commit()
                conexao.close()

                return True
        except Error as erro:
            print("Falha ao inserir dados na tabela funcionario: {}".format(erro))
            return False


    def sqlite_readSec_fornecedor(self,cpf):
        try:
            if(True):
                conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
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

    def sqlite_readSec_fornecedor_todos(self):
        try:
            if(True):
                conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
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
                conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
                cursor = conexao.cursor()
                cursor.execute('SELECT * FROM `cliete` WHERE CPF= %s'%cpf)
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
                conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
                cursor = conexao.cursor()
                cursor.execute('SELECT * FROM `cliete`')
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
                conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
                cursor = conexao.cursor()

                cursor.execute("SELECT * FROM `funcionari` WHERE CPF=%s AND senha= MD5('%s')" %(cpf,senha))
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

            if(fornecedor != []):

                conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
                cursor = conexao.cursor()

                cursor.execute('INSERT INTO Produto (n_bebida,nome_da_bebida,data_de_fabricacao,data_validade,condicoes_de_armazenamento,quantidades,local_armazenado,valor_de_compra_UN,valor_revenda_UN,Fornecedor_idFornecedor) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' , (bd_n_bebida,bd_nome_da_bebida,bd_data_de_fabricacao,bd_data_de_validade,bd_condicoes_de_armazenamento,bd_quantidades,bd_local_armazenado,bd_valor_de_compra_UN,bd_valor_revenda_UN,fornecedor[0][0]))

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
                conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
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
                conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
                cursor = conexao.cursor()

                cursor.execute("SELECT * FROM `produto` WHERE n_bebida= %s" %(n_bebida))
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


    def sqlite_create_venda(self,forma_de_pagamento,data_da_venda,nome_bebida,cpf_cliente,cpf_funcionario,senha_funcionario):
        
        try:

            bd_forma_de_pagamento = str(forma_de_pagamento)
            bd_data_da_venda = str(data_da_venda)
            produto = self.sqlite_read_produto(nome_bebida)
            cliente = self.sqlite_readSec_cliente(cpf_cliente)
            funcioanrio = self.sqlite_read_funcionario(cpf_funcionario,senha_funcionario)

            

            if(cliente != [] and funcioanrio != [] and produto != []):

                conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
                cursor = conexao.cursor()

                print(cliente[0][0])
                print(funcioanrio[0][0])
                cursor.execute('INSERT INTO Vendas (forma_de_pagamento,data_da_venda,Produto_idproduto,Cliete_idCliete,Funcionari_idFuncionari) VALUES (%s,%s,%s,%s,%s)' , (bd_forma_de_pagamento,bd_data_da_venda,produto[0][0],cliente[0][0],funcioanrio[0][0]))

                conexao.commit()
                conexao.close()

                nova_quantidade = int(produto[0][6]) - 1
                self.sqlite_update_produto_crinado_venda(nome_bebida,nova_quantidade)

                return True

            else:
                print('Não foi possivel cadastrar a venda pois o cliente, ou produto informado não estao cadastrado')

        except Error as erro:
            print("Falha ao inserir dados na tabela vendas: {}".format(erro))
            return False

    def sqlite_read_venda(self):
        try:
            if(True):
                conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
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


    def sqlite_update_produto_crinado_venda(self,n_bebida,nova_quantidade):
        try:

            #produto = self.sqlite_read_produto(nome_produto)

            if(True):

                conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
                cursor = conexao.cursor()
                #print(lista)
                cursor.execute('UPDATE `produto` SET quantidades="%s" WHERE n_bebida = %s' % (str(nova_quantidade),n_bebida))
                conexao.commit()
                conexao.close()

                return True

        except Error as erro:
            print("Falha ao fazer update da tabela produto: {}".format(erro))
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
            fornecedor = self.sqlite_readSec_fornecedor(cnpj_fornecedor)          

            if(fornecedor != []):

                conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
                cursor = conexao.cursor()
                #print(lista)
                cursor.execute('UPDATE `produto` SET nome_da_bebida="%s",data_de_fabricacao = "%s",data_validade = "%s", condicoes_de_armazenamento = "%s",quantidades="%s", local_armazenado = "%s",valor_de_compra_UN = "%s",valor_revenda_UN = "%s", Fornecedor_idFornecedor = "%s" WHERE n_bebida = %s' % (bd_nome_da_bebida,bd_data_de_fabricacao,bd_data_de_validade,bd_condicoes_de_armazenamento,bd_quantidades,bd_local_armazenado,bd_valor_de_compra_UN,bd_valor_revenda_UN,fornecedor[0][0],bd_n_bebida))
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

                conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
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

                conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
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

                conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
                cursor = conexao.cursor()
                #print(lista)
                cursor.execute('UPDATE Cliete SET nome = "%s",endereco = "%s",data_de_nascimento = "%s",email = "%s",telefone = "%s" WHERE cpf = %s' % (bd_nome,bd_edereco,bd_data_de_nascimento,bd_email,bd_telefone,bd_cpf))
                conexao.commit()
                conexao.close()

                return True


        except Error as erro:
            print("Falha ao fazer update da tabela cliente: {}".format(erro))
            return False

    def sqlite_remove_fornecedor(self,cnpj):
        try:      
            if(True):

                conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
                cursor = conexao.cursor()
                #print(lista)
                cursor.execute('DELETE FROM `mydb`.`fornecedor` WHERE CNPJ = %s' % (str(cnpj)))
                conexao.commit()
                conexao.close()

                return True


        except Error as erro:
            print("Falha ao remover fornecedor: {}".format(erro))
            return False

    def sqlite_remove_cliente(self,cpf):
        try:      
            if(True):

                conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
                cursor = conexao.cursor()
                #print(lista)
                cursor.execute('DELETE FROM `mydb`.`cliete` WHERE CPF = %s' % (str(cpf)))
                conexao.commit()
                conexao.close()

                return True


        except Error as erro:
            print("Falha ao remover cliente: {}".format(erro))
            return False

    def sqlite_remove_produto(self,n_bebida):
        try:      
            if(True):

                conexao = mysql.connect(host = 'localhost',db='mydb',user='root')
                cursor = conexao.cursor()
                #print(lista)
                cursor.execute('DELETE FROM `mydb`.`produto` WHERE n_bebida = %s' %(str(n_bebida)))
                conexao.commit()
                conexao.close()

                return True


        except Error as erro:
            print("Falha ao remover produto: {}".format(erro))
            return False

    