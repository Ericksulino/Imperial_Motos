import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QMainWindow,QApplication,QFileDialog
from PyQt5.QtCore import QCoreApplication

from cadastro_moto import Cadastro_Moto
from cadastro_pessoa import Cadastro_Pessoa
from login import Login
from home import Home

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640,480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()

        self.tela_inicio = Home()
        self.tela_inicio.setupUi(self.stack0)

        self.tela_cadastro_moto = Cadastro_Moto()
        self.tela_cadastro_moto.setupUi(self.stack1)

        self.tela_cadsClie = Cadastro_Pessoa()
        self.tela_cadsClie.setupUi(self.stack2)

        self.tela_login = Login()
        self.tela_login.setupUi(self.stack3)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)

class Main(QMainWindow,Ui_Main):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)

        #self.tela_inicio.pushButton.clicked.connect(self.tela_compra)
        self.tela_inicio.pushButton_2.clicked.connect(self.abrirCadastroMoto)
        self.tela_inicio.pushButton_3.clicked.connect(self.abrirLogin)
        self.tela_inicio.pushButton_4.clicked.connect(self.abrirCadastroPessoa)
                
    def botaoCadastraMoto(self):
        numero_chassi = self.cadastro_moto.lineEdit.text()
        modelo = self.cadatro_moto.lineEdit_2.text()
        marca = self.cadastro_moto.lineEdit_3.text()
        categorio = self.cadastro_mooto.lineEdit_4.text()
        ano = self.cadastro_moto.lineEdit_5.text()
        valor = self.cadastro_moto.lineEdit_6.text()
        cpf_cnpj = self.cadastro_moto.lineEdit_7.text()

        if not(numero_chassi == '' or modelo == '' or marca == '' or categorio == '' or ano == '' or valor == '' or cpf_cnpj == ''):
            #m = Moto(numero_chassi,modelo,marca,categorio,ano,valor,cpf_cnpj)
            pass

    def abrirHome(self):
        self.QtStack.setCurrentIndex(0)

    def abrirCadastroMoto(self):
        self.QtStack.setCurrentIndex(1)

    def abrirLogin(self):
        self.QtStack.setCurrentIndex(3)

    def abrirCadastroPessoa(self):
        self.QtStack.setCurrentIndex(2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    show_main = Main()
    sys.exit(app.exec_())