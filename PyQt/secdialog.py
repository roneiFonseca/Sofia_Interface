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
from verificacao import Ui_VerifyWindow
import parametros
import sys
from help_box import Ui_Dialog

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

        SecDialog.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);color: rgb(255, 255, 255)"))

        self.pushButton_help = QtGui.QPushButton(SecDialog)
        self.pushButton_help.setGeometry(QtCore.QRect(700, 20, 71, 31))
        self.pushButton_help.setObjectName(_fromUtf8("pushButton_help"))
        self.pushButton_help.setStyleSheet("font-weight:bold;background-color: blue;border-radius: 5px;")

        self.label_2 = QtGui.QLabel(SecDialog)
        self.label_2.setGeometry(QtCore.QRect(210, 50, 391, 71))
        self.label_2.setStyleSheet(_fromUtf8("font: 26pt \"Arial\";\n""font-weight:bold;"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))


        self.pushButton_4 = QtGui.QPushButton(SecDialog)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 350, 151, 71))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.setStyleSheet("font-weight:bold;background-color: rgb(40, 255, 0);border-radius: 10px;")


        self.pushButton_5 = QtGui.QPushButton(SecDialog)
        self.pushButton_5.setGeometry(QtCore.QRect(410, 350, 151, 71))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.setStyleSheet("font-weight:bold;background-color: red;border-radius: 10px;")
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        


        # self.pushButton_6 = QtGui.QPushButton(SecDialog)
        # self.pushButton_6.setGeometry(QtCore.QRect(520, 190, 231, 71))
        # self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        # self.pushButton_6.setStyleSheet("font-weight:bold;background-color: blue;border-radius: 10px;")
       


        self.pushButton_7 = QtGui.QPushButton(SecDialog)
        self.pushButton_7.setGeometry(QtCore.QRect(150,190,151,71))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_7.setStyleSheet("font-weight:bold;background-color: blue;border-radius: 10px;")
       


        self.pushButton_8 = QtGui.QPushButton(SecDialog)
        self.pushButton_8.setGeometry(QtCore.QRect(490, 190, 151, 71))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_8.setStyleSheet("font-weight:bold;background-color: blue;border-radius: 10px;")
       

        self.retranslateUi(SecDialog)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), SecDialog.close)
        QtCore.QMetaObject.connectSlotsByName(SecDialog)

    def retranslateUi(self, SecDialog):
        SecDialog.setWindowTitle(_translate("SecDialog", "Dialog", None))
        self.label_2.setText(_translate("SecDialog", "CONFIGURAÇÕES", None))
        self.pushButton_4.setText(_translate("SecDialog", "INICIAR", None))
        self.pushButton_5.setText(_translate("SecDialog", "DESLIGAR", None))
        # self.pushButton_6.setText(_translate("SecDialog", "MODO DE OPERAÇÃO", None))
        self.pushButton_7.setText(_translate("SecDialog", "POTÊNCIA", None))
        QtCore.QObject.connect(self.pushButton_7 , QtCore.SIGNAL("clicked()") , self.Power_Func)
        self.pushButton_8.setText(_translate("SecDialog", "TEMPO", None))
        self.pushButton_help.setText(_translate("SecDialog", "Ajuda", None))

        QtCore.QObject.connect(self.pushButton_8 , QtCore.SIGNAL("clicked()") , self.Timer_Func)
        # QtCore.QObject.connect(self.pushButton_6 , QtCore.SIGNAL("clicked()") , self.Operation_mode)
        QtCore.QObject.connect(self.pushButton_4 , QtCore.SIGNAL("clicked()") , self.Verify_window)
       
        QtCore.QObject.connect(self.pushButton_help , QtCore.SIGNAL("clicked()") , self.Help)

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

        parametros.todos['potenciaStep'] = (parametros.todos['potenciaFinal'] - parametros.todos['potenciaInicial'])//parametros.todos['tempo']
        print parametros.todos['potenciaStep']
        VerifyWindow = QtGui.QDialog()
        ui = Ui_VerifyWindow()
        ui.setupUi(VerifyWindow)
        VerifyWindow.exec_()

    def Help(self): # Clicar em Help
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.exec_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    SecDialog = QtGui.QDialog()
    ui = Ui_SecDialog()
    ui.setupUi(SecDialog)
    SecDialog.show()
    sys.exit(app.exec_())

