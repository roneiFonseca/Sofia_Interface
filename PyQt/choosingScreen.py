# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choosingScreen.ui'
#
# Created: Sun Apr 10 14:49:19 2016
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox,QWidget
from thirddialog import Ui_thirdDialog
from fifdialog import Ui_fifDialog
from help_box import Ui_Dialog
import parametros
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SecDialog(object):
    def setupUi(self, SecDialog):
        SecDialog.setObjectName(_fromUtf8("SecDialog"))
        SecDialog.resize(800, 480)
        SecDialog.setStyleSheet(_fromUtf8("background-color: black;"))
        self.label_2 = QtGui.QLabel(SecDialog)
        self.label_2.setGeometry(QtCore.QRect(260, 20, 301, 31))
        self.label_2.setStyleSheet(_fromUtf8("font: 26pt \"Arial\";\n""color:rgb(255, 255, 255)"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(SecDialog)
        self.label_3.setGeometry(QtCore.QRect(40, 80, 191, 31))
        self.label_3.setStyleSheet(_fromUtf8("font: 18pt \"Arial\";\n""color: white;"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(SecDialog)
        self.label_4.setGeometry(QtCore.QRect(540, 80, 191, 31))
        self.label_4.setStyleSheet(_fromUtf8("font: 18pt \"Arial\";\n""color: white;"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(SecDialog)
        self.label_5.setGeometry(QtCore.QRect(310, 180, 191, 31))
        self.label_5.setStyleSheet(_fromUtf8("font: 18pt \"Arial\";\n""color: white;"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.textBrowser = QtGui.QTextBrowser(SecDialog)
        self.textBrowser.setGeometry(QtCore.QRect(110, 370, 571, 81))
        self.textBrowser.setStyleSheet(_fromUtf8("border-style: outset;\n""border-width: 1px;\n""border-color: gray;"))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        
        self.pushButton_2 = QtGui.QPushButton(SecDialog) # "?" Button 
        self.pushButton_2.setGeometry(QtCore.QRect(20, 400, 61, 51))
        self.pushButton_2.setStyleSheet(_fromUtf8("font: 20pt \"Arial\";\n""background-color: red;color:bla;\n""border-radius: 5px;"))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.setIcon(QtGui.QIcon("power.png"))
        self.pushButton_2.setIconSize(QtCore.QSize(35,35))
        

        self.pushButton_3 = QtGui.QPushButton("",SecDialog) # "?" Button 
        self.pushButton_3.setGeometry(QtCore.QRect(710, 400, 61, 51))
        self.pushButton_3.setStyleSheet(_fromUtf8("font: 34pt \"Arial\";\n""background-color: gray;color:bla;\n""border-radius: 5px;"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        
        self.pushButton_4 = QtGui.QPushButton(SecDialog)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 220, 221, 91))
        self.pushButton_4.setStyleSheet(_fromUtf8("font: 24pt \"Arial\";\n""background-color: purple;\n""border-radius: 5px;"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.setIcon(QtGui.QIcon("people.png"))
        self.pushButton_4.setIconSize(QtCore.QSize(65,65))
        self.pushButton_5 = QtGui.QPushButton(SecDialog)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 120, 211, 91))
        self.pushButton_5.setStyleSheet(_fromUtf8("font: 18pt \"Arial\";\n""background-color: blue;\n""border-radius: 5px;"))
        self.pushButton_5.setText(_fromUtf8(""))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.setIcon(QtGui.QIcon("clock.png"))
        self.pushButton_5.setIconSize(QtCore.QSize(65,65))
        self.pushButton_6 = QtGui.QPushButton(SecDialog)
        self.pushButton_6.setGeometry(QtCore.QRect(530, 120, 211, 91))
        self.pushButton_6.setStyleSheet(_fromUtf8("font: 18pt \"Arial\";\n""background-color: green;\n""border-radius: 5px;"))
        self.pushButton_6.setText(_fromUtf8(""))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_6.setIcon(QtGui.QIcon("set.png"))
        self.pushButton_6.setIconSize(QtCore.QSize(65,65))

        self.retranslateUi(SecDialog)
        QtCore.QMetaObject.connectSlotsByName(SecDialog)

    def retranslateUi(self, SecDialog):
        SecDialog.setWindowTitle(QtGui.QApplication.translate("SecDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SecDialog", "MODO DE OPERAÇÃO", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SecDialog", "AUTOMÁTICO", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("SecDialog", "MANUAL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("SecDialog", "PRÉ-CLÍNICO", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("SecDialog", "?", None, QtGui.QApplication.UnicodeUTF8))
        QtCore.QObject.connect(self.pushButton_2 , QtCore.SIGNAL("clicked()") , self.showDialog)
        QtCore.QObject.connect(self.pushButton_3 , QtCore.SIGNAL("clicked()") , self.Help)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL("clicked()") , self.Power_Func)
        QtCore.QObject.connect(self.pushButton_5 , QtCore.SIGNAL("clicked()") , self.Operation_mode)

        self.textBrowser.setHtml(QtGui.QApplication.translate("SecDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.Helvetica Neue DeskInterface\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Automático - Escolha dentre as opções o modo dejesado para o procedimento de ablação.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Manual: Ajuste seus próprios parâmetros para o procedimento.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Pré-clínico: Entre com os dados médicos do paciente.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

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

    def showDialog(self):
        w = QWidget()
        result = QMessageBox.question(w, 'Message', "Do you like Python?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # palette     = QPalette()
        # palette.setColor(QPalette.Background, Qt.cyan)
        # msgBox.setPalette(palette)
        # msgBox.show()
         
        if result == QMessageBox.Yes:
            print 'Yes.'
            sys.exit()
        else:
            print 'No.' 



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SecDialog = QtGui.QDialog()
    ui = Ui_SecDialog()
    ui.setupUi(SecDialog)
    SecDialog.show()
    sys.exit(app.exec_())