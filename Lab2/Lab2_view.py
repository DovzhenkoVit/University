# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lab2_view.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 452)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.f_label = QtWidgets.QLabel(self.centralwidget)
        self.f_label.setGeometry(QtCore.QRect(60, 90, 351, 71))
        self.f_label.setText("")
        self.f_label.setPixmap(QtGui.QPixmap("formula.png"))
        self.f_label.setAlignment(QtCore.Qt.AlignCenter)
        self.f_label.setObjectName("f_label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 40, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 210, 131, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 300, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ans_label = QtWidgets.QLabel(self.centralwidget)
        self.ans_label.setGeometry(QtCore.QRect(190, 300, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ans_label.setFont(font)
        self.ans_label.setText("")
        self.ans_label.setObjectName("ans_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Розрахувати значення x"))
        self.pushButton.setText(_translate("MainWindow", "Обчислити"))
        self.label_2.setText(_translate("MainWindow", "Результат"))
