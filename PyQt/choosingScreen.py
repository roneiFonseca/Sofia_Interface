# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choosingScreen.ui'
#
# Created: Tue Apr  5 22:26:19 2016
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from secdialog import Ui_SecDialog
from fifdialog import Ui_fifDialog
import parametros
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_choosingScreen(object):
    def setupUi(self, choosingScreen):
        choosingScreen.setObjectName(_fromUtf8("choosingScreen"))
        choosingScreen.resize(800, 480)
        choosingScreen.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);color: white"))
        self.label = QtGui.QLabel(choosingScreen)
        self.label.setGeometry(QtCore.QRect(10, 10, 721, 111))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(choosingScreen)
        self.label_2.setGeometry(QtCore.QRect(200, 130, 391, 71))
        self.label_2.setStyleSheet(_fromUtf8("font: 26pt \"Arial\";"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(choosingScreen)
        self.pushButton.setGeometry(QtCore.QRect(100, 230, 251, 121))
        self.pushButton.setStyleSheet(_fromUtf8("font: 18pt \"Arial\";\n"
"border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));\n"
"alternate-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));background-color: blue;"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(choosingScreen)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 230, 261, 121))
        self.pushButton_2.setStyleSheet(_fromUtf8("font: 18pt \"Arial\";background-color: green;"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        # self.pushButton_3 = QtGui.QPushButton(choosingScreen)
        # self.pushButton_3.setGeometry(QtCore.QRect(340, 400, 131, 51))
        # self.pushButton_3.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";background-color: blue;"))
        # self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(choosingScreen)
        QtCore.QMetaObject.connectSlotsByName(choosingScreen)


    def retranslateUi(self, choosingScreen):
        choosingScreen.setWindowTitle(QtGui.QApplication.translate("choosingScreen", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("choosingScreen", "CONFIGURAÇÕES", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("choosingScreen", "AUTOMÁTICO", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("choosingScreen", "MANUAL", None, QtGui.QApplication.UnicodeUTF8))
        # self.pushButton_3.setText(QtGui.QApplication.translate("choosingScreen", "VOLTAR", None, QtGui.QApplication.UnicodeUTF8))

        QtCore.QObject.connect(self.pushButton , QtCore.SIGNAL("clicked()") , self.automatic)
        QtCore.QObject.connect(self.pushButton_2 , QtCore.SIGNAL("clicked()") , self.manual)


    def automatic(self):
        # choosingScreen.close()
        parametros.flag['manualMode'] = False
        fifDialog = QtGui.QDialog()
        ui = Ui_fifDialog()
        ui.setupUi(fifDialog)
        fifDialog.exec_()

    def manual(self):
        # choosingScreen.close()
        parametros.flag['manualMode'] = True
        secDialog = QtGui.QDialog()
        ui = Ui_SecDialog()
        ui.setupUi(secDialog)
        secDialog.exec_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    choosingScreen = QtGui.QMainWindow()
    ui = Ui_choosingScreen()
    ui.setupUi(choosingScreen)
    choosingScreen.show()
    sys.exit(app.exec_())


