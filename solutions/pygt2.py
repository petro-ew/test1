#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
import sys
from os import path, curdir
from PyQt4 import QtGui, QtCore, uic, Qt

Form, Base = uic.loadUiType("1-06-04-13.ui")

def on_clicked():
	print("Нажата кнопка button1")

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

class MyWindow(QtGui.QMainWindow, Form):
	def __init__(self, parent=None):
		"""


		:type self: object MainWindow
		:param parent:
		"""
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

		def find():
			"""поиск и вывод синонима"""
			word = self.lineEdit.text()
			#result = ''
			print("word = ", word)

		#self.lineEdit.textChanged[str].connect(onChanged) #не убирать !!! работает как начинаешь набирать в едите !!!
		# Назначаем обработчиком функцию
		QtCore.QObject.connect(self.pushButton_input, QtCore.SIGNAL("clicked()"), on_clicked)
		QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL("editingFinished()"), find)
		# Назначаем обработчиком метод класса
		QtCore.QObject.connect(self.pushButton_input, QtCore.SIGNAL("clicked()"), obj.on_clicked)
		QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL("editingFinished()"), MyClass())
		# Передача параметра в обработчик
		QtCore.QObject.connect(self.pushButton_input, QtCore.SIGNAL("clicked()"), find)
		QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL("returnPressed()"), find)

if __name__ == "__main__":
	import sys
	obj = MyClass()
	app = QtGui.QApplication(sys.argv)
	window = MyWindow()
	window.show()
	sys.exit(app.exec_())
