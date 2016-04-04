# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verificacao.ui'
#
# Created: Thu Mar  3 14:46:55 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from monidialog import Ui_moniDialog
import parametros
import sys
import os

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

class Ui_VerifyWindow(object):
    def setupUi(self, VerifyWindow):
        VerifyWindow.setObjectName(_fromUtf8("VerifyWindow"))
        VerifyWindow.resize(800, 480)
        VerifyWindow.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);color: rgb(255, 255, 255)"))
        self.label = QtGui.QLabel(VerifyWindow)
        self.label.setGeometry(QtCore.QRect(260, 50, 301, 61))
        self.label.setStyleSheet(_fromUtf8("font: 26pt \"Arial\";font-weight:bold;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.lcdNumber = QtGui.QLCDNumber(VerifyWindow)
        self.lcdNumber.setGeometry(QtCore.QRect(30, 220, 111, 81))
        self.lcdNumber.setStyleSheet(_fromUtf8("background-color: blue;"))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.lcdNumber_2 = QtGui.QLCDNumber(VerifyWindow)
        self.lcdNumber_2.setGeometry(QtCore.QRect(220, 220, 111, 81))
        self.lcdNumber_2.setStyleSheet(_fromUtf8("background-color: blue;"))
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.lcdNumber_3 = QtGui.QLCDNumber(VerifyWindow)
        self.lcdNumber_3.setGeometry(QtCore.QRect(640, 220, 111, 81))
        self.lcdNumber_3.setStyleSheet(_fromUtf8("background-color: blue;"))
        self.lcdNumber_3.setObjectName(_fromUtf8("lcdNumber_3"))
        self.label_2 = QtGui.QLabel(VerifyWindow)
        self.label_2.setGeometry(QtCore.QRect(50, 170, 61, 31))
        self.label_2.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(VerifyWindow)
        self.label_3.setGeometry(QtCore.QRect(205, 170, 140, 31))
        self.label_3.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(VerifyWindow)
        self.label_4.setGeometry(QtCore.QRect(670, 170, 140, 31))
        self.label_4.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(VerifyWindow)
        self.label_5.setGeometry(QtCore.QRect(150, 290, 55, 16))
        self.label_5.setStyleSheet(_fromUtf8("font: 10pt \"Arial\";"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(VerifyWindow)
        self.label_6.setGeometry(QtCore.QRect(340, 290, 55, 16))
        self.label_6.setStyleSheet(_fromUtf8("font: 10pt \"Arial\";"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton = QtGui.QPushButton(VerifyWindow)
        self.pushButton.setGeometry(QtCore.QRect(450, 400, 181, 51))
        self.pushButton.setStyleSheet(_fromUtf8("font-weight:bold;background-color: rgb(40, 255, 0);border-radius: 10px;"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(VerifyWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 400, 181, 51))
        self.pushButton_2.setStyleSheet(_fromUtf8("font-weight:bold;background-color: red;border-radius: 10px;"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lcdNumber_4 = QtGui.QLCDNumber(VerifyWindow)
        self.lcdNumber_4.setGeometry(QtCore.QRect(430, 220, 111, 81))
        self.lcdNumber_4.setStyleSheet(_fromUtf8("background-color: blue;"))
        self.lcdNumber_4.setObjectName(_fromUtf8("lcdNumber_4"))
        self.label_7 = QtGui.QLabel(VerifyWindow)
        self.label_7.setGeometry(QtCore.QRect(420, 170, 140, 31))
        self.label_7.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(VerifyWindow)
        self.label_8.setGeometry(QtCore.QRect(550, 290, 55, 16))
        self.label_8.setStyleSheet(_fromUtf8("font: 10pt \"Arial\";"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        # self.label_9 = QtGui.QLabel(VerifyWindow)
        # self.label_9.setGeometry(QtCore.QRect(0, 0, 821, 121))
        # self.label_9.setText(_fromUtf8(""))
        # self.label_9.setPixmap(QtGui.QPixmap(_fromUtf8(":/imagens/logo.png")))
        # self.label_9.setObjectName(_fromUtf8("label_9"))

        self.retranslateUi(VerifyWindow)
        QtCore.QMetaObject.connectSlotsByName(VerifyWindow)

    def retranslateUi(self, VerifyWindow):
        VerifyWindow.setWindowTitle(_translate("VerifyWindow", "Dialog", None))
        self.label.setText(_translate("VerifyWindow", "VERIFICAÇÃO", None))
        self.label_2.setText(_translate("VerifyWindow", "TEMPO", None))
        self.label_3.setText(_translate("VerifyWindow", "POTÊNCIA INICIAL", None))
        self.label_4.setText(_translate("VerifyWindow", "MODO", None))
        self.label_5.setText(_translate("VerifyWindow", "min", None))
        self.label_6.setText(_translate("VerifyWindow", "W", None))
        self.pushButton.setText(_translate("VerifyWindow", "CONFIRMAR", None))
        self.pushButton_2.setText(_translate("VerifyWindow", "VOLTAR", None))
        self.label_7.setText(_translate("VerifyWindow", "POTÊNCIA FINAL", None))
        self.label_8.setText(_translate("VerifyWindow", "W", None))
        self.lcdNumber.display(parametros.todos['tempo'])
        self.lcdNumber_2.display(parametros.todos['potenciaInicial'])
        self.lcdNumber_3.display(parametros.todos['modo'])
        self.lcdNumber_4.display(parametros.todos['potenciaFinal'])
        QtCore.QObject.connect(self.pushButton , QtCore.SIGNAL("clicked()") , self.Monitoring_Window)
        QtCore.QObject.connect(self.pushButton , QtCore.SIGNAL("clicked()") , VerifyWindow.close)
        QtCore.QObject.connect(self.pushButton_2 , QtCore.SIGNAL("clicked()") , VerifyWindow.close)

    def Monitoring_Window(self): # Clicar para a tela de monitoramento

        # moniDialog = QtGui.QDialog()
        # ui = Ui_moniDialog()
        # ui.setupUi(moniDialog)
        # moniDialog.exec_()
        os.system("sudo /usr/bin/python monidialog.py")
      

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    VerifyWindow = QtGui.QDialog()
    ui = Ui_VerifyWindow()
    ui.setupUi(VerifyWindow)
    VerifyWindow.show()
    sys.exit(app.exec_())

