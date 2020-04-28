# Довженко Віталій
# Лабораторна робота №6
# 

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi

import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(__class__, self).__init__()
        loadUi("Lab6_view.ui", self)

        self.button_Add.clicked.connect(self.btnAddClicked)
        self.button_Remove.clicked.connect(self.btnRemoveClicked)
        self.button_RemAll.clicked.connect(self.btnRemAllClicked)
        self.button_Buy.clicked.connect(self.btnBuyClicked)


    def btnAddClicked(self):
        self.listOrder.addItem(self.listMenu.currentItem().text())

    def btnRemoveClicked(self):
    	self.listOrder.takeItem(self.listOrder.currentRow())

    def btnRemAllClicked(self):
        self.listOrder.clear()

    def btnBuyClicked(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Смачного")
        msg.exec()

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
