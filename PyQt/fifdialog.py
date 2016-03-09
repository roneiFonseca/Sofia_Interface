# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fifdialog.ui'
#
# Created: Wed Mar  2 15:46:05 2016
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!
import random
import parametros
import pylab_plot
from PyQt4 import QtCore, QtGui
import imagens2

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
        fifDialog.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);color: rgb(255, 255, 255)"))
        self.label_2 = QtGui.QLabel(fifDialog)
        self.label_2.setGeometry(QtCore.QRect(120, 120, 561, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("font: 22pt \"Arial\";"))
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(fifDialog)
        self.label.setGeometry(QtCore.QRect(20, 0, 721, 111))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_9 = QtGui.QLabel(fifDialog)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 821, 121))
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setPixmap(QtGui.QPixmap(_fromUtf8(":/imagens/logo.png")))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.pushButton_2 = QtGui.QPushButton(fifDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 200, 241, 51))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.setStyleSheet("font-weight:bold;background-color: gray")
        self.pushButton_3 = QtGui.QPushButton(fifDialog)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 260, 241, 51))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.setStyleSheet("font-weight:bold;background-color: gray")
        self.pushButton_4 = QtGui.QPushButton(fifDialog)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 320, 241, 51))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.setStyleSheet("font-weight:bold;background-color: gray")
#         self.pushButton_5 = QtGui.QPushButton(fifDialog)
#         self.pushButton_5.setGeometry(QtCore.QRect(20, 380, 111, 51))
#         self.pushButton_5.setStyleSheet(_fromUtf8("font: 14pt \"Arial\";\n"
# "\n"
# ""))
        # self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(fifDialog)
        self.pushButton_6.setGeometry(QtCore.QRect(75, 380, 111, 51))
        self.pushButton_6.setStyleSheet(_fromUtf8("font: 14pt \"Arial\";\n""\n"""))
        self.pushButton_6.setStyleSheet("background-color: green")
        self.pic = QtGui.QLabel(fifDialog)
        self.pic.setGeometry(QtCore.QRect(309, 180, 461, 261))
        self.pic.setScaledContents(True)
        pylab_plot.plotMode(self,1)
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
        self.pushButton_2.setText(QtGui.QApplication.translate("fifDialog", "2 W por minuto", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("fifDialog", "2.5 W por minuto", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("fifDialog", "5 W por minuto", None, QtGui.QApplication.UnicodeUTF8))
    #    self.pushButton_5.setText(QtGui.QApplication.translate("fifDialog", "VOLTAR", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("fifDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))

        QtCore.QObject.connect(self.pushButton_2 , QtCore.SIGNAL("clicked()") , self.mode1)
        QtCore.QObject.connect(self.pushButton_3 , QtCore.SIGNAL("clicked()") , self.mode2)
        QtCore.QObject.connect(self.pushButton_4 , QtCore.SIGNAL("clicked()") , self.mode3)
        # QtCore.QObject.connect(self.pushButton_5 , QtCore.SIGNAL("clicked()") , fifDialog.close)
        QtCore.QObject.connect(self.pushButton_6 , QtCore.SIGNAL("clicked()") , fifDialog.close)



    def mode1 (self):
        global pixmap
        parametros.todos['potenciaStep'] = 2
        parametros.todos['tempoStep'] = 1
        parametros.todos['modo'] = 1
        self.pushButton_2.setStyleSheet("font-weight:bold;background-color: blue")
        self.pushButton_3.setStyleSheet("font-weight:bold;background-color: gray")
        self.pushButton_4.setStyleSheet("font-weight:bold;background-color: gray")
        pylab_plot.plotMode(self,1)
        pixmap = QtGui.QPixmap('mode1.png')
        self.pic.setPixmap(pixmap)  


    def mode2 (self):
        parametros.todos['potenciaStep'] = 2.5
        parametros.todos['tempoStep'] = 1
        parametros.todos['modo'] = 2
        self.pushButton_2.setStyleSheet("font-weight:bold;background-color: gray")
        self.pushButton_3.setStyleSheet("font-weight:bold;background-color: green")
        self.pushButton_4.setStyleSheet("font-weight:bold;background-color: gray")        
        pylab_plot.plotMode(self,2)
        pixmap = QtGui.QPixmap('mode2.png')
        self.pic.setPixmap(pixmap)



    def mode3 (self):
        parametros.todos['potenciaStep'] = 5
        parametros.todos['tempoStep'] = 1
        parametros.todos['modo'] = 3
        self.pushButton_2.setStyleSheet("font-weight:bold;background-color: gray")
        self.pushButton_3.setStyleSheet("font-weight:bold;background-color: gray")
        self.pushButton_4.setStyleSheet("font-weight:bold;background-color: red")
        pylab_plot.plotMode(self,3) 
        pixmap = QtGui.QPixmap('mode3.png')  
        self.pic.setPixmap(pixmap)  

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    fifDialog = QtGui.QDialog()
    ui = Ui_fifDialog()
    ui.setupUi(fifDialog)
    fifDialog.show()
    sys.exit(app.exec_())