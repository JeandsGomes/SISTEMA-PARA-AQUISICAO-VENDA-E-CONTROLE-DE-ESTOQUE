import socket

from mysql.connector.utils import print_buffer

class plataforma_funcionario():
    '''
        O objeto plataforma_funcionario contém um cliente.
        Todos as informações do objeto são inicializados
        e deixados vazios até ser adicionado informações.
    '''
    __slots__ = ['_nome','_cpf','_data_de_nascimento','_email','_telefone','_cargo','_senha']

    def __init__(self):
        self._nome = ''
        self._cpf = ''
        self._data_de_nascimento = ''
        self._email = ''
        self._telefone = ''
        self._cargo = ''
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
    
    @property
    def cargo(self):
        '''
            retorna o cargo do funcionario.
        '''
        return self._cargo

    @property
    def senha(self):
        '''
            retorna a senha do funcionario.
        '''
        return self._senha

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

    def cadastro(self,nome,cpf,data_de_nascimento,email,telefone,cargo,senha):
        '''
            Para cadastrar uma pessoa é preciso se conectar ao servidor do banco.

            :Parametros nome,sobrenome,CPf: contém as informações da pessoa que deseja ser cliente do banco.
            :tipo nome,sobrenome,CPf: str
            :raise: se a classe retornar false, não foi possivel fazer o cadastro da pessoa no banco.
            :retorna bool. 

        '''
        codigo = '0/'+nome+'/'+cpf+'/'+data_de_nascimento+'/'+email+'/'+telefone+'/'+cargo+'/'+senha
        try:
            saida = self.conecxao_servidor(codigo)
        except:
            return False
        print(codigo)
        saida_lst = saida.split('/')
        if(saida_lst[0]=='1'):
            return True
        return False