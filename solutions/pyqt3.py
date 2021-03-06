#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'

import sys
#from os import path, curdir
from PyQt4 import  QtGui, QtCore, uic
Form, Base = uic.loadUiType("pyqt3.ui")
class MyWindow(QtGui.QMainWindow, Form):
    def __init__(self, parent=None):
        """


        :type self: object MainWindow
        :param parent:
        """
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.pushButton, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit)
        self.pushButton.setToolTip("Нажав эту кнопку покидаем программу")
        #self.setToolTip("Главное Окно")
        #tab = self.tabWidget
        self.lineEdit1.setToolTip("Введите что нибудь")
        self.lineEdit1.setPlaceholderText("Введите Бяку")
        self.lineEdit2.setPlaceholderText("Введите Бяку")

        def lineedit1():
            word = self.lineEdit1.text()
            self.label1.setText("<b>"+word+"<b>")
            print("word = ", word)
        def lineedit2():
            word2 = self.lineEdit2.text()
            print("word = ", word2)

        QtCore.QObject.connect(self.lineEdit1, QtCore.SIGNAL("returnPressed()"), lineedit1)
        QtCore.QObject.connect(self.pushButton1, QtCore.SIGNAL("clicked()"), lineedit1)
        QtCore.QObject.connect(self.lineEdit2, QtCore.SIGNAL("returnPressed()"), lineedit2)
        QtCore.QObject.connect(self.pushButton2, QtCore.SIGNAL("clicked()"), lineedit2)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
