import sqlite3
from sqlite3.dbapi2 import Cursor
from tkinter import Tk, filedialog
import tkinter
import testeArqui
import sys
import os
from os import chdir, getcwd, listdir
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
        self.pasta =dir_path+ '/cache'
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
        self.listaMoto={}
        self.fotoComp=self.pegaFotos()
        self.contaLogada=None
        self.buttClick=0
        self.produto=None
        self.telaCompra.buttonComp1.clicked.connect(self.buttonCompra1)
        self.telaCompra.buttonComp2.clicked.connect(self.buttonCompra2)
        self.telaCompra.buttonComp3.clicked.connect(self.buttonCompra3)
        self.telaCompra.buttonComp4.clicked.connect(self.buttonCompra4)
        self.telaCompra.buttonComp5.clicked.connect(self.buttonCompra5)
        self.telaCompra.buttonComp6.clicked.connect(self.buttonCompra6)
        self.telaCompra.buttonComp7.clicked.connect(self.buttonCompra7)
        self.telaCompra.buttonComp8.clicked.connect(self.buttonCompra8)

        self.telaCompra.buttonAnt.clicked.connect(self.buttBack)
        self.telaCompra.buttonProx.clicked.connect(self.buttF)
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
        print(getcwd())
        print(path)
        dire = os.listdir(path)
        for file in dire: 
            os.remove(file)
        c=self.pasta.split('/cache')
        chdir(c[0])
        testeArqui.readBlobData(1)
        chdir(path)
    def botaoAttCadas(self):
        #pega os campos
        self.abrirMenu()
    def buttonCompra1(self):#-8
        try:

            tes=self.fotoComp[self.buttClick-8]
            tes=self.pegaCodCache(tes)
            if(tes!='unknown'):
                self.produto=tes
                self.abrirInter()
                self.telaIntere.lineEdit.setText('test1')
                self.telaIntere.lineEdit_2.setText('test1')
                self.telaIntere.lineEdit_3.setText('tes1')
                self.telaIntere.setImage(self.fotoComp[self.buttClick-8]) 
        except:
            pass
                
    def buttonCompra2(self):#-7

        try:
         
            tes=self.fotoComp[self.buttClick-7]
            tes=self.pegaCodCache(tes)
            if(tes!='unknown'):

                self.produto=tes
                self.abrirInter()
                self.telaIntere.lineEdit.setText('tes1')
                self.telaIntere.lineEdit_2.setText('test1')
                self.telaIntere.lineEdit_3.setText('test1')
                self.telaIntere.setImage(self.fotoComp[self.buttClick-7]) 
        except:
            pass
         
    def buttonCompra3(self):#-6
        try:

            tes=self.fotoComp[self.buttClick-6]
            tes=self.pegaCodCache(tes)
            if(tes!='unknown'):

                self.produto=tes
                self.abrirInter()
                self.telaIntere.lineEdit.setText()
                self.telaIntere.lineEdit_2.setText()
                self.telaIntere.lineEdit_3.setText()
                self.telaIntere.setImage(self.fotoComp[self.buttClick-6])
        except:
            pass
         
    def buttonCompra4(self):#-5
        try:
            tes=self.fotoComp[self.buttClick-5]
            tes=self.pegaCodCache(tes)
            self.produto=tes
            if(tes!='unknown'):

                self.abrirInter()
                self.telaIntere.lineEdit.setText()
                self.telaIntere.lineEdit_2.setText()
                self.telaIntere.lineEdit_3.setText()
                self.telaIntere.setImage(self.fotoComp[self.buttClick-5]) 
        except:
            pass
         
    def buttonCompra5(self):#-4
        try:

            tes=self.fotoComp[self.buttClick-4]
            tes=self.pegaCodCache(tes)
            if(tes!='unknown'):

                self.abrirInter()
                self.produto=tes
                self.telaIntere.lineEdit.setText()
                self.telaIntere.lineEdit_2.setText()
                self.telaIntere.lineEdit_3.setText()
                self.telaIntere.setImage(self.fotoComp[self.buttClick-4]) 
        except:
            pass
         
    def buttonCompra6(self):#-3
        try:
            tes=self.fotoComp[self.buttClick-3]
            tes=self.pegaCodCache(tes)
            if(tes!='unknown'):

                self.abrirInter()
                self.produto=tes
                self.telaIntere.lineEdit.setText()
                self.telaIntere.lineEdit_2.setText()
                self.telaIntere.lineEdit_3.setText()
                self.telaIntere.setImage(self.fotoComp[self.buttClick-3]) 
        except:
            pass
         
    def buttonCompra7(self):#-2
        try:
            tes=self.fotoComp[self.buttClick-2]
            tes=self.pegaCodCache(tes)
            if(tes!='unknown'):
                self.produto=tes
                self.abrirInter()
                self.telaIntere.lineEdit.setText()
                self.telaIntere.lineEdit_2.setText()
                self.telaIntere.lineEdit_3.setText()
                self.telaIntere.setImage(self.fotoComp[self.buttClick-2]) 
        except:
            pass
         
    def buttonCompra8(self):#-1
        try:

            tes=self.fotoComp[self.buttClick-1]
            tes=self.pegaCodCache(tes)
            if(tes!='unknown'):
                self.abrirInter()
                self.produto=tes
                self.telaIntere.lineEdit.setText()
                self.telaIntere.lineEdit_2.setText()
                self.telaIntere.lineEdit_3.setText()
                self.telaIntere.setImage(self.fotoComp[self.buttClick-1]) 
        except:
            pass
    def pegaCodCache(self,path):
        #path=path.split('$') 
        path=path.split('.')
        return path[0]
    def pegaFotos(self):
        
        fotoComp=[]
        #self.pasta =self.pasta+ './cache'
        print(getcwd())
        v=self.pasta.split('/cache')
        print(self.pasta)
        chdir(v[0])
        print('oi')
        #print(listdir('cache'))
        for c in listdir('cache'):
           
            fotoComp.append(c)
        chdir(self.pasta)
        return fotoComp
    def mostrarVendas(self):
        pass
    def mostrarCompras(self):
        pass
    def botaoInteres(self):
        pass
    def buttBack(self):
        if(self.buttClick>0&(self.buttClick-8)>=0):
            lista=[]
           
            for i in range(8,0,-1):
                try:
                    if(len(self.fotoComp)-i>=0):
                        lista.append(self.fotoComp[self.buttClick-(i)])
                    else:
                        lista.append('unknown.jpg')

                except:
                    lista.append('unknown.jpg')
            self.telaCompra.setImgens(lista,self.buttClick)  
            self.buttClick-=8
         
    def buttF(self):
        if(self.buttClick<len(self.fotoComp)):
            lista=[]

            for i in range(8):
                if(self.buttClick+i<len(self.fotoComp)):
                    lista.append(self.fotoComp[self.buttClick+i])
                    #print(self.fotoComp[i])
                else:
                    lista.append('unknown.jpg')
            self.buttClick+=8
            #self.coloca(lista,self.buttClick)
            self.telaCompra.setImgens(lista,self.buttClick)  
            #self.compra.setImgens(lista,self.buttClick)
            #self.TelaComprar.setImgens(lista,self.buttClick)
     
    def butComprar(self):
        pass
    def telaComp(self):
        print(getcwd())
        self.buttClick=0
        self.buttF()
        #self.telaCompra.setImagem(self.fotoComp)
        #TelaComprar.setImgens()
         
    def botaoCadastraMoto(self):
        numero_chassi = self.tela_cadastro_moto.Linechassi.text()
        modelo = self.tela_cadastro_moto.LineModelo.text()
        marca = self.tela_cadastro_moto.LineMarca.text()
        categoria = self.tela_cadastro_moto.LineCategoria.text()
        ano = self.tela_cadastro_moto.LineAno.text()
        valor = self.tela_cadastro_moto.LineValor.text()
        cpf_cnpj = self.tela_cadastro_moto.LineCPFVendedor.text()
        v=self.pasta.split('/cache')
        chdir(v[0])
        moto=Moto(numero_chassi,marca,categoria,ano,valor,modelo,cpf_cnpj)
        m=CadastroMoto()
        if not(numero_chassi == '' or modelo == '' or marca == '' or categoria == '' or ano == '' or valor == '' or cpf_cnpj == ''or len(self.fotos)==0):
            #self.pasta =self.pasta+ './cache'
            if (m.cadastra_moto(moto)):
                QMessageBox.information(None,'Sistema','Cadastro realizado com sucesso!')
                print(len(self.fotos))
                print(self.fotos)

                testeArqui.insertBLOB(moto._num_chas,moto._tipo,self.fotos[0])
                print(getcwd())
                chdir(self.pasta)
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
            QMessageBox.information(None,'Sistema','Campo vazio ou nenhuma foto selecionado!')
            #self.abrirHome()
        print(self.pasta)

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
        v=self.pasta.split('./cache')
        chdir(v[0])
        if not(nome == '' or endereco == '' or cpf == '' or dtnas == '' or senha == ''):
            p=Pessoa(nome,endereco,cpf,dtnas,senha)
            c=PessoaCadas()
            #self.pasta =self.pasta+ './cache'
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
        chdir(self.pasta)
    
    def botaoLogin(self):
        cpf_cnpj = self.tela_login.lineEdit.text()
        senha = self.tela_login.lineEdit_2.text()
        if not(cpf_cnpj == '' or senha == ''):
            v=self.pasta.split('/cache')
            chdir(v[0])
            c=PessoaCadas()
            self.contaLogada=c.busca_pess(cpf_cnpj)
            if self.contaLogada!=None:
                self.abrirMenu()
            else:
                QMessageBox.information(None,'Sistema','CPF não cadastrado')

        else:
            QMessageBox.information(None,'Sistema','Preecha todos os campos!')
        chdir(self.pasta)
    
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
        if(self.contaLogada!=None):
           # print(getcwd())
            
             
            self.telaComp()
            self.QtStack.setCurrentIndex(4)
        else:
            self.abrirLogin()
            if(self.contaLogada!=None):
                self.abrircompra()
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