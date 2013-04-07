#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'

import sys
#from os import path, curdir
from PyQt4 import  QtGui, QtCore, uic
Form, Base = uic.loadUiType("pyqt3.ui")

class MyClass():
    def __init__(self, x=0):
        self.x = x
    def __call__(self):
        print("Кнопка нажата. Метод MyClass.__call__()")
        print("x =", self.x)
    def on_clicked(self):
        print("Кнопка нажата. Метод MyClass.on_clicked()")
    """
    def editing_finished():
        print("Кнопка нажата. Метод get_text1.on_clicked()")
        #zz  = QtGui.QMainWindow.__init__.lineEdit.text()
        #print("zz = ", zz)
    """
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
        self.lineEdit1.setToolTip("Введите что нибудь")
        self.lineEdit1.setPlaceholderText("Введите Бяку")
        self.lineEdit2.setPlaceholderText("Введите Бяку")
        def find():
            """поиск и вывод синонима"""
            word = self.lineEdit.text()
            #result = ''
            print("word = ", word)
        QtCore.QObject.connect(self.lineEdit1, QtCore.SIGNAL("returnPressed()"), find)


if __name__ == "__main__":
    import sys
    obj = MyClass()
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
