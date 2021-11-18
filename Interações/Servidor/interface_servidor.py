import socket
import threading
from cadastrar import Cadastro

class ClientThread(threading.Thread):

    def __init__(self,clientAddress,con,sinc):
        self._cadastro = Cadastro()
        threading.Thread.__init__(self)
        self.con = con
        self.sinc = sinc
        self._servidor = Servidor()
        print("Nova conexao: ",clientAddress)

    def run(self):
        self.sinc.acquire()
        self._codigo=self.operacao_da_thread()
        self.sinc.release()
        print("Finalizando")

    def operacao_da_thread(self):

        #operacoes do servidor
        print('-aguardando solicitacao...')
        recebe = self.con.recv(1024) #define que os pacotes recebidos são de ate 1024 bytes
        
        print('-solicitacao recebida...')

        #pre-processamento do codigo
        codigo_str = recebe.decode()
        codigo = codigo_str.split('/')
        print(codigo)
    
        #cadastra funcionario
        #op,nome,CPF,data_de_ascimento,email,telefone,Cargo,senha
        if(codigo[0] == '0'):
            dados_ja_usado = []
            flag = False
            print("Cadastrando funcionario")
            dados_ja_usado.append(self._cadastro.sqlite_read_funcionario_cpf(codigo[2]))
            if(dados_ja_usado == [False]):
                dados_ja_usado.append(self._cadastro.sqlite_read_funcionario(codigo[2],codigo[7]))
            if(dados_ja_usado == [False,False]):
                flag = self._cadastro.sqlite_create_funcionario(codigo[1],codigo[2],codigo[3],codigo[4],codigo[5],codigo[6],codigo[7])
            else:
                print('CPF ou Senha ja utilizados')
            if(flag == True):
                saida = '1/'
            else:
                saida = '0/'
            
        #login funcionario
        #cpf,senha
        elif(codigo[0] == '1'):
            print("Login do funcionario")
            flag = self._cadastro.sqlite_read_funcionario(codigo[1],codigo[2])
            print(flag)
            if(flag == False):
                saida = '0/'
            else:
                saida = '1/'+flag[0][1]+'/'+flag[0][2]+'/'+codigo[2]

        #Cadastrar Cliente
        #op,nome,cpf,edereco,data_de_nascimento,email,telefone
        elif(codigo[0] == '2'):
            dados_ja_usado = []
            flag = False
            print("Cadastrando Cliente")
            print(codigo[2])
            dados_ja_usado.append(self._cadastro.sqlite_readSec_cliente(codigo[2]))
            if(dados_ja_usado == [False]):
                flag = self._cadastro.sqlite_create_cliente(codigo[1],codigo[2],codigo[3],codigo[4],codigo[5],codigo[6])
            else:
                print('CPF ou ja utilizado')
            if(flag == True):
                saida = '1/'
            else:
                saida = '0/'

        #Busca Cliente
        #opc/cpf
        elif(codigo[0] == '3'):
            print("Busca do Cliente")
            flag = self._cadastro.sqlite_readSec_cliente(codigo[1])
            print(flag)
            if(flag == False):
                saida = '0/'
            else:
                saida = '1/'+flag[0][1]+'/'+flag[0][2]+'/'+flag[0][3]+'/'+flag[0][4]+'/'+flag[0][5]+'/'+flag[0][6]

        #Busca todos os Cliente
        #opc/qnt
        elif(codigo[0] == '4'):
            print("Busca todos os Cliente")
            flag = self._cadastro.sqlite_readSec_cliente_todos()
            print(flag)
            if(flag == False):
                saida = '0/'
            else:
                saida = '1'
                for i in range(int(codigo[1]),int(codigo[1])+5):
                    if(i < len(flag)):
                        saida = saida+'/-/'+flag[i][1]+'/'+flag[i][2]+'/'+flag[i][3]+'/'+flag[i][4]+'/'+flag[i][5]+'/'+flag[i][6]  

        #Atualizar Cliente
        #op,nome,cpf,edereco,data_de_nascimento,email,telefone
        elif(codigo[0] == '5'):
            print("Atualzar Cliente")
            flag = self._cadastro.sqlite_update_cliente(codigo[1],codigo[2],codigo[3],codigo[4],codigo[5],codigo[6])
            print(flag)
            if(flag == False):
                saida = '0/'
            else:
                saida = '1/'

        #Remover Cliente
        #op,cpf
        elif(codigo[0] == '6'):
            print("Remover Cliente Cliente")
            flag = self._cadastro.sqlite_remove_cliente(codigo[1])
            print(flag)
            if(flag == False):
                saida = '0/'
            else:
                saida = '1/'

        #Cadastrar Fornecedor
        #opc,razao_social,CNPJ,nacionalidade,endereco,telefone,passoa_contato
        elif(codigo[0] == '7'):
            dados_ja_usado = []
            flag = False
            print("Cadastrando Fornecedor")
            dados_ja_usado.append(self._cadastro.sqlite_readSec_fornecedor(codigo[2]))
            if(dados_ja_usado == [False]):
                flag = self._cadastro.sqlite_create_fornecedor(codigo[1],codigo[2],codigo[3],codigo[4],codigo[5],codigo[6])
            else:
                print('CNPJ ou ja utilizado')
            if(flag == True):
                saida = '1/'
            else:
                saida = '0/'

        #Buscar Fornecedor
        #opc,CNPJ
        elif(codigo[0] == '8'):
            print("Busca do Fornecedor")
            flag = self._cadastro.sqlite_readSec_fornecedor(codigo[1])
            print(flag)
            if(flag == False):
                saida = '0/'
            else:
                saida = '1/'+flag[0][1]+'/'+flag[0][2]+'/'+flag[0][3]+'/'+flag[0][4]+'/'+flag[0][5]+'/'+flag[0][6]

        #Buscar Todos Fornecedores
        #opc,qtd
        elif(codigo[0] == '9'):
            print("Busca todos os Fornecedores")
            flag = self._cadastro.sqlite_readSec_fornecedor_todos()
            print(flag)
            if(flag == False):
                saida = '0/'
            else:
                saida = '1'
                for i in range(int(codigo[1]),int(codigo[1])+5):
                    if(i < len(flag)):
                        saida = saida+'/-/'+flag[i][1]+'/'+flag[i][2]+'/'+flag[i][3]+'/'+flag[i][4]+'/'+flag[i][5]+'/'+flag[i][6]

        #Atualizar Fornecedor
        #opc,razao_social,CNPJ,nacionalidade,endereco,telefone,passoa_contato
        elif(codigo[0] == '10'):
            print("Atualzar Fornecedor")
            flag = self._cadastro.sqlite_update_fornecedor(codigo[1],codigo[2],codigo[3],codigo[4],codigo[5],codigo[6])
            print(flag)
            if(flag == False):
                saida = '0/'
            else:
                saida = '1/'

        #Remover Fornecedor
        #opc,CNPJ
        elif(codigo[0] == '11'):
            print("Remover Cliente Cliente")
            flag = self._cadastro.sqlite_remove_fornecedor(codigo[1])
            print(flag)
            if(flag == False):
                saida = '0/'
            else:
                saida = '1/'

        #Cadastra Produto
        #opc,n_bebida,nome_da_bebida,data_de_fabricacao,data_de_validade,condicoes_de_armazenamento,quantidades,local_armazenado,valor_de_compra_UN,valor_revenda_UN,cnpj_fornecedor
        elif(codigo[0] == '12'):
            dados_ja_usado = []
            flag = False
            print("Cadastrando Produto")
            dados_ja_usado.append(self._cadastro.sqlite_read_produto(codigo[1]))
            if(dados_ja_usado == [False]):
                print('aqui')
                flag = self._cadastro.sqlite_create_produto(codigo[1],codigo[2],codigo[3],codigo[4],codigo[5],codigo[6],codigo[7],codigo[8],codigo[9],codigo[10])
            else:
                print('Dados informados são invalidos')
            if(flag == True):
                saida = '1/'
            else:
                saida = '0/'

        #Buscar Produto
        #opc,n_bebida
        elif(codigo[0] == '13'):
            print("Busca do Produto")
            flag = self._cadastro.sqlite_read_produto(codigo[1])
            print(flag)
            if(flag == False):
                saida = '0/'
            else:
                saida = '1/'+flag[0][1]+'/'+flag[0][2]+'/'+flag[0][3]+'/'+flag[0][4]+'/'+flag[0][5]+'/'+flag[0][6]+'/'+flag[0][7]+'/'+flag[0][8]+'/'+flag[0][9]+'/'+str(flag[0][10])

        #Busca Todos os Produtos
        #opc,qtd
        elif(codigo[0] == '14'):
            print("Busca todos os Produtos")
            flag = self._cadastro.sqlite_read_produto_todos()
            print(flag)
            if(flag == False):
                saida = '0/'
            else:
                saida = '1'

                for i in range(int(codigo[1]),int(codigo[1])+5):
                    if(i < len(flag)):
                        saida = saida+'/-/'+flag[i][1]+'/'+flag[i][2]+'/'+flag[i][3]+'/'+flag[i][4]+'/'+flag[i][5]+'/'+flag[i][6]+'/'+flag[i][7]

        #Atualziar Produto
        #opc,n_bebida,nome_da_bebida,data_de_fabricacao,data_de_validade,condicoes_de_armazenamento,quantidades,local_armazenado,valor_de_compra_UN,valor_revenda_UN,cnpj_fornecedor
        elif(codigo[0] == '15'):
            print("Atualzar Produto")
            flag = self._cadastro.sqlite_update_produto(codigo[1],codigo[2],codigo[3],codigo[4],codigo[5],codigo[6],codigo[7],codigo[8],codigo[9],codigo[10])
            print(flag)
            if(flag == False):
                saida = '0/'
            else:
                saida = '1/'

        #Remoção de Produto
        #opc,n_bebida
        elif(codigo[0] == '16'):
            print("Remover Produto")
            flag = self._cadastro.sqlite_remove_produto(codigo[1])
            print(flag)
            if(flag == False):
                saida = '0/'
            else:
                saida = '1/'


        #Cadastrar Venda
        #opc,forma_de_pagamento,data_da_venda,n_bebida,cpf_cliente,cpf_funcionario,senha_funcionario
        elif(codigo[0] == '17'):
            print("Cadastrar Venda")
            flag = self._cadastro.sqlite_create_venda(codigo[1],codigo[2],codigo[3],codigo[4],codigo[5],codigo[6])
            print(flag)
            if(flag == False):
                saida = '0/'
            else:
                saida = '1/'

        #Buscar Historico
        #opc,forma_de_pagamento,data_da_venda,n_bebida,cpf_cliente,cpf_funcionario,senha_funcionario
        #forma_de_pagamento,data_da_venda,Produto_idproduto,Cliete_idCliete,Funcionari_idFuncionari,valor_da_compra
        elif(codigo[0] == '18'):
            print("Historico de Vendas")
            flag = self._cadastro.sqlite_read_venda_todas()
            print(flag)
            if(flag == False):
                saida = '0/'
            else:
                saida = '1'
                for i in range(int(codigo[1]),int(codigo[1])+5):
                    if(i < len(flag)):
                        saida = saida+'/-/'+flag[i][1]+'/'+flag[i][2]+'/'+str(flag[i][3])+'/'+str(flag[i][4])+'/'+str(flag[i][5])+'/'+str(flag[i][6])
                

        self.con.send(saida.encode())
        print('-solicitacao recebida...')
        #print('-{} feito por conta {}'.format(codigo[0],codigo[1]))
        #print('')
        #self._servidor.mostrar_todas_contas()
        #print('')

    @property
    def codigo(self):
        return self._codigo

    
class Servidor():
    '''
        O objeto da class Servidor representar a interface de conecção do servido com o cliente.
        Todos as informações do objeto são inicializados e inicializando um objeto do tipo cadastro
        um contador de contas cadastradas.
    '''
    def __init__(self):
        self._n_conta = 0


    def ligar_servidor(self):
            '''
                Para deixar o srvidor apto a realizar coneções e receber mensagens,
                realizando as devidas operações de acordo com o que o cliente informa
                por meio do codigo.
            '''
            host = 'localhost'
            port = 8000
            addr = (host, port)
            serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
            serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reinicializa o socket
            serv_socket.bind(addr) #define a porta e quais ips podem se conectar com o servidor
            serv_socket.listen(10) #define o limite de conexões


            '''
            serv_socket,
            '''

            sinc = threading.Lock()

            while(True):
                print('-aguardando conexao...')
                con, clientAddress = serv_socket.accept() #servidor aguardando conexão
                print('-coneccao realizada')

                newthread = ClientThread(clientAddress, con, sinc)
                newthread.start()
                newthread.join()
                #print('codigo recebido: {}'.format(codigo))

            serv_socket.close()