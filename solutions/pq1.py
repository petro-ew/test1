__author__ = 'petro-ew'
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("1 proga")
window.resize(300, 70)
label = QtGui.QLabel("<center>Privet Mir!<center>")
btnQuit = QtGui.QPushButton("&Zakrit Okno")
vbox = QtGui.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQuit)
window.setLayout(vbox)
QtCore.QObject.connect(btnQuit, QtCore.SIGNAL("clicked()"), QtGui.qApp, QtCore.SLOT("quit()"))
window.show()
sys.exit(app.exec_())
