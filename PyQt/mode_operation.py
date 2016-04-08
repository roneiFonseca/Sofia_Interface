# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secdialog.ui'
#
# Created: Mon Apr  4 11:47:02 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from thirddialog import Ui_thirdDialog
from fifdialog import Ui_fifDialog
from help_box import Ui_Dialog
import parametros
<<<<<<< HEAD
=======
import pylab_plot
>>>>>>> galho_do_matias

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
        self.PlotterThread = PlotterThread()
        self.PlotterThread.start()
        SecDialog.setObjectName(_fromUtf8("SecDialog"))
        SecDialog.resize(800, 480)
        SecDialog.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);color: rgb(255, 255, 255)"))


        #Label para colocar o titulo da janela - CONFIGURAÇÕES

        self.label_2 = QtGui.QLabel(SecDialog)
        self.label_2.setGeometry(QtCore.QRect(210, 20, 391, 71))
        self.label_2.setStyleSheet(_fromUtf8("font: 26pt \"Arial\";\n""font-weight:bold;"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        #PushButton para selecionar o Mode de Operação Automatico
        self.pushButton = QtGui.QPushButton(SecDialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 110, 201, 101))
        self.pushButton.setStyleSheet(_fromUtf8("font-weight:bold;background-color: blue;border-radius: 5px;"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        #PushButton para selecionar o Mode de Operação Manual
        self.pushButton_2 = QtGui.QPushButton(SecDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 110, 201, 101))
        self.pushButton_2.setStyleSheet(_fromUtf8("font-weight:bold;background-color: green;border-radius: 5px;"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        #PushButton para realizar o diagnostico pré clínico
        self.pushButton_3 = QtGui.QPushButton(SecDialog)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 300, 201, 101))
        self.pushButton_3.setStyleSheet(_fromUtf8("font-weight:bold;background-color: purple;border-radius: 5px;"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        #pushButton help
        self.pushButton_help = QtGui.QPushButton(SecDialog)
        self.pushButton_help.setGeometry(QtCore.QRect(700, 400, 71, 31))
        self.pushButton_help.setObjectName(_fromUtf8("pushButton_help"))
        self.pushButton_help.setStyleSheet("color: red;font: 26pt;font-weight:bold;background-color: blue;border-radius: 5px;")

        
        self.retranslateUi(SecDialog)
        QtCore.QMetaObject.connectSlotsByName(SecDialog)

    def retranslateUi(self, SecDialog):
        SecDialog.setWindowTitle(_translate("SecDialog", "Dialog", None))
        self.label_2.setText(_translate("SecDialog", "MODO DE OPERAÇÃO", None))
        self.pushButton.setText(_translate("SecDialog", "MANUAL", None))
        self.pushButton_2.setText(_translate("SecDialog", "AUTOMÁTICO", None))
        self.pushButton_3.setText(_translate("SecDialog", "PRÉ-CLÍNICO", None))
        self.pushButton_help.setText(_translate("SecDialog", "?", None))

        QtCore.QObject.connect(self.pushButton_help , QtCore.SIGNAL("clicked()") , self.Help)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()") , self.Power_Func)
        QtCore.QObject.connect(self.pushButton_2 , QtCore.SIGNAL("clicked()") , self.Operation_mode)


    def Help(self): # Clicar em Help
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.exec_()

    def Power_Func(self): # Clicar em Potencia
        parametros.flag['manualMode'] = True
        thirdDialog = QtGui.QDialog()
        ui = Ui_thirdDialog()
        ui.setupUi(thirdDialog)
        thirdDialog.exec_()

    def Operation_mode(self): # Clicar em Modo de Operação
        parametros.flag['manualMode'] = False
        fifDialog = QtGui.QDialog()
        ui = Ui_fifDialog()
        ui.setupUi(fifDialog)
        fifDialog.exec_()


class PlotterThread(QtCore.QThread):

    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        for option in range(1,4):
            pylab_plot.plotMode(option)
        print "Done with the thread"



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SecDialog = QtGui.QDialog()
    ui = Ui_SecDialog()
    ui.setupUi(SecDialog)
    SecDialog.show()
    sys.exit(app.exec_())

