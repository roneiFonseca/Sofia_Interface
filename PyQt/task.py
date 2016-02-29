import time


step_minute = 0.1*60;
time_before = time.time()
while 1:
  	time_now = time.time()
  	# time.sleep(5)
	if time_now - time_before > step_minute:
		print "Beeeeep"
		print time_now -time_before
		time_before = time_now


 


