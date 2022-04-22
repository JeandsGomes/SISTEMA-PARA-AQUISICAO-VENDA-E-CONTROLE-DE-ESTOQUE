# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\menu_busca_modifica_produto.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
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
        self.frame_12 = QtWidgets.QFrame(self.frame)
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton_vendas = QtWidgets.QPushButton(self.frame_12)
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
        self.verticalLayout_9.addWidget(self.pushButton_vendas)
        self.verticalLayout.addWidget(self.frame_12)
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
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 30, 181, 30))
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_2.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_busca = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_busca.setGeometry(QtCore.QRect(290, 30, 50, 30))
        self.pushButton_busca.setMinimumSize(QtCore.QSize(50, 30))
        self.pushButton_busca.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_busca.setFont(font)
        self.pushButton_busca.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_busca.setStyleSheet("QPushButton{\n"
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
        self.pushButton_busca.setObjectName("pushButton_busca")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(10, 80, 421, 391))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.pushButton_atualiza = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_atualiza.setGeometry(QtCore.QRect(20, 230, 161, 50))
        self.pushButton_atualiza.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_atualiza.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_atualiza.setFont(font)
        self.pushButton_atualiza.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_atualiza.setStyleSheet("QPushButton{\n"
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
        self.pushButton_atualiza.setObjectName("pushButton_atualiza")
        self.pushButton_cadastro_cadastrar_17 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_cadastro_cadastrar_17.setGeometry(QtCore.QRect(250, 230, 161, 50))
        self.pushButton_cadastro_cadastrar_17.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_cadastro_cadastrar_17.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cadastro_cadastrar_17.setFont(font)
        self.pushButton_cadastro_cadastrar_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_cadastro_cadastrar_17.setStyleSheet("QPushButton{\n"
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
        self.pushButton_cadastro_cadastrar_17.setObjectName("pushButton_cadastro_cadastrar_17")
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setGeometry(QtCore.QRect(10, 10, 401, 214))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_11 = QtWidgets.QFrame(self.frame_9)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_11)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_6.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_8.addWidget(self.lineEdit_6)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_11)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_3.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_8.addWidget(self.lineEdit_3)
        self.frame_13 = QtWidgets.QFrame(self.frame_11)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.frame_13)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.lineEdit_7 = QtWidgets.QDateEdit(self.frame_13)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_4.addWidget(self.lineEdit_7)
        self.verticalLayout_8.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_11)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.frame_14)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.lineEdit_14 = QtWidgets.QDateEdit(self.frame_14)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.horizontalLayout_5.addWidget(self.lineEdit_14)
        self.verticalLayout_8.addWidget(self.frame_14)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame_11)
        self.lineEdit_15.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_15.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.verticalLayout_8.addWidget(self.lineEdit_15)
        self.horizontalLayout_3.addWidget(self.frame_11)
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_15 = QtWidgets.QFrame(self.frame_10)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.frame_15)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.lineEdit_8 = QtWidgets.QSpinBox(self.frame_15)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_6.addWidget(self.lineEdit_8)
        self.verticalLayout_7.addWidget(self.frame_15)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_9.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_7.addWidget(self.lineEdit_9)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_10.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_7.addWidget(self.lineEdit_10)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_12.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_7.addWidget(self.lineEdit_12)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_11.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_7.addWidget(self.lineEdit_11)
        self.horizontalLayout_3.addWidget(self.frame_10)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 301, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
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
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Numero da Bibida"))
        self.pushButton_busca.setText(_translate("MainWindow", "Buscar"))
        self.pushButton_atualiza.setText(_translate("MainWindow", "Atualizar Fornecedor"))
        self.pushButton_cadastro_cadastrar_17.setText(_translate("MainWindow", "Remover Fornecedor"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Numero da Bebida (Remoção)"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Nome da Bebida"))
        self.label_6.setText(_translate("MainWindow", "Fabricacão:"))
        self.label_7.setText(_translate("MainWindow", "Validade:"))
        self.lineEdit_15.setPlaceholderText(_translate("MainWindow", "Condições de armazenamento"))
        self.label_8.setText(_translate("MainWindow", "Quantidade:"))
        self.lineEdit_9.setPlaceholderText(_translate("MainWindow", "Local de Armazenamento"))
        self.lineEdit_10.setPlaceholderText(_translate("MainWindow", "Valor de compra Unidade"))
        self.lineEdit_12.setPlaceholderText(_translate("MainWindow", "Valor de re-venda Unidade"))
        self.lineEdit_11.setPlaceholderText(_translate("MainWindow", "Id do Fornecedor"))
        self.label_2.setText(_translate("MainWindow", "Atualizar, Remoção ou Buscar Vinhos"))

