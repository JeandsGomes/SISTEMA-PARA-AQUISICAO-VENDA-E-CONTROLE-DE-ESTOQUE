#from Banco import Cliente
import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from menu_inicial import Menu_Inicial
from tela_cadastro import Tela_Cadastro
from tela_fornecedor_cadastra import Tela_Fornecedor_Cadastra
from tela_fornecedor_busca_modifica import Tela_Fornecedor_Busca_Modifica
from tela_cliente_cadastra import Tela_Cliente_Cadastra
from tela_cliente_busca_modifica import Tela_Cliente_Busca_Modifica
from tela_login import Tela_Login
from tela_produto_cadastra import Tela_Produto_Cadastra
from tela_produto_busca_modifica import Tela_Produto_Busca_Modifica

#Programa


class Ui_Main(QtWidgets.QWidget):
    '''
    O objeto Ui_Main possui varias telas.
    
    '''
    def setupUi(self,Main):
        Main.setObjectName('Main')
        Main.resize(640,480)#tamnaho da tela

        self.QtStack=QtWidgets.QStackedLayout()#cria pilha

        #qts de telas
        self.stack0=QtWidgets.QMainWindow()
        self.stack1=QtWidgets.QMainWindow()
        self.stack2=QtWidgets.QMainWindow()
        self.stack3=QtWidgets.QMainWindow()
        self.stack4=QtWidgets.QMainWindow()
        self.stack5=QtWidgets.QMainWindow()
        self.stack6=QtWidgets.QMainWindow()
        self.stack7=QtWidgets.QMainWindow()
        self.stack8=QtWidgets.QMainWindow()

        #cria objetos para as telas
        self.tela_login = Tela_Login()
        self.tela_login.setupUi(self.stack0)

        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_menu_inicial = Menu_Inicial()
        self.tela_menu_inicial.setupUi(self.stack2)

        self.tela_cadastra_cliente = Tela_Cliente_Cadastra()
        self.tela_cadastra_cliente.setupUi(self.stack3)

        self.tela_busca_modifica_cliente = Tela_Cliente_Busca_Modifica()
        self.tela_busca_modifica_cliente.setupUi(self.stack4)

        self.tela_cadastra_fornecedor = Tela_Fornecedor_Cadastra()
        self.tela_cadastra_fornecedor.setupUi(self.stack5)

        self.tela_busca_modifica_fornecedor = Tela_Fornecedor_Busca_Modifica()
        self.tela_busca_modifica_fornecedor.setupUi(self.stack6)

        self.tela_cadastra_produto = Tela_Produto_Cadastra()
        self.tela_cadastra_produto.setupUi(self.stack7)

        self.tela_busca_modifica_produto = Tela_Produto_Busca_Modifica()
        self.tela_busca_modifica_produto.setupUi(self.stack8)

        #add ao QtStack
        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)

class Main(QMainWindow,Ui_Main):
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        #Objeto Usuario
        #

        #Botões
        #self.tela_login.pushButton_login_login.clicked.connect(self.abrirSenha)
        
        self.tela_login.login_pushButton_logar.clicked.connect(self.botaoLogin)
        self.tela_login.login_pushButton_entrar_cadastro.clicked.connect(self.abrirCadastro)

        self.tela_cadastro.cadastro_pushButton_cadastrar.clicked.connect(self.botaoCadastro)
        self.tela_cadastro.pushButton_cadastro_entrar_login.clicked.connect(self.abrirLogin)

        #Menu Inicial
        self.tela_menu_inicial.pushButton_vendas.clicked.connect(self.abrirMenuInicial)
        self.tela_menu_inicial.pushButton_cadastra_cliente.clicked.connect(self.abrirCadastraCliente)
        self.tela_menu_inicial.pushButton_atualiza_cliente.clicked.connect(self.abrirBuscaModificaCliente)
        self.tela_menu_inicial.pushButton_cadastra_fornecedor.clicked.connect(self.abrirCadastraFornecedor)
        self.tela_menu_inicial.pushButton_atualiza_fornecedor.clicked.connect(self.abrirBuscaModificaFornecedor)
        self.tela_menu_inicial.pushButton_cadastra_produto.clicked.connect(self.abrirCadastraProduto)
        self.tela_menu_inicial.pushButton_atualiza_produto.clicked.connect(self.abrirBuscaModificaProduto)
        self.tela_menu_inicial.pushButton_sair.clicked.connect(self.abrirLogin)
        self.tela_menu_inicial.pushButton_mostrar_mais.clicked.connect(self.botaoMostrarMaisVendas)
        self.tela_menu_inicial.pushButton_realizar_venda.clicked.connect(self.botaoRealizaVendas)

        #Menu Cliente Cadastra
        self.tela_cadastra_cliente.pushButton_vendas.clicked.connect(self.abrirMenuInicial)
        self.tela_cadastra_cliente.pushButton_cadastra_cliente.clicked.connect(self.abrirCadastraCliente)
        self.tela_cadastra_cliente.pushButton_atualiza_cliente.clicked.connect(self.abrirBuscaModificaCliente)
        self.tela_cadastra_cliente.pushButton_cadastra_fornecedor.clicked.connect(self.abrirCadastraFornecedor)
        self.tela_cadastra_cliente.pushButton_atualiza_fornecedor.clicked.connect(self.abrirBuscaModificaFornecedor)
        self.tela_cadastra_cliente.pushButton_cadastra_produto.clicked.connect(self.abrirCadastraProduto)
        self.tela_cadastra_cliente.pushButton_atualiza_produto.clicked.connect(self.abrirBuscaModificaProduto)
        self.tela_cadastra_cliente.pushButton_sair.clicked.connect(self.abrirLogin)
        self.tela_cadastra_cliente.pushButton_mostrar_mais.clicked.connect(self.botaoMostrarMaisCliente)
        self.tela_cadastra_cliente.pushButton_cadastrar_cliente.clicked.connect(self.botaoCadastrarCliente)

        #Menu Cliente Busca Modifica
        self.tela_busca_modifica_cliente.pushButton_vendas.clicked.connect(self.abrirMenuInicial)
        self.tela_busca_modifica_cliente.pushButton_cadastra_cliente.clicked.connect(self.abrirCadastraCliente)
        self.tela_busca_modifica_cliente.pushButton_atualiza_cliente.clicked.connect(self.abrirBuscaModificaCliente)
        self.tela_busca_modifica_cliente.pushButton_cadastra_fornecedor.clicked.connect(self.abrirCadastraFornecedor)
        self.tela_busca_modifica_cliente.pushButton_atualiza_fornecedor.clicked.connect(self.abrirBuscaModificaFornecedor)
        self.tela_busca_modifica_cliente.pushButton_cadastra_produto.clicked.connect(self.abrirCadastraProduto)
        self.tela_busca_modifica_cliente.pushButton_atualiza_produto.clicked.connect(self.abrirBuscaModificaProduto)
        self.tela_busca_modifica_cliente.pushButton_sair.clicked.connect(self.abrirLogin)
        self.tela_busca_modifica_cliente.pushButton_cadastro_entrar_login.clicked.connect(self.botaoMostrarMaisCliente)
        self.tela_busca_modifica_cliente.pushButton_buscar.clicked.connect(self.botaoBuscaClieten)
        self.tela_busca_modifica_cliente.pushButton_atualizar.clicked.connect(self.botaoAtualizaClieten)
        self.tela_busca_modifica_cliente.pushButton_remover.clicked.connect(self.botaoRemoveClieten)

        #Menu Fornece Cadastra
        self.tela_cadastra_fornecedor.pushButton_vendas.clicked.connect(self.abrirMenuInicial)
        self.tela_cadastra_fornecedor.pushButton_cadastra_cliente.clicked.connect(self.abrirCadastraCliente)
        self.tela_cadastra_fornecedor.pushButton_atualiza_cliente.clicked.connect(self.abrirBuscaModificaCliente)
        self.tela_cadastra_fornecedor.pushButton_cadastra_fornecedor.clicked.connect(self.abrirCadastraFornecedor)
        self.tela_cadastra_fornecedor.pushButton_atualiza_fornecedor.clicked.connect(self.abrirBuscaModificaFornecedor)
        self.tela_cadastra_fornecedor.pushButton_cadastra_produto.clicked.connect(self.abrirCadastraProduto)
        self.tela_cadastra_fornecedor.pushButton_atualiza_produto.clicked.connect(self.abrirBuscaModificaProduto)
        self.tela_cadastra_fornecedor.pushButton_sair.clicked.connect(self.abrirLogin)
        self.tela_cadastra_fornecedor.pushButton_mostrar_mais.clicked.connect(self.botaoMostrarMaisFornecedor)
        self.tela_cadastra_fornecedor.pushButton_cadastra_fornecedor_2.clicked.connect(self.botaoCadastraFornecedor)

        #Menu Fornecedor Busca Modifica
        self.tela_busca_modifica_fornecedor.pushButton_vendas.clicked.connect(self.abrirMenuInicial)
        self.tela_busca_modifica_fornecedor.pushButton_cadastra_cliente.clicked.connect(self.abrirCadastraCliente)
        self.tela_busca_modifica_fornecedor.pushButton_atualiza_cliente.clicked.connect(self.abrirBuscaModificaCliente)
        self.tela_busca_modifica_fornecedor.pushButton_cadastra_fornecedor.clicked.connect(self.abrirCadastraFornecedor)
        self.tela_busca_modifica_fornecedor.pushButton_atualiza_fornecedor.clicked.connect(self.abrirBuscaModificaFornecedor)
        self.tela_busca_modifica_fornecedor.pushButton_cadastra_produto.clicked.connect(self.abrirCadastraProduto)
        self.tela_busca_modifica_fornecedor.pushButton_atualiza_produto.clicked.connect(self.abrirBuscaModificaProduto)
        self.tela_busca_modifica_fornecedor.pushButton_sair.clicked.connect(self.abrirLogin)
        self.tela_busca_modifica_fornecedor.pushButton_cadastro_entrar_login.clicked.connect(self.botaoMostrarMaisFornecedor)
        self.tela_busca_modifica_fornecedor.pushButton_buscar.clicked.connect(self.botaoBuscaFornecedor)
        self.tela_busca_modifica_fornecedor.pushButton_atualiza.clicked.connect(self.botaoAtualizaFornecedor)
        self.tela_busca_modifica_fornecedor.pushButton_remove.clicked.connect(self.botaoRemoveFornecedor)

        #Menu Produto Cadastra
        self.tela_cadastra_produto.pushButton_vendas.clicked.connect(self.abrirMenuInicial)
        self.tela_cadastra_produto.pushButton_cadastra_cliente.clicked.connect(self.abrirCadastraCliente)
        self.tela_cadastra_produto.pushButton_atualiza_cliente.clicked.connect(self.abrirBuscaModificaCliente)
        self.tela_cadastra_produto.pushButton_cadastra_fornecedor.clicked.connect(self.abrirCadastraFornecedor)
        self.tela_cadastra_produto.pushButton_atualiza_fornecedor.clicked.connect(self.abrirBuscaModificaFornecedor)
        self.tela_cadastra_produto.pushButton_cadastra_produto.clicked.connect(self.abrirCadastraProduto)
        self.tela_cadastra_produto.pushButton_atualiza_produto.clicked.connect(self.abrirBuscaModificaProduto)
        self.tela_cadastra_produto.pushButton_sair.clicked.connect(self.abrirLogin)
        self.tela_cadastra_produto.pushButton_mostrar_mais.clicked.connect(self.botaoMostrarMaisProduto)
        self.tela_cadastra_produto.pushButton_cadastrafornecedor.clicked.connect(self.abrirCadastraProduto)

        #Menu Produto Busca Modifica
        self.tela_busca_modifica_produto.pushButton_vendas.clicked.connect(self.abrirMenuInicial)
        self.tela_busca_modifica_produto.pushButton_cadastra_cliente.clicked.connect(self.abrirCadastraCliente)
        self.tela_busca_modifica_produto.pushButton_atualiza_cliente.clicked.connect(self.abrirBuscaModificaCliente)
        self.tela_busca_modifica_produto.pushButton_cadastra_fornecedor.clicked.connect(self.abrirCadastraFornecedor)
        self.tela_busca_modifica_produto.pushButton_atualiza_fornecedor.clicked.connect(self.abrirBuscaModificaFornecedor)
        self.tela_busca_modifica_produto.pushButton_cadastra_produto.clicked.connect(self.abrirCadastraProduto)
        self.tela_busca_modifica_produto.pushButton_atualiza_produto.clicked.connect(self.abrirBuscaModificaProduto)
        self.tela_busca_modifica_produto.pushButton_sair.clicked.connect(self.abrirLogin)
        self.tela_busca_modifica_produto.pushButton_mostrar_mais.clicked.connect(self.botaoMostrarMaisProduto)
        self.tela_busca_modifica_produto.pushButton_busca.clicked.connect(self.abrirBuscaModificaProduto)
        self.tela_busca_modifica_produto.pushButton_atualiza.clicked.connect(self.botaoAtualizaProduto)
        self.tela_busca_modifica_produto.pushButton_cadastro_cadastrar_17.clicked.connect(self.botaoRemoveProduto)

    def botaoCadastro(self):
        pass

    def botaoLogin(self):
        self.abrirMenuInicial()

    def botaoMostrarMaisVendas(self):
        pass

    def botaoRealizaVendas(self):
        pass

    def botaoMostrarMaisCliente(self):
        pass

    def botaoCadastrarCliente(self):
        pass

    def botaoBuscaClieten(self):
        pass

    def botaoAtualizaClieten(self):
        pass

    def botaoRemoveClieten(self):
        pass

    def botaoMostrarMaisFornecedor(self):
        pass

    def botaoCadastraFornecedor(self):
        pass

    def botaoBuscaFornecedor(self):
        pass

    def botaoAtualizaFornecedor(self):
        pass

    def botaoRemoveFornecedor(self):
        pass

    def botaoMostrarMaisProduto(self):
        pass

    def botaoCadastraProduto(self):
        pass

    def botaoBuscaProduto(self):
        pass

    def botaoAtualizaProduto(self):
        pass

    def botaoRemoveProduto(self):
        pass

    def abrirLogin(self):
        self.QtStack.setCurrentIndex(0)
    
    def abrirCadastro(self):
        self.QtStack.setCurrentIndex(1)

    def abrirMenuInicial(self):
        self.QtStack.setCurrentIndex(2)

    def abrirCadastraCliente(self):
        self.QtStack.setCurrentIndex(3)
    
    def abrirBuscaModificaCliente(self):
        self.QtStack.setCurrentIndex(4)

    def abrirCadastraFornecedor(self):
        self.QtStack.setCurrentIndex(5)

    def abrirBuscaModificaFornecedor(self):
        self.QtStack.setCurrentIndex(6)

    def abrirCadastraProduto(self):
        self.QtStack.setCurrentIndex(7)
    
    def abrirBuscaModificaProduto(self):
        self.QtStack.setCurrentIndex(8)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main=Main()
    sys.exit(app.exec_())