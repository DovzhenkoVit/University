from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.uic import loadUi
from math import sqrt
# Импортируем наш шаблон.
from Lab1_view import Ui_MainWindow



import sys


#def _herons_formula(a, b, c):
 #       p = (int(a) + int(b) + int(c)) / 2
  #      return str(sqrt(p * (p-int(a))*(p-int(b))*(p-int(c))))
 

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        loadUi("Lab1_view.ui", self)
        #self.ui = Ui_MainWindow()
        #self.ui.setupUi(self)

        self.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        
        self.lineEdit.setValidator(QIntValidator(1, 999))
        a = self.lineEdit.text()
        self.lineEdit_2.setValidator(QIntValidator(1, 999))
        b = self.lineEdit_2.text()
        self.lineEdit_3.setValidator(QIntValidator(1, 999))
        c = self.lineEdit_3.text()

        ans = int(a) * 2

        print(ans)
        #self.ui.label_5.setText("4")
        self.label_5.setText(str(ans))
        #self.ui.textBrowser.adjustSize()

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())
