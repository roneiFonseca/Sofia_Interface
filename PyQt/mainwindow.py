# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Feb 23 14:35:16 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from secdialog import Ui_SecDialog
import imagens
import pylab_plot
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 480)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../teste/imagens/teste1.JPG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);color: blue"))
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(-10, -10, 800, 480))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Leelawadee;"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setFrameShadow(QtGui.QFrame.Plain)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 800, 111))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/imagens/logo.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Sofia_Gerador_RF", None))
        self.label.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Calibri\'; font-size:44pt; font-weight:600; color:#000000;\">Gerador RF</span><span style=\" font-family:\'Calibri\'; font-size:44pt; font-weight:600; font-style:italic; color:#000000;\"> – SOFIA</span><span style=\" font-family:\'Calibri\'; font-size:44pt; font-style:italic; color:#000000;\"/></p></body></html>", None))
# <<<<<<< Updated upstream
        self.label.setText(_translate("MainWindow", "<html><head/><body><br><p><span style=\" font-size:26pt;\">Seja Bem Vindo</span></p><p><span style=\" font-size:26pt;\">ao </span></p><p><span style=\" font-size:26pt;\">Gerador RF – </span><span style=\" font-size:26pt; font-style:italic;\">SOFIA </span></p></body></html>", None))
        QtCore.QTimer.singleShot(5000, self.OpenIT)   
        #MainWindow.showFullScreen()
# =======
        # self.label.setText(_translate("MainWindow", "<html><head/><body><br><p><span style=\" font-size:26pt;\">SEJA BEM VINDO</span></p><p><span style=\" font-size:26pt;\">AO </span></p><p><span style=\" font-size:26pt;\">Gerador RF – </span><span style=\" font-size:26pt; font-style:italic;\">SOFIA </span></p></body></html>", None))
        # QtCore.QTimer.singleShot(1000, self.OpenIT)   
# >>>>>>> Stashed changes
    
    def OpenIT(self):
        MainWindow.close()
        SecDialog = QtGui.QDialog()
        ui = Ui_SecDialog()
        ui.setupUi(SecDialog)
        SecDialog.exec_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

