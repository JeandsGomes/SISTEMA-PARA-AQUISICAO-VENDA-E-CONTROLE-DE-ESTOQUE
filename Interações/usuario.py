import socket

#from mysql.connector.utils import print_buffer

class plataforma_funcionario():
    '''
        O objeto plataforma_funcionario contém um cliente.
        Todos as informações do objeto são inicializados
        e deixados vazios até ser adicionado informações.
    '''
    __slots__ = ['_nome_completo','_cpf','_endereco','_data_de_nascimento','_email','_telefone','_cargo','_senha']

    def __init__(self):
        self._nome_completo = ''
        self._cpf = ''
        self._endereco = ''
        self._data_de_nascimento = ''
        self._email = ''
        self._telefone = ''
        self._senha= ''

    @property
    def nome(self):
        '''
            retorna o nome do funcionario.
        '''
        return self._nome

    @property
    def cpf(self):
        '''
            retorna o cpf do funcionario.
        '''
        return self._cpf

    @property
    def data_de_nascimento(self):
        '''
            retorna a data de nascimento do funcionario.
        '''
        return self._data_de_nascimento

    @property
    def email(self):
        '''
            retorna o email do funcionario.
        '''
        return self._email

    @property
    def telefone(self):
        '''
            retorna o telefone do funcionario.
        '''
        return self._telefone


    def conecxao_servidor(self,codigo):
        '''
            Para os dados do cliente serem salvos, devera se conectar com o servidor do banco.

            Após se conectar com o servidor será possivel fazer todas as operações disponíveis.

            :parametro codigo: são as informaçoes com alteraçoes na conta de algum cliente no servidor.
            :retorna as informações obtidas no servidor.
        '''
        
        ip = 'localhost'
        port = 8000
        addr = ((ip, port)) #define a tupla de endereco
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET parametro para informar familia do protocolo
        client_socket.connect(addr) #realizar conexao
        client_socket.send(codigo.encode()) #envia mensagfem
        print('entrada: '+codigo)
        saida = client_socket.recv(1024).decode()
        client_socket.close() #fecha conexao

        return saida

    def cadastro_funcionario(self,nome_completo,cpf,endereco,data_de_nascimento,email,telefone,senha):
        '''
            Para cadastrar uma pessoa é preciso se conectar ao servidor do banco.

        '''
        codigo = '0/'+nome_completo+'/'+cpf+'/'+endereco+'/'+data_de_nascimento+'/'+email+'/'+telefone+'/'+senha
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            return True
        return False

    def login_funcionario(self,cpf,senha):
        '''
            Para um cliente realizar operações em sua conta é preciso realizar o login.
        '''
        codigo = '1/'+cpf+'/'+senha
        try:
            saida = self.conecxao_servidor(codigo)
            
        except:
            return False
        saida_lst = saida.split('/')
        
        if(saida_lst[0]=='1'):
            self._nome_completo = saida_lst[1]
            self._cpf = saida_lst[2]
            self._endereco = saida_lst[3]
            self._data_de_nascimento = saida_lst[4]
            self._email = saida_lst[5]
            self._telefone = saida_lst[6]
            #self._senha= saida_lst[7]

            return True
        return False

    def buscar_de_bebidas(self,nome_bebida):
        '''
            Busca as bebidas com o nome informado
        '''
        codigo = '2/'+nome_bebida
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        saida_lst = saida.split('/')
        
        if(saida_lst[0]=='1'):
            return saida_lst

        return False

    def realizar_venda(self,index_bebida,quantidade,index_cliente,forma_de_pagamento):
        '''
            Envia uma mensagem solicitando uma venda ao servidor
        '''
        codigo = '3/'+index_bebida+'/'+quantidade+'/'+index_cliente+'/'+forma_de_pagamento
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        saida_lst = saida.split('/')
        
        if(saida_lst[0]=='1'):
            return True

        return False

    def busca_cliente(self,cpf_cliente):
        '''
            Buscar clientes
        '''
        codigo = '4/'+cpf_cliente
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        saida_lst = saida.split('/')
        
        if(saida_lst[0]=='1'):
            return saida_lst

        return False

    def cadastro_cliente(self,nome_completo,cpf,endereco,data_de_nascimento,email,telefone):
        '''
            Para cadastrar clientes.
        '''
        codigo = '5/'+nome_completo+'/'+cpf+'/'+endereco+'/'+data_de_nascimento+'/'+email+'/'+telefone
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            return True
        return False
    
    def cadastro_mercadoria(self,nome_bebida,numero_lote,data_fabricacao,local_fabricacao,condicoes_armazenamento,quantidade,local_armazenado,valor_compra,valor_revenda,data_entrada,id_fornecedor):
        '''
            Para cadastrar mercadoria.
        '''
        codigo = '6/'+nome_bebida+'/'+numero_lote+'/'+data_fabricacao+'/'+local_fabricacao+'/'+condicoes_armazenamento+'/'+quantidade+'/'+local_armazenado+'/'+valor_compra+'/'+valor_revenda+'/'+data_entrada+'/'+id_fornecedor
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            return True
        return False

    def consiultar_historico_de_vendas(self):
        '''
            Buscar historico de vendas
        '''
        codigo = '7/'
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        saida_lst = saida.split('/')
        
        if(saida_lst[0]=='1'):
            return saida_lst

        return False

    def cadastro_fornecedor(self,razao_social,cnpj,nacionalidade,endereco,telefone,nome_do_contato):
        '''
            Cadastrar fornecedor.
        '''
        codigo = '8/'+razao_social+'/'+cnpj+'/'+nacionalidade+'/'+endereco+'/'+telefone+'/'+nome_do_contato
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            return True
        return False

    def busca_fornecedor(self,cnpj_fornecedor):
        '''
            Buscar fornecedor.
        '''
        codigo = '9/'+cnpj_fornecedor
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        saida_lst = saida.split('/')
        
        if(saida_lst[0]=='1'):
            return saida_lst

        return False
