# Довженко Віталій
# Лабораторна робота №3
# 

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi

import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(__class__, self).__init__()
        loadUi("Lab3_view.ui", self)

        self.pushButton.clicked.connect(
            lambda: self.btnClicked(self.checkBox.isChecked())
            )

    def btnClicked(self, chk):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        if chk and self.radioButton.isChecked():
            msg.setText("First notification")
            msg.exec()
        elif chk and self.radioButton_2.isChecked():
            msg.setText("Second notification")
            msg.exec()
        elif chk and self.radioButton_3.isChecked():
            msg.setText("Third notification")
            msg.exec()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
