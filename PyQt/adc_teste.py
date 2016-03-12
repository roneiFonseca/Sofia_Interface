from __future__ import division
import smbus
import time
import os

bus = smbus.SMBus(1)

try:

   while True:

         bus.write_byte(0x48, 0)
         x = bus.read_byte(0x48)
         y = (3/5)*x-73
         print('Temperatura: ' + str(y))
         time.sleep(0.5)
	 os.system('clear')
except:
   pass



