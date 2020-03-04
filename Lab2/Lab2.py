# Довженко Віталій
# Лабораторна робота №2
# Розрахувати значення x, визначивши і використавши відповідну функцію

from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

from math import sqrt
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(__class__, self).__init__()
        loadUi("Lab2_view.ui", self)

        self.pushButton.clicked.connect(self.btnClicked)

    @staticmethod
    def my_formula(a):
        return (sqrt(a) + a) / 2

    def btnClicked(self):
        a = mywindow.my_formula(7)
        b = mywindow.my_formula(14)
        c = mywindow.my_formula(24)
        ans = a + b + c

        self.ans_label.setText(str(ans))


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
