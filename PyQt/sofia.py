# -*- coding: utf-8 -*-

from PyQt4.QtCore import pyqtSignal,QTimer
from PyQt4.QtGui import QApplication, QMainWindow, QPushButton, \
            QLabel, QVBoxLayout, QWidget, QMessageBox, QDialog

from mainwindow import Ui_MainWindow
from choosingScreen import Ui_SecDialog
from help_box import Ui_Dialog
from thirddialog import Ui_thirdDialog
from time_window import Ui_fourthDialog
from fifdialog import Ui_fifDialog
from step_configure import Ui_stepDialog
from verificacao import Ui_VerifyWindow
from monidialog import Ui_moniDialog

import sys
import imagens2 
import pylab_plot
import parametros

class loadingWindow(QMainWindow,Ui_MainWindow):
	def __init__(self,parent=None): 
		QMainWindow.__init__(self)
		self.setupUi(self)
		self.retranslateUi(self)
		QTimer.singleShot(5000, self.newWindow)

	def newWindow(self):
		self.close()
		self.mainwindow2 = OperationMode(self)
		self.mainwindow2.show()

class OperationMode (QMainWindow,Ui_SecDialog):
	def __init__(self,parent=None): 
		QMainWindow.__init__(self,parent)
		self.setupUi(self)
		self.retranslateUi(self)
		self.pushButton_2.clicked.connect(self.questionBox)
		self.pushButton_3.clicked.connect(self.help)
		self.pushButton_6.clicked.connect(self.power)
		self.pushButton_5.clicked.connect(self.auto)

	def questionBox(self):
		reply = QMessageBox.question(self, 'Message',
    	"Tem certeza?", QMessageBox.Yes | 
    	QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.Yes:
		    self.close()
		else:
			pass

	def help(self):
		self.otherwindow = Help(self)
		self.otherwindow.show()

	def power(self): #Manual Mode
		parametros.flag['manualMode'] = True
		self.close()
		self.power = PowerSetup(self)
		self.power.show()

	def auto(self): #Automatic Mode
		parametros.flag['manualMode'] = False
		self.automatic = Automatic(self)
		self.automatic.show()


class Help(QDialog,Ui_Dialog):
	def __init__(self,parent=None):
		QDialog.__init__(self,parent)
		self.setupUi(self)
		self.pushButton_5.clicked.connect(self.close)



class PowerSetup(QMainWindow,Ui_thirdDialog):
	def __init__(self,parent=None): 
		QMainWindow.__init__(self,parent)
		self.setupUi(self)
		self.pushButton_off.clicked.connect(self.goBack)
		self.pushButton_5.clicked.connect(self.goTimer)

	def goBack(self):
		self.close()
		self.operationMode = OperationMode(self)
		self.operationMode.show()

	def goTimer(self):
		self.close()
		self.timerConfig = TimerSetup(self)
		self.timerConfig.show()

class TimerSetup(QMainWindow,Ui_fourthDialog):
	def __init__(self,parent=None):
		QMainWindow.__init__(self,parent)
		self.setupUi(self)
		self.pushButton_off.clicked.connect(self.goBack)
		self.pushButton_5.clicked.connect(self.goStep)

	def goBack(self):
		self.close()
		self.power = PowerSetup(self)
		self.power.show()

	def goStep(self):
		self.close()
		self.stepMode = StepSetup(self)
		self.stepMode.show()

class StepSetup(QMainWindow,Ui_stepDialog):
	def __init__(self,parent=None):
		QMainWindow.__init__(self,parent)
		self.setupUi(self)
		self.pushButton_BACK.clicked.connect(self.goBack)
		self.pushButton_OK.clicked.connect(self.goVerify)

	def goBack(self):
		self.close()
		self.timerConfig = TimerSetup(self)
		self.timerConfig.show()

	def goVerify(self):
		self.close()
		self.verifyMode = Verification(self)
		self.verifyMode.show()


class Verification(QMainWindow,Ui_VerifyWindow):
	def __init__(self,parent=None):
		QMainWindow.__init__(self,parent)
		self.setupUi(self)
		self.retranslateUi(self)
		self.pushButton_2.clicked.connect(self.goBack)
		self.pushButton.clicked.connect(self.goStart)

	def goBack(self):
		if (parametros.flag['manualMode']): # If in Manual Mode
			self.close()
			self.stepMode = StepSetup(self)
			self.stepMode.show()
		else: #in Auto Mode
			self.close()
			self.automatic = Automatic(self)
			self.automatic.show()

	def goStart(self):
		self.close()
		self.startProcedure = StartProcedure(self)
		self.startProcedure.show()

class StartProcedure(QMainWindow,Ui_moniDialog):
	def __init__(self,parent=None):
		QMainWindow.__init__(self,parent)
		self.setupUi(self)
		self.retranslateUi(self)
		self.pushButton_8.clicked.connect(self.goBack)
		# self.pushButton_7.clicked.connect(self.begin)

	def goBack(self):
		self.close()
		self.verifyMode = Verification(self)
		self.verifyMode.show()

	# def begin(self):





class Automatic(QMainWindow,Ui_fifDialog):
	def __init__(self,parent=None):
		QMainWindow.__init__(self,parent)
		self.setupUi(self)
		self.pushButton_7.clicked.connect(self.goBack)
		self.pushButton_6.clicked.connect(self.goVerify)

	def goBack(self):
		self.close()
		self.operationMode = OperationMode(self)
		self.operationMode.show()

	def goVerify(self):
		self.close()
		self.verifyMode = Verification(self)
		self.verifyMode.show()


if __name__ == "__main__": 

    app = QApplication(sys.argv) 
    ui = loadingWindow() 
    ui.show() 
    sys.exit(app.exec_()) 