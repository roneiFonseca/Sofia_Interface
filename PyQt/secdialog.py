# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secdialog.ui'
#
# Created: Tue Feb 23 14:50:15 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from thirddialog import Ui_thirdDialog
from fifdialog import Ui_fifDialog
from time_window import Ui_fourthDialog
from verificacao import Ui_modo_de_op
import imagens

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

class Ui_SecDialog(object):
    def setupUi(self, SecDialog):
        SecDialog.setObjectName(_fromUtf8("SecDialog"))
        SecDialog.resize(800, 480)
        SecDialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label = QtGui.QLabel(SecDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 721, 111))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/imagens/logo.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(SecDialog)
        self.label_2.setGeometry(QtCore.QRect(260, 130, 301, 71))
        self.label_2.setStyleSheet(_fromUtf8("font: 22pt \"Times New Roman\";"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_4 = QtGui.QPushButton(SecDialog)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 340, 91, 61))
        self.pushButton_4.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(SecDialog)
        self.pushButton_5.setGeometry(QtCore.QRect(400, 340, 101, 61))
        self.pushButton_5.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(SecDialog)
        self.pushButton_6.setGeometry(QtCore.QRect(530, 220, 161, 61))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(SecDialog)
        self.pushButton_7.setGeometry(QtCore.QRect(80, 220, 161, 61))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(SecDialog)
        self.pushButton_8.setGeometry(QtCore.QRect(300, 220, 161, 61))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))

        self.retranslateUi(SecDialog)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), SecDialog.close)
        QtCore.QMetaObject.connectSlotsByName(SecDialog)

    def retranslateUi(self, SecDialog):
        SecDialog.setWindowTitle(_translate("SecDialog", "Dialog", None))
        self.label_2.setText(_translate("SecDialog", "CONFIGURAÇÕES", None))
        self.pushButton_4.setText(_translate("SecDialog", "Iniciar", None))
        self.pushButton_5.setText(_translate("SecDialog", "Desligar", None))
        self.pushButton_6.setText(_translate("SecDialog", "MODO DE OPERAÇÃO", None))
        self.pushButton_7.setText(_translate("SecDialog", "POTÊNCIA", None))
        QtCore.QObject.connect(self.pushButton_7 , QtCore.SIGNAL("clicked()") , self.Power_Func)
        self.pushButton_8.setText(_translate("SecDialog", "TEMPO", None))

        QtCore.QObject.connect(self.pushButton_8 , QtCore.SIGNAL("clicked()") , self.Timer_Func)
        QtCore.QObject.connect(self.pushButton_6 , QtCore.SIGNAL("clicked()") , self.Operation_mode)
        QtCore.QObject.connect(self.pushButton_4 , QtCore.SIGNAL("clicked()") , self.Verify_window)


    def Power_Func(self): # Clicar em Potencia
        thirdDialog = QtGui.QDialog()
        ui = Ui_thirdDialog()
        ui.setupUi(thirdDialog)
        thirdDialog.exec_()

    def Timer_Func(self): # Clicar em Tempo
        fourthDialog = QtGui.QDialog()
        ui = Ui_fourthDialog()
        ui.setupUi(fourthDialog)
        fourthDialog.exec_()

    def Operation_mode(self): # Clicar em Modo de Operação
        fifDialog = QtGui.QDialog()
        ui = Ui_fifDialog()
        ui.setupUi(fifDialog)
        fifDialog.exec_()

    def Verify_window(self): # Clicar em tela de verifição
        modo_de_op = QtGui.QDialog()
        ui = Ui_modo_de_op()
        ui.setupUi(modo_de_op)
        modo_de_op.exec_()



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SecDialog = QtGui.QDialog()
    ui = Ui_SecDialog()
    ui.setupUi(SecDialog)
    SecDialog.show()
    sys.exit(app.exec_())

