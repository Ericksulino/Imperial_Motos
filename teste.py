import sys
from PyQt5 import QtWidgets
   

class Test(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.buttonA = QtWidgets.QPushButton('Click!', self)
        self.buttonB = QtWidgets.QPushButton('Click!', self)
        self.buttonA.clicked.connect(self.clickCallback)
        self.buttonA.move(100, 50)
        self.buttonB.clicked.connect(self.clickCallback)
        self.buttonB.move(200, 50)

        self.labelA = QtWidgets.QLabel(self)
        self.labelA.move(110, 100)

        self.setGeometry(100, 100, 300, 200)

    def clickCallback(self):
        print(self.buttonB.click)
        if(self.buttonA.clicked):
            print('a')

            self.labelA.setText(" ")

            self.labelA.setText("Button is A clicked")
        else:
            if(self.buttonB.clicked):
                print('b')
                self.labelA.setText(" ")
                self.labelA.setText("Button is B clicked")
            
'''
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    test = Test()
    test.show()
    sys.exit( app.exec_() )'''
'''for i in range(8,0,-1):
    print(i)'''
path="Prototipo\Imperial_Motos\cache\-asd.jpg"
print(path)
path=path.split('-')
path=path[1].split('.')
print(path[0])