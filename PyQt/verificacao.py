# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verificacao.ui'
#
# Created: Thu Mar  3 14:46:55 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import imagens
from monidialog import Ui_moniDialog

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

class Ui_modo_de_op(object):
    def setupUi(self, modo_de_op):
        modo_de_op.setObjectName(_fromUtf8("modo_de_op"))
        modo_de_op.resize(800, 480)
        modo_de_op.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label = QtGui.QLabel(modo_de_op)
        self.label.setGeometry(QtCore.QRect(260, 100, 301, 61))
        self.label.setStyleSheet(_fromUtf8("font: 26pt \"Arial\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.lcdNumber = QtGui.QLCDNumber(modo_de_op)
        self.lcdNumber.setGeometry(QtCore.QRect(30, 250, 111, 81))
        self.lcdNumber.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.lcdNumber_2 = QtGui.QLCDNumber(modo_de_op)
        self.lcdNumber_2.setGeometry(QtCore.QRect(220, 250, 111, 81))
        self.lcdNumber_2.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.lcdNumber_3 = QtGui.QLCDNumber(modo_de_op)
        self.lcdNumber_3.setGeometry(QtCore.QRect(640, 250, 111, 81))
        self.lcdNumber_3.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.lcdNumber_3.setObjectName(_fromUtf8("lcdNumber_3"))
        self.label_2 = QtGui.QLabel(modo_de_op)
        self.label_2.setGeometry(QtCore.QRect(50, 210, 61, 31))
        self.label_2.setStyleSheet(_fromUtf8("font: 10pt \"Arial\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(modo_de_op)
        self.label_3.setGeometry(QtCore.QRect(220, 210, 111, 31))
        self.label_3.setStyleSheet(_fromUtf8("font: 8pt \"Arial\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(modo_de_op)
        self.label_4.setGeometry(QtCore.QRect(670, 210, 71, 21))
        self.label_4.setStyleSheet(_fromUtf8("font: 10pt \"Arial\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(modo_de_op)
        self.label_5.setGeometry(QtCore.QRect(160, 310, 55, 16))
        self.label_5.setStyleSheet(_fromUtf8("font: 10pt \"Arial\";"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(modo_de_op)
        self.label_6.setGeometry(QtCore.QRect(350, 310, 55, 16))
        self.label_6.setStyleSheet(_fromUtf8("font: 10pt \"Arial\";"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton = QtGui.QPushButton(modo_de_op)
        self.pushButton.setGeometry(QtCore.QRect(450, 400, 181, 51))
        self.pushButton.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(modo_de_op)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 400, 181, 51))
        self.pushButton_2.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lcdNumber_4 = QtGui.QLCDNumber(modo_de_op)
        self.lcdNumber_4.setGeometry(QtCore.QRect(430, 250, 111, 81))
        self.lcdNumber_4.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.lcdNumber_4.setObjectName(_fromUtf8("lcdNumber_4"))
        self.label_7 = QtGui.QLabel(modo_de_op)
        self.label_7.setGeometry(QtCore.QRect(430, 210, 121, 20))
        self.label_7.setStyleSheet(_fromUtf8("font: 8pt \"Arial\";"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(modo_de_op)
        self.label_8.setGeometry(QtCore.QRect(550, 310, 55, 16))
        self.label_8.setStyleSheet(_fromUtf8("font: 10pt \"Arial\";"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(modo_de_op)
        self.label_9.setGeometry(QtCore.QRect(10, -10, 801, 111))
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setPixmap(QtGui.QPixmap(_fromUtf8(":/imagens/logo.png")))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.retranslateUi(modo_de_op)
        QtCore.QMetaObject.connectSlotsByName(modo_de_op)

    def retranslateUi(self, modo_de_op):
        modo_de_op.setWindowTitle(_translate("modo_de_op", "Dialog", None))
        self.label.setText(_translate("modo_de_op", "VERIFICAÇÃO", None))
        self.label_2.setText(_translate("modo_de_op", "TEMPO", None))
        self.label_3.setText(_translate("modo_de_op", "POTÊNCIA INICIAL", None))
        self.label_4.setText(_translate("modo_de_op", "MODO", None))
        self.label_5.setText(_translate("modo_de_op", "min", None))
        self.label_6.setText(_translate("modo_de_op", "W", None))
        self.pushButton.setText(_translate("modo_de_op", "CONFIRMAR", None))
        self.pushButton_2.setText(_translate("modo_de_op", "VOLTAR", None))
        self.label_7.setText(_translate("modo_de_op", "POTÊNCIA FINAL", None))
        self.label_8.setText(_translate("modo_de_op", "W", None))
        QtCore.QObject.connect(self.pushButton , QtCore.SIGNAL("clicked()") , self.Init)


    def Init(self): # Clicar em Iniciar
        moniDialog = QtGui.QDialog()
        ui = Ui_moniDialog()
        ui.setupUi(moniDialog)
        moniDialog.exec_()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    modo_de_op = QtGui.QDialog()
    ui = Ui_modo_de_op()
    ui.setupUi(modo_de_op)
    modo_de_op.show()
    sys.exit(app.exec_())

