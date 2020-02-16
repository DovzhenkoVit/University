from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.uic import loadUi
from math import sqrt
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        loadUi("Lab1_view.ui", self)
        self.lineEdit.setValidator(QIntValidator(1, 999))
        self.lineEdit_2.setValidator(QIntValidator(1, 999))
        self.lineEdit_3.setValidator(QIntValidator(1, 999))
        self.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        #self.lineEdit.setValidator(QIntValidator(1, 999))
        a = self.lineEdit.text()
        #self.lineEdit_2.setValidator(QIntValidator(1, 999))
        b = self.lineEdit_2.text()
        #self.lineEdit_3.setValidator(QIntValidator(1, 999))
        c = self.lineEdit_3.text()

        p = (int(a) + int(b) + int(c)) / 2
        ans = sqrt(p * (p-int(a))*(p-int(b))*(p-int(c)))

        self.label_5.setText(str(ans))


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
