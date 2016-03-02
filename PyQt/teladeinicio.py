# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teladeinicio.ui'
#
# Created: Tue Mar  1 23:47:32 2016
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../teste/imagens/teste1.JPG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(-10, -10, 800, 480))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Leelawadee"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setFrameShadow(QtGui.QFrame.Plain)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 340, 121, 61))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 701, 111))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Sofia_Gerador_RF", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setWhatsThis(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Calibri\'; font-size:44pt; font-weight:600; color:#000000;\">Gerador RF</span><span style=\" font-family:\'Calibri\'; font-size:44pt; font-weight:600; font-style:italic; color:#000000;\"> – SOFIA</span><span style=\" font-family:\'Calibri\'; font-size:44pt; font-style:italic; color:#000000;\"/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt;\">Seja Bem Vindo</span></p><p><span style=\" font-size:26pt;\">ao </span></p><p><span style=\" font-size:26pt;\">Gerador RF – </span><span style=\" font-size:26pt; font-style:italic;\">SOFIA </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Configurações", None, QtGui.QApplication.UnicodeUTF8))

