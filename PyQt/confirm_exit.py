# -*- coding: utf-8 -*-

################################### LIBRARIES ###############################################
from PyQt4 import QtCore, QtGui
import icons_mode_operation
#############################################################################################

##################################  Error Treatment #########################################
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

############################################################################################

################################### UI_FORM ##############################################
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 133)
        Form.setStyleSheet(_fromUtf8("font-weight:bold;background-color: gray;color: black"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 10, 221, 81))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 90, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.setStyleSheet(_fromUtf8("font-weight:bold;font: \"Arial\";\n""background-color: rgb(40, 255, 0);color:white;\n""border-radius: 5px;"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 90, 99, 27))
        self.pushButton_2.setStyleSheet(_fromUtf8("font-weight:bold;font:\"Arial\";\n""background-color: red;color:white;\n""border-radius: 5px;"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 141, 101))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/ask.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        # self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self):
        self.label.setText(_translate("Form", "Tem certeza que deseja sair?", None))
        self.pushButton.setText(_translate("Form", "Sim", None))
        self.pushButton_2.setText(_translate("Form", "Não", None))

        QtCore.QObject.connect(self.pushButton , QtCore.SIGNAL("clicked()") , self.turn_off)
        # QtCore.QObject.connect(self.pushButton_2 , QtCore.SIGNAL("clicked()") , Form.close)


    def turn_off(self):
        self.close()   #Desliga a tela de confirmação e em seguida, desliga o equipamento -> aciona os respectivos reles!


#############################################################################################

################################### MAIN ####################################################

# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     Form = QtGui.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
#############################################################################################
