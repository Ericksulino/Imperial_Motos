# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro_moto.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Cad_moto(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(613, 512)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 131, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 67, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 220, 81, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 270, 67, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 320, 67, 17))
        self.label_7.setObjectName("label_7")
        self.Linechassi = QtWidgets.QLineEdit(self.centralwidget)
        self.Linechassi.setGeometry(QtCore.QRect(170, 70, 181, 25))
        self.Linechassi.setObjectName("Linechassi")
        self.LineModelo = QtWidgets.QLineEdit(self.centralwidget)
        self.LineModelo.setGeometry(QtCore.QRect(170, 120, 181, 25))
        self.LineModelo.setObjectName("LineModelo")
        self.LineMarca = QtWidgets.QLineEdit(self.centralwidget)
        self.LineMarca.setGeometry(QtCore.QRect(170, 170, 181, 25))
        self.LineMarca.setObjectName("LineMarca")
        self.LineCategoria = QtWidgets.QLineEdit(self.centralwidget)
        self.LineCategoria.setGeometry(QtCore.QRect(170, 220, 181, 25))
        self.LineCategoria.setObjectName("LineCategoria")
        self.LineAno = QtWidgets.QLineEdit(self.centralwidget)
        self.LineAno.setGeometry(QtCore.QRect(170, 270, 181, 25))
        self.LineAno.setObjectName("LineAno")
        self.LineValor = QtWidgets.QLineEdit(self.centralwidget)
        self.LineValor.setGeometry(QtCore.QRect(170, 320, 181, 25))
        self.LineValor.setObjectName("LineValor")
        self.LineCPFVendedor = QtWidgets.QLineEdit(self.centralwidget)
        self.LineCPFVendedor.setGeometry(QtCore.QRect(170, 370, 181, 25))
        self.LineCPFVendedor.setObjectName("LineCPFVendedor")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 370, 171, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(420, 50, 67, 17))
        self.label_9.setObjectName("label_9")
        self.ButtoAnunciar = QtWidgets.QPushButton(self.centralwidget)
        self.ButtoAnunciar.setGeometry(QtCore.QRect(40, 430, 89, 25))
        self.ButtoAnunciar.setObjectName("ButtoAnunciar")
        self.buttonVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.buttonVoltar.setGeometry(QtCore.QRect(260, 430, 89, 25))
        self.buttonVoltar.setObjectName("buttonVoltar")
        self.ButtonImagem = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonImagem.setGeometry(QtCore.QRect(420, 70, 101, 31))
        self.ButtonImagem.setObjectName("ButtonImagem")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Informações do veiculo"))
        self.label_2.setText(_translate("MainWindow", "Número do chassi:"))
        self.label_3.setText(_translate("MainWindow", "Modelo:"))
        self.label_4.setText(_translate("MainWindow", "Marca:"))
        self.label_5.setText(_translate("MainWindow", "Categoria:"))
        self.label_6.setText(_translate("MainWindow", "Ano:"))
        self.label_7.setText(_translate("MainWindow", "Valor:"))
        self.label_8.setText(_translate("MainWindow", "CPF/CNPJ do vendedor:"))
        self.label_9.setText(_translate("MainWindow", "Imagens:"))
        self.ButtoAnunciar.setText(_translate("MainWindow", "Anunciar"))
        self.buttonVoltar.setText(_translate("MainWindow", "Voltar"))
        self.ButtonImagem.setText(_translate("MainWindow", "Selecionar imagem"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Cad_moto()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())