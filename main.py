import sqlite3
from sqlite3.dbapi2 import Cursor

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QMainWindow,QApplication,QFileDialog
from PyQt5.QtCore import QCoreApplication

from cadastro_moto import Cadastro_Moto
from cadastro_pessoa import Cadastro_Pessoa
from login import Login
from home import Home

from moto import Moto
from pessoa import Pessoa

bd = sqlite3.connect('bd.sqlite')
cursor = bd.cursor()

pessoas = """CREATE TABLE IF NOT EXISTS pessoas(id integir PRIMARY KEY,nome text NOT NULL,endereco text NOT NULL,cpf text NOT NULL,data_nascimento text NOT NULL,senha text NOT NULL);"""
motos = """CREATE TABLE IF NOT EXISTS motos(id integir PRIMARY KEY,numero_chassi text NOT NULL,modelo text NOT NULL,marca text NOT NULL,categoria text NOT NULL,ano text NOT NULL,valor float NOT NULL);"""

cursor.execute(pessoas)
cursor.execute(motos)

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
        self.tela_cadastro_moto.pushButton.clicked.connect(self.botaoCadastraMoto)
        self.tela_cadsClie.pushButton.clicked.connect(self.botaoCadastraPes)
        self.tela_login.pushButton.clicked.connect(self.botaoLogin)
                
    def botaoCadastraMoto(self):
        numero_chassi = self.tela_cadastro_moto.lineEdit.text()
        modelo = self.tela_cadastro_moto.lineEdit_2.text()
        marca = self.tela_cadastro_moto.lineEdit_3.text()
        categoria = self.tela_cadastro_moto.lineEdit_4.text()
        ano = self.tela_cadastro_moto.lineEdit_5.text()
        valor = self.tela_cadastro_moto.lineEdit_6.text()
        cpf_cnpj = self.tela_cadastro_moto.lineEdit_7.text()

        if not(numero_chassi == '' or modelo == '' or marca == '' or categoria == '' or ano == '' or valor == '' or cpf_cnpj == ''):
            if (Moto.cadastra_moto(numero_chassi,modelo,marca,categoria,ano,valor,cursor)):
                QMessageBox.information(None,'Sistema','Cadastro realizado com sucesso!')
        else:
            QMessageBox.information(None,'Sistema','Preecha todos os campos!')

    def botaoCadastraPes(self):
        nome = self.tela_cadsClie.lineEdit.text()
        endereco = self.tela_cadsClie.lineEdit_2.text()
        cpf = self.tela_cadsClie.lineEdit_3.text()
        dtnas = self.tela_cadsClie.lineEdit_4.text()
        senha = self.tela_cadsClie.lineEdit_5.text()

        if not(nome == '' or endereco == '' or cpf == '' or dtnas == '' or senha == ''):
            if (Pessoa.cadast_pess(nome,endereco,cpf,dtnas,senha,cursor)):
                QMessageBox.information(None,'Sistema','Cadastro realizado com sucesso!')
        else:
            QMessageBox.information(None,'Sistema','Preecha todos os campos!')
    
    def botaoLogin(self):
        cpf_cnpj = self.tela_login.lineEdit.text()
        senha = self.tela_login.lineEdit_2.text()
        if not(cpf_cnpj == '' or senha == ''):
            if (Pessoa.login(cpf_cnpj,senha,cursor)):
                QMessageBox.information(None,'Sistema','Login Efetuado!')
            else:
                QMessageBox.information(None,'Sistema','Login Não Efetuado!')
        else:
            QMessageBox.information(None,'Sistema','Preecha todos os campos!')
    
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