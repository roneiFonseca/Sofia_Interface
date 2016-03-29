# coding=utf-8

from __future__ import division
import smbus
import time
import os

bus = smbus.SMBus(1)
address2 = 0x48
address1 = 0x4c
# voltageValue =128

while True:

	bus.write_byte(address1, 0) #Requisitando leitura do Canal 0 do PCF8591 (1)
	voltageValue1 = bus.read_byte(address2) #Realizando leitura do Canal 0 do PCF8591 (1)
	time.sleep(0.5)
	bus.write_byte(address2, 0) #Requisitando leitura do Canal 0 do PCF8591 (1)
	voltageValue2 = bus.read_byte(address1) #Realizando leitura do Canal 0 do PCF8591 (1)
	# time.sleep(0.5)
	print "Tensão (0x48): " + str(voltageValue1)
	print "Tensão (0x4c): " + str(voltageValue2)
	# bus.write_byte_data(address1, 0x44,voltageValue)





