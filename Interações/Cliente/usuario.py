import socket
from proxy import Cliente

#from mysql.connector.utils import print_buffer

class plataforma_funcionario():
    '''
        O objeto plataforma_funcionario contém um cliente.
        Todos as informações do objeto são inicializados
        e deixados vazios até ser adicionado informações.
    '''

    def __init__(self):
        self.cliente = Cliente()
        self.funcionario = []
        self.vendas_todas = []
        self.vendas = []
        self.fornecedor_todos = []
        self.fornecedor = []
        self.cliente_todos = []
        self.cliete = []
        self.prdotos_todas = []
        self.prdotos = []

    def cadastro_funcionario(self,nome,CPF,data_de_ascimento,email,telefone,Cargo,senha):
        '''
            Para cadastrar uma pessoa é preciso se conectar ao servidor do banco.
        '''
        codigo = '0/'+nome+'/'+str(CPF)+'/'+data_de_ascimento+'/'+email+'/'+telefone+'/'+Cargo+'/'+senha
        try:
            saida = self.cliente.conecxao_servidor(codigo)
        except:
            return False
        #print(codigo)
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            return True
        return False

    def login_funcionario(self,cpf,senha):
        '''
            Para um cliente realizar operações em sua conta é preciso realizar o login.
        '''
        codigo = '1/'+str(cpf)+'/'+senha
        try:
            saida = self.cliente.conecxao_servidor(codigo)
            
        except:
            return False
        saida_lst = saida.split('/')
        print(saida_lst)
        
        if(saida_lst[0]=='1'):
            self.funcionario = saida_lst
            print(self.funcionario)
            return True
        return False
    
    def cadastrar_cliente(self,nome,cpf,edereco,data_de_nascimento,email,telefone):        
        codigo = '2/'+nome+'/'+str(cpf)+'/'+edereco+'/'+data_de_nascimento+'/'+email+'/'+telefone
        try:
            saida = self.cliente.conecxao_servidor(codigo)
        except:
            return False
        #print(codigo)
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            return True
        return False

    def buscar_clente(self,cpf):
        codigo = '3/'+str(cpf)
        try:
            saida = self.cliente.conecxao_servidor(codigo)
            
        except:
            return False
        saida_lst = saida.split('/')
        #print(saida_lst)
        
        if(saida_lst[0]=='1'):
            self.cliete = saida_lst
            #print(self.funcionario)
            return True
        return False

    def buscar_todos_clientes(self):
        codigo = '4/'+str(len(self.cliente_todos))
        try:
            saida = self.cliente.conecxao_servidor(codigo)
            
        except:
            return False
        saida_lst = saida.split('/')
        #print(saida_lst)
        
        if(saida_lst[0]=='1'):
            cont = len(self.cliente_todos)-1
            for i in range(1,len(saida_lst)):
                if(saida_lst[i] == '-'):
                    self.cliente_todos.append([])
                    cont = cont + 1
                else:
                    self.cliente_todos[cont].append(saida_lst[i])
            #print(self.cliente_todos)
            return True
        return False

    def atualiza_cliente(self,nome,cpf,edereco,data_de_nascimento,email,telefone):
        codigo = '5/'+nome+'/'+str(cpf)+'/'+edereco+'/'+data_de_nascimento+'/'+email+'/'+telefone
        try:
            saida = self.cliente.conecxao_servidor(codigo)
        except:
            return False
        #print(codigo)
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            return True
        return False

    def remover_cliente(self,cpf):
        codigo = '6/'+str(cpf)
        try:
            saida = self.cliente.conecxao_servidor(codigo)
        except:
            return False
        #print(codigo)
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            return True
        return False

    def cadastra_fornecedor(self,razao_social,CNPJ,nacionalidade,endereco,telefone,passoa_contato):
        codigo = '7/'+razao_social+'/'+str(CNPJ)+'/'+nacionalidade+'/'+endereco+'/'+telefone+'/'+passoa_contato
        try:
            saida = self.cliente.conecxao_servidor(codigo)
        except:
            return False
        #print(codigo)
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            return True
        return False

    def buscar_fornecedor(self,CNPJ):
        codigo = '8/'+str(CNPJ)
        try:
            saida = self.cliente.conecxao_servidor(codigo)
            
        except:
            return False
        saida_lst = saida.split('/')
        #print(saida_lst)
        
        if(saida_lst[0]=='1'):
            self.fornecedor = saida_lst
            #print(self.funcionario)
            return True
        return False

    def buscar_todos_fornecedores(self):
        codigo = '9/'+str(len(self.fornecedor_todos))
        try:
            saida = self.cliente.conecxao_servidor(codigo)
            
        except:
            return False
        saida_lst = saida.split('/')
        #print(saida_lst)
        
        if(saida_lst[0]=='1'):
            cont = len(self.fornecedor_todos)-1
            for i in range(1,len(saida_lst)):
                if(saida_lst[i] == '-'):
                    self.fornecedor_todos.append([])
                    cont = cont + 1
                else:
                    self.fornecedor_todos[cont].append(saida_lst[i])
            #print(self.cliente_todos)
            return True
        return False

    def atualziar_fornecedor(self,razao_social,CNPJ,nacionalidade,endereco,telefone,passoa_contato):
        codigo = '10/'+razao_social+'/'+str(CNPJ)+'/'+nacionalidade+'/'+endereco+'/'+telefone+'/'+passoa_contato
        try:
            saida = self.cliente.conecxao_servidor(codigo)
        except:
            return False
        #print(codigo)
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            return True
        return False

    def remover_fornecedor(self,CNPJ):
        codigo = '11/'+str(CNPJ)
        try:
            saida = self.cliente.conecxao_servidor(codigo)
        except:
            return False
        #print(codigo)
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            return True
        return False

    def cadastra_produto(self,n_bebida,nome_da_bebida,data_de_fabricacao,data_de_validade,condicoes_de_armazenamento,quantidades,local_armazenado,valor_de_compra_UN,valor_revenda_UN,cnpj_fornecedor):
        codigo = '12/'+str(n_bebida)+'/'+nome_da_bebida+'/'+data_de_fabricacao+'/'+data_de_validade+'/'+condicoes_de_armazenamento+'/'+quantidades+'/'+local_armazenado+'/'+str(valor_de_compra_UN)+'/'+str(valor_revenda_UN)+'/'+str(cnpj_fornecedor)
        try:
            saida = self.cliente.conecxao_servidor(codigo)
        except:
            return False
        #print(codigo)
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            return True
        return False

    def buscar_produto(self,n_bebida):

        codigo = '13/'+str(n_bebida)
        try:
            saida = self.cliente.conecxao_servidor(codigo)
            
        except:
            return False
        saida_lst = saida.split('/')
        #print(saida_lst)
        
        if(saida_lst[0]=='1'):
            self.prdotos = saida_lst
            #print(self.funcionario)
            return True
        return False

    def buscar_produto_todos(self):
        codigo = '14/'+str(len(self.prdotos_todas))
        try:
            saida = self.cliente.conecxao_servidor(codigo)
            
        except:
            return False
        saida_lst = saida.split('/')
        #print(saida_lst)
        
        if(saida_lst[0]=='1'):
            cont = len(self.prdotos_todas)-1
            for i in range(1,len(saida_lst)):
                if(saida_lst[i] == '-'):
                    self.prdotos_todas.append([])
                    cont = cont + 1
                else:
                    self.prdotos_todas[cont].append(saida_lst[i])
            #print(self.cliente_todos)
            return True
        return False

    def atualizar_produto(self,n_bebida,nome_da_bebida,data_de_fabricacao,data_de_validade,condicoes_de_armazenamento,quantidades,local_armazenado,valor_de_compra_UN,valor_revenda_UN,cnpj_fornecedor):
        codigo = '15/'+str(n_bebida)+'/'+nome_da_bebida+'/'+data_de_fabricacao+'/'+data_de_validade+'/'+condicoes_de_armazenamento+'/'+quantidades+'/'+local_armazenado+'/'+str(valor_de_compra_UN)+'/'+str(valor_revenda_UN)+'/'+str(cnpj_fornecedor)
        try:
            saida = self.cliente.conecxao_servidor(codigo)
        except:
            return False
        #print(codigo)
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            return True
        return False

    def remover_produto(self,n_bebida):
        codigo = '16/'+str(n_bebida)
        try:
            saida = self.cliente.conecxao_servidor(codigo)
        except:
            return False
        #print(codigo)
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            return True
        return False

    def cadastrar_venda(self,forma_de_pagamento,data_da_venda,n_bebida,cpf_cliente,cpf_funcionario,senha_funcionario):
        codigo = '17/'+forma_de_pagamento+'/'+data_da_venda+'/'+str(n_bebida)+'/'+str(cpf_cliente)+'/'+str(cpf_funcionario)+'/'+senha_funcionario
        try:
            saida = self.cliente.conecxao_servidor(codigo)
        except:
            return False
        #print(codigo)
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            return True
        return False

    def buscar_vendas_todas(self):
        codigo = '18/'+str(len(self.vendas_todas))
        try:
            saida = self.cliente.conecxao_servidor(codigo)
            
        except:
            return False
        saida_lst = saida.split('/')
        #print(saida_lst)
        
        if(saida_lst[0]=='1'):
            cont = len(self.vendas_todas)-1
            for i in range(1,len(saida_lst)):
                if(saida_lst[i] == '-'):
                    self.vendas_todas.append([])
                    cont = cont + 1
                else:
                    print('cont = {}'.format(cont))
                    print('i = {}'.format(i))
                    print(self.vendas_todas[cont])
                    print(saida_lst[i])
                    self.vendas_todas[cont].append(saida_lst[i])
            #print(self.cliente_todos)
            return True
        return False
