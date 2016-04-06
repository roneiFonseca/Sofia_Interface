# coding=utf-8

from __future__ import division
import smbus
import time
import controller
import math

bus = smbus.SMBus(1)
address2 = 0x48
address1 = 0x49
# voltageValue =128
actuator = 0

while True:

	bus.write_byte(address1, 0) #Requisitando leitura do Canal 0 do PCF8591 (1)
	bus.read_byte(address1)
	tempValue = bus.read_byte(address1) #Realizando leitura do Canal 0 do PCF8591 (1)
	# Corrente
	bus.write_byte(address1, 1) #Requisitando leitura do Canal 0 do PCF8591 (1)
	bus.read_byte(address1)
	currentValue = bus.read_byte(address1) #Realizando leitura do Canal 0 do PCF8591 (1)
	currentValue = (currentValue/255.0)*5.0
	# Tensao
	bus.write_byte(address1, 2) #Requisitando leitura do Canal 0 do PCF8591 (1)
	bus.read_byte(address1)
	voltageValue = bus.read_byte(address1) #Realizando leitura do Canal 0 do PCF8591 (1)
	voltageValue = (voltageValue/255.0)*5.0
	time.sleep(1.0)
	print "Temperatura: " + str(tempValue)
	print "Corrente: " + str(currentValue)
	print "Tensão: " + str(voltageValue)

	
	while actuator<255:
		# actuator = raw_input("Valor para DAC: ")
		actuator += 1
		bus.write_byte_data(address2, 0x44, int(actuator))
	while actuator >0:
		actuator -=1
		bus.write_byte_data(address2, 0x44, int(actuator))





