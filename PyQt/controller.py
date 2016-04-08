# coding=utf-8
import math
import parametros
import logging

actuatorValue = 0
parametros.flag['impedance'] = False
parametros.flag['temperature'] = False

def getImpedance(measuredVoltage,measuredCurrent):

   if(measuredCurrent>0.0):
      impedance = measuredVoltage/measuredCurrent
      # print "Impedancia (ADC): " + str(impedance)
   else:
      impedance = "INF"
      parametros.flag['impedance'] = True
      print "Impedancia: INF"
   return impedance*10     # para colocar dentro do range necessario do AGC -PETE

#Teste Controle AGC - Peter
def controlAGC (measuredImpedance):

   if(measuredImpedance>=0 and measuredImpedance<=50):
      agc = 0
   elif(measuredImpedance>50 and measuredImpedance<=100):
      agc = 1
   elif(measuredImpedance>100 and measuredImpedance<=150):
      agc = 2
   elif(measuredImpedance>150 and measuredImpedance<=200):
      agc = 3
   elif(measuredImpedance>200 and measuredImpedance<=250):
      agc = 4
   else:
      agc = 5
   return agc


def getPower(measuredVoltage,measuredCurrent):
   power = measuredVoltage*measuredCurrent
   print power
   return power


def impedanceCalc(powerValue,measuredVoltage,measuredCurrent):
   print "Potencia Desejada: " + str(powerValue)
   print "Tensao Medida: " + str(measuredVoltage)
   print "Corrente Medida: " + str(measuredCurrent)
   if (measuredCurrent < 0.2) or (measuredVoltage<0.2): #Se a corrente for desprezível
      impedance = 50 # impedancia base (chutando impedancia)
   else:
      impedance = measuredVoltage/measuredCurrent
   print "Impedancia calculada: " + str(impedance) 
   newVoltage = math.sqrt(powerValue*impedance)
   return newVoltage

def applyVoltage(address,dacAddress,desiredValue):
   global actuatorValue
   if(desiredValue>255):
      desiredValue = 255
   elif(desiredValue<0):
      desiredValue = 0
   else:
      for x in xrange(0,10):
         try:
            actuatorValue += desiredValue
            bus.write_byte_data(address,dacAddress,desiredValue)
            break #sai do for se chegar aqui
         except Exception, e:
            logger.error('Erro na escrita do DAC', exc_info=True) 


def errorCalc(measuredValue,idealValue):

   dacResolution = 0.01960784314
   smallestError = 0.02

   print "Valor Medido: "+str(measuredValue)
   print "Valor Ideal: " + str(idealValue)


   measuredError = idealValue - measuredValue
   print "Erro Medido: " + str(measuredError)
   absError = abs(measuredError)
   print "Erro Medido(Abs): " + str(absError)
   errorBits = int(absError/dacResolution)
   print "Erro Medido(Bits): " + str(errorBits)


   if (absError<smallestError): #Erro menor que resolucao
      increment = 0 #Nada a fazer aqui
   else: #Erro pode ser corrigido
      if(absError>=5.0): #Caso o erro seja maior do que a saída máx. do DAC
         errorBits = 255
         increment = errorBits   
      elif(measuredError > 0.0): #Erro positivo
         print "Positive Error!"
         increment = errorBits
      elif(measuredError < 0.0): #Erro negativo
         print "Negative Error!"
         increment = -errorBits
      else:
         increment = 0
   print "Error (bits) modificado: " + str(increment)
   return increment

def controlImpedance(measuredImpedance):
   impMinValue = 0.5
   impMaxValue = 250
   if(measuredImpedance<impMinValue): #Impedancia muito baixa (Curto-circuito)
      parametros.flag['impedance'] = True
   elif(measuredImpedance>=impMaxValue): # Impedancia muito alta (Circuito aberto)
      parametros.flag['impedance'] = True
   else:
         parametros.flag['impedance'] = False
   return parametros.flag['impedance']

def controlTemperature(measuredTemperature):
   tempMaxValue = 30
   if(measuredTemperature>=tempMaxValue): # Temperatua muito alta
      parametros.flag['temperature'] = True
   else:
      parametros.flag['temperature'] = False      
   return parametros.flag['temperature']

# print controlAGC(251)
