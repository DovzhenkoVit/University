# Довженко Віталій
# Лабораторна робота №2
# Розрахувати значення x, визначивши і використавши відповідну функцію

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi

from math import sqrt
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(__class__, self).__init__()
        loadUi("Lab2_view.ui", self)

        self.pushButton.clicked.connect(
            lambda: self.btnClicked(self.checkBox.isChecked())
            )

    @staticmethod
    def my_formula(a):
        return (sqrt(a) + a) / 2

    def btnClicked(self, chk):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        if chk:
            a = mywindow.my_formula(7)
            b = mywindow.my_formula(14)
            c = mywindow.my_formula(24)
            ans = a + b + c
            msg.setText("Результат = " + str(round(ans, 2)))
            msg.exec()
            self.ans_label.setText(str(round(ans, 2)))
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Заборонений показ результату")
            msg.exec()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
