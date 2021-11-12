import socket
import threading
from cadastrar import Cadastro

class ClientThread(threading.Thread):

    def __init__(self,clientAddress,con,sinc):
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
        codigo = self._servidor.pre_processamento(recebe.decode())
        print(codigo)
    
        if(codigo[0] == 'cadastra'):
            print("Cadastrando funcionario")
            
        elif(codigo[0] == 'login'):
            print("Login do funcionario")

        elif(codigo[0] == 'dados_bebida'):
            print("Buscando dados da bebida")

        elif(codigo[0] == 'venda'):
            print("Realizar venda")

        elif(codigo[0] == 'busca_cliente'):
            print("Buscar dados do cliente")

        elif(codigo[0] == 'cadastrar_cliente'):
            print("Cadastrar cliente")

        elif(codigo[0] == 'cadas_mercadoria'):
            print("Cadastrar mercadoria")

        elif(codigo[0] == 'historico'):
            print("Consultar historico de vendas")

        elif(codigo[0] == 'Cadastrar fornecedor'):
            print("Cadastrar fornecedor")

        elif(codigo[0] == 'buscar_fornecedor'):
            print("Buscar fornecedor")
            
            
        saida = 'Comunicacao realizada'

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
        self._cadastro = Cadastro()
        self._n_conta = 0

    def pre_processamento(self,codigo):
        '''
            Para realizar o pre-processamento do codigo enviado pelo cliente.

            :parametro codigo: string enviada pelo cliente e obtido apos a conecção com o cliente.
            :retorna o codigo_lista, que é o codigo pre processado em formato de lista.

        '''

        codigo_lista = codigo.split('/')
        #cadastra
        #'0/'+nome_completo+'/'+cpf+'/'+endereco+'/'+data_de_nascimento+'/'+email+'/'+telefone+'/'+senha
        if(codigo_lista[0]=='0'):
            codigo_lista[0] = 'cadastra'

        #login
        #'1/'+cpf+'/'+senha
        elif(codigo_lista[0]=='1'):
            codigo_lista[0] = 'login'

        #Busca por dados da bebida solicitada
        #2/'+nome_bebida
        elif(codigo_lista[0]=='2'):
            codigo_lista[0] = 'dados_bebida'

        #Realizar uma venda
        #'3/'+index_bebida+'/'+quantidade+'/'+index_cliente+'/'+forma_de_pagamento
        elif(codigo_lista[0]=='3'):
            codigo_lista[0] = 'venda'

        #Buscar dados do cliente
        #'4/'+cpf_cliente
        elif(codigo_lista[0]=='4'):
            codigo_lista[0] = 'busca_cliente'

        #Cadastrar cliente
        #'5/'+nome_completo+'/'+cpf+'/'+endereco+'/'+data_de_nascimento+'/'+email+'/'+telefone
        elif(codigo_lista[0]=='5'):
            codigo_lista[0] = 'cadastrar_cliente'

        #Cadastrar mercadoria
        #'6/'+nome_bebida+'/'+numero_lote+'/'+data_fabricacao+'/'+local_fabricacao+'/'+condicoes_armazenamento+'/'+quantidade+'/'+local_armazenado+'/'+valor_compra+'/'+valor_revenda+'/'+data_entrada+'/'+id_fornecedor
        elif(codigo_lista[0]=='6'):
            codigo_lista[0] = 'cadas_mercadoria'

        #Consultar historico de vendas
        #'7/'
        elif(codigo_lista[0]=='7'):
            codigo_lista[0] = 'historico'

        #Cadastrar fornecedor
        #'8/'+razao_social+'/'+cnpj+'/'+nacionalidade+'/'+endereco+'/'+telefone+'/'+nome_do_contato
        elif(codigo_lista[0]=='8'):
            codigo_lista[0] = 'Cadastrar fornecedor'

        #buscar fornecedor
        #'9/'+cnpj_fornecedor
        elif(codigo_lista[0]=='9'):
            codigo_lista[0] = 'buscar_fornecedor'
            
        return codigo_lista

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