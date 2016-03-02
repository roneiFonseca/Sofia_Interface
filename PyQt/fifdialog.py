# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fifdialog.ui'
#
# Created: Wed Mar  2 15:46:05 2016
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!
import random
from PyQt4 import QtCore, QtGui

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
        fifDialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label_2 = QtGui.QLabel(fifDialog)
        self.label_2.setGeometry(QtCore.QRect(120, 110, 561, 51))
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
        self.pushButton_2 = QtGui.QPushButton(fifDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 200, 361, 51))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(fifDialog)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 260, 361, 51))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(fifDialog)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 320, 361, 51))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(fifDialog)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 390, 131, 51))
        self.pushButton_5.setStyleSheet(_fromUtf8("font: 14pt \"Arial\";\n"
"\n"
""))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.graphicsView = QtGui.QGraphicsView(fifDialog)
        self.graphicsView.scale(5,5)
        self.graphicsView.setGeometry(QtCore.QRect(395, 161, 381, 211))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.retranslateUi(fifDialog)
        QtCore.QMetaObject.connectSlotsByName(fifDialog)

    def retranslateUi(self, fifDialog):
        fifDialog.setWindowTitle(QtGui.QApplication.translate("fifDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("fifDialog", "MODO DE OPERAÇÃO", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("fifDialog", "5 W a cada 2 minutos", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("fifDialog", "10 W a cada 4 minutos", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("fifDialog", "2.5 W a cada 1 minuto", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("fifDialog", "VOLTAR", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    fifDialog = QtGui.QDialog()
    ui = Ui_fifDialog()
    ui.setupUi(fifDialog)
    fifDialog.show()
    sys.exit(app.exec_())