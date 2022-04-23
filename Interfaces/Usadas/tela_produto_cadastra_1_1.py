# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\menu_cadastra_produto.ui'
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
        self.centralwidget.setMinimumSize(QtCore.QSize(640, 480))
        self.centralwidget.setMaximumSize(QtCore.QSize(640, 480))
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
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(190, 10, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(10, 190, 421, 281))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setGeometry(QtCore.QRect(10, 10, 401, 222))
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
        self.lineEdit_n_bebida = QtWidgets.QLineEdit(self.frame_11)
        self.lineEdit_n_bebida.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_n_bebida.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.lineEdit_n_bebida.setObjectName("lineEdit_n_bebida")
        self.verticalLayout_8.addWidget(self.lineEdit_n_bebida)
        self.lineEdit_nome_bebida = QtWidgets.QLineEdit(self.frame_11)
        self.lineEdit_nome_bebida.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_nome_bebida.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.lineEdit_nome_bebida.setText("")
        self.lineEdit_nome_bebida.setObjectName("lineEdit_nome_bebida")
        self.verticalLayout_8.addWidget(self.lineEdit_nome_bebida)
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
        self.lineEdit_data_fabricacao = QtWidgets.QDateEdit(self.frame_13)
        self.lineEdit_data_fabricacao.setObjectName("lineEdit_data_fabricacao")
        self.horizontalLayout_4.addWidget(self.lineEdit_data_fabricacao)
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
        self.lineEdit_data_vencimento_2 = QtWidgets.QDateEdit(self.frame_14)
        self.lineEdit_data_vencimento_2.setObjectName("lineEdit_data_vencimento_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_data_vencimento_2)
        self.verticalLayout_8.addWidget(self.frame_14)
        self.lineEdit_condicoes = QtWidgets.QLineEdit(self.frame_11)
        self.lineEdit_condicoes.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_condicoes.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.lineEdit_condicoes.setObjectName("lineEdit_condicoes")
        self.verticalLayout_8.addWidget(self.lineEdit_condicoes)
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
        self.lineEdit_quantidade = QtWidgets.QSpinBox(self.frame_15)
        self.lineEdit_quantidade.setObjectName("lineEdit_quantidade")
        self.horizontalLayout_6.addWidget(self.lineEdit_quantidade)
        self.verticalLayout_7.addWidget(self.frame_15)
        self.lineEdit_local = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_local.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_local.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.lineEdit_local.setObjectName("lineEdit_local")
        self.verticalLayout_7.addWidget(self.lineEdit_local)
        self.lineEdit_v_compra_uni = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_v_compra_uni.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_v_compra_uni.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.lineEdit_v_compra_uni.setObjectName("lineEdit_v_compra_uni")
        self.verticalLayout_7.addWidget(self.lineEdit_v_compra_uni)
        self.lineEdit_re_venda_uni = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_re_venda_uni.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_re_venda_uni.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.lineEdit_re_venda_uni.setObjectName("lineEdit_re_venda_uni")
        self.verticalLayout_7.addWidget(self.lineEdit_re_venda_uni)
        self.lineEdit_id_forncedor = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_id_forncedor.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_id_forncedor.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.lineEdit_id_forncedor.setObjectName("lineEdit_id_forncedor")
        self.verticalLayout_7.addWidget(self.lineEdit_id_forncedor)
        self.horizontalLayout_3.addWidget(self.frame_10)
        self.pushButton_cadastrafornecedor = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_cadastrafornecedor.setGeometry(QtCore.QRect(100, 220, 230, 50))
        self.pushButton_cadastrafornecedor.setMinimumSize(QtCore.QSize(230, 50))
        self.pushButton_cadastrafornecedor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cadastrafornecedor.setFont(font)
        self.pushButton_cadastrafornecedor.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_cadastrafornecedor.setStyleSheet("QPushButton{\n"
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
        self.pushButton_cadastrafornecedor.setObjectName("pushButton_cadastrafornecedor")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(160, 170, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_mostrar_mais = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_mostrar_mais.setGeometry(QtCore.QRect(110, 150, 230, 13))
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
        self.textEdit_tabela_fornecedores.setGeometry(QtCore.QRect(10, 30, 421, 121))
        self.textEdit_tabela_fornecedores.setObjectName("textEdit_tabela_fornecedores")
        self.textEdit_tabela_fornecedores.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.textEdit_tabela_fornecedores.setHorizontalHeaderItem(7, item)
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
        self.label.setText(_translate("MainWindow", "Vinhos"))
        self.lineEdit_n_bebida.setPlaceholderText(_translate("MainWindow", "Numero da Bebida"))
        self.lineEdit_nome_bebida.setPlaceholderText(_translate("MainWindow", "Nome da Bebida"))
        self.label_6.setText(_translate("MainWindow", "Fabricacão:"))
        self.label_7.setText(_translate("MainWindow", "Validade:"))
        self.lineEdit_condicoes.setPlaceholderText(_translate("MainWindow", "Condições de armazenamento"))
        self.label_8.setText(_translate("MainWindow", "Quantidade:"))
        self.lineEdit_local.setPlaceholderText(_translate("MainWindow", "Local de Armazenamento"))
        self.lineEdit_v_compra_uni.setPlaceholderText(_translate("MainWindow", "Valor de compra Unidade"))
        self.lineEdit_re_venda_uni.setPlaceholderText(_translate("MainWindow", "Valor de re-venda Unidade"))
        self.lineEdit_id_forncedor.setPlaceholderText(_translate("MainWindow", "Id do Fornecedor"))
        self.pushButton_cadastrafornecedor.setText(_translate("MainWindow", "Cadastrar Produto"))
        self.label_2.setText(_translate("MainWindow", "Cadastrar Vinho"))
        self.pushButton_mostrar_mais.setText(_translate("MainWindow", "Mostrar mais ..."))
        item = self.textEdit_tabela_fornecedores.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "n_bebida"))
        item = self.textEdit_tabela_fornecedores.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "nome"))
        item = self.textEdit_tabela_fornecedores.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "fabricacao"))
        item = self.textEdit_tabela_fornecedores.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "validade"))
        item = self.textEdit_tabela_fornecedores.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "armazenamento"))
        item = self.textEdit_tabela_fornecedores.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "quantidades"))
        item = self.textEdit_tabela_fornecedores.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "local"))
        item = self.textEdit_tabela_fornecedores.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "valor"))

