# Довженко Віталій
# Лабораторна робота №1
# Розробити додаток, що обчислює площу трикутника за формулою Герона.

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.uic import loadUi

from math import sqrt
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        loadUi("Lab1_view.ui", self)

        # Here I used validator to avoid a non-integer values.
        #
        # Тут я використав валідатор аби уникнути введення
        # значень не чисельних типів.
        self.lineEdit.setValidator(QIntValidator(1, 999))
        self.lineEdit_2.setValidator(QIntValidator(1, 999))
        self.lineEdit_3.setValidator(QIntValidator(1, 999))

        # Call function btnClicked by clicking on the button.
        #
        # Виклик функції btnClicked при натискані кнопки.
        self.pushButton.clicked.connect(self.btnClicked)

        # Call function clear_btnClicked which clears cells.
        #
        # Виклик функції clear_btnClicked, яка очищає комірки від значень.
        self.pushButton_2.clicked.connect(self.clear_btnClicked)

    def btnClicked(self):
        a = self.lineEdit.text()
        b = self.lineEdit_2.text()
        c = self.lineEdit_3.text()

        # Heron`s formula
        #
        # Формула герона
        p = (int(a) + int(b) + int(c)) / 2
        try:
            ans = sqrt(p * (p-int(a))*(p-int(b))*(p-int(c)))
        except ValueError:
            self.label_5.setText("Doesn`t exist!")
        else:
            self.label_5.setText(str(ans))

    def clear_btnClicked(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
