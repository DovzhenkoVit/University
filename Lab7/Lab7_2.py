import sys
from PyQt5.QtWidgets import (QWidget,
                             QPushButton, QApplication, QGridLayout)
from PyQt5.QtCore import QThread, QObject


class Worker(QObject):

    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)

    def do_work(self):
        i = 1
        while True:
            print(i)
            QThread.sleep(1)
            i = i + 1

    def stop(self):
        print("stopped")
        self.deleteLater() # How do I stop it?


class Gui(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # Buttons:
        self.btn_start = QPushButton('Start')
        self.btn_start.resize(self.btn_start.sizeHint())
        self.btn_start.move(50, 50)
        self.btn_stop = QPushButton('Stop')
        self.btn_stop.resize(self.btn_stop.sizeHint())
        self.btn_stop.move(150, 50)

        # GUI title, size, etc...
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('ThreadTest')
        self.layout = QGridLayout()
        self.layout.addWidget(self.btn_start, 0, 0)
        self.layout.addWidget(self.btn_stop, 0, 50)
        self.setLayout(self.layout)

        # Thread:
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.do_work) # when thread starts, start worker
        self.thread.finished.connect(self.worker.stop) # when thread finishes, stop worker

        # Start Button action:
        self.btn_start.clicked.connect(self.thread.start)

        # Stop Button action:
        self.btn_stop.clicked.connect(self.stop_thread)

        self.show()

    # When stop_btn is clicked this runs. Terminates the worker and the thread.
    def stop_thread(self):
        print("It should stop printing numbers now and not crash")
        self.worker.disconnect()
        self.thread.terminate()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Gui()
    sys.exit(app.exec_())