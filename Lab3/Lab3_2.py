# Довженко Віталій
# Лабораторна робота №3_2
# 

from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(__class__, self).__init__()
        loadUi("Lab3_2_view.ui", self)

        self.horizontalSlider.valueChanged.connect(self.sliderValue)
        self.spinBox.valueChanged.connect(self.spinValue)

    def sliderValue(self):
        self.progressBar.setValue(self.horizontalSlider.value())
        self.spinBox.setValue(self.horizontalSlider.value())

    def spinValue(self):
        self.progressBar.setValue(self.spinBox.value())
        self.horizontalSlider.setValue(self.spinBox.value())


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
