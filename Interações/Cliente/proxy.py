from abc import ABC, abstractmethod
import socket

"""
A interface Subject declara operações comuns para RealSubject e
o procurador. Contanto que o cliente trabalhe com o RealSubject usando este
interface, você poderá passar um proxy em vez de um assunto real. 
"""
class Subject(ABC):
    @abstractmethod
    def conecxao_servidor(self) -> None:
        pass


"""
O RealSubject contém alguma lógica de negócios principal. Normalmente, RealSubjects são
capaz de fazer algum trabalho útil que também pode ser muito lento ou sensível -
por exemplo. corrigindo os dados de entrada. Um Proxy pode resolver esses problemas sem qualquer
alterações no código do RealSubject. 
"""
class RealSubject(Subject):
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


"""
O Proxy tem a interface identica ao RealSubject.
"""
"""
As aplicações mais comuns do padrão Proxy são carregamento lento,
cache, controle de acesso, log, etc. Um Proxy pode realizar um
dessas coisas e depois, dependendo do resultado, passar a execução para
o mesmo método em um objeto RealSubject vinculado. 
"""
class Proxy(Subject):
    def __init__(self) -> None:
        self._real_subject = RealSubject()

    def conecxao_servidor(self,codigo):
        return self._real_subject.conecxao_servidor(codigo)



"""
O código cliente deve funcionar com todos os objetos (tanto Realsubject quanto
Proxies) por meio da interface Subject para oferecer suporte a assuntos reais
e procurações. Na vida real, no entanto, os clientes trabalham principalmente com seus
assuntos diretamente. Neste caso, para implementar o padrão mais facilmente, você
pode estender seu Proxy da classe do sujeito real. 
"""
class Cliente:
    def __init__(self):
        self.subject = Proxy()

    def conecxao_servidor(self,codigo):
        return self.subject.conecxao_servidor(codigo)
