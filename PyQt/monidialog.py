# -*- coding: utf-8 -*-

################################### LIBRARIES ###############################################
from __future__ import division
from PyQt4 import QtCore, QtGui
import sys
import parametros
import controller
import time
import math
import os
import logging
#############################################################################################



################################### SET-UP ##################################################
#configurando arquivo de log
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#criando handler file
handler = logging.FileHandler('Teste.log')
handler.setLevel(logging.INFO)
#Formatacao das mensagens de log
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

#configurando o Log para printar no terminal
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

RPI_ON = False

if (RPI_ON):
    import RPi.GPIO as GPIO
    import smbus
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.output(24, 1)        #ajusta os reles
    GPIO.output(23, 1)
    #Teste de relés utilizando LEDS (Matias e Peter 2/4/16)
    GPIO.setup(19,GPIO.OUT)
    GPIO.setup(26,GPIO.OUT)
    GPIO.output(19,0)
    GPIO.output(26,0)

    #Teste controle AGC (Peter 5/4/16)
    #Entrada de controle
    GPIO.setup(16,GPIO.OUT)
    GPIO.setup(20,GPIO.OUT)
    GPIO.setup(21,GPIO.OUT)
    GPIO.output(16,0)
    GPIO.output(20,0)
    GPIO.output(21,0)
    #Saida de controle - Reles
    GPIO.setup(5,GPIO.OUT)
    GPIO.setup(6,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
    GPIO.output(5,0)
    GPIO.output(6,0)
    GPIO.output(13,0)
#############################################################################################



################################### GLOBAL VARIABLES #########################################
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
teste = 22


#flag de monitoramento de erro
parametros.flag['callErrorWindow'] = False

#Contadores do Step Down de Potencia
stepDownTop = 0
stepDownBottom = 0


actuatorValue = 0

if (RPI_ON):
    bus = smbus.SMBus(1)
    address1 = 0x48
    address2 = 0x49
#############################################################################################



################################### ERROR TREATMENT #########################################
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
#############################################################################################


################################### UI_MONIDIALOG ###########################################
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
        self.lcd_imp.setStyleSheet(_fromUtf8("alternate-background-color: rgb(0, 0, 0);background-color: blue;"))
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

        QtCore.QMetaObject.connectSlotsByName(moniDialog)


    def retranslateUi(self):
        self.setWindowTitle(_translate("moniDialog", "Dialog", None))
        self.label_2.setText(_translate("moniDialog", "TELA DE MONITORAMENTO", None))
        self.label_14.setText(_translate("moniDialog", "min", None))

        self.pushButton_7.setText(_translate("moniDialog", "INICIAR ", None))
        self.label_20.setText(_translate("moniDialog", "ºC", None))
        self.pushButton_8.setText(_translate("moniDialog", "DESLIGAR", None))
        self.label_23.setText(_translate("moniDialog", "W", None))
        self.label_24.setText(_translate("moniDialog", "Ω", None))
        QtCore.QObject.connect(self.pushButton_7 , QtCore.SIGNAL("clicked()") , self.start)
        self.lcd_temp.display("---")
        self.lcd_imp.display("---")
        self.label_15.setText(_translate("moniDialog", "Modo de Operação: Aguardando INICIAR", None))
        self.lcd_potencia.display(parametros.todos['potenciaInicial'])

    def control(self):
        global time_before, time_beginning, minute, stop_press, initial_press,time_old, restart, time_off, time_now, cont
        global stepDownTop,stepDownBottom
        if(RPI_ON):
            global bus, address, actuatorValue
        self.pushButton_7.setText(_translate("moniDialog", "PARAR ", None))
        self.pushButton_7.setStyleSheet("font-weight:bold;background-color: red;border-radius: 10px;")

        # self.lcd_potencia.display(parametros.todos['potenciaRT']*5)
        # if(RPI_ON):
        #     bus.write_byte_data(address1, 0x44, parametros.todos['potenciaRT']*5)


        # self.lcd_potencia.display(parametros.todos['potenciaRT']*1)

        cont += 1
        if cont == 60:

            if(RPI_ON):
                for x in xrange(0,10):
                    try:
                        #Leitura de Tensão
                        bus.write_byte(address2, 0)
                        bus.read_byte(address2)
                        voltage = bus.read_byte(address2)
                        voltage = voltage*5/255
                        callErrorWindow = False
                        break #sai do for se chegar aqui
                    except Exception, e:
                        logger.error('Erro na leitura ADC Tensao', exc_info=True)
                        callErrorWindow = True

                if(callErrorWindow):
                    logger.error('Nao foi possivel realizar a leitura da Tensao - ADC')
                    os.system("sudo /usr/bin/python error_window.py")  #inumeros problemas com a execução de GUI em uma interrupçao, optou-se por executar o codigo referente a janela de erro.
                    GPIO.cleanup()
                    moniDialog.close()


                for x in xrange(0,10):
                    try:
                        #Leitura de corrente
                        bus.write_byte(address2, 1)
                        bus.read_byte(address2)
                        current = bus.read_byte(address2)
                        current = current*5/255
                        callErrorWindow = False
                        break #sai do for se chegar aqui
                    except Exception, e:
                        logger.error('Erro na leitura ADC Corrente', exc_info=True)
                        callErrorWindow = True

                if(callErrorWindow):
                    logger.error('Nao foi possivel realizar a leitura da Corrente - ADC')
                    os.system("sudo /usr/bin/python error_window.py")  #inumeros problemas com a execução de GUI em uma interrupçao, optou-se por executar o codigo referente a janela de erro.
                    GPIO.cleanup()
                    moniDialog.close()


                for x in xrange(0,10):
                    try:
                        #Leitura de Temperatura
                        bus.write_byte(address2, 2)
                        bus.read_byte(address2)
                        temp_aux = bus.read_byte(address2)
                        temperature = 0.6040*temp_aux-72.9358
                        self.lcd_temp.display(temperature)
                        callErrorWindow = False
                        break #sai do for se chegar aqui
                    except Exception, e:
                        logger.error('Erro na leitura ADC Temperatura', exc_info=True)
                        callErrorWindow = True

                if(callErrorWindow):
                    logger.error('Nao foi possivel realizar a leitura da Temperatura - ADC')
                    os.system("sudo /usr/bin/python error_window.py")  #inumeros problemas com a execução de GUI em uma interrupçao, optou-se por executar o codigo referente a janela de erro.
                    GPIO.cleanup()
                    moniDialog.close()


                impedance = controller.getImpedance(voltage,current) #calculando impedancia
                #Teste controle AGC (Peter 5/4/16)
                agc = controller.controlAGC(impedance)
                print agc
                if(agc == 0):
                    GPIO.output(16,0)
                    GPIO.output(20,0)
                    GPIO.output(21,0)
                    GPIO.output(5,0)
                    GPIO.output(6,0)
                    GPIO.output(13,0)
                elif(agc == 1):
                    GPIO.output(16,0)
                    GPIO.output(20,0)
                    GPIO.output(21,1)
                    GPIO.output(5,0)
                    GPIO.output(6,0)
                    GPIO.output(13,1)
                elif(agc == 2):
                    GPIO.output(16,0)
                    GPIO.output(20,1)
                    GPIO.output(21,0)
                    GPIO.output(5,0)
                    GPIO.output(6,1)
                    GPIO.output(13,0)
                elif(agc == 3):
                    GPIO.output(16,0)
                    GPIO.output(20,1)
                    GPIO.output(21,1)
                    GPIO.output(5,0)
                    GPIO.output(6,1)
                    GPIO.output(13,1)
                elif(agc == 4):
                    GPIO.output(16,1)
                    GPIO.output(20,0)
                    GPIO.output(21,0)
                    GPIO.output(5,1)
                    GPIO.output(6,0)
                    GPIO.output(13,0)
                else:
                    print "Valor de Impedancia fora de range - AGC"
                    logger.warn('Valor de Impedancia fora de range - AGC')
                power =  controller.getPower(voltage,current) #calculando potencia
                self.lcd_imp.display(impedance) #Print Impedancia
                self.lcd_potencia.display(power) #Print power

            #CONTROLE DE TENSAO
            #Calculando o novo valor de tensao que deve ser colocado
                newVoltage = controller.impedanceCalc(parametros.todos['potenciaRT'],voltage,current)
                actuatorValue += controller.errorCalc(voltage,newVoltage)
                print "Tensao de Entrada: " +str(actuatorValue)
                if (actuatorValue < 0):
                    actuatorValue = 0
                elif(actuatorValue>255):
                    actuatorValue = 255
                else:
                    pass
                if(RPI_ON):
                    for x in xrange(0,10):
                        try:
                            bus.write_byte_data(address1, 0x44, actuatorValue)
                            time.sleep(1.0)
                            print "Tensao de Entrada(modificada): " +str(actuatorValue) #depois das condicoes
                            callErrorWindow = False
                            break #sai do for se chegar aqui
                        except Exception, e:
                            logger.error('Erro na escrita do DAC', exc_info=True)
                            callErrorWindow = True

                    if(callErrorWindow):
                        logger.error('Nao foi possivel realizar a escrita no DAC')
                        os.system("sudo /usr/bin/python error_window.py")  #inumeros problemas com a execução de GUI em uma interrupçao, optou-se por executar o codigo referente a janela de erro.
                        GPIO.cleanup()
                        moniDialog.close()


            #CONTROLE DE TEMPERATURA
                if (controller.controlTemperature(temperature)):
                    GPIO.output(19,1)                     #ATIVAR RELÉ DE TEMPERATURA
                    print "TEMPERATURA MÁXIMA"
                    logger.warn('Temperarura muito alta - %s',temperature)
                    if(controller.controlImpedance(impedance)):
                        GPIO.output(26,1)         #ATIVAR RELÉ DE IMPEDÂNCIA (DESLIGAR APARELHO)
                        print "IMPEDANCIA MUITO ALTA/BAIXA"
                        logger.warn('Nivel de Impedancia muito Alto/Baixo - %s',impedance)
                        self.timer.stop()
                    else:
                        print "IMPEDANCIA OK!"
                        GPIO.output(26,0)         #DESATIVAR RELÉ DE POTÊNCIA (DESLIGAR APARELHO)
                        if(parametros.todos['potenciaRT']>=parametros.todos['potenciaStep']): # Nao diminuir step caso potencia seja 0
                            if(not(parametros.flag['stepDown'])):
                                parametros.todos['potenciaRT'] -= parametros.todos['potenciaStep']
                                parametros.flag['stepDown'] = True # Significa que a potência já foi abaixada
                                stepDownTop = time.time() # Começa a contar
                                stepDownBottom = stepDownTop
                            else:
                                stepDownTop = time.time()
                                if (stepDownTop - stepDownBottom > 1.0):
                                    parametros.flag['stepDown'] = False #Libera para mais um step-Down
                else:
                    print "TEMPERATURA OK!"
                    GPIO.output(19,0)                     #DESATIVAR RELÉ DE IMPEDÂNCIA

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

        #Atualizando o valor de potenciaRT
        if ( time_now - time_before > float(parametros.todos['tempoStep']*60) ) and (parametros.todos['potenciaRT']<parametros.todos['potenciaFinal']):
            if (minute == parametros.todos['tempo']) and (seconds == 0): #Verificação do Fim da Operação
                # definir o protocolo de desligamento do aparelho quando o tempo acaba
                parametros.flag['endOfOperation'] = True # Flag do fim da operacao
                self.timer.stop() #"Desligar"
            else:
                parametros.todos['potenciaRT'] += parametros.todos['potenciaStep']
            time_before = time_now #Atualizar contagem

        #CONTROLE DE IMPEDÂNCIA
        if cont == 60: #Esta verificacao é feita a cada 60 ms
            if(controller.controlImpedance(impedance)):
                print "IMPEDANCIA MUITO ALTA/BAIXA"
                logger.warn('Nivel de Impedancia muito Alto/Baixo - %s',impedance)
                GPIO.output(26,1)         #ATIVAR RELÉ DE POTÊNCIA (DESLIGAR APARELHO)
                #self.timer.stop() #"Desligar"
            else:
                print "IMPEDANCIA OK!"
                GPIO.output(26,0)         #DESATIVAR RELÉ DE POTÊNCIA (DESLIGAR APARELHO)
            cont = 0


    def stop(self):
        global time_before, stop_press,initial_press, time_old,restart,time_off,time_now
        logger.info('Operação pausada')
        logger.info('Potencia RT: %s  Tempo: %s  Modo: %s',parametros.todos['potenciaRT'],parametros.todos['tempo'],parametros.todos['modo'])
        self.pushButton_7.setText(_translate("moniDialog", "INICIAR ", None))
        self.pushButton_7.setStyleSheet("font-weight:bold;background-color: rgb(40, 255, 0);border-radius: 10px;")
        time_old = time_now
        self.timer.stop()

        #seta as flags usadas
        time_off = 0
        stop_press = 1
        initial_press = 0
        restart = 1


    def start(self):
        global time_before,time_beginning,stop_press, initial_press,pwm_pin1
        global RPI_ON

        logger.info('Operação iniciada')
        logger.info('Potencia Inicial: %s  Potencia Final: %s  Step de Potencia: %s  Tempo: %s  Step de Tempo: %s  Modo: %s',parametros.todos['potenciaInicial'],parametros.todos['potenciaFinal'],parametros.todos['potenciaStep'],parametros.todos['tempo'],parametros.todos['tempoStep'],parametros.todos['modo'])

        if((initial_press == 0) and (stop_press == 1)) :               #condicao para reiniciar a contagem
            self.timer.start(1) #1 miliseconds

        if ((initial_press == 1) and (stop_press == 1)):                #condicao para o primeiro acionamento
            self.label_15.setText(_translate("moniDialog", "Modo de Operação: " + str (parametros.todos['modo']), None))
            self.label_15.setGeometry(QtCore.QRect(280, 280, 300, 90))
            time_before = time.time()
            time_beginning = time_before
            self.timer.start(1) #1 miliseconds

        if stop_press != 1:                                             #condicao para parar a contagem
            self.stop()
            if(RPI_ON):
                for x in xrange(0,10):
                    try:
                        bus.write_byte_data(address1, 0x44, 0X00)
                        callErrorWindow = False
                        break #sai do for se chegar aqui
                    except Exception, e:
                        logger.error('Erro na escrita do DAC', exc_info=True)
                        callErrorWindow = True

                if(callErrorWindow):
                    logger.error('Nao foi possivel realizar a escrta no DAC')
                    os.system("sudo /usr/bin/python error_window.py")  #inumeros problemas com a execução de GUI em uma interrupçao, optou-se por executar o codigo referente a janela de erro.
                    GPIO.cleanup()
                    moniDialog.close()


    def shutdown_function(self):

        GPIO.output(24, 0)        #ajusta os reles
        GPIO.output(23, 0)

        ui.timer.stop()           #para o clock
        ui.Reset_Parameters()     #coloca as variaveis no padrao default


        print "Aumento súbito de corrente. Verifique IRF540 e se o circuito está em aberto."
        logger.warn('Aumento súbito de corrente. Verifique IRF540 e se o circuito está em aberto')
        os.system("sudo /usr/bin/python error_window.py")  #inumeros problemas com a execução de GUI em uma interrupçao, optou-se por executar o codigo referente a janela de erro.
        GPIO.cleanup()
        moniDialog.close()



    def Reset_Parameters(self):
        global time_before,time_beginning,minute,stop_press,initial_press,time_old,restart,time_off,time_now


        if(RPI_ON):
            for x in xrange(0,10):
                try:
                    bus.write_byte_data(address1, 0x44, 0X00)
                    callErrorWindow = False
                    break #sai do for se chegar aqui
                except Exception, e:
                    logger.error('Erro na escrita do DAC', exc_info=True)
                    callErrorWindow = True

            if(callErrorWindow):
                logger.error('Nao foi possivel realizar a escrita no DAC')
                os.system("sudo /usr/bin/python error_window.py")  #inumeros problemas com a execução de GUI em uma interrupçao, optou-se por executar o codigo referente a janela de erro.
                GPIO.cleanup()
                moniDialog.close()



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
        parametros.todos['tempo']=1
        parametros.todos['tempoStep']=1
        parametros.todos['modo'] = 1

    if(RPI_ON):
        GPIO.add_event_detect(17, GPIO.FALLING, callback=shutdown_function)
#############################################################################################



################################### MAIN ####################################################
# if __name__ == "__main__":
#     app = QtGui.QApplication(sys.argv)
#     moniDialog = QtGui.QDialog()
#     ui = Ui_moniDialog()
#     ui.setupUi(moniDialog)
#############################################################################################
