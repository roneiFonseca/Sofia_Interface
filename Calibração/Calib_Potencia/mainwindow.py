# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Mar 25 18:35:37 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 480)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.pushButton_menos = QtGui.QPushButton(self.centralWidget)
        self.pushButton_menos.setGeometry(QtCore.QRect(80, 210, 301, 91))
        self.pushButton_menos.setObjectName(_fromUtf8("pushButton_menos"))
        self.pushButton_mais = QtGui.QPushButton(self.centralWidget)
        self.pushButton_mais.setGeometry(QtCore.QRect(410, 210, 291, 91))
        self.pushButton_mais.setObjectName(_fromUtf8("pushButton_mais"))
        self.lcdNumber = QtGui.QLCDNumber(self.centralWidget)
        self.lcdNumber.setGeometry(QtCore.QRect(83, 20, 611, 161))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        counter = 0

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_menos.setText(_translate("MainWindow", "-", None))
        self.pushButton_mais.setText(_translate("MainWindow", "+", None))
        QtCore.QObject.connect(self.pushButton_menos , QtCore.SIGNAL("clicked()") , self.initial_button_Plus_click)
        QtCore.QObject.connect(self.pushButton_mais , QtCore.SIGNAL("clicked()") , self.initial_button_Minus_click)
        
        counter = 0

    

    def initial_button_Plus_click(self):
		counter
		counter +=1
		self.lcdNumber.display(counter)
        
    def initial_button_Minus_click(self):
        counter -=1 
        self.lcdNumber.display(counter)
        
    def final_button_Plus_click(self):        
        counter += 1
        self.lcdNumber_2.display(counter)
        counter = counter -1
    def final_button_Minus_click(self):
		counter -=1 
		self.lcdNumber_2.display(counter)
	
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

