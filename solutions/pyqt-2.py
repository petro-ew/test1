#!/usr/bin/env python3
__author__ = 'petro-ew'
import sys
from PyQt4 import QtGui, QtCore, uic, Qt

Form, Base = uic.loadUiType("1-06-04-13.ui")

def on_clicked():

    print("Кнопка нажата. Функция on_clicked()")

def editing_finished():
    print ("Editing Finished Закончили редактировать Едит")


class MyClass():
    def __init__(self, x=0):
        self.x = x
    def __call__(self):
        print("Кнопка нажата. Метод MyClass.__call__()")
        print("x =", self.x)
    def on_clicked(self):
        print("Кнопка нажата. Метод MyClass.on_clicked()")
    def editing_finished():
        print("Кнопка нажата. Метод get_text1.on_clicked()")

class get_text1():

    def __init__(self, y=0):
       # self.y = "xx"
        self.y = str(y)
    def __call__(self):
        print("Кнопка нажата. Метод get_text1.__call__()")
        print("y =", self.y)
    def editing_finished():
        print("Кнопка нажата. Метод get_text1.on_clicked()")


class MyWindow(QtGui.QMainWindow, Form):
    def __init__(self, parent=None):
        """


        :type self: object MainWindow
        :param parent:
        """
        def event(self, e):
            if e.type() == QtCore.QEvent.KeyPress:
                print("Нажата клавиша на клавиатуре")
                print("Код:", e.key(), ", текст:", e.text())
            elif e.type() == QtCore.QEvent.Close:
                print("Окно закрыто")
            elif e.type() == QtCore.QEvent.MouseButtonPress:
                print("Щелчок мышью. Координаты:", e.x(), e.y())
            return QtGui.QMainWindow.event(self, e) # Отправляем дальше

        def changeEvent(self, e):
            if e.type() == QtCore.QEvent.WindowStateChange:
                if self.isMinimized():
                    print("Окно свернуто")
                elif self.isMaximized():
                    print("Окно раскрыто до максимальных размеров")
                elif self.isFullScreen():
                    print("Полноэкранный режим")
                elif self.isActiveWindow():
                    print("Окно находится в фокусе ввода")

                QtGui.QMainWindow.changeEvent(self, e) # Отправляем дальше

        def closeEvent(self, e):
            result = QtGui.QMessageBox.question(self,
                                                "Подтверждение закрытия окна",
                                                "Вы действительно хотите закрыть окно?",
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                                QtGui.QMessageBox.No)
            if result == QtGui.QMessageBox.Yes:
                e.accept()
                QtGui.QWidget.closeEvent(self, e)
            else:
                e.ignore()


        def showEvent(self, e):
            print("Окно отображено")
            QtGui.QMainWindow.showEvent(self, e)   # Отправляем дальше

        def hideEvent(self, e):
            print("Окно скрыто")
            QtGui.QMainWindow.hideEvent(self, e)   # Отправляем дальше

        def moveEvent(self, e):
            print("x = {0}; y = {1}".format(e.pos().x(), e.pos().y()))
            QtGui.QMainWindow.moveEvent(self, e)   # Отправляем дальше
        def resizeEvent(self, e):
            print("w = {0}; h = {1}".format(e.size().width(), e.size().height()))
            QtGui.QMainWindow.resizeEvent(self, e) # Отправляем дальше

        def onChanged(text):

            self.xx = text
            print(self.xx)
            return self.xx

        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.pushButton_exit, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit)
        self.pushButton_exit.setToolTip("Нажав эту кнопку покидаем программу")
        #self.setToolTip("Главное Окно")
        self.lineEdit.setToolTip("Введите что нибудь")
        self.lineEdit.setPlaceholderText("Введите Бяку")
        self.lineEdit.setPlaceholderText("Введите Бяку")
        #self.lineEdit.textChanged[str].connect(onChanged) #не убирать !!! работает как начинаешь набирать в едите !!!
        #self.lineEdit.textEdited[str].connect(onChanged)
        #self.lineEdit.editingFinished().connect(onChanged())
        self.text = self.lineEdit.text()
        print("text =", self.text)
        # Назначаем обработчиком функцию
        QtCore.QObject.connect(self.pushButton_input, QtCore.SIGNAL("clicked()"), on_clicked)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL("editingFinished()"), editing_finished)
        # Назначаем обработчиком метод класса
        QtCore.QObject.connect(self.pushButton_input, QtCore.SIGNAL("clicked()"), obj.on_clicked)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL("editingFinished()"), obj.editing_finished)

        # Передача параметра в обработчик
        QtCore.QObject.connect(self.pushButton_input, QtCore.SIGNAL("clicked()"), MyClass(10))
        QtCore.QObject.connect(self.pushButton_input, QtCore.SIGNAL("clicked()"), MyClass(5))
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL("editingFinished()"), get_text1(self.lineEdit.text()))

if __name__ == "__main__":
    import sys
    obj = MyClass()
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
