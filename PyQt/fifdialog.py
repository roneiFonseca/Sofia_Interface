# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fifdialog.ui'
#
# Created: Wed Mar  2 15:46:05 2016
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!
from __future__ import division
import random
import parametros
import pylab_plot
from PyQt4 import QtCore, QtGui
from verificacao import Ui_VerifyWindow
import math

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s



class Ui_fifDialog(object):
    def setupUi(self, fifDialog):
        fifDialog.setObjectName(_fromUtf8("fifDialog"))
        fifDialog.resize(800, 480)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        fifDialog.setFont(font)
        fifDialog.setFocusPolicy(QtCore.Qt.NoFocus)
        fifDialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        fifDialog.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);"))
        self.label_2 = QtGui.QLabel(fifDialog)
        self.label_2.setGeometry(QtCore.QRect(120, 50, 561, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("font: 22pt \"Arial\";font-weight:bold;"))
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_2 = QtGui.QPushButton(fifDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 150, 241, 51))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.setStyleSheet("font-weight:bold;background-color: blue;border-radius: 10px;")
        self.pushButton_3 = QtGui.QPushButton(fifDialog)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 230, 241, 51))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.setStyleSheet("font-weight:bold;background-color: gray;border-radius: 10px;")
        self.pushButton_4 = QtGui.QPushButton(fifDialog)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 310, 241, 51))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.setStyleSheet("font-weight:bold;background-color: gray;border-radius: 10px;")

        self.pushButton_6 = QtGui.QPushButton(fifDialog)
        self.pushButton_6.setGeometry(QtCore.QRect(145, 390, 111, 51))
        self.pushButton_6.setStyleSheet(_fromUtf8("font: 14pt \"Arial\";\n""\n"""))
        self.pushButton_6.setStyleSheet("font-weight:bold;background-color:rgb(40, 255, 0);border-radius: 10px;")
        
        self.pushButton_7 = QtGui.QPushButton(fifDialog)
        self.pushButton_7.setGeometry(QtCore.QRect(25, 390, 111, 51))
        self.pushButton_7.setStyleSheet(_fromUtf8("font: 14pt \"Arial\";\n""\n"""))
        self.pushButton_7.setStyleSheet("font-weight:bold;background-color:red;border-radius: 10px;")
        
        self.pic = QtGui.QLabel(fifDialog)
        self.pic.setGeometry(QtCore.QRect(309, 130, 461, 261))
        self.pic.setStyleSheet(_fromUtf8("border: 2px solid white;\n"))
        self.pic.setScaledContents(True)

        # pylab_plot.plotMode(self,1)
        pixmap = QtGui.QPixmap('mode1.png')
        self.pic.setPixmap(pixmap)
        
        # self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        # self.frame.setFrameShadow(QtGui.QFrame.Raised)
        # self.frame.setObjectName(_fromUtf8("frame"))
        self.retranslateUi(fifDialog)
        QtCore.QMetaObject.connectSlotsByName(fifDialog)

    def retranslateUi(self, fifDialog):
        fifDialog.setWindowTitle(QtGui.QApplication.translate("fifDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("fifDialog", "MODO DE OPERAÇÃO", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("fifDialog", "10min 2W 5W-25W", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("fifDialog", "12min 2.5W 1W-31W", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("fifDialog", "15min 1W 10W-25W", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("fifDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("fifDialog", "Voltar", None, QtGui.QApplication.UnicodeUTF8))


        QtCore.QObject.connect(self.pushButton_2 , QtCore.SIGNAL("clicked()") , self.mode1)
        QtCore.QObject.connect(self.pushButton_3 , QtCore.SIGNAL("clicked()") , self.mode2)
        QtCore.QObject.connect(self.pushButton_4 , QtCore.SIGNAL("clicked()") , self.mode3)
        QtCore.QObject.connect(self.pushButton_6 , QtCore.SIGNAL("clicked()") , self.ok)
        QtCore.QObject.connect(self.pushButton_7 , QtCore.SIGNAL("clicked()") , fifDialog.close)



    def mode1 (self):
        global pixmap
        
        parametros.todos['modo'] = 1
        parametros.todos['potenciaInicial'] = 5
        parametros.todos['potenciaFinal'] = 25
        parametros.todos['potenciaRT'] = 5
        parametros.todos['potenciaStep'] = 2
        parametros.todos['tempo'] = 10
        parametros.todos['tempoStep'] = 1


        #pot_diff = parametros.todos['potenciaFinal'] - parametros.todos['potenciaInicial']
        #parametros.todos['tempoStep'] = pot_diff/parametros.todos['tempo']
        #time_ratio = parametros.todos['tempo']/parametros.todos['tempoStep']
        #parametros.todos['potenciaStep'] = pot_diff/time_ratio

        self.pushButton_2.setStyleSheet("font-weight:bold;background-color: blue;border-radius: 10px;")
        self.pushButton_3.setStyleSheet("font-weight:bold;background-color: gray;border-radius: 10px;")
        self.pushButton_4.setStyleSheet("font-weight:bold;background-color: gray;border-radius: 10px;")
        # pylab_plot.plotMode(self,1)
        pixmap = QtGui.QPixmap('mode1.png')
        self.pic.setPixmap(pixmap)  


    def mode2 (self):

        
        parametros.todos['modo'] = 2
        parametros.todos['potenciaInicial'] = 1
        parametros.todos['potenciaFinal'] = 31
        parametros.todos['potenciaRT'] = 1
        parametros.todos['potenciaStep'] = 2.5
        parametros.todos['tempo'] = 12
        parametros.todos['tempoStep'] = 1


        #pot_diff2 = parametros.todos['potenciaFinal'] - parametros.todos['potenciaInicial']
        #parametros.todos['tempoStep'] = pot_diff2/parametros.todos['tempo']
        #parametros.todos['potenciaStep'] = 2
        #parametros.todos['tempoStep'] = parametros.todos['potenciaStep']*parametros.todos['tempoStep']
        # print (parametros.todos['tempoStep'])

        self.pushButton_2.setStyleSheet("font-weight:bold;background-color: gray;border-radius: 10px;")
        self.pushButton_3.setStyleSheet("font-weight:bold;background-color: green;border-radius: 10px;")
        self.pushButton_4.setStyleSheet("font-weight:bold;background-color: gray;border-radius: 10px;")        
        # pylab_plot.plotMode(self,2)
        pixmap = QtGui.QPixmap('mode2.png')
        self.pic.setPixmap(pixmap)



    def mode3 (self):
        
        
        parametros.todos['modo'] = 3
        parametros.todos['potenciaInicial'] = 10
        parametros.todos['potenciaFinal'] = 25
        parametros.todos['potenciaRT'] = 10
        parametros.todos['potenciaStep'] = 1
        parametros.todos['tempo'] = 15
        parametros.todos['tempoStep'] = 1
        
        #pot_diff2 = parametros.todos['potenciaFinal'] - parametros.todos['potenciaInicial']
        #parametros.todos['tempoStep'] = pot_diff2/parametros.todos['tempo']
        #parametros.todos['potenciaStep'] = 3
        #parametros.todos['tempoStep'] = parametros.todos['potenciaStep']*parametros.todos['tempoStep']
        # print (parametros.todos['tempoStep'])

        self.pushButton_2.setStyleSheet("font-weight:bold;background-color: gray;border-radius: 10px;")
        self.pushButton_3.setStyleSheet("font-weight:bold;background-color: gray;border-radius: 10px;")
        self.pushButton_4.setStyleSheet("font-weight:bold;background-color: red;border-radius: 10px;")
        # pylab_plot.plotMode(self,3) 
        pixmap = QtGui.QPixmap('mode3.png') 
        self.pic.setPixmap(pixmap)


    def ok (self):
        VerifyWindow = QtGui.QDialog()
        ui = Ui_VerifyWindow()
        ui.setupUi(VerifyWindow)
        VerifyWindow.exec_()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    fifDialog = QtGui.QDialog()
    ui = Ui_fifDialog()
    ui.setupUi(fifDialog)
    fifDialog.show()
    sys.exit(app.exec_())
