# coding=utf-8
import math

def getImpedance(measuredVoltage,measuredCurrent):
   if (measuredCurrent < 0.2) or (measuredVoltage<0.2): #Se a corrente for desprezível
      impedance = 100 # impedancia base (chutando impedancia)
   else:
      impedance = measuredVoltage/measuredCurrent
      print impedance
      return impedance

def getPower(measuredVoltage,measuredCurrent):
   power = measuredVoltage*measuredCurrent
   print power
   return power


def impedanceCalc(powerValue,measuredVoltage,measuredCurrent):
   if (measuredCurrent < 0.2) or (measuredVoltage<0.2): #Se a corrente for desprezível
      impedance = 100 # impedancia base (chutando impedancia)
   else:
      impedance = measuredVoltage/measuredCurrent

   newVoltage = math.sqrt(powerValue*impedance)
   return newVoltage


def errorCalc(measuredValue,idealValue):

   dacResolution = 0.00390625
   smallestError = 0.02
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
