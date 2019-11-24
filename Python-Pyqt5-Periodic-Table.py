import json
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from PyQt5.QtWidgets import *


class Period(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
    
    def setUI(self):

        self.window = QWidget()
        grid = QGridLayout()
       
        names = [
        "H","","","","","","","","","","","","","","","","","He",
        "Li","Be","","","","","","","","","","","B","C","N","O","F","Ne",
        "Na","Mg","","","","","","","","","","","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr",
        "Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er",
        "Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","T","l","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm",
        "Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Uub","Uut","Uuq","Uup","Uuh","Uus","Uuo"]

        positions = [(i,j) for i in range(9) for j in range(18)]
        for position, name in zip(positions, names):
            #print(name)
            if name == '':
                continue
            
            self.button = QPushButton(name,self)
            self.button.setStyleSheet("background-color: dark")
            self.button.setFont(QFont("Century Gothic",18))
            grid.addWidget(self.button, *position)
            #print(name, *position)

            self.button.setToolTip("Merhaba ben " + self.button.text() + " Elementi, Element Numaramı Tahmin edebilir misin?")
            self.button.clicked.connect(self.consolebutton)
            self.button.clicked.connect(self.messageconnect)
            
            

        self.window.setLayout(grid)
        self.window.setStyleSheet("background-color: blue")
        self.window.setWindowTitle("PeriyodikTablo-Author-@bilalyasar07")

        self.window.showMaximized()
        self.window.show()
        sys.exit(app.exec())
    
    def consolebutton(self):
        self.button = self.sender()
        print("Tıkladığınız Element: " +  self.button.text())
    
    def messageconnect(self):
        self.messagebox = QMessageBox()
        self.messagebox.setWindowTitle("Element Bilgileri")
        self.messagebox.setText("Tıkladığınız Element: "  + self.button.text())

        with open("elements.json") as f:
            data = json.load(f)

        for element in data:
            if self.button.text() == element["symbol"]:

                number = element["number"]
                symbol = element["symbol"]
                name = element["name"]
                mass = element["mass"]
                standardState = element["standardState"]
                bondingType = element["bondingType"]
                family = element["family"]
                yearDiscovered = element["yearDiscovered"]
                print(number,symbol, name, mass, standardState, bondingType, family, yearDiscovered)

                #mesajdetayyazısı
                self.messagebox.setInformativeText(str(" Number: {}\n Symbol: {}\n Name: {}\n Mass: {}\n StandardState: {}\n BondingType: {}\n Family: {}\n YearDiscovered: {}"
                    .format(number,symbol,name,mass,standardState,bondingType,family,yearDiscovered)))

                self.messagebox.exec()
        
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = Period()
    sys.exit(app.exec())