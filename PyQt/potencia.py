# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thirddialog.ui'
#
# Created: Wed Feb 24 15:04:30 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import parametros
import math, time
import thread
from threading import Thread, Lock


mutex = Lock()

RPI_ON = True
if (RPI_ON):
    import RPi.GPIO as GPIO
    import smbus
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    bus = smbus.SMBus(1)
    address = 0x48
    address2 = 0x48
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
        self.label_2.setGeometry(QtCore.QRect(240, 10, 301, 71))
        self.label_2.setStyleSheet(_fromUtf8("font: 26pt \"Arial\";\n""font-weight:bold;"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.lcdNumber = QtGui.QLCDNumber(thirdDialog)
        self.lcdNumber.setGeometry(QtCore.QRect(80, 200, 121, 81))
        self.lcdNumber.setStyleSheet(_fromUtf8("border: 2px solid gray;\n""background-color: rgb(0, 0, 0);\n"))
        self.lcdNumber.display(parametros.todos['potenciaInicial'])
        self.lcdNumber.setStyleSheet(_fromUtf8("background-color: blue;color:white"))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))

        self.lcdVoltage = QtGui.QLCDNumber(thirdDialog)
        self.lcdVoltage.setGeometry(QtCore.QRect(380, 110, 121, 81))
        self.lcdVoltage.setStyleSheet(_fromUtf8("background-color: blue;color:white"))

        self.lcdCurrent = QtGui.QLCDNumber(thirdDialog)
        self.lcdCurrent.setGeometry(QtCore.QRect(380, 250, 121, 81))
        self.lcdCurrent.setStyleSheet(_fromUtf8("background-color: blue;color:white"))
        


        

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


        # self.pushButton_3 = QtGui.QPushButton(thirdDialog)
        # self.pushButton_3.setFont(font)
        # self.pushButton_3.setGeometry(QtCore.QRect(640, 180, 61, 61))
        # self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        # self.pushButton_3.setStyleSheet("font-weight:bold;background-color: blue;border-radius: 10px;")
        # self.pushButton_3.setStyleSheet(_fromUtf8("border: 2px solid gray;\n""background-color: rgb(0, 0, 0);\n""color: rgb(0, 255, 0);\n""font: 30pt \"Arial\";"))


        self.label_4 = QtGui.QLabel(thirdDialog)
        self.label_4.setGeometry(QtCore.QRect(625, 80, 91, 21))
        # self.label_4.setStyleSheet(_fromUtf8("font: 16pt \"Times New Roman\";"))
        self.label_4.setStyleSheet(_fromUtf8("font: 16pt \"Arial\";\n"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))


        self.lcdNumber_2 = QtGui.QLCDNumber(thirdDialog)
        self.lcdNumber_2.setGeometry(QtCore.QRect(620, 110, 121, 81))
        self.lcdNumber_2.setStyleSheet(_fromUtf8("border: 2px solid gray;\n""background-color: rgb(0, 0, 0);\n"))
        self.lcdNumber_2.setStyleSheet(_fromUtf8("background-color: blue;color:white"))
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))

        self.lcdNumber_2.display(parametros.todos['potenciaInicial'])

        # self.pushButton_4 = QtGui.QPushButton(thirdDialog)
        # self.pushButton_4.setGeometry(QtCore.QRect(640, 250, 61, 61))
        # self.pushButton_4.setStyleSheet(_fromUtf8("font-weight:bold;background-color: blue;border-radius: 10px;"))
        # font = QtGui.QFont()
        # font.setPointSize(18)
        # self.pushButton_4.setFont(font)
        # self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))


        self.pushButton_5 = QtGui.QPushButton(thirdDialog)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 350, 151, 71))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.setStyleSheet("font-weight:bold;background-color: rgb(40, 255, 0); border-radius: 10px;")

        self.pushButton_6 = QtGui.QPushButton(thirdDialog)
        self.pushButton_6.setGeometry(QtCore.QRect(510, 350, 151, 71))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_6.setStyleSheet("font-weight:bold;background-color: red; border-radius: 10px;")

        self.label_8 = QtGui.QLabel(thirdDialog)
        self.label_8.setGeometry(QtCore.QRect(750, 180, 40, 13))
        self.label_8.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";\n"))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.label_9 = QtGui.QLabel(thirdDialog)
        self.label_9.setGeometry(QtCore.QRect(390, 215, 100, 30))
        self.label_9.setStyleSheet(_fromUtf8("font: 16pt \"Arial\";\n"))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.label_V = QtGui.QLabel(thirdDialog)
        self.label_V.setGeometry(QtCore.QRect(390, 70, 100, 40))
        self.label_V.setStyleSheet(_fromUtf8("font: 16pt \"Arial\";\n"))
        self.label_V.setObjectName(_fromUtf8("label_V"))


        self.lcdTemp = QtGui.QLCDNumber(thirdDialog)
        self.lcdTemp.setGeometry(QtCore.QRect(620, 250, 121, 81))
        self.lcdTemp.setStyleSheet(_fromUtf8("background-color: blue;color:white"))

        self.label_temp = QtGui.QLabel(thirdDialog)
        self.label_temp.setGeometry(QtCore.QRect(620, 215, 120, 30))
        self.label_temp.setStyleSheet(_fromUtf8("font: 16pt \"Arial\";\n"))
        self.label_temp.setObjectName(_fromUtf8("label_V"))

        self.retranslateUi(thirdDialog)
        #QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")),thirdDialog.close)

        QtCore.QMetaObject.connectSlotsByName(thirdDialog)

    def retranslateUi(self, thirdDialog):
        thirdDialog.setWindowTitle(_translate("thirdDialog", "Dialog", None))
        self.label_2.setText(_translate("thirdDialog", "Calibração ", None))
        self.pushButton.setText(_translate("thirdDialog", "+", None))
        self.pushButton_2.setText(_translate("thirdDialog", "-", None))
        self.label_3.setText(_translate("thirdDialog", "Referência", None))
        # self.pushButton_3.setText(_translate("thirdDialog", "+", None))
        self.label_4.setText(_translate("thirdDialog", "P. Lida", None))
        # self.pushButton_4.setText(_translate("thirdDialog", "-", None))
        self.pushButton_5.setText(_translate("thirdDialog", "INICIAR", None))
        self.pushButton_6.setText(_translate("thirdDialog", "PARAR", None))
        self.label_8.setText(_translate("thirdDialog", "W", None))
        self.label_9.setText(_translate("thirdDialog", "Corrente", None))
        self.label_V.setText(_translate("thirdDialog", "Voltagem", None))
        self.label_temp.setText(_translate("thirdDialog", "Temperatura", None))

        QtCore.QObject.connect(self.pushButton , QtCore.SIGNAL("clicked()") , self.initial_button_Plus_click)
        QtCore.QObject.connect(self.pushButton_2 , QtCore.SIGNAL("clicked()") , self.initial_button_Minus_click)
        #QtCore.QObject.connect(self.pushButton_3 , QtCore.SIGNAL("clicked()") , self.final_button_Plus_click)
        #QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL("clicked()") , self.final_button_Minus_click)
        QtCore.QObject.connect(self.pushButton_5 , QtCore.SIGNAL("clicked()") , self.iniciar_click)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL("clicked()") , self.parar_click)
        # QtCore.QObject.connect(self.pushButton_5 , QtCore.SIGNAL("clicked()") , self.update_Display)
     # t1 = Thread(target = getPower, args = ("nada",1))
    def initial_button_Plus_click(self):
        parametros.todos['potenciaInicial'] +=1
        self.lcdNumber.display(parametros.todos['potenciaInicial'])

    def initial_button_Minus_click(self):
        parametros.todos['potenciaInicial'] -=1
        if parametros.todos['potenciaInicial'] < 0:
            parametros.todos['potenciaInicial'] = 0
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
        # if (RPI_ON):
        #     try:
        #         bus.write_byte_data(address, 0x41, parametros.todos['potenciaInicial']*5)
        #     except Exception, e:
        #         raise e

    def parar_click(self):
        print'========== swithing off ADC ==========='
        parametros.todos['potenciaInicial'] = 0
        self.lcdNumber.display(parametros.todos['potenciaInicial'])
        if (RPI_ON):
            try:
                bus.write_byte_data(address, 0x41, 0X00)
            except Exception, e:
                raise e

def update_Display(threadname, delay):
    # print'========== update_Display ==========='

    while 1 :
        # print'========== update_Display ==========='
        mutex.acquire()
        ui.lcdNumber_2.display(parametros.todos['power'])
        # ui.lcdVoltage.display(parametros.todos['voltagem'])
        # ui.lcdCurrent.display(parametros.todos['corrente'])
        mutex.release()
        time.sleep(delay)
        pass
def setPower(threadname,delay):
    print '========== set Power==========='
    while  True:
        if (RPI_ON):
            for x in xrange(0,10):
                try:
                    bus.write_byte_data(address, 0x41, parametros.todos['potenciaInicial']*5)
                    break
                except Exception, e:
                    # raise e
                    print"erro com o ADC"
                time.sleep(0.5)
            
        time.sleep(delay)

def getPower(threadname, delay):

    while (1):
        print '========== Reading Power==========='
        for k in range (1,10):
            try:
                if (RPI_ON):
                    
                    mutex.acquire()
                    bus.write_byte(address, 1)
                    current = bus.read_byte(address)
                    current = bus.read_byte(address)
                    current = current*5.0/255.0
                    # current = current/10

                    bus.write_byte(address, 2)
                    # time.sleep(0.1)
                    voltage = bus.read_byte(address)
                    voltage = bus.read_byte(address)
                    mutex.release()
                    voltage = voltage*5.0/255.0
                    # voltage = voltage/10

                    print 'V %f ='% voltage
                    print 'I %f=' %current

                    impedancia = voltage/current
                    power =  voltage*current
                    parametros.todos['power'] = power
                    
                    ui.lcdCurrent.display(current)
                    ui.lcdVoltage.display(voltage)
                    break
            except ZeroDivisionError:
                impedancia =10E9
            except IOError as e:
                print "ADC I/O ERRO({0}): {1}".format(e.errno, e.strerror)
            time.sleep(0.5)


            #impedancia = voltage/current

        time.sleep(delay)
def getTemp(threadname, delay):
    while (1):
        print '========== Reading temperatura ==========='
        if (RPI_ON):
            mutex.acquire()
            bus.write_byte(address, 0)
            bus.read_byte(address)
            temp_aux = bus.read_byte(address)
            mutex.release()
            temperatura = 0.6040*temp_aux-72.9358
            parametros.todos['temperatura'] = temperatura
            ui.lcdCurrent.display(temperatura)
        time.sleep(delay)

    if not thread.isAlive():
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(thread.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")





if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    thirdDialog = QtGui.QDialog()
    ui = Ui_thirdDialog()
    ui.setupUi(thirdDialog)
    thirdDialog.show()
    print '========== newTread.. ==========='
    
    t1 = Thread(target = getPower, args = ("GetPowerThread",1))
    t2 = Thread(target = update_Display, args = ("DisplayThread",1))
    t3 = Thread(target = getTemp, args = ("TempThread",1))
    t4 = Thread(target = setPower, args = ("SetPowerThread",0.001))

    t1.daemon = True
    t2.daemon = True
    t3.daemon = True
    t4.daemon = True

    t1.start()
    t2.start()
    # t3.start()
    t4.start()
    sys.exit(app.exec_())
       