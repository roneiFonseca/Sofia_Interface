# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monidialog.ui'
#
# Created: Wed Feb 24 16:46:35 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!




from __future__ import division
from PyQt4 import QtCore, QtGui
from thirddialog import Ui_thirdDialog
import sys 
import parametros
import time
import math
RPI_ON = False;
if (RPI_ON):
    import RPi.GPIO as GPIO
    import smbus

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

time_before= 0 
time_beginning = 0
minute = 0
stop_press = 1
initial_press = 1
time_old = 0
restart = 0
time_off = 0
time_now = 0
cont = 0

if (RPI_ON):
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

class Ui_moniDialog(object):
    def setupUi(self, moniDialog):
        moniDialog.setObjectName(_fromUtf8("moniDialog"))
        moniDialog.resize(800, 480)
        moniDialog.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);color:white"))
        self.label_2 = QtGui.QLabel(moniDialog)
        self.label_2.setGeometry(QtCore.QRect(170, 50, 441, 71))
        self.label_2.setStyleSheet(_fromUtf8("font: 22pt \"Arial\";font-weight:bold;"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_14 = QtGui.QLabel(moniDialog)
        self.label_14.setGeometry(QtCore.QRect(760, 240, 47, 13))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(_fromUtf8("font: 75 12pt \"Arial\";"))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(moniDialog)
        self.label_15.setGeometry(QtCore.QRect(168, 280, 500, 90))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_15.setStyleSheet("font-weight:bold;")
        self.pushButton_7 = QtGui.QPushButton(moniDialog)
        self.pushButton_7.setGeometry(QtCore.QRect(450, 400, 181, 51))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_7.setStyleSheet("font-weight:bold;background-color: rgb(40, 255, 0);border-radius: 10px;")
        self.label_20 = QtGui.QLabel(moniDialog)
        self.label_20.setGeometry(QtCore.QRect(550, 240, 55, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(_fromUtf8("font: 75 12pt \"Arial\";"))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.lcd_tempo = QtGui.QLCDNumber(moniDialog)
        self.lcd_tempo.setGeometry(QtCore.QRect(640, 180, 111, 81))
        self.lcd_tempo.setStyleSheet(_fromUtf8("background-color: blue;"))
        self.lcd_tempo.setObjectName(_fromUtf8("lcd_tempo"))
        self.pushButton_8 = QtGui.QPushButton(moniDialog)
        self.pushButton_8.setGeometry(QtCore.QRect(160, 400, 181, 51))
        self.pushButton_8.setStyleSheet(_fromUtf8("font-weight:bold;background-color: red;border-radius: 10px;"))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.lcd_temp = QtGui.QLCDNumber(moniDialog)
        self.lcd_temp.setGeometry(QtCore.QRect(430, 180, 111, 81))
        self.lcd_temp.setStyleSheet(_fromUtf8("background-color: blue;"))
        self.lcd_temp.setObjectName(_fromUtf8("lcd_temp"))
        self.lcd_imp = QtGui.QLCDNumber(moniDialog)
        self.lcd_imp.setGeometry(QtCore.QRect(220, 180, 111, 81))
       
        self.lcd_imp.setStyleSheet(_fromUtf8("alternate-background-color: rgb(0, 0, 0);\n"
"background-color: blue;"))
        self.lcd_imp.setObjectName(_fromUtf8("lcd_imp"))
        self.label_23 = QtGui.QLabel(moniDialog)
        self.label_23.setGeometry(QtCore.QRect(150, 240, 55, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(_fromUtf8("font: 75 12pt \"Arial\";"))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_24 = QtGui.QLabel(moniDialog)
        self.label_24.setGeometry(QtCore.QRect(340, 240, 55, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(_fromUtf8("font: 75 12pt \"Arial\";"))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.lcd_potencia = QtGui.QLCDNumber(moniDialog)
        self.lcd_potencia.setGeometry(QtCore.QRect(30, 180, 111, 81))
        self.lcd_potencia.setStyleSheet(_fromUtf8("background-color:blue;"))
        self.lcd_potencia.setObjectName(_fromUtf8("lcd_potencia"))
        self.timer = QtCore.QTimer(moniDialog)
        self.timer.timeout.connect(self.control)


        self.retranslateUi(moniDialog)



        QtCore.QMetaObject.connectSlotsByName(moniDialog)
    

    def retranslateUi(self, moniDialog):
        moniDialog.setWindowTitle(_translate("moniDialog", "Dialog", None))
        self.label_2.setText(_translate("moniDialog", "TELA DE MONITORAMENTO", None))
        self.label_14.setText(_translate("moniDialog", "min", None))
        
        self.pushButton_7.setText(_translate("moniDialog", "INICIAR ", None))
        self.label_20.setText(_translate("moniDialog", "ºC", None))
        self.pushButton_8.setText(_translate("moniDialog", "DESLIGAR", None))
        self.label_23.setText(_translate("moniDialog", "W", None))
        self.label_24.setText(_translate("moniDialog", "Ω", None))
        QtCore.QObject.connect(self.pushButton_7 , QtCore.SIGNAL("clicked()") , self.start)
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")),self.Reset_Parameters)
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")),moniDialog.close)
        self.lcd_temp.display("---")
        self.lcd_imp.display("---")
        self.label_15.setText(_translate("moniDialog", "Modo de Operação: Aguardando INICIAR", None))
        self.lcd_potencia.display(parametros.todos['potenciaInicial'])

    

    def control(self):
        global time_before, time_beginning, minute, stop_press, initial_press,time_old, restart, time_off, time_now, cont
        if(RPI_ON):
            global bus, address
        self.pushButton_7.setText(_translate("moniDialog", "PARAR ", None))
        self.pushButton_7.setStyleSheet("font-weight:bold;background-color: red;border-radius: 10px;")
        # self.lcd_potencia.display(parametros.todos['potenciaRT'])

        cont += 1

        if cont == 60:


            bus.write_byte(address, 0)
            bus.read_byte(address)
            temp_aux = bus.read_byte(address)
            temperatura = 0.6040*temp_aux-72.9358
	        self.lcd_temp.display(temperatura) 

            bus.write_byte(address, 1)
            bus.read_byte(address)
            current = bus.read_byte(address)
	        current = current*5/255	

            bus.write_byte(address, 2)
	        bus.read_byte(address)
            voltage = bus.read_byte(address)
            voltage = voltage*5/255

            if(RPI_ON):
                bus.write_byte(address, 0)
                temp_aux = bus.read_byte(address)
                temperatura = 0.6040*temp_aux-72.9358
                self.lcd_temp.display(temperatura) 
            if(RPI_ON):
                bus.write_byte(address, 1)
                current = bus.read_byte(address)
                bus.write_byte(address, 2)
                voltage = bus.read_byte(address)

            impedancia = voltage/current
            power =  voltage*current
            
            self.lcd_imp.display(impedancia)
            self.lcd_potencia.display(power)
	   
            if(RPI_ON):
                bus.write_byte_data(address, 0x44, parametros.todos['potenciaRT']*5)
            cont = 0 

        if restart == 0:
            time_now = time.time() - time_off
            seconds = round(time_now - time_beginning,0)
           
        if restart == 1 :
            time_off = time.time() - time_old   #duracao do botao desligado
            time_now = time_old                  #ultimo tempo no qual botao foi desligado
            seconds = round(time_now - time_beginning,0)
           
            restart = 0
            time_old = 0
          
        stop_press = seconds
        if seconds >= 60:
            minute +=1
            time_beginning = time_now
        if seconds < 10:
            str_count = str(minute) + ':0' + str(int(seconds))

        else:
            str_count = str(minute) + ':' + str(int(seconds))
        self.lcd_tempo.display(str_count)
          
        if ( time_now - time_before > float(parametros.todos['tempoStep']*60) ) and (parametros.todos['potenciaRT']<parametros.todos['potenciaFinal']):
            parametros.todos['potenciaRT'] += parametros.todos['potenciaStep']
            print time_now - time_before
            print float(parametros.todos['tempoStep']*60)
           
            time_before = time_now

        if (minute == parametros.todos['tempo']) and (seconds == 0):
            # definir o protocolo de desligamento do aparelho quando o tempo acaba
            self.timer.stop()


    def stop(self):
        global time_before, stop_press,initial_press, time_old,restart,time_off,time_now
        self.pushButton_7.setText(_translate("moniDialog", "INICIAR ", None))
        self.pushButton_7.setStyleSheet("font-weight:bold;background-color: rgb(40, 255, 0);border-radius: 10px;")
      

        self.timer.stop()
       
        #seta as flags usadas
        time_off = 0
        stop_press = 1
        initial_press = 0
        restart = 1


    def start(self):
        global time_before,time_beginning,stop_press, initial_press,pwm_pin1
        global RPI_ON
       
        if(RPI_ON):
            bus.write_byte_data(address, 0x44, parametros.todos['potenciaRT']*5)

        if((initial_press == 0) and (stop_press == 1)) :               #condicao para reiniciar a contagem
             self.timer.start(1)
        
        if ((initial_press == 1) and (stop_press == 1)):                #condicao para o primeiro acionamento
            self.label_15.setText(_translate("moniDialog", "Modo de Operação: " + str (parametros.todos['modo']), None))
            self.label_15.setGeometry(QtCore.QRect(280, 280, 300, 90))
            time_before = time.time()
            time_beginning = time_before
            self.timer.start(1)
           
        if stop_press != 1:                                             #condicao para parar a contagem
            self.stop()
            if(RPI_ON):
                bus.write_byte_data(address, 0x44, 0X00)
           

    def Reset_Parameters(self):
        global time_before,time_beginning,minute,stop_press,initial_press,time_old,restart,time_off,time_now
       
        if(RPI_ON):
            bus.write_byte_data(address, 0x44, 0X00)
        time_before= 0 
        time_beginning = 0
        minute = 0
        stop_press = 1
        initial_press = 1
        time_old = 0
        restart = 0
        time_off = 0
        time_now = 0
        parametros.todos['potenciaInicial']= 0
        parametros.todos['potenciaRT']= 0
        parametros.todos['potenciaStep']=2 
        parametros.todos['potenciaFinal']= 20
        parametros.todos['tempo']=10
        parametros.todos['tempoStep']=1 
        parametros.todos['modo'] = 1
    
    def shutdown_function():
        print "oiiiiii"
    


    GPIO.add_event_detect(17, GPIO.FALLING, callback=shutdown_function) 
        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    moniDialog = QtGui.QDialog()
    ui = Ui_moniDialog()
    ui.setupUi(moniDialog)
    moniDialog.show()
    sys.exit(app.exec_())
