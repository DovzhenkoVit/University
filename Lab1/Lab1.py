from PyQt5 import QtWidgets
from math import sqrt
# Импортируем наш шаблон.
from Lab1_view import Ui_MainWindow
 
import sys


def _herons_formula(a, b, c):
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):

        def _herons_formula(a, b, c):
            p = (a + b + c) / 2
            return sqrt(p * (p-a)*(p-b)*(p-c))

        a = self.ui.lineEdit.text().setValidator("009")
        b = self.ui.lineEdit_2.text()
        
        
        #self.ui.label_5.setText("4")
        self.ui.label_5.setText(a)
        #self.ui.textBrowser.adjustSize()

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())
