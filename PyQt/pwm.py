from RPIO import PWM
import time 
import parametros

# filename = "/home/pi/Desktop/potencia.txt" 
servo = PWM.Servo()
servo.set_servo(17,0)
potencia_old = 0
while 1:
    # target = open(filename, 'r')
    # potencia = int(target.read())
    # target.close()
    potencia = parametros.todos['potenciaInicial']*400
    # if potencia == 40000:
    #    target = open(filename,'w')
    #    target.write('0')
    #    target.close()		
    #    break
    # if potencia_old != potencia:
    #     if potencia == 20000:
    #             potencia = 19990
    servo.set_servo(17,potencia)
    potencia_old = potencia
servo.stop_servo(17)
