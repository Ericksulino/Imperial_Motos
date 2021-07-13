import sqlite3
from sqlite3.dbapi2 import Cursor
from tkinter import filedialog
import testeArqui
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QMainWindow,QApplication,QFileDialog
from PyQt5.QtCore import QCoreApplication

from cadastro_moto2 import Cad_moto
from cadastro_pessoa2 import Cad_pessoa
from login2 import Login
from home2 import Home
from telaCompra import TelaComprar
from telaintere import TelaIntere
from telaMenUsario import TelaMenUsuario
from telaEditPerf import TelaEditPerfs

from moto import Moto,CadastroMoto
from pessoa import Pessoa, PessoaCadas

#bd = sqlite3.connect('bd.sqlite')
#cursor = bd.cursor()

#pessoas = """CREATE TABLE IF NOT EXISTS pessoas(id integir PRIMARY KEY,nome text NOT NULL,endereco text NOT NULL,cpf text NOT NULL,data_nascimento text NOT NULL,senha text NOT NULL);"""
#motos = """CREATE TABLE IF NOT EXISTS motos(id integir PRIMARY KEY,numero_chassi text NOT NULL,modelo text NOT NULL,marca text NOT NULL,categoria text NOT NULL,ano text NOT NULL,valor float NOT NULL);"""

#cursor.execute(pessoas)
#cursor.execute(motos)

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640,480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()

        self.tela_inicio = Home()
        self.tela_inicio.setupUi(self.stack0)

        self.tela_cadastro_moto = Cad_moto()
        self.tela_cadastro_moto.setupUi(self.stack1)

        self.tela_cadsClie = Cad_pessoa()
        self.tela_cadsClie.setupUi(self.stack2)


        self.tela_login = Login()
        self.tela_login.setupUi(self.stack3)
        
        self.telaCompra=TelaComprar()
        self.telaCompra.setupUi(self.stack4)

        self.telaPerfil=TelaEditPerfs()
        self.telaPerfil.setupUi(self.stack5)

        self.telaIntere=TelaIntere()
        self.telaIntere.setupUi(self.stack6)

        self.telamenUsu=TelaMenUsuario()
        self.telamenUsu.setupUi(self.stack7)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)

class Main(QMainWindow,Ui_Main):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.pasta =dir_path+ '\cache'
        if os.path.isdir(self.pasta): # vemos de este diretorio ja existe
            print ('Ja existe uma pasta com esse nome!')
        else:
            os.mkdir(self.pasta) # aqui criamos a pasta caso nao exista
            print ('Pasta criada com sucesso!')
        self.tela_inicio.pushButton.clicked.connect(self.abrircompra)

        self.tela_inicio.pushButton_2.clicked.connect(self.abrirCadastroMoto)
        self.tela_inicio.pushButton_3.clicked.connect(self.abrirLogin)
        self.tela_inicio.pushButton_4.clicked.connect(self.abrirCadastroPessoa)
        self.fotos=[]
        self.fotoComp=[]
        self.contaLogada=None
        self.telaCompra.buttonComp1.clicked.connect(self.abrirInter)
        self.telaCompra.buttonComp2.clicked.connect(self.abrirInter)
        self.telaCompra.buttonComp3.clicked.connect(self.abrirInter)
        self.telaCompra.buttonComp4.clicked.connect(self.abrirInter)
        self.telaCompra.buttonComp5.clicked.connect(self.abrirInter)
        self.telaCompra.buttonComp6.clicked.connect(self.abrirInter)

        self.telaCompra.buttonAnt.clicked.connect(self.butComprar)
        self.telaCompra.buttonProx.clicked.connect(self.butComprar)
        self.telaCompra.buttonVoltar.clicked.connect(self.abrirHome)


        self.tela_cadastro_moto.ButtoAnunciar.clicked.connect(self.botaoCadastraMoto)
        self.tela_cadastro_moto.buttonVoltar.clicked.connect(self.abrirHome)
        self.tela_cadastro_moto.ButtonImagem.clicked.connect(self.pegarFotos)
        self.tela_cadsClie.pushButton.clicked.connect(self.botaoCadastraPes)

        self.tela_login.pushButton.clicked.connect(self.botaoLogin)
        self.tela_login.pushButton_2.clicked.connect(self.abrirHome)

        self.telaPerfil.pushButton.clicked.connect(self.botaoAttCadas)

        self.telamenUsu.pushButton.clicked.connect(self.abrirPerfil)
        self.telamenUsu.pushButton_2.clicked.connect(self.mostrarVendas)
        self.telamenUsu.pushButton_3.clicked.connect(self.abrircompra)
        self.telamenUsu.pushButton_5.clicked.connect(self.abrirHome)

        self.telaIntere.pushButton.clicked.connect(self.botaoInteres)
        self.telaIntere.pushButton_2.clicked.connect(self.abrirMenu)
    #remove todas as foto da pasta cache para att quando for cadastrada uma nova moto
    def atualizaPasta(self,path):
        dire = os.listdir(path)
        for file in dire: 
                os.remove(file)
        testeArqui.readBlobData(1)
    def botaoAttCadas(self):
        #pega os campos
        self.abrirMenu()
        
    def mostrarVendas(self):
        pass
    def mostrarCompras(self):
        pass
    def botaoInteres(self):
        pass
    def buttBack(self):
        pass
    def buttF(self):
        pass
    def butComprar(self):
        pass
    def telaCompra(self):
        self.telaCompra.setImagem(self.fotoComp)
        #TelaComprar.setImgens()
        pass
    def botaoCadastraMoto(self):
        numero_chassi = self.tela_cadastro_moto.Linechassi.text()
        modelo = self.tela_cadastro_moto.LineModelo.text()
        marca = self.tela_cadastro_moto.LineMarca.text()
        categoria = self.tela_cadastro_moto.LineCategoria.text()
        ano = self.tela_cadastro_moto.LineAno.text()
        valor = self.tela_cadastro_moto.LineValor.text()
        cpf_cnpj = self.tela_cadastro_moto.LineCPFVendedor.text()
        moto=Moto(numero_chassi,marca,categoria,ano,valor,modelo,cpf_cnpj)
        m=CadastroMoto()
        if not(numero_chassi == '' or modelo == '' or marca == '' or categoria == '' or ano == '' or valor == '' or cpf_cnpj == ''):
            if (m.cadastra_moto(moto)):
                QMessageBox.information(None,'Sistema','Cadastro realizado com sucesso!')
                testeArqui.insertBLOB(moto._num_chas,moto._tipo,self.fotos[0][0])
                self.atualizaPasta(self.pasta)
                self.tela_cadastro_moto.Linechassi.setText('')
                self.tela_cadastro_moto.LineModelo.setText('')
                self.tela_cadastro_moto.LineMarca.setText('')
                self.tela_cadastro_moto.LineCategoria.setText('')
                self.tela_cadastro_moto.LineAno.setText('')
                self.tela_cadastro_moto.LineValor.setText('')
                self.tela_cadastro_moto.LineCPFVendedor.setText('')
                self.abrirHome()
            else:
                QMessageBox.information(None,'Sistema','Chassi já cadastrado.')

        else:
            QMessageBox.information(None,'Sistema','Preencha todos os campos!')
            #self.abrirHome()

    def pegarFotos(self):

        arquivos=filedialog.askopenfilename()
        self.fotos.append(arquivos)
        #print(len(arquivos))
        
    def botaoCadastraPes(self):
        nome = self.tela_cadsClie.lineEdit.text()
        endereco = self.tela_cadsClie.lineEdit_2.text()
        cpf = self.tela_cadsClie.lineEdit_3.text()
        dtnas = self.tela_cadsClie.lineEdit_4.text()
        senha = self.tela_cadsClie.lineEdit_5.text()
        if not(nome == '' or endereco == '' or cpf == '' or dtnas == '' or senha == ''):
            p=Pessoa(nome,endereco,cpf,dtnas,senha)
            c=PessoaCadas()
            
            if (c.cadast_pess(p)):
                QMessageBox.information(None,'Sistema','Cadastro realizado com sucesso!')
                self.tela_cadsClie.lineEdit.setText('')
                self.tela_cadsClie.lineEdit_2.setText('')
                self.tela_cadsClie.lineEdit_3.setText('')
                self.tela_cadsClie.lineEdit_4.setText('')
                self.tela_cadsClie.lineEdit_5.setText('')
                self.abrirHome()
            else:
                QMessageBox.information(None,'Sistema','Cadastro não realizado!')
                self.tela_cadsClie.lineEdit.setText('')
                self.tela_cadsClie.lineEdit_2.setText('')
                self.tela_cadsClie.lineEdit_3.setText('')
                self.tela_cadsClie.lineEdit_4.setText('')
                self.tela_cadsClie.lineEdit_5.setText('')
                self.abrirHome()
        else:
            QMessageBox.information(None,'Sistema','Preecha todos os campos!')
    
    def botaoLogin(self):
        cpf_cnpj = self.tela_login.lineEdit.text()
        senha = self.tela_login.lineEdit_2.text()
        if not(cpf_cnpj == '' or senha == ''):
            c=PessoaCadas()
            self.contaLogada=c.busca_pess(cpf_cnpj)
            if self.contaLogada!=None:
                self.abrirMenu()
            else:
                QMessageBox.information(None,'Sistema','CPF não cadastrado')

        else:
            QMessageBox.information(None,'Sistema','Preecha todos os campos!')
    
    def abrirHome(self):
        self.contaLogada=None
        self.QtStack.setCurrentIndex(0)

    def abrirCadastroMoto(self):
        self.QtStack.setCurrentIndex(1)


    def abrirCadastroPessoa(self):
        self.QtStack.setCurrentIndex(2)

    def abrirLogin(self):
        self.QtStack.setCurrentIndex(3)
    def abrircompra(self):
        self.QtStack.setCurrentIndex(4)
    def abrirPerfil(self):
        self.QtStack.setCurrentIndex(5)
    def abrirInter(self):
        if(self.contaLogada!=None):
            self.QtStack.setCurrentIndex(6)
        else:
            self.abrirLogin()
            

    def abrirMenu(self):
        self.QtStack.setCurrentIndex(7)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    show_main = Main()
    sys.exit(app.exec_())