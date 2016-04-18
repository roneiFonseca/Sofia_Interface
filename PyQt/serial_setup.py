#!/usr/bin/env python
          
import time
import serial
from serial import SerialException

def serial_setup():
  conected_flag = False
  for x in xrange(0,10):
    try:
      print 'Tentando conexao com VERA...'
      ser = serial.Serial(
      port= '/dev/ttyAMA0',
      baudrate = 9600,
      parity=serial.PARITY_NONE,
      stopbits=serial.STOPBITS_ONE,
      bytesize=serial.EIGHTBITS,
      timeout=1)
      break

    except Exception as e:
      # raise e
      print "ERRO NA CONEXAO SERIAL I/O ERRO({0}): {1}".format(e.errno, e.strerror)
      return conected_flag
  
  print 'Conexao estabelecida.'
  conected_flag = True
  return conected_flag
