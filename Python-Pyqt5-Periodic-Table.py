"""
kaynaklar zetcode qgridlayout, 17 signalslots


Geliştirme gunlüğü
periyodik tabloyu yapma fıkrı tamam bende var olan pyqt5 kodlarına bakmadan once
ınternette arasırma yaptım periodic isimli kutuphane var ama amacıma pek hızmet etmıyor ben ıse butona bastıgımda donen bır kart uygulması
taarzında yapacagım o kutuphanyeı butona tıkladgımda ekrana yazı yazdıran degıle arayyuze yazı yazdıran tarzzda kullanabılırım 
çalısmaya devam koda takılıp tum eğitim surecını aksatamam aklıma geldıkce yazmaya devam
https://pythonhosted.org/periodic/

19/11/2019: salı gunu: pıck kard kodlarını ıncelemeye devam
20/11/2019 çarsamba zip fonksıyonu sabah 9 oglen 14 arstırıldı donen değer non oldu sadece arastırmya devam bugnluk bu kadar
21/11/2019 zip fonksoynu daha ıyı arastırıldı strıng ler ıle ılgılı bıraz daha deneyım kazandım saat 01:20

22/11/2019 parwizin 21 ı random lcd generator rastgele tıkaldııgnda rsayı yazan element acılsın
parwizin cocları oncelemeye devam 13.00 16. arası deneme basarıszı sadece kodu nesne yonelımlı programlama mantıgına gore
cevırdım objectname bos donuyor...
22/11//2019 mehmet hoca saolsun qtoolbuton ornegı attı proje gelısım asamsına gecsınde saglam bır blog yazacam
ekranda gorme ıslemı tamamdır

buttonların setObjectname veya setText methodları uzerinden deger gireceksin
Qobject üzerinden de yapılabilirde ona hiç girmek istemiyorum karışık çünkü şöyle anlatayım olusturdugun Qobject nesnesi ile ile diziyi girersin fonksiyonda o nesnenin  methodu olur zaten qwidget da bir nesnen var ( ex = Example() dediğin yerde ki ex senin qwidgetten türettiğin nesne oluyor) o ex ile qobject nesnesi arasında signal slot yazıp butona tiklandiginda qobjectten listeden veriyi alıp ex nesnesi çıktı vermesi gerekiyor
Yani iki nesne arasında veri alışverişi olacak bunun için sinyal slot lazım sinyal slotta qobjectten tüketilmiş sınıflarla çalışır direk bir python nesnesi olustur çalışmaz zaten qwidget vs hepsi qobjectten turetilme

23/11/2019  saat 00:30 ekrana messagebox olusturmak daha mantıklı geldi devam
23/11/2019 saat 15:45 pyqt5 de normal buton ısmıne erısmek ıcın text yazısı kullanılır
#24/112019 14:29 json dosyasını mesaj kutusu ıcıne yazmam lazım 
 https://github.com/AlexGustafsson/molecular-data/blob/master/json/elements.json
bu dosyayı ıslemeye basladım oncelık json dosyası nasıl ıslenır ogrenmek   json dosya okuma da tamamdır :) 16:22
16:43 sonunda qlabel da eklendı
18:59 bu kısa projede burada bıter dıyelım :) gelıstırmeye acık

"""
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

        self.window = QWidget()#pencere
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

            self.button.setToolTip("Merhaba ben " + self.button.text() + " Elementi, Element Numaramı Tahmin edebilir misin?")#buton ustune gelınce verılcek yazı
            
            self.button.clicked.connect(self.consolebutton)
            self.button.clicked.connect(self.messageconnect)
            
            

        self.window.setLayout(grid)
        self.window.setStyleSheet("background-color: blue")
        self.window.setWindowTitle("PeriyodikTablo-Author-@bilalyasar07")

        self.window.showMaximized()#pencereyi max yapar
        self.window.show()
        sys.exit(app.exec())
    
    def consolebutton(self):
        self.button = self.sender()
        print("Tıkladığınız Element: " +  self.button.text())
    
    def messageconnect(self):
        self.messagebox = QMessageBox()
        self.messagebox.setWindowTitle("Element Bilgileri")#MESAJ KUTUSU BAŞLIGI
        self.messagebox.setText("Tıkladığınız Element: "  + self.button.text())#mesaj tıtle içerik

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
    window = Period()#( ex = Example() dediğin yerde ki ex senin qwidgetten türettiğin nesne oluyor)
    sys.exit(app.exec())






















"""
import json
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from PyQt5.QtWidgets import *

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.pencere = QWidget()
        izgara = QGridLayout()

        names = [
        "H","","","","","","","","","","","","","","","","","He",
        "Li","Be","","","","","","","","","","","B","C","N","O","F","Ne",
        "Na","Mg","","","","","","","","","","","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr",
        "Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er",
        "Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","T","l","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm",
        "Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Uub","Uut","Uuq","Uup","Uuh","Uus","Uuo"]

        positions = [(i,j) for i in range(9) for j in range(18)]
        global name
        for position, name in zip(positions, names):
            #print(name)
            if name == '':
                continue
            
            self.button = QPushButton(name,self)
            
            self.button.setStyleSheet("background-color: yellow")
            #qtoolbutton yapısı
            #self.button = QToolButton()
            #self.button.setText(name)
            ##button.setObjectName('Button%d' % name)
            #self.button.setObjectName(name)
            #print(name)
            #resultlist = list(name[0:3].split())
            #print(resultlist[0])
            

            izgara.addWidget(self.button, *position)
            #print(name, *position)

            self.button.setToolTip("Merhaba ben " + self.button.text() + " Elementi, Element Numaramı Tahmin edebilir misin?")#buton ustune gelınce verılcek yazı
            self.button.clicked.connect(self.buttonTiklandi)
            self.button.clicked.connect(self.messagebaglan)
            
  
        self.pencere.setLayout(izgara)
        self.pencere.setStyleSheet("background-color: green")
        
        self.pencere.setWindowTitle("PeriyodikTablo")
        #self.pencere.showMaximized()#pencereyi max yapar
        self.pencere.show()
        sys.exit(app.exec())
    
    def buttonTiklandi(self):
        print("buttonTiklandi")
        self.button = self.sender()
        print(self.button.text())#Hayır fonksiyonda da dediği gibi setText. 
        #Yani verdiğiniz parametreyi butonun textine koyar. 
        #Siz butonun textini almak istiyorsanız,
        #yapısını kullanmanız yeterli olacaktır.#ayrıca bana attığınız koddaki button, 
        #eğer benim buttonTiklandi fonksiyonunda yazdığım button ise self yapısını 
        #kullanmanıza gerek yok. Çünkü tanımladığımız button değişkeni o fonksiyonda kullanılacak sonrasında ihtiyacımız kalmayacak.     

    def messagebaglan(self):
        self.mesajkutusu = QMessageBox()
        self.mesajkutusu.setWindowTitle("Elementin Bilgileri")#MESAJ KUTUSU BAŞLIGI
        self.mesajkutusu.setText("Tıkladığınız Element" + " " + self.button.text())#mesaj tıtle içerik
        self.mesajkutusu.setInformativeText("MESAJ DETAY YAZISI")#mesaj detay yazısı
        
        #self.mesajkutusu.setDetailedText("DETAYLI BILGI VERILEN ALAN")#detaylı bılgı alanı
        #self.mesajkutusu.setIcon(QMessageBox.Critical)
        #self.mesajkutusu.setStandardButtons(QMessageBox.Yes | QMessageBox.No ) #(QMessageBox.Yes | QMessageBox.No | QMessageBox.Close)
        self.mesajkutusu.buttonClicked.connect(self.uygula)
        self.mesajkutusu.exec()

    def uygula(self,q):
        print("Kullanıcının tıkladıgı button : {}".format(q.text()))
        
if __name__ == '__main__':
    app=QApplication(sys.argv)
    pencere = Pencere()#( ex = Example() dediğin yerde ki ex senin qwidgetten türettiğin nesne oluyor)
    sys.exit(app.exec())
"""





























"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from PyQt5.QtWidgets import *

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
    def setUI(self):

        self.pencere = QWidget()
        izgara = QGridLayout()

        names = [
        "H","","","","","","","","","","","","","","","","","He",
        "Li","Be","","","","","","","","","","","B","C","N","O","F","Ne",
        "Na","Mg","","","","","","","","","","","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr",
        "Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er",
        "Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","T","l","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm",
        "Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Uub","Uut","Uuq","Uup","Uuh","Uus","Uuo"]


        positions = [(i,j) for i in range(9) for j in range(18)]
        global name
        for position, name in zip(positions, names):
            #print(name)
            if name == '':
                continue
            
            #self.button = QPushButton(name,self)
            self.button = QToolButton()

            #self.button.minimumSizeHint()
            self.button.setText(name)
            #button.setObjectName('Button%d' % name)
            self.button.setObjectName(name)
            #print(name)
            #resultlist = list(name[0:3].split())
            #print(resultlist[0])
            

            izgara.addWidget(self.button, *position)
            #print(name, *position)

            self.button.setToolTip('Merhaba ben ... Numaramı Tahmin edebilir misin?')
            #self.button.clicked.connect(self.buttonTiklandi)
            self.button.clicked.connect(self.messagebaglan)
            
  
        self.pencere.setLayout(izgara)
        self.pencere.setWindowTitle("PeriyodikTablo")
        self.pencere.showMaximized()#pencereyi max yapar
        self.pencere.show()
        sys.exit(app.exec())
    
    #def buttonTiklandi(self):
    #    print("buttonTiklandi")
    #    button = self.sender()
    #    self.button.setText('%s Clicked!' % str(button.objectName()))
    #    print(self.button.setText('%s Clicked!' % button.objectName()))
        

    def messagebaglan(self):
        self.mesajkutusu = QMessageBox()
        self.mesajkutusu.setWindowTitle("Tıkladığınız Elementın Bilgiler")#MESAJ KUTUSU BAŞLIGI
        self.mesajkutusu.setText("Tıkladığınız Element")#mesaj tıtle
        self.mesajkutusu.setInformativeText("MESAJ DETAY YAZISI")#mesaj detay yazısı
        #mesaj kutu baslıgı
        self.mesajkutusu.setDetailedText("DETAYLI BILGI VERILEN ALAN")#detaylı bılgı alanı
        self.mesajkutusu.setIcon(QMessageBox.Critical)
        self.mesajkutusu.setStandardButtons(QMessageBox.Yes | QMessageBox.No ) #(QMessageBox.Yes | QMessageBox.No | QMessageBox.Close)
        self.mesajkutusu.buttonClicked.connect(self.uygula)
        self.mesajkutusu.exec()

    def uygula(self,q):
        print("Kullanıcının tıklafıgı button : {}".format(q.text()))
        

if __name__ == '__main__':
    app=QApplication(sys.argv)
    pencere = Pencere()#( ex = Example() dediğin yerde ki ex senin qwidgetten türettiğin nesne oluyor)
    sys.exit(app.exec())
"""
























"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from PyQt5.QtWidgets import *

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
    def setUI(self):

        self.pencere = QWidget()
        izgara = QGridLayout()
        mesajkutusu = QMessageBox()
        
        
        
        
        names = [
        "H","","","","","","","","","","","","","","","","","He",
        "Li","Be","","","","","","","","","","","B","C","N","O","F","Ne",
        "Na","Mg","","","","","","","","","","","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr",
        "Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er",
        "Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","T","l","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm",
        "Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Uub","Uut","Uuq","Uup","Uuh","Uus","Uuo"]


        positions = [(i,j) for i in range(9) for j in range(18)]
        global name
        for position, name in zip(positions, names):
            #print(name)
            if name == '':
                continue
            
            #self.button = QPushButton(name,self)
            self.button = QToolButton()
            self.button.setText(name)
            #button.setObjectName('Button%d' % name)
            self.button.setObjectName(name)
            #print(name)

            #resultlist = list(name[0:3].split())
            #print(resultlist[0])
            

            izgara.addWidget(self.button, *position)
 
            #print(name, *position)
            #b = list(a)
            #print(b)
            #a = list(name,*position)

            #translist = izgara.addWidget()
            #print(name,*position)
            
            #print(name)

            self.button.setToolTip('Merhaba ben ... Numaramı Tahmin edebilir misin?')
            self.button.clicked.connect(self.buttonTiklandi)
            
  
        self.pencere.setLayout(izgara)
        self.pencere.setWindowTitle("PyQt5-PeriyodikTablo")
        #self.pencere.showMaximized()#pencereyi max yapar
        self.pencere.show()
        sys.exit(app.exec())
     
    def buttonTiklandi(self):

        print("buttonTiklandi")
        button = self.sender()
        self.button.setText('%s Clicked!' % str(button.objectName()))
        print(self.button.setText('%s Clicked!' % button.objectName()))
        
        #self.status_label.setText('%s Clicked!' % str(sending_button.objectName()))
        #print(self.button.setText())
        #print(self.button.objectName())
        #print(self.button.sender())
      

if __name__ == '__main__':
    app=QApplication(sys.argv)
    pencere = Pencere()#( ex = Example() dediğin yerde ki ex senin qwidgetten türettiğin nesne oluyor)
    sys.exit(app.exec())
"""








"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        grid = QGridLayout()
        self.setLayout(grid)
        names = ["cl", "back", "", "close",
                    "7","8","9", "/",
                    "4","5","6","-",
                    "1","2","3","+",
                    "0",".","=","*"]
        positions = [(i,j) for i in range(5) for j in range(4)]
        for position, name in zip(positions, names):

           #print(name)

            if name == '':
               continue
            button = QPushButton(name)
            #print(name)
            grid.addWidget(button, *position)
            button.clicked.connect(self.buttonTiklandi)

        self.show()
    def buttonTiklandi(self):
        print("buttonTiklandi")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


"""















"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
def pencere():
    app = QApplication(sys.argv)
    pencere = QWidget()
    izgara = QGridLayout()
    
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
        
        button = QPushButton(name)
        #print(name)

        global resultlist
        resultlist = list(name[0:3].split())
        print(resultlist[0])

        izgara.addWidget(button, *position)
        
        #print(name, *position)
        #b = list(a)
        #print(b)
        #a = list(name,*position)

        #translist = izgara.addWidget()
        #print(name,*position)
        
        #print(name)

        button.setToolTip('Merhaba ben ... Numaramı Tahmin edebilir misin?')
        button.clicked.connect(buttonTiklandi)
        
        #her element ıcın aytı yap
        #buton uzerıne gelınce verilcek bilgi 

        label = QLabel(pencere, text="Modern Periyodik Tablo  !")
        label.move(400, 100)
        
        #setCentralWidget(label)
        #label.setCentralWidget(label)    
        #label = QLabel(pencere, text='UserName')
        #label.setAlignment(Qt.AlignCenter)#anlık çalısmadı

        #global ulasliste
        #ulasliste = []
        #ulasliste.append(resultlist)
        #print(ulasliste)
   
    pencere.setLayout(izgara)
    pencere.setWindowTitle("PyQt5-PeriyodikTablo")
    #pencere.showMaximized()#pencereyi max yapar
    pencere.show(),
    sys.exit(app.exec())

def buttonTiklandi():
  print("buttonTiklandi")
  print(button.setText(""))
  

if __name__ == '__main__':
    pencere()
"""
    










"""
from PyQt5 import QtCore, QtGui, QtWidgets
import time  # Used to simulate the progress in the progressbar
import numpy as np  # Used to generabte a permutation
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import re 
import sys


def pencere():
  app = QApplication(sys.argv)
 
  pencere = QWidget()
  izgara = QGridLayout()

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
    
    button = QPushButton(name)
    #print(name)
    izgara.addWidget(button, *position)
    print(name,*position)

    button.clicked.connect(buttonTiklandi)

    #label = QLabel(pencere, text='UserName')
    #label.move(400, 100)
    #label.setAlignment(Qt.AlignCenter)#anlık çalısmadı

  pencere.setLayout(izgara)
  pencere.setWindowTitle("PyQt5-PeriyodikTablo")
  #pencere.showMaximized()#pencereyi max yapar
  pencere.show()
  sys.exit(app.exec())

def buttonTiklandi():
  print("buttonTiklandi")
  print(name,*position)
  #button = QPushButton()
  print(QPushButton())
  #button.setToolTip(setText='butonun üzerine gelince verilecek bilgi')

if __name__ == "__main__":
  pencere()
"""




"""
import sys
from PyQt5 import QtWidgets,QtGui
class pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.asdasd()

    def asdasd(self):
        self.yazialani =  QtWidgets.QLabel("Henüz hiç tıklanmadu...")
        self.button = QtWidgets.QPushButton("TIkla")
        self.say = 0
        self.show()
    layout = QtWidgets.QVBoxLayout(self)
    layout.addWidget(self.yazialani)
    layout.addWidget(self.button)
    self.setLayout(layout)   
app = QtWidgets.QApplication(sys.argv)
pencere = pencere()
sys.exit(app.exec_())
"""



"""  
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(object):
    def setupUi(self, MainFrame):
        MainFrame.setObjectName("MainFrame")
        MainFrame.resize(870, 230)
        MainFrame.setFrameShape(QFrame.Box)

        self.Function1Button = QPushButton(MainFrame)
        #I want to go Function 1's frame with this button
        self.Function1Button.clicked.connect(????)
        self.Function2Button = QPushButton(MainFrame)
        #I want to go Function 2's frame with this button
        self.Function2Button.clicked.connect(????)

class Function1(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(870, 230)

        self.BackButton = QPushButton(MainFrame)
        # I want to go previous frame with this button
        self.BackButton.clicked.connect(????)
        self.Function2Button = QPushButton(MainFrame)
        #I want to go Function 2's frame with this button
        self.Function2Button.clicked.connect(????)
        self.ExecuteButton = QPushButton(MainFrame)
        self.ExecuteButton.clicked.connect(self.runfunc)

    def runfunc(self):
        # Computations

class Function2(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(870, 230)

        self.BackButton = QPushButton(MainFrame)
        self.BackButton.clicked.connect(????)
        self.Function1Button = QPushButton(MainFrame)
        #I want to go Function 1's frame with this button
        self.Function1Button.clicked.connect(????)
        self.ExecuteButton = QPushButton(MainFrame)
        self.ExecuteButton.clicked.connect(self.runfunc)

    def runfunc(self):
        # Computations
"""

"""
class App(QWidget):

    def __init__(self):
        super().__init__()

        self.title = 'Pencerem'
        self.left = 300
        self.top = 300
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.butonum = QPushButton('bu butona henüz basılmadı', self)
        self.butonum.setToolTip('butonun üzerine gelince verilecek bilgi')
        self.butonum.move(100, 70)
        self.butonum.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        self.butonum.setText("Butona basıldı")
        print('butona basıldı')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
"""
"""
#buton ısmı değiştirme
from PyQt5 import QtCore, QtGui, QtWidgets
import time  # Used to simulate the progress in the progressbar
import numpy as np  # Used to generabte a permutation
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import re 
import sys
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Pencerem'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)

        self.butonum = QPushButton('bu butona henüz basılmadı', self)
        self.butonum.setToolTip('butonun üzerine gelince verilecek bilgi')
        self.butonum.move(100, 70)
        self.butonum.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        self.butonum.setText("Butona basıldı")
        print('butona basıldı')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
"""
 




#def mendeleiev_table ():
#  """Returns the mendeleiev table as a python list of lists.
#     Each cell contains either None or a pair (symbol, atomic number),
#     or a list of pairs for the cells * and **.
#  """
#  import re 
#  L =[(e ,i +1 )for (i ,e )in enumerate (
#   re .compile ("[A-Z][a-z]*").findall ("""
#    HHeLiBeBCNOFNeNaMgAlSiPSClArKCaScTiVCrMnFeCoNiCuZnGaGeAsSeBrKr
#    RbSrYZrNbMoTcRuRhPdAgCdInSnSbTeIXeCsBaLaCePrNdPmSmEuGdTbDyHoEr
#    TmYbLuHfTaWReOsIrPtAuHgTlPbBiPoAtRnFrRaAcThPaUNpPuAmCmBkCfEsFm
#    MdNoLrRfDbSgBhHsMtDsRgUubUutUuqUupUuhUusUuo"""))]
#  for i ,j in ((88 ,103 ),(56 ,71 )):
#    L [i ]=L [i :j ]
#    L [i +1 :]=L [j :]
#  for i ,j in ((12 ,10 ),(4 ,10 ),(1 ,16 )):
#    L [i :i ]=[None ]*j 
#  return [L [18 *i :18 *(i +1 )]for i in range (7 )]
#
#print(mendeleiev_table())