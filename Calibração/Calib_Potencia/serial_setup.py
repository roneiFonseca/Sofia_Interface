#!/usr/bin/env python
          
import time
import serial
from serial import SerialException

def serial_setup():
  conected_flag = False

  try:
    print 'Tentnado conexcao com VERA...'
    ser = serial.Serial(
    port= '/dev/ttyAMA0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
  )

  except Exception as e:
    # raise e
    print "ERRO NA CONEXAO SERIAL I/O ERRO({0}): {1}".format(e.errno, e.strerror)
    return conected_flag
  
  print 'Conexao estabelicida.'
  conected_flag = True
  return conected_flag
