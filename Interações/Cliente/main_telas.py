# Transformar .ui em .py:
# pyuic <nome_do_arquivo.ui> -o <nome_do_arquivo.py>

#from Banco import Cliente
import sys
import os

from PyQt5.QtCore import QDate

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from menu_inicial_1_1 import Menu_Inicial
from tela_cadastro1_1 import Tela_Cadastro
from tela_fornecedor_cadastra_1_1 import Tela_Fornecedor_Cadastra
from tela_fornecedor_busca_modifica import Tela_Fornecedor_Busca_Modifica
from tela_cliente_cadastra_1_1 import Tela_Cliente_Cadastra
from tela_cliente_busca_modifica_1_1 import Tela_Cliente_Busca_Modifica
from tela_login import Tela_Login
from tela_produto_cadastra_1_1 import Tela_Produto_Cadastra
from tela_produto_busca_modifica_1_1 import Tela_Produto_Busca_Modifica

from usuario import plataforma_funcionario

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
        self.cadastro = plataforma_funcionario()
        self.row_vendas = 0
        self.row_cliente = 0
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
        self.tela_cadastra_produto.pushButton_cadastrafornecedor.clicked.connect(self.botaoCadastraProduto)

        #Menu Produto Busca Modifica
        self.tela_busca_modifica_produto.pushButton_vendas.clicked.connect(self.abrirMenuInicial)
        self.tela_busca_modifica_produto.pushButton_cadastra_cliente.clicked.connect(self.abrirCadastraCliente)
        self.tela_busca_modifica_produto.pushButton_atualiza_cliente.clicked.connect(self.abrirBuscaModificaCliente)
        self.tela_busca_modifica_produto.pushButton_cadastra_fornecedor.clicked.connect(self.abrirCadastraFornecedor)
        self.tela_busca_modifica_produto.pushButton_atualiza_fornecedor.clicked.connect(self.abrirBuscaModificaFornecedor)
        self.tela_busca_modifica_produto.pushButton_cadastra_produto.clicked.connect(self.abrirCadastraProduto)
        self.tela_busca_modifica_produto.pushButton_atualiza_produto.clicked.connect(self.abrirBuscaModificaProduto)
        self.tela_busca_modifica_produto.pushButton_sair.clicked.connect(self.abrirLogin)
        self.tela_busca_modifica_produto.pushButton_busca.clicked.connect(self.botaoBuscaProduto)
        self.tela_busca_modifica_produto.pushButton_atualiza.clicked.connect(self.botaoAtualizaProduto)
        self.tela_busca_modifica_produto.pushButton_cadastro_cadastrar_17.clicked.connect(self.botaoRemoveProduto)

    def botaoCadastro(self):
        #nome,CPF,data_de_ascimento,email,telefone,Cargo,senha
        nome = self.tela_cadastro.cadastro_lineEdit_nome_completo.text()
        CPF = self.tela_cadastro.cadastro_lineEdit_cpf.text()
        print('Telefone:',type(self.tela_cadastro.cadastro_lineEdit_cpf))
        data_de_ascimento = self.tela_cadastro.cadastro_lineEdit_data_nascimento.text()
        data_split = data_de_ascimento.split('/')
        data_de_ascimento = data_split[0]+'-'+data_split[1]+'-'+data_split[2]
        email = self.tela_cadastro.cadastro_lineEdit_email.text()
        telefone = self.tela_cadastro.cadastro_lineEdit_telefone.text()
        self.tela_cadastro.cadastro_lineEdit_telefone_2
        Cargo = self.tela_cadastro.cadastro_lineEdit_telefone_2.currentText()
        senha = self.tela_cadastro.cadastro_lineEdit_senha.text()
        if(nome !='' or CPF !='' or data_de_ascimento !='' or email !='' or telefone !='' or Cargo !='' or senha !=''):
            if(self.cadastro.cadastro_funcionario(nome,CPF,data_de_ascimento,email,telefone,Cargo,senha)):
                QMessageBox.information(None, 'Cadastro Funcionario', 'Cadastro realizado!')
                #self.tela_cadastro.lineEdit_cadastro_nome.setText('')
                self.tela_cadastro.cadastro_lineEdit_nome_completo.setText('')
                self.tela_cadastro.cadastro_lineEdit_cpf.setText('')
                date = QDate(2000, 1, 1)
                self.tela_cadastro.cadastro_lineEdit_data_nascimento.setDate(date)
                self.tela_cadastro.cadastro_lineEdit_email.setText('')
                self.tela_cadastro.cadastro_lineEdit_telefone.setText('')
                #self.tela_cadastro.cadastro_lineEdit_telefone_2.setText('')
                self.tela_cadastro.cadastro_lineEdit_senha.setText('')

            else:
                QMessageBox.information(None, 'Cadastro Funcioanrio', 'Nao foi possivel realizar o cadastro!')
                self.tela_cadastro.cadastro_lineEdit_nome_completo.setText('')
                self.tela_cadastro.cadastro_lineEdit_cpf.setText('')
                date = QDate(2000, 1, 1)
                self.tela_cadastro.cadastro_lineEdit_data_nascimento.setDate(date)
                self.tela_cadastro.cadastro_lineEdit_email.setText('')
                self.tela_cadastro.cadastro_lineEdit_telefone.setText('')
                #self.tela_cadastro.cadastro_lineEdit_telefone_2.setText('')
                self.tela_cadastro.cadastro_lineEdit_senha.setText('')
        else:
            QMessageBox.information(None, 'Cadastro Funcioanrio', 'Todos os campos devem ser preenchidos!')

    def botaoLogin(self):
        #login_funcionario(self,cpf,senha)
        cpf = self.tela_login.login_lineEdit_cpf.text()
        senha = self.tela_login.login_lineEdit_senha.text()
        if(cpf != '' or senha != ''):
            if(self.cadastro.login_funcionario(cpf,senha)):
                self.abrirMenuInicial()
                self.tela_login.login_lineEdit_cpf.setText('')
                self.tela_login.login_lineEdit_senha.setText('')
            else:
                QMessageBox.information(None, 'Login Funcioanrio', 'CPF ou Senha errados!') 
                self.tela_login.login_lineEdit_cpf.setText('')
                self.tela_login.login_lineEdit_senha.setText('')
            
        else:
            QMessageBox.information(None, 'Login Funcioanrio', 'Todos os campos devem ser preenchidos!')

    def botaoMostrarMaisVendas(self):
        self.cadastro.buscar_vendas_todas()
        #historico = 'forma_de_pagamento/data/valor/ID_Cliente/ID_Funcionario/ID_Produto\n'
        #print(self.cadastro.vendas_todas)
        last_row = self.row_vendas
        self.row_vendas = len(self.cadastro.vendas_todas)
        print('self.row_vendas:',self.row_vendas)
        self.tela_menu_inicial.tableWidget_tabela_vendas.setRowCount(self.row_vendas)
        for index in range(last_row,self.row_vendas):
            #print(i)
            print('self.cadastro.vendas_todas[index]:',self.cadastro.vendas_todas[index])
            self.tela_menu_inicial.tableWidget_tabela_vendas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(self.cadastro.vendas_todas[index][0])))
            self.tela_menu_inicial.tableWidget_tabela_vendas.setItem(index, 1, QtWidgets.QTableWidgetItem(str(self.cadastro.vendas_todas[index][1])))
            self.tela_menu_inicial.tableWidget_tabela_vendas.setItem(index, 2, QtWidgets.QTableWidgetItem(str(self.cadastro.vendas_todas[index][2])))
            self.tela_menu_inicial.tableWidget_tabela_vendas.setItem(index, 3, QtWidgets.QTableWidgetItem(str(self.cadastro.vendas_todas[index][3])))
            self.tela_menu_inicial.tableWidget_tabela_vendas.setItem(index, 4, QtWidgets.QTableWidgetItem(str(self.cadastro.vendas_todas[index][4])))
            self.tela_menu_inicial.tableWidget_tabela_vendas.setItem(index, 5, QtWidgets.QTableWidgetItem(str(self.cadastro.vendas_todas[index][5])))
            
            #historico = historico+i[0]+'/'+i[1]+'/'+i[2]+'/'+i[3]+'/'+i[4]+'/'+i[5]+'\n'
        #textEdit_tabela_vendas
        #self.tela_menu_inicial.textEdit_tabela_vendas.setText(historico)

        

    def botaoRealizaVendas(self):
        #cadastrar_venda(self,forma_de_pagamento,data_da_venda,n_bebida,cpf_cliente,cpf_funcionario,senha_funcionario)
        qnt_vendas = self.tela_menu_inicial.lineEdit_quabtidade.text()

        print(self.cadastro.funcionario)
        forma_de_pagamento = self.tela_menu_inicial.lineEdit_index_forma_pagamento.currentText()
        data_da_venda= '18-11-2021'
        n_bebida= self.tela_menu_inicial.lineEdit_index_bebida.text()
        cpf_cliente= self.tela_menu_inicial.lineEdit_index_cliente.text()
        cpf_funcionario= self.cadastro.funcionario[1]
        senha_funcionario= self.cadastro.funcionario[3]

        if(int(qnt_vendas) > 0):
            for i in range(0,int(qnt_vendas)):
                if(forma_de_pagamento !='' or n_bebida !='' or cpf_cliente !=''):
                    if(self.cadastro.cadastrar_venda(forma_de_pagamento,data_da_venda,n_bebida,cpf_cliente,cpf_funcionario,senha_funcionario)):
                        QMessageBox.information(None, 'Realizar venda', 'Venda Realizada!')
                        #self.tela_cadastro.lineEdit_cadastro_nome.setText('')

                        #self.tela_menu_inicial.lineEdit_quabtidade.setText(0)
                        #self.tela_menu_inicial.lineEdit_index_forma_pagamento.setText('')
                        self.tela_menu_inicial.lineEdit_index_bebida.setText('')
                        self.tela_menu_inicial.lineEdit_index_cliente.setText('')
                        self.cadastro.prdotos_todas = []
                        self.botaoMostrarMaisVendas()
                        self.row_vendas = 0

                    else:
                        QMessageBox.information(None, 'Realizar venda', 'Nao foi possivel realizar a venda!')
                        #self.tela_menu_inicial.lineEdit_quabtidade.setText('')
                        #self.tela_menu_inicial.lineEdit_index_forma_pagamento.setText('')
                        self.tela_menu_inicial.lineEdit_index_bebida.setText('')
                        self.tela_menu_inicial.lineEdit_index_cliente.setText('')
                else:
                    QMessageBox.information(None, 'Realizar venda', 'Todos os campos devem ser preenchidos!')
        else:
            QMessageBox.information(None, 'Realizar venda', 'Quantidade de pedidos nao validas!')

    def botaoMostrarMaisCliente(self):
        self.cadastro.buscar_todos_clientes()
        #print(self.cadastro.cliente_todos)
        last_row = self.row_cliente
        self.row_cliente = len(self.cadastro.cliente_todos)
        print('self.row_cliente:',self.row_cliente)
        self.tela_cadastra_cliente.tableWidget_tabela_vendas.setRowCount(self.row_cliente)
        for index in range(last_row,self.row_cliente):
            #print(i)
            print('self.cadastro.vendas_todas[index]:',self.cadastro.cliente_todos[index])
            self.tela_cadastra_cliente.tableWidget_tabela_vendas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(self.cadastro.cliente_todos[index][0])))
            self.tela_cadastra_cliente.tableWidget_tabela_vendas.setItem(index, 1, QtWidgets.QTableWidgetItem(str(self.cadastro.cliente_todos[index][1])))
            self.tela_cadastra_cliente.tableWidget_tabela_vendas.setItem(index, 2, QtWidgets.QTableWidgetItem(str(self.cadastro.cliente_todos[index][2])))
            self.tela_cadastra_cliente.tableWidget_tabela_vendas.setItem(index, 3, QtWidgets.QTableWidgetItem(str(self.cadastro.cliente_todos[index][3])))
            self.tela_cadastra_cliente.tableWidget_tabela_vendas.setItem(index, 4, QtWidgets.QTableWidgetItem(str(self.cadastro.cliente_todos[index][4])))
            self.tela_cadastra_cliente.tableWidget_tabela_vendas.setItem(index, 5, QtWidgets.QTableWidgetItem(str(self.cadastro.cliente_todos[index][5])))

    def botaoCadastrarCliente(self):
        #nome,cpf,edereco,data_de_nascimento,email,telefone

        nome = self.tela_cadastra_cliente.lineEdit_nome_completo.text()
        cpf = self.tela_cadastra_cliente.lineEdit_cpf.text()
        edereco = self.tela_cadastra_cliente.lineEdit_endereco.text()
        data_de_nascimento = self.tela_cadastra_cliente.lineEdit_data_nascimento.text()
        data_split = data_de_nascimento.split('/')
        data_de_nascimento = data_split[0]+'-'+data_split[1]+'-'+data_split[2]
        email = self.tela_cadastra_cliente.lineEdit_email.text()
        telefone = self.tela_cadastra_cliente.lineEdit_n_telefone.text()

        if(nome !='' or cpf !='' or edereco !='' or data_de_nascimento !='' or email !='' or telefone !=''):
            if(self.cadastro.cadastrar_cliente(nome,cpf,edereco,data_de_nascimento,email,telefone)):
                QMessageBox.information(None, 'Cadastro Cliente', 'Cadastro realizado!')
                #self.tela_cadastro.lineEdit_cadastro_nome.setText('')

                self.tela_cadastra_cliente.lineEdit_nome_completo.setText('')
                self.tela_cadastra_cliente.lineEdit_cpf.setText('')
                self.tela_cadastra_cliente.lineEdit_endereco.setText('')
                self.tela_cadastra_cliente.lineEdit_data_nascimento.setDate(QDate(2000, 1, 1))
                self.tela_cadastra_cliente.lineEdit_email.setText('')
                self.tela_cadastra_cliente.lineEdit_n_telefone.setText('')
                self.botaoMostrarMaisCliente()

            else:
                QMessageBox.information(None, 'Cadastro Cliente', 'Nao foi possivel realizar o cadastro!')
                self.tela_cadastra_cliente.lineEdit_nome_completo.setText('')
                self.tela_cadastra_cliente.lineEdit_cpf.setText('')
                self.tela_cadastra_cliente.lineEdit_endereco.setText('')
                self.tela_cadastra_cliente.lineEdit_data_nascimento.setDate(QDate(2000, 1, 1))
                self.tela_cadastra_cliente.lineEdit_email.setText('')
                self.tela_cadastra_cliente.lineEdit_n_telefone.setText('')
        else:
            QMessageBox.information(None, 'Cadastro Cliente', 'Todos os campos devem ser preenchidos!')
        

    def botaoBuscaClieten(self):
        cpf = self.tela_busca_modifica_cliente.lineEdit_busca_cpf.text()
        if(self.cadastro.buscar_clente(cpf)):
            print(self.cadastro.cliete)
            self.tela_busca_modifica_cliente.lineEdit_cpf.setText(self.cadastro.cliete[2])
            self.tela_busca_modifica_cliente.lineEdit_nome.setText(self.cadastro.cliete[1])
            self.tela_busca_modifica_cliente.lineEdit_endereco.setText(self.cadastro.cliete[3])
            data_split = self.cadastro.cliete[4].split('-')
            print('data_split:',data_split)
            self.tela_busca_modifica_cliente.lineEdit_nascimento.setDate(QDate(int(data_split[2]), int(data_split[1]), int(data_split[0])))
            self.tela_busca_modifica_cliente.lineEdit_email.setText(self.cadastro.cliete[5])
            self.tela_busca_modifica_cliente.lineEdit_telefone.setText(self.cadastro.cliete[6])
            QMessageBox.information(None, 'Buscar Cliente', 'Clietne encontrado com sucesso!')
        else:
            QMessageBox.information(None, 'Buscar Cliente', 'Cliente nao encontrado!')
            self.tela_busca_modifica_cliente.lineEdit_busca_cpf.setText('')

    def rezetar_tabela_cliente(self):
        self.cadastro.cliente_todos = []
        self.row_cliente = 0
        self.botaoMostrarMaisCliente()

    def botaoAtualizaClieten(self):
        #atualiza_cliente(self,nome,cpf,edereco,data_de_nascimento,email,telefone)
        nome = self.tela_busca_modifica_cliente.lineEdit_nome.text()
        cpf = self.tela_busca_modifica_cliente.lineEdit_cpf.text()
        edereco = self.tela_busca_modifica_cliente.lineEdit_endereco.text()
        data_de_nascimento = self.tela_busca_modifica_cliente.lineEdit_nascimento.text()
        data_split = data_de_nascimento.split('/')
        data_de_nascimento = data_split[0]+'-'+data_split[1]+'-'+data_split[2]
        email = self.tela_busca_modifica_cliente.lineEdit_email.text()
        telefone = self.tela_busca_modifica_cliente.lineEdit_telefone.text()
        if(nome != '' or cpf != '' or edereco != ''or data_de_nascimento != ''or email != ''or telefone != ''):
            if(self.cadastro.atualiza_cliente(nome,cpf,edereco,data_de_nascimento,email,telefone)):
                #print(self.cadastro.cliete)
                QMessageBox.information(None, 'Atualizar Cliente', 'Dados do Clietne Atualizados com sucesso!')
                self.rezetar_tabela_cliente()

            else:
                QMessageBox.information(None, 'Atualizar Cliente', 'Dados do Clietne nao foram Atualizados!')
                self.tela_busca_modifica_cliente.lineEdit_cpf.setText('')
                self.tela_busca_modifica_cliente.lineEdit_nome.setText('')
                self.tela_busca_modifica_cliente.lineEdit_endereco.setText('')
                self.tela_busca_modifica_cliente.lineEdit_nascimento.setDate(QDate(2000, 1, 1))
                self.tela_busca_modifica_cliente.lineEdit_email.setText('')
                self.tela_busca_modifica_cliente.lineEdit_telefone.setText('')
                self.tela_busca_modifica_cliente.lineEdit_busca_cpf.setText('')
        else:
            QMessageBox.information(None, 'Atualizar Cliente', 'Nescessario que todos os campos sejam preenchidos!')

    def botaoRemoveClieten(self):
        #remover_cliente(self,cpf)
        cpf = self.tela_busca_modifica_cliente.lineEdit_cpf.text()

        if(cpf != ''):
            if(self.cadastro.remover_cliente(cpf)):
                #print(self.cadastro.cliete)
                QMessageBox.information(None, 'Remover Cliente', 'Clietne Removido!')
                self.tela_busca_modifica_cliente.lineEdit_cpf.setText('')
                self.tela_busca_modifica_cliente.lineEdit_nome.setText('')
                self.tela_busca_modifica_cliente.lineEdit_endereco.setText('')
                self.tela_busca_modifica_cliente.lineEdit_nascimento.setDate(QDate(2000, 1, 1))
                self.tela_busca_modifica_cliente.lineEdit_email.setText('')
                self.tela_busca_modifica_cliente.lineEdit_telefone.setText('')
                self.tela_busca_modifica_cliente.lineEdit_busca_cpf.setText('')
                self.rezetar_tabela_cliente()
            else:
                QMessageBox.information(None, 'Remover Cliente', 'Nao foi possivel realziar a remocao!')
                self.tela_busca_modifica_cliente.lineEdit_cpf.setText('')
                self.tela_busca_modifica_cliente.lineEdit_nome.setText('')
                self.tela_busca_modifica_cliente.lineEdit_endereco.setText('')
                self.tela_busca_modifica_cliente.lineEdit_nascimento.setDate(QDate(2000, 1, 1))
                self.tela_busca_modifica_cliente.lineEdit_email.setText('')
                self.tela_busca_modifica_cliente.lineEdit_telefone.setText('')
                self.tela_busca_modifica_cliente.lineEdit_busca_cpf.setText('')
        else:
            QMessageBox.information(None, 'Remover Cliente', 'Nescessario pelomenos o campo do CPF prenchido!')

    def botaoMostrarMaisFornecedor(self):
        #razao_social,CNPJ,nacionalidade,endereco,telefone,passoa_contato
        self.cadastro.buscar_todos_fornecedores()
        #print(self.cadastro.cliente_todos)
        historico = 'razao_social/CNPJ/nacionalidade/endereco,telefone/passoa_contato\n'
        for i in self.cadastro.fornecedor_todos:
            historico = historico+i[0]+'/'+i[1]+'/'+i[2]+'/'+i[3]+'/'+i[4]+'/'+i[5]+'\n'
        #textEdit_tabela_vendas
        self.tela_cadastra_fornecedor.textEdit_tabela_fornecedores.setText(historico)

    def botaoCadastraFornecedor(self):
        #razao_social,CNPJ,nacionalidade,endereco,telefone,passoa_contato

        razao_social = self.tela_cadastra_fornecedor.lineEdit_razao_social.text()
        CNPJ = self.tela_cadastra_fornecedor.lineEdit_cnpj.text()
        nacionalidade= self.tela_cadastra_fornecedor.lineEdit_nacionalidade.text()
        endereco= self.tela_cadastra_fornecedor.lineEdit_endereco.text()
        telefone= self.tela_cadastra_fornecedor.lineEdit_telefone.text()
        passoa_contato= self.tela_cadastra_fornecedor.lineEdit_pessoa.text()


        if(razao_social !='' or CNPJ !='' or nacionalidade !='' or endereco !='' or telefone !='' or passoa_contato !=''):
            if(self.cadastro.cadastra_fornecedor(razao_social,CNPJ,nacionalidade,endereco,telefone,passoa_contato)):
                QMessageBox.information(None, 'Cadastro Fornecedor', 'Cadastro realizado!')
                #self.tela_cadastro.lineEdit_cadastro_nome.setText('')

                self.tela_cadastra_fornecedor.lineEdit_razao_social.setText('')
                self.tela_cadastra_fornecedor.lineEdit_cnpj.setText('')
                self.tela_cadastra_fornecedor.lineEdit_nacionalidade.setText('')
                self.tela_cadastra_fornecedor.lineEdit_endereco.setText('')
                self.tela_cadastra_fornecedor.lineEdit_telefone.setText('')
                self.tela_cadastra_fornecedor.lineEdit_pessoa.setText('')
                self.botaoMostrarMaisFornecedor()

            else:
                QMessageBox.information(None, 'Cadastro Fornecedor', 'Nao foi possivel realizar o cadastro!')
                self.tela_cadastra_fornecedor.lineEdit_razao_social.setText('')
                self.tela_cadastra_fornecedor.lineEdit_cnpj.setText('')
                self.tela_cadastra_fornecedor.lineEdit_nacionalidade.setText('')
                self.tela_cadastra_fornecedor.lineEdit_endereco.setText('')
                self.tela_cadastra_fornecedor.lineEdit_telefone.setText('')
                self.tela_cadastra_fornecedor.lineEdit_pessoa.setText('')
        else:
            QMessageBox.information(None, 'Cadastro Fornecedor', 'Todos os campos devem ser preenchidos!')

    def botaoBuscaFornecedor(self):
        cpf = self.tela_busca_modifica_fornecedor.lineEdit_cnpj_buscar.text()
        if(self.cadastro.buscar_fornecedor(cpf)):
            #print(self.cadastro.cliete)

            self.tela_busca_modifica_fornecedor.lineEdit_cnpj.setText(self.cadastro.fornecedor[2])
            self.tela_busca_modifica_fornecedor.lineEdit_rasao_social.setText(self.cadastro.fornecedor[1])
            self.tela_busca_modifica_fornecedor.lineEdit_nacionalida.setText(self.cadastro.fornecedor[3])
            self.tela_busca_modifica_fornecedor.lineEdit_endereco.setText(self.cadastro.fornecedor[4])
            self.tela_busca_modifica_fornecedor.lineEdit_telefone.setText(self.cadastro.fornecedor[5])
            self.tela_busca_modifica_fornecedor.lineEdit_pessoa.setText(self.cadastro.fornecedor[6])
            QMessageBox.information(None, 'Buscar Fornecedor', 'Fornecedor encontrado com sucesso!')
        else:
            self.tela_busca_modifica_fornecedor.lineEdit_cnpj.setText('')
            self.tela_busca_modifica_fornecedor.lineEdit_rasao_social.setText('')
            self.tela_busca_modifica_fornecedor.lineEdit_nacionalida.setText('')
            self.tela_busca_modifica_fornecedor.lineEdit_endereco.setText('')
            self.tela_busca_modifica_fornecedor.lineEdit_telefone.setText('')
            self.tela_busca_modifica_fornecedor.lineEdit_pessoa.setText('')
            QMessageBox.information(None, 'Buscar Fornecedor', 'Fornecedor nao encontrado!')
            self.tela_busca_modifica_fornecedor.lineEdit_cnpj_buscar.setText('')

    def botaoAtualizaFornecedor(self):
        #atualziar_fornecedor(self,razao_social,CNPJ,nacionalidade,endereco,telefone,passoa_contato)
        razao_social = self.tela_busca_modifica_fornecedor.lineEdit_rasao_social.text()
        CNPJ = self.tela_busca_modifica_fornecedor.lineEdit_cnpj.text()
        nacionalidade= self.tela_busca_modifica_fornecedor.lineEdit_nacionalida.text()
        endereco= self.tela_busca_modifica_fornecedor.lineEdit_endereco.text()
        telefone= self.tela_busca_modifica_fornecedor.lineEdit_telefone.text()
        passoa_contato= self.tela_busca_modifica_fornecedor.lineEdit_pessoa.text()
        if(razao_social != '' or CNPJ != '' or nacionalidade != ''or endereco != ''or passoa_contato != ''or telefone != ''):
            if(self.cadastro.atualziar_fornecedor(razao_social,CNPJ,nacionalidade,endereco,telefone,passoa_contato)):
                #print(self.cadastro.cliete)
                QMessageBox.information(None, 'Atualizar Fornecedor', 'Dados do Fornecedor Atualizados com sucesso!')
                self.cadastro.fornecedor_todos = []
            else:
                QMessageBox.information(None, 'Atualizar Fornecedor', 'Dados do Fornecedor nao foram Atualizados!')
                self.tela_busca_modifica_fornecedor.lineEdit_rasao_social.setText('')
                self.tela_busca_modifica_fornecedor.lineEdit_cnpj.setText('')
                self.tela_busca_modifica_fornecedor.lineEdit_nacionalidade.setText('')
                self.tela_busca_modifica_fornecedor.lineEdit_endereco.setText('')
                self.tela_busca_modifica_fornecedor.lineEdit_telefone.setText('')
                self.tela_busca_modifica_fornecedor.lineEdit_pessoa.setText('')
        else:
            QMessageBox.information(None, 'Atualizar Cliente', 'Nescessario que todos os campos sejam preenchidos!')

    def botaoRemoveFornecedor(self):
        #remover_fornecedor(self,CNPJ)
        CNPJ = self.tela_busca_modifica_fornecedor.lineEdit_cnpj.text()

        if(CNPJ != ''):
            if(self.cadastro.remover_fornecedor(CNPJ)):
                #print(self.cadastro.cliete)
                QMessageBox.information(None, 'Remover Fornecedor', 'Fornecedor Removido!')
                self.tela_busca_modifica_fornecedor.lineEdit_cnpj_buscar.setText('')
                self.tela_busca_modifica_fornecedor.lineEdit_cnpj.setText('')
                self.tela_busca_modifica_fornecedor.lineEdit_rasao_social.setText('')
                self.tela_busca_modifica_fornecedor.lineEdit_nacionalida.setText('')
                self.tela_busca_modifica_fornecedor.lineEdit_endereco.setText('')
                self.tela_busca_modifica_fornecedor.lineEdit_telefone.setText('')
                self.tela_busca_modifica_fornecedor.lineEdit_pessoa.setText('')

                self.cadastro.fornecedor_todos = []
            else:
                QMessageBox.information(None, 'Remover Fornecedor', 'Nao foi possivel realziar a remocao!')
                self.tela_busca_modifica_fornecedor.lineEdit_cnpj_buscar.setText('')
                self.tela_busca_modifica_fornecedor.lineEdit_cnpj.setText('')
                self.tela_busca_modifica_fornecedor.lineEdit_rasao_social.setText('')
                self.tela_busca_modifica_fornecedor.lineEdit_nacionalida.setText('')
                self.tela_busca_modifica_fornecedor.lineEdit_endereco.setText('')
                self.tela_busca_modifica_fornecedor.lineEdit_telefone.setText('')
                self.tela_busca_modifica_fornecedor.lineEdit_pessoa.setText('')
        else:
            QMessageBox.information(None, 'Remover Fornecedor', 'Nescessario pelomenos o campo do CNPJ prenchido!')


    def botaoMostrarMaisProduto(self):
        #razao_social,CNPJ,nacionalidade,endereco,telefone,passoa_contato
        self.cadastro.buscar_produto_todos()
        print(self.cadastro.prdotos_todas)
        historico = 'n_bebida/nome/fabricacao/validade/armazenamento/quantidades/local/valor\n'
        for i in self.cadastro.prdotos_todas:
            historico = historico+i[0]+'/'+i[1]+'/'+i[2]+'/'+i[3]+'/'+i[4]+'/'+i[5]+'/'+i[7]+'\n'
        #textEdit_tabela_vendas
        self.tela_cadastra_produto.textEdit_tabela_produto.setText(historico)

    def botaoCadastraProduto(self):
        #cadastra_produto(self,n_bebida,nome_da_bebida,data_de_fabricacao,data_de_validade,condicoes_de_armazenamento,quantidades,local_armazenado,valor_de_compra_UN,valor_revenda_UN,cnpj_fornecedor)

        n_bebida = self.tela_cadastra_produto.lineEdit_n_bebida.text()
        nome_da_bebida= self.tela_cadastra_produto.lineEdit_nome_bebida.text()
        data_de_fabricacao= self.tela_cadastra_produto.lineEdit_data_fabricacao.text()
        data_de_validade= self.tela_cadastra_produto.lineEdit_data_vencimento.text()
        condicoes_de_armazenamento= self.tela_cadastra_produto.lineEdit_condicoes.text()
        quantidades= self.tela_cadastra_produto.lineEdit_quantidade.text()
        local_armazenado= self.tela_cadastra_produto.lineEdit_local.text()
        valor_de_compra_UN= self.tela_cadastra_produto.lineEdit_v_compra_uni.text()
        valor_revenda_UN= self.tela_cadastra_produto.lineEdit_re_venda_uni.text()
        cnpj_fornecedor = self.tela_cadastra_produto.lineEdit_id_forncedor.text()

        if(n_bebida !='' or nome_da_bebida !='' or data_de_fabricacao !='' or data_de_validade !='' or condicoes_de_armazenamento !='' or quantidades !='' or local_armazenado !='' or valor_de_compra_UN !='' or valor_revenda_UN !='' or cnpj_fornecedor !=''):
            if(self.cadastro.cadastra_produto(n_bebida,nome_da_bebida,data_de_fabricacao,data_de_validade,condicoes_de_armazenamento,quantidades,local_armazenado,valor_de_compra_UN,valor_revenda_UN,cnpj_fornecedor)):
                QMessageBox.information(None, 'Cadastro Produto', 'Cadastro realizado!')
                #self.tela_cadastro.lineEdit_cadastro_nome.setText('')

                self.tela_cadastra_produto.lineEdit_n_bebida.setText('')
                self.tela_cadastra_produto.lineEdit_nome_bebida.setText('')
                self.tela_cadastra_produto.lineEdit_data_fabricacao.setText('')
                self.tela_cadastra_produto.lineEdit_data_vencimento.setText('')
                self.tela_cadastra_produto.lineEdit_condicoes.setText('')
                self.tela_cadastra_produto.lineEdit_quantidade.setText('')
                self.tela_cadastra_produto.lineEdit_local.setText('')
                self.tela_cadastra_produto.lineEdit_v_compra_uni.setText('')
                self.tela_cadastra_produto.lineEdit_re_venda_uni.setText('')
                self.tela_cadastra_produto.lineEdit_id_forncedor.setText('')
                self.botaoMostrarMaisProduto()

            else:
                QMessageBox.information(None, 'Cadastro Produto', 'Nao foi possivel realizar o cadastro!')
                self.tela_cadastra_produto.lineEdit_n_bebida.setText('')
                self.tela_cadastra_produto.lineEdit_nome_bebida.setText('')
                self.tela_cadastra_produto.lineEdit_data_fabricacao.setText('')
                self.tela_cadastra_produto.lineEdit_data_vencimento.setText('')
                self.tela_cadastra_produto.lineEdit_condicoes.setText('')
                self.tela_cadastra_produto.lineEdit_quantidade.setText('')
                self.tela_cadastra_produto.lineEdit_local.setText('')
                self.tela_cadastra_produto.lineEdit_v_compra_uni.setText('')
                self.tela_cadastra_produto.lineEdit_re_venda_uni.setText('')
                self.tela_cadastra_produto.lineEdit_id_forncedor.setText('')
        else:
            QMessageBox.information(None, 'Cadastro Produto', 'Todos os campos devem ser preenchidos!')

    def botaoBuscaProduto(self):
        cpf = self.tela_busca_modifica_produto.lineEdit_2.text()
        if(self.cadastro.buscar_produto(cpf)):
            #print(self.cadastro.cliete)
            self.tela_busca_modifica_produto.lineEdit_6.setText(self.cadastro.prdotos[1])
            self.tela_busca_modifica_produto.lineEdit_3.setText(self.cadastro.prdotos[2])
            self.tela_busca_modifica_produto.lineEdit_7.setText(self.cadastro.prdotos[3])
            self.tela_busca_modifica_produto.lineEdit_14.setText(self.cadastro.prdotos[4])
            self.tela_busca_modifica_produto.lineEdit_15.setText(self.cadastro.prdotos[5])
            self.tela_busca_modifica_produto.lineEdit_8.setText(self.cadastro.prdotos[6])
            self.tela_busca_modifica_produto.lineEdit_9.setText(self.cadastro.prdotos[7])
            self.tela_busca_modifica_produto.lineEdit_10.setText(self.cadastro.prdotos[8])
            self.tela_busca_modifica_produto.lineEdit_12.setText(self.cadastro.prdotos[9])
            self.tela_busca_modifica_produto.lineEdit_11.setText(self.cadastro.prdotos[10])
            QMessageBox.information(None, 'Buscar Fornecedor', 'Fornecedor encontrado com sucesso!')
        else:
            QMessageBox.information(None, 'Buscar Fornecedor', 'Fornecedor nao encontrado!')
            self.tela_busca_modifica_fornecedor.lineEdit_cnpj_buscar.setText('')

    def botaoAtualizaProduto(self):
        #atualizar_produto(self,n_bebida,nome_da_bebida,data_de_fabricacao,data_de_validade,condicoes_de_armazenamento,quantidades,local_armazenado,valor_de_compra_UN,valor_revenda_UN,cnpj_fornecedor)

        n_bebida = self.tela_busca_modifica_produto.lineEdit_6.text()
        nome_da_bebida = self.tela_busca_modifica_produto.lineEdit_3.text()
        data_de_fabricacao = self.tela_busca_modifica_produto.lineEdit_7.text()
        data_de_validade = self.tela_busca_modifica_produto.lineEdit_14.text()
        condicoes_de_armazenamento = self.tela_busca_modifica_produto.lineEdit_15.text()
        quantidades = self.tela_busca_modifica_produto.lineEdit_8.text()
        local_armazenado = self.tela_busca_modifica_produto.lineEdit_9.text()
        valor_de_compra_UN = self.tela_busca_modifica_produto.lineEdit_10.text()
        valor_revenda_UN = self.tela_busca_modifica_produto.lineEdit_12.text()
        cnpj_fornecedor = self.tela_busca_modifica_produto.lineEdit_11.text()            

        if(n_bebida != '' or nome_da_bebida != '' or data_de_fabricacao != ''or data_de_validade != ''or condicoes_de_armazenamento != ''or quantidades != ''or local_armazenado != ''or valor_de_compra_UN != ''or valor_revenda_UN != ''or cnpj_fornecedor != ''):
            if(self.cadastro.atualizar_produto(n_bebida,nome_da_bebida,data_de_fabricacao,data_de_validade,condicoes_de_armazenamento,quantidades,local_armazenado,valor_de_compra_UN,valor_revenda_UN,cnpj_fornecedor)):
                #print(self.cadastro.cliete)
                QMessageBox.information(None, 'Atualizar Produto', 'Dados do Produto Atualizados com sucesso!')
                self.cadastro.prdotos_todas = []
            else:
                QMessageBox.information(None, 'Atualizar Produto', 'Dados do Produto nao foram Atualizados!')

                self.tela_busca_modifica_produto.lineEdit_6.setText('')
                self.tela_busca_modifica_produto.lineEdit_3.setText('')
                self.tela_busca_modifica_produto.lineEdit_7.setText('')
                self.tela_busca_modifica_produto.lineEdit_14.setText('')
                self.tela_busca_modifica_produto.lineEdit_15.setText('')
                self.tela_busca_modifica_produto.lineEdit_8.setText('')
                self.tela_busca_modifica_produto.lineEdit_9.setText('')
                self.tela_busca_modifica_produto.lineEdit_10.setText('')
                self.tela_busca_modifica_produto.lineEdit_12.setText('')
                self.tela_busca_modifica_produto.lineEdit_11.setText('')  

        else:
            QMessageBox.information(None, 'Atualizar Produto', 'Nescessario que todos os campos sejam preenchidos!')

    def botaoRemoveProduto(self):
        #remover_produto(self,n_bebida)
        cpf = self.tela_busca_modifica_produto.lineEdit_2.text()

        if(cpf != ''):
            if(self.cadastro.remover_produto(cpf)):
                #print(self.cadastro.cliete)
                QMessageBox.information(None, 'Remover Produto', 'Produto Removido!')
                self.tela_busca_modifica_produto.lineEdit_6.setText('')
                self.tela_busca_modifica_produto.lineEdit_3.setText('')
                self.tela_busca_modifica_produto.lineEdit_7.setText('')
                self.tela_busca_modifica_produto.lineEdit_14.setText('')
                self.tela_busca_modifica_produto.lineEdit_15.setText('')
                self.tela_busca_modifica_produto.lineEdit_8.setText('')
                self.tela_busca_modifica_produto.lineEdit_9.setText('')
                self.tela_busca_modifica_produto.lineEdit_10.setText('')
                self.tela_busca_modifica_produto.lineEdit_12.setText('')
                self.tela_busca_modifica_produto.lineEdit_11.setText('')  

                self.cadastro.prdotos_todas = []
            else:
                QMessageBox.information(None, 'Remover Produto', 'Nao foi possivel realziar a remocao!')
                self.tela_busca_modifica_produto.lineEdit_6.setText('')
                self.tela_busca_modifica_produto.lineEdit_3.setText('')
                self.tela_busca_modifica_produto.lineEdit_7.setText('')
                self.tela_busca_modifica_produto.lineEdit_14.setText('')
                self.tela_busca_modifica_produto.lineEdit_15.setText('')
                self.tela_busca_modifica_produto.lineEdit_8.setText('')
                self.tela_busca_modifica_produto.lineEdit_9.setText('')
                self.tela_busca_modifica_produto.lineEdit_10.setText('')
                self.tela_busca_modifica_produto.lineEdit_12.setText('')
                self.tela_busca_modifica_produto.lineEdit_11.setText('')  
        else:
            QMessageBox.information(None, 'Remover Produto', 'Nescessario pelomenos o campo do numero do produto prenchido!')


    def abrirLogin(self):
        self.QtStack.setCurrentIndex(0)
    
    def abrirCadastro(self):
        self.QtStack.setCurrentIndex(1)

    def abrirMenuInicial(self):
        self.botaoMostrarMaisVendas()
        self.tela_menu_inicial.lineEdit_menu_nome_sobrenome_cliente.setText(self.cadastro.funcionario[1])
        self.QtStack.setCurrentIndex(2)

    def abrirCadastraCliente(self):
        self.botaoMostrarMaisCliente()
        self.tela_cadastra_cliente.lineEdit_menu_nome_sobrenome_cliente.setText(self.cadastro.funcionario[1])
        self.QtStack.setCurrentIndex(3)
    
    def abrirBuscaModificaCliente(self):
        self.tela_busca_modifica_cliente.lineEdit_menu_nome_sobrenome_cliente.setText(self.cadastro.funcionario[1])
        self.QtStack.setCurrentIndex(4)

    def abrirCadastraFornecedor(self):
        self.botaoMostrarMaisFornecedor()
        self.tela_cadastra_fornecedor.lineEdit_menu_nome_sobrenome_cliente.setText(self.cadastro.funcionario[1])
        self.QtStack.setCurrentIndex(5)

    def abrirBuscaModificaFornecedor(self):
        self.tela_busca_modifica_fornecedor.lineEdit_menu_nome_sobrenome_cliente.setText(self.cadastro.funcionario[1])
        self.QtStack.setCurrentIndex(6)

    def abrirCadastraProduto(self):
        self.botaoMostrarMaisProduto()
        self.tela_cadastra_produto.lineEdit_menu_nome_sobrenome_cliente.setText(self.cadastro.funcionario[1])
        self.QtStack.setCurrentIndex(7)
    
    def abrirBuscaModificaProduto(self):
        self.tela_busca_modifica_produto.lineEdit_menu_nome_sobrenome_cliente.setText(self.cadastro.funcionario[1])
        self.QtStack.setCurrentIndex(8)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main=Main()
    sys.exit(app.exec_())