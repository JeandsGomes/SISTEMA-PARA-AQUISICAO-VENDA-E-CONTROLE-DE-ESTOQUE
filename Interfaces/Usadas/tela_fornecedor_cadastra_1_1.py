# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\menu_cadastra_fornecedor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(640, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setMinimumSize(QtCore.QSize(50, 0))
        self.frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame.setStyleSheet("background-color: rgb(255, 144, 14);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_string_ola = QtWidgets.QLabel(self.frame_3)
        self.label_string_ola.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_string_ola.setFont(font)
        self.label_string_ola.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_string_ola.setStyleSheet("color: rgb(240, 233, 249);")
        self.label_string_ola.setObjectName("label_string_ola")
        self.horizontalLayout_2.addWidget(self.label_string_ola)
        self.lineEdit_menu_nome_sobrenome_cliente = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_menu_nome_sobrenome_cliente.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_menu_nome_sobrenome_cliente.setFont(font)
        self.lineEdit_menu_nome_sobrenome_cliente.setStyleSheet("\n"
"QLineEdit{\n"
"    background:transparent;\n"
"    border:none;\n"
"    color: rgb(240, 233, 249);\n"
"\n"
"}")
        self.lineEdit_menu_nome_sobrenome_cliente.setObjectName("lineEdit_menu_nome_sobrenome_cliente")
        self.horizontalLayout_2.addWidget(self.lineEdit_menu_nome_sobrenome_cliente)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_11 = QtWidgets.QFrame(self.frame)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_vendas = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_vendas.setMinimumSize(QtCore.QSize(100, 10))
        self.pushButton_vendas.setMaximumSize(QtCore.QSize(230, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_vendas.setFont(font)
        self.pushButton_vendas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_vendas.setStyleSheet("QPushButton{\n"
"    border-radius: 10px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"        \n"
"    color: rgb(240, 233, 249);\n"
"    background-color: rgb(255, 174, 35);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(207, 110, 0);\n"
"    color: rgb(240, 233, 249);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.pushButton_vendas.setObjectName("pushButton_vendas")
        self.verticalLayout_7.addWidget(self.pushButton_vendas)
        self.verticalLayout.addWidget(self.frame_11)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(240, 233, 249);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.pushButton_cadastra_cliente = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_cadastra_cliente.setMinimumSize(QtCore.QSize(100, 10))
        self.pushButton_cadastra_cliente.setMaximumSize(QtCore.QSize(230, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cadastra_cliente.setFont(font)
        self.pushButton_cadastra_cliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_cadastra_cliente.setStyleSheet("QPushButton{\n"
"    border-radius: 10px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"        \n"
"    color: rgb(240, 233, 249);\n"
"    background-color: rgb(255, 174, 35);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(207, 110, 0);\n"
"    color: rgb(240, 233, 249);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.pushButton_cadastra_cliente.setObjectName("pushButton_cadastra_cliente")
        self.verticalLayout_2.addWidget(self.pushButton_cadastra_cliente)
        self.pushButton_atualiza_cliente = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_atualiza_cliente.setMinimumSize(QtCore.QSize(100, 10))
        self.pushButton_atualiza_cliente.setMaximumSize(QtCore.QSize(230, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_atualiza_cliente.setFont(font)
        self.pushButton_atualiza_cliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_atualiza_cliente.setStyleSheet("QPushButton{\n"
"    border-radius: 10px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"        \n"
"    color: rgb(240, 233, 249);\n"
"    background-color: rgb(255, 174, 35);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(207, 110, 0);\n"
"    color: rgb(240, 233, 249);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.pushButton_atualiza_cliente.setObjectName("pushButton_atualiza_cliente")
        self.verticalLayout_2.addWidget(self.pushButton_atualiza_cliente)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(240, 233, 249);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.pushButton_cadastra_fornecedor = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_cadastra_fornecedor.setMinimumSize(QtCore.QSize(100, 10))
        self.pushButton_cadastra_fornecedor.setMaximumSize(QtCore.QSize(230, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cadastra_fornecedor.setFont(font)
        self.pushButton_cadastra_fornecedor.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_cadastra_fornecedor.setStyleSheet("QPushButton{\n"
"    border-radius: 10px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"        \n"
"    color: rgb(240, 233, 249);\n"
"    background-color: rgb(255, 174, 35);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(207, 110, 0);\n"
"    color: rgb(240, 233, 249);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.pushButton_cadastra_fornecedor.setObjectName("pushButton_cadastra_fornecedor")
        self.verticalLayout_5.addWidget(self.pushButton_cadastra_fornecedor)
        self.pushButton_atualiza_fornecedor = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_atualiza_fornecedor.setMinimumSize(QtCore.QSize(100, 10))
        self.pushButton_atualiza_fornecedor.setMaximumSize(QtCore.QSize(230, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_atualiza_fornecedor.setFont(font)
        self.pushButton_atualiza_fornecedor.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_atualiza_fornecedor.setStyleSheet("QPushButton{\n"
"    border-radius: 10px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"        \n"
"    color: rgb(240, 233, 249);\n"
"    background-color: rgb(255, 174, 35);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(207, 110, 0);\n"
"    color: rgb(240, 233, 249);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.pushButton_atualiza_fornecedor.setObjectName("pushButton_atualiza_fornecedor")
        self.verticalLayout_5.addWidget(self.pushButton_atualiza_fornecedor)
        self.verticalLayout.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(240, 233, 249);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.pushButton_cadastra_produto = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_cadastra_produto.setMinimumSize(QtCore.QSize(100, 10))
        self.pushButton_cadastra_produto.setMaximumSize(QtCore.QSize(230, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cadastra_produto.setFont(font)
        self.pushButton_cadastra_produto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_cadastra_produto.setStyleSheet("QPushButton{\n"
"    border-radius: 10px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"        \n"
"    color: rgb(240, 233, 249);\n"
"    background-color: rgb(255, 174, 35);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(207, 110, 0);\n"
"    color: rgb(240, 233, 249);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.pushButton_cadastra_produto.setObjectName("pushButton_cadastra_produto")
        self.verticalLayout_6.addWidget(self.pushButton_cadastra_produto)
        self.pushButton_atualiza_produto = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_atualiza_produto.setMinimumSize(QtCore.QSize(100, 10))
        self.pushButton_atualiza_produto.setMaximumSize(QtCore.QSize(230, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_atualiza_produto.setFont(font)
        self.pushButton_atualiza_produto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_atualiza_produto.setStyleSheet("QPushButton{\n"
"    border-radius: 10px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"        \n"
"    color: rgb(240, 233, 249);\n"
"    background-color: rgb(255, 174, 35);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(207, 110, 0);\n"
"    color: rgb(240, 233, 249);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.pushButton_atualiza_produto.setObjectName("pushButton_atualiza_produto")
        self.verticalLayout_6.addWidget(self.pushButton_atualiza_produto)
        self.verticalLayout.addWidget(self.frame_8)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pushButton_sair = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_sair.setGeometry(QtCore.QRect(10, 10, 160, 30))
        self.pushButton_sair.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_sair.setMaximumSize(QtCore.QSize(230, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_sair.setFont(font)
        self.pushButton_sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_sair.setStyleSheet("QPushButton{\n"
"    border-radius: 10px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"        \n"
"    color: rgb(240, 233, 249);\n"
"    background-color: rgb(255, 174, 35);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(207, 110, 0);\n"
"    color: rgb(240, 233, 249);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.pushButton_sair.setObjectName("pushButton_sair")
        self.verticalLayout.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setEnabled(True)
        self.frame_2.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(170, 10, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(10, 240, 421, 231))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setGeometry(QtCore.QRect(10, 10, 401, 142))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.login_conteudo = QtWidgets.QFrame(self.frame_9)
        self.login_conteudo.setMaximumSize(QtCore.QSize(16777215, 600))
        self.login_conteudo.setStyleSheet("background-color: rgb(242, 242, 243);")
        self.login_conteudo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_conteudo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_conteudo.setObjectName("login_conteudo")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.login_conteudo)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_razao_social = QtWidgets.QLineEdit(self.login_conteudo)
        self.lineEdit_razao_social.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_razao_social.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.lineEdit_razao_social.setText("")
        self.lineEdit_razao_social.setObjectName("lineEdit_razao_social")
        self.verticalLayout_3.addWidget(self.lineEdit_razao_social)
        self.lineEdit_cnpj = QtWidgets.QLineEdit(self.login_conteudo)
        self.lineEdit_cnpj.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_cnpj.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.lineEdit_cnpj.setObjectName("lineEdit_cnpj")
        self.verticalLayout_3.addWidget(self.lineEdit_cnpj)
        self.lineEdit_nacionalidade = QtWidgets.QLineEdit(self.login_conteudo)
        self.lineEdit_nacionalidade.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_nacionalidade.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.lineEdit_nacionalidade.setObjectName("lineEdit_nacionalidade")
        self.verticalLayout_3.addWidget(self.lineEdit_nacionalidade)
        self.horizontalLayout_3.addWidget(self.login_conteudo)
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_endereco = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_endereco.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_endereco.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.lineEdit_endereco.setObjectName("lineEdit_endereco")
        self.verticalLayout_4.addWidget(self.lineEdit_endereco)
        self.lineEdit_telefone = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_telefone.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_telefone.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.lineEdit_telefone.setObjectName("lineEdit_telefone")
        self.verticalLayout_4.addWidget(self.lineEdit_telefone)
        self.lineEdit_pessoa = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_pessoa.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_pessoa.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.lineEdit_pessoa.setObjectName("lineEdit_pessoa")
        self.verticalLayout_4.addWidget(self.lineEdit_pessoa)
        self.horizontalLayout_3.addWidget(self.frame_10)
        self.pushButton_cadastra_fornecedor_2 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_cadastra_fornecedor_2.setGeometry(QtCore.QRect(100, 170, 230, 50))
        self.pushButton_cadastra_fornecedor_2.setMinimumSize(QtCore.QSize(230, 50))
        self.pushButton_cadastra_fornecedor_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cadastra_fornecedor_2.setFont(font)
        self.pushButton_cadastra_fornecedor_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_cadastra_fornecedor_2.setStyleSheet("QPushButton{\n"
"    border-radius: 10px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"        \n"
"    color: rgb(240, 233, 249);\n"
"    background-color: rgb(255, 144, 14);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(207, 110, 0);\n"
"    color: rgb(240, 233, 249);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.pushButton_cadastra_fornecedor_2.setObjectName("pushButton_cadastra_fornecedor_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(130, 220, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_mostrar_mais = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_mostrar_mais.setGeometry(QtCore.QRect(110, 200, 230, 13))
        self.pushButton_mostrar_mais.setMaximumSize(QtCore.QSize(300, 16777215))
        self.pushButton_mostrar_mais.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_mostrar_mais.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"    \n"
"    color: rgb(0,127,255);\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_mostrar_mais.setObjectName("pushButton_mostrar_mais")
        self.textEdit_tabela_fornecedores = QtWidgets.QTableWidget(self.frame_2)
        self.textEdit_tabela_fornecedores.setGeometry(QtCore.QRect(10, 30, 421, 161))
        self.textEdit_tabela_fornecedores.setObjectName("textEdit_tabela_fornecedores")
        self.textEdit_tabela_fornecedores.setColumnCount(7)
        self.textEdit_tabela_fornecedores.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.textEdit_tabela_fornecedores.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.textEdit_tabela_fornecedores.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.textEdit_tabela_fornecedores.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.textEdit_tabela_fornecedores.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.textEdit_tabela_fornecedores.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.textEdit_tabela_fornecedores.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.textEdit_tabela_fornecedores.setHorizontalHeaderItem(6, item)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_string_ola.setText(_translate("MainWindow", "Olá,"))
        self.pushButton_vendas.setText(_translate("MainWindow", "Vendas"))
        self.label_3.setText(_translate("MainWindow", "Cliente:"))
        self.pushButton_cadastra_cliente.setText(_translate("MainWindow", "Cadastrar cliente"))
        self.pushButton_atualiza_cliente.setText(_translate("MainWindow", "Atualizar cliente"))
        self.label_4.setText(_translate("MainWindow", "Fornecedor:"))
        self.pushButton_cadastra_fornecedor.setText(_translate("MainWindow", "Cadastrar fornecedor"))
        self.pushButton_atualiza_fornecedor.setText(_translate("MainWindow", "Atualizar fornecedor"))
        self.label_5.setText(_translate("MainWindow", "Produto:"))
        self.pushButton_cadastra_produto.setText(_translate("MainWindow", "Cadastrar produto"))
        self.pushButton_atualiza_produto.setText(_translate("MainWindow", "Atualizar produto"))
        self.pushButton_sair.setText(_translate("MainWindow", "Sair"))
        self.label.setText(_translate("MainWindow", "Fornecedores"))
        self.lineEdit_razao_social.setPlaceholderText(_translate("MainWindow", "Razão Social"))
        self.lineEdit_cnpj.setPlaceholderText(_translate("MainWindow", "CNPJ"))
        self.lineEdit_nacionalidade.setPlaceholderText(_translate("MainWindow", "Nacionalidade"))
        self.lineEdit_endereco.setPlaceholderText(_translate("MainWindow", "Endereco"))
        self.lineEdit_telefone.setPlaceholderText(_translate("MainWindow", "Telefone para contato"))
        self.lineEdit_pessoa.setPlaceholderText(_translate("MainWindow", "Pessoa do contato"))
        self.pushButton_cadastra_fornecedor_2.setText(_translate("MainWindow", "Cadastrar Fornecedor"))
        self.label_2.setText(_translate("MainWindow", "Cadastrar Fornecedores"))
        self.pushButton_mostrar_mais.setText(_translate("MainWindow", "Mostrar mais ..."))
        item = self.textEdit_tabela_fornecedores.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "razao_social"))
        item = self.textEdit_tabela_fornecedores.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.textEdit_tabela_fornecedores.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CNPJ"))
        item = self.textEdit_tabela_fornecedores.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "nacionalidade"))
        item = self.textEdit_tabela_fornecedores.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "endereco"))
        item = self.textEdit_tabela_fornecedores.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "telefone"))
        item = self.textEdit_tabela_fornecedores.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "passoa_contato"))

