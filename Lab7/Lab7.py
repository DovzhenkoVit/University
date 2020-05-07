# Довженко Віталій
# Лабораторна робота №6
# 

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer, QEventLoop, QThread
import sys
from random import sample, randint
# from time import sleep


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(__class__, self).__init__()
        loadUi("Lab7_view.ui", self)

        self.btn_ClickMe.clicked.connect(self.btnClickMeClicked)
        self.btn_Faster.clicked.connect(self.btnFasterClicked)

        

        self.btn_Exit.clicked.connect(self.btnExitClicked)

        self.thread = QThread()
        self.btn_Slower.clicked.connect(self.thread.start)
        self.thread.started.connect(self.func) # when thread starts, start worker
        # self.thread.finished.connect(self.worker.stop) # when thread finishes, stop worker        
        # self.loop = QEventLoop()
        # self.timer = QTimer(self)
        # def _inn(self):
        #     x = randint(10, 450)
        #     y = randint(10, 150)

        #     return self.btn_ClickMe.move(x, y)
        # _inn(self)

        # self.timer.start(100)
        # self.loop.exec_()


    def func(self):

        while True:   
            x = randint(10, 450)
            y = randint(10, 150)
            self.btn_ClickMe.move(x, y)
            print("rwtest")
            QThread.sleep(1)

    def btnClickMeClicked(self):
        pass

    def btnFasterClicked(self):
        # timer = QTimer()
        # loop = QEventLoop()
        # loop.exec_()
        # def _inn(self):
        #     x = randint(10, 450)
        #     y = randint(10, 150)

        #     return self.btn_ClickMe.move(x, y)

        # timer.start(1)
        pass

    def btnSlowerClicked(self):
        # loop = QEventLoop()
        # timer = QTimer()
        # timer.setSingleShot(True)
        # timer.timeout.connect(loop.quit)
        # timer.start(1)
        # while True:   
        #     x = randint(10, 450)
        #     y = randint(10, 150)
        #     self.btn_ClickMe.move(x, y)
        #     QThread.sleep(1)
        # loop.exec_()
        pass

    def btnExitClicked(self):
        sys.exit(app.exec())

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
