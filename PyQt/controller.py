# coding=utf-8
import math

actuatorValue = 0

def getImpedance(measuredVoltage,measuredCurrent):

   if(measuredCurrent>0.0):
      impedance = measuredVoltage/measuredCurrent
      # print "Impedancia (ADC): " + str(impedance)
      return impedance
   else:
      impedance = "INF"
      # print "Impedancia: INF"
      return impedance

def getPower(measuredVoltage,measuredCurrent):
   power = measuredVoltage*measuredCurrent
   print power
   return power


def impedanceCalc(powerValue,measuredVoltage,measuredCurrent):
   print "Potencia Desejada: " + str(powerValue)
   print "Tensao Medida: " + str(measuredVoltage)
   print "Corrente Medida: " + str(measuredCurrent)
   if (measuredCurrent < 0.2) or (measuredVoltage<0.2): #Se a corrente for desprezível
      impedance = 100 # impedancia base (chutando impedancia)
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
      actuatorValue += desiredValue
      bus.write_byte_data(address,dacAddress,desiredValue)


def errorCalc(measuredValue,idealValue):

   dacResolution = 0.01960784314
   smallestError = 0.02
<<<<<<< HEAD

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

   return increment

print errorCalc(5.0,2.5)
=======
   while(absError > smallestError)
      print "Valor Medido: "+str(measuredValue)
      print "Valor Ideal: " + str(idealValue)

      measuredError = idealValue - measuredValue
      print "Erro Medido: " + str(measuredError)
      absError = abs(measuredError)
      print "Erro Medido(Abs): " + str(absError)
      errorBits = (absError//dacResolution)
      print "Erro Medido(Bits): " + str(errorBits)
   

      if (absError<smallestError): #Erro menor que resolucao
         increment = 0 #Nada a fazer aqui
      elif(absError>=5.0): #Caso o erro seja maior do que a saída máx. do DAC
         errorBits = 255
         increment = errorBits   
      elif(measuredError > 0.0): #Erro positivo
         increment = errorBits
      elif(measuredError < 0.0): #Erro negativo
         increment = -errorBits
      else:
         increment = 0

      bus.write_byte_data(address, 0x44, increment)#Atualiza o ADC

   return increment
>>>>>>> origin/master
