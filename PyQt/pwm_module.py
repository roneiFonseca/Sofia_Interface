import RPi.GPIO as GPIO
import time



def pwm(duty_cycle,total_time,step_time):
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(25, GPIO.OUT)
	PWM_FREQ = 1200
	pwm_pin1 = GPIO.PWM(25,PWM_FREQ)
	pwm_pin1.start(0)
	step_cycle = duty_cycle
	
	while(total_time>0):
		
		pwm_pin1.ChangeDutyCycle(step_cycle)
		time.sleep(step_time)
		total_time = total_time - 1
		step_cycle += duty_cycle
		print "duty_cycle: %d  total_time: %d" % (step_cycle, total_time)
		
	pwm_pin1.stop()
	GPIO.cleanup()
		
