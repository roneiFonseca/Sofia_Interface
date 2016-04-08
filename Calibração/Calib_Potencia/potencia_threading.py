# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thirddialog.ui'
#
# Created: Wed Feb 24 15:04:30 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import parametros
import math
import threading, time

RPI_ON = False
if (RPI_ON):
    import RPi.GPIO as GPIO
    import smbus
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    bus = smbus.SMBus(1)
    address = 0x48

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

class Ui_thirdDialog(object):

    def setupUi(self, thirdDialog):

        thirdDialog.setObjectName(_fromUtf8("thirdDialog"))
        thirdDialog.resize(800, 480)
        font = QtGui.QFont()
        font.setPointSize(18)
        thirdDialog.setFont(font)
        thirdDialog.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);color: rgb(255,255,255);"))

        
        self.label_2 = QtGui.QLabel(thirdDialog)
        self.label_2.setGeometry(QtCore.QRect(240, 50, 301, 71))

        self.label_2.setStyleSheet(_fromUtf8("font: 26pt \"Arial\";\n""font-weight:bold;"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.lcdNumber = QtGui.QLCDNumber(thirdDialog)
        self.lcdNumber.setGeometry(QtCore.QRect(80, 200, 121, 81))
        self.lcdNumber.setStyleSheet(_fromUtf8("border: 2px solid gray;\n""background-color: rgb(0, 0, 0);\n"))
    
        self.lcdNumber.display(parametros.todos['potenciaInicial'])


        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lcdNumber.setPalette(palette)
        self.lcdNumber.setStyleSheet(_fromUtf8("background-color: blue;color:white"))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))

        self.pushButton = QtGui.QPushButton(thirdDialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 180, 61, 61))
        self.pushButton.setStyleSheet("font-weight:bold;background-color: blue;border-radius: 10px;")
        
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton_2 = QtGui.QPushButton(thirdDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 250, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        # self.pushButton_2.setStyleSheet(_fromUtf8("border: 2px solid gray;\n""background-color: rgb(0, 0, 0);\n""color: rgb(0, 255, 0);\n""font: 30pt \"Arial\";"))
        self.pushButton_2.setStyleSheet("font-weight:bold;background-color: blue;border-radius: 10px;")


        self.label_3 = QtGui.QLabel(thirdDialog)
        self.label_3.setGeometry(QtCore.QRect(90, 290, 120, 21))
        # self.label_3.setStyleSheet(_fromUtf8("font: 16pt \"Times New Roman\";"))
        self.label_3.setStyleSheet(_fromUtf8("font: 16pt \"Arial\";\n"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        
        self.pushButton_3 = QtGui.QPushButton(thirdDialog)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 180, 61, 61))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.setStyleSheet("font-weight:bold;background-color: blue;border-radius: 10px;")
        # self.pushButton_3.setStyleSheet(_fromUtf8("border: 2px solid gray;\n""background-color: rgb(0, 0, 0);\n""color: rgb(0, 255, 0);\n""font: 30pt \"Arial\";"))        


        self.label_4 = QtGui.QLabel(thirdDialog)
        self.label_4.setGeometry(QtCore.QRect(480, 290, 91, 21))
        # self.label_4.setStyleSheet(_fromUtf8("font: 16pt \"Times New Roman\";"))
        self.label_4.setStyleSheet(_fromUtf8("font: 16pt \"Arial\";\n"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))


        self.lcdNumber_2 = QtGui.QLCDNumber(thirdDialog)
        self.lcdNumber_2.setGeometry(QtCore.QRect(470, 200, 121, 81))
        self.lcdNumber_2.setStyleSheet(_fromUtf8("border: 2px solid gray;\n""background-color: rgb(0, 0, 0);\n"))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lcdNumber_2.setPalette(palette)
        self.lcdNumber_2.setStyleSheet(_fromUtf8("background-color: blue;color:white"))
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))

        self.lcdNumber_2.display(parametros.todos['potenciaInicial'])

        self.pushButton_4 = QtGui.QPushButton(thirdDialog)
        self.pushButton_4.setGeometry(QtCore.QRect(640, 250, 61, 61))
        self.pushButton_4.setStyleSheet(_fromUtf8("font-weight:bold;background-color: blue;border-radius: 10px;"))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
             

        self.pushButton_5 = QtGui.QPushButton(thirdDialog)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 350, 151, 71))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.setStyleSheet("font-weight:bold;background-color: rgb(40, 255, 0); border-radius: 10px;")
        
        self.pushButton_6 = QtGui.QPushButton(thirdDialog)
        self.pushButton_6.setGeometry(QtCore.QRect(510, 350, 151, 71))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_6.setStyleSheet("font-weight:bold;background-color: red; border-radius: 10px;")
       
        self.label_8 = QtGui.QLabel(thirdDialog)
        self.label_8.setGeometry(QtCore.QRect(210, 280, 40, 13))
        self.label_8.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";\n"))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.label_9 = QtGui.QLabel(thirdDialog)
        self.label_9.setGeometry(QtCore.QRect(600, 280, 30, 13))
        self.label_9.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";\n"))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.retranslateUi(thirdDialog)
        #QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")),thirdDialog.close)

        QtCore.QMetaObject.connectSlotsByName(thirdDialog)

    def retranslateUi(self, thirdDialog):
        thirdDialog.setWindowTitle(_translate("thirdDialog", "Dialog", None))
        self.label_2.setText(_translate("thirdDialog", "POTÊNCIA ", None))
        self.pushButton.setText(_translate("thirdDialog", "+", None))
        self.pushButton_2.setText(_translate("thirdDialog", "-", None))
        self.label_3.setText(_translate("thirdDialog", "Referência", None))
        self.pushButton_3.setText(_translate("thirdDialog", "+", None))
        self.label_4.setText(_translate("thirdDialog", "Lida", None))
        self.pushButton_4.setText(_translate("thirdDialog", "-", None))
        self.pushButton_5.setText(_translate("thirdDialog", "INICIAR", None))
        self.pushButton_6.setText(_translate("thirdDialog", "PARAR", None))
        self.label_8.setText(_translate("thirdDialog", "W", None))
        self.label_9.setText(_translate("thirdDialog", "W", None))

        QtCore.QObject.connect(self.pushButton , QtCore.SIGNAL("clicked()") , self.initial_button_Plus_click)
        QtCore.QObject.connect(self.pushButton_2 , QtCore.SIGNAL("clicked()") , self.initial_button_Minus_click)
        #QtCore.QObject.connect(self.pushButton_3 , QtCore.SIGNAL("clicked()") , self.final_button_Plus_click)
        #QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL("clicked()") , self.final_button_Minus_click)
        QtCore.QObject.connect(self.pushButton_5 , QtCore.SIGNAL("clicked()") , self.iniciar_click)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL("clicked()") , self.parar_click)
        # QtCore.QObject.connect(self.pushButton_5 , QtCore.SIGNAL("clicked()") , self.update_Display)
 
    def initial_button_Plus_click(self):
        parametros.todos['potenciaInicial'] +=1
        self.lcdNumber.display(parametros.todos['potenciaInicial'])
        
    def initial_button_Minus_click(self):
        parametros.todos['potenciaInicial'] -=1 
        self.lcdNumber.display(parametros.todos['potenciaInicial'])
        
    def final_button_Plus_click(self):        
        parametros.todos['potenciaInicial'] += 1
        self.lcdNumber_2.display(parametros.todos['potenciaInicial'])
        parametros.todos['potenciaInicial']-=1
    
    def final_button_Minus_click(self):
        parametros.todos['potenciaInicial'] -=1 
        self.lcdNumber_2.display(parametros.todos['potenciaInicial'])
    
    def iniciar_click(self):
        print '========== New power set ==========='
        print parametros.todos['potenciaInicial']    
        if (RPI_ON):
            bus.write_byte_data(address, 0x44, parametros.todos['potenciaInicial'])
        # while 1 :
        #     print'========== update_Display ==========='
        #     self.lcdNumber_2.display(10)   
        #     # time.sleep(1)   
        # pass
            
    def parar_click(self):
        print'========== swithing off ADC ==========='
        if (RPI_ON):
            bus.write_byte_data(address, 0x44, 0X00)

class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        if (self.name == "GetPowerThread"):
            print 'getPower'
            getPower(self.name, 2)
        if (self.name == "DisplayThread"):
            print 'update_Display'
            update_Display(self.name,1)



def update_Display(threadname, delay):
    print'========== update_Display ==========='
    while 1 :
        print'========== update_Display ==========='
        ui.lcdNumber_2.display(parametros.todos['power'])   
        time.sleep(delay)   
        pass  

def getPower(threadname, delay):
    
    while (1):
        print '========== Reading V and I ==========='
        if (RPI_ON):
            bus.write_byte(address, 1)
            bus.read_byte(address)
            current = bus.read_byte(address)
            current = current*5/255 
            
            bus.write_byte(address, 2)
            bus.read_byte(address)
            voltage = bus.read_byte(address)
            voltage = voltage*5/255
                    
            print 'V %f ='% voltage
            print 'I %f=' %current

            try:
                impedancia = voltage/current
            except ZeroDivisionError:
                impedancia =10E9

            #impedancia = voltage/current
            power =  voltage*current
            parametros.todos['power'] = power

        time.sleep(delay)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    thirdDialog = QtGui.QDialog()
    ui = Ui_thirdDialog()
    ui.setupUi(thirdDialog)
    thirdDialog.show()
    print '========== newTread.. ==========='

    threadLock = threading.Lock()
    threads = []

    # Create new threads
    thread1 = myThread(1, "GetPowerThread")
    thread2 = myThread(2, "DisplayThread")

    # Start new Threads
    thread1.start()
    thread2.start()

    # Add threads to thread list
    threads.append(thread1)
    threads.append(thread2)
    # thread1.()
    # thread2.exit()

    sys.exit(app.exec_())
    
    


    # Wait for all threads to complete
    # for t in threads:
    #     t.join()
    # print "Exiting Main Thread"
    # # thread.start_new_thread( getPower, ("GetPowerThread", 2, ) )
    # thread.start_new_thread( update_Display, ("DisplayThread", 5, ) )
        

   


