#!/usr/bin/env python
 
import os
import sys
import getch
import subprocess
import signal
import multiprocessing
# import RPi.GPIO as GPIO
import time
# GPIO.setmode(GPIO.BCM)

# TRIG = 17                                   
# ECHO = 27

# GPIO.setup(TRIG,GPIO.OUT)	#Set pin as GPIO out
# GPIO.setup(ECHO,GPIO.IN)	#Set pin as GPIO in
# GPIO.setwarnings(False)

def takechar():
	global key
	key = ord(getch.getch())
	pass

def fucking_killme():
	if(output.poll() == None):
		os.killpg(os.getpgid(output.pid), signal.SIGTERM)
	pass

def fucking_runme(numberofshit):
	global output
	numberofshit = numberofshit-45
	if(numberofshit >= 10):
		string = "aplay %d.wav" %numberofshit
	else:
		string = "aplay 0%d.wav" %numberofshit
	output = subprocess.Popen(string, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
	pass
# def gpioood():

# 	GPIO.output(TRIG, False)                  
# 	time.sleep(0.1)                             

# 	GPIO.output(TRIG, True)                   
# 	time.sleep(0.00001)                       
# 	GPIO.output(TRIG, False)                  

# 	while GPIO.input(ECHO)==0:                
# 		pulse_start = time.time()               

# 	while GPIO.input(ECHO)==1:                
# 		pulse_end = time.time()                 

# 	pulse_duration = pulse_end - pulse_start  

# 	distance = pulse_duration * 17150         
# 	distance = round(distance, 2)             

# 	if distance > 1 and distance < 8:      
# 		os.system('aplay  10.wav')  
# def worker(file):
# 	pass

# files = ["/home/pi/Desktop/data/gitdata/ultrasonic.py"]
# for i in files:
# 	p = multiprocessing.Process(target=worker(i))
# 	p.start()


## runsensor = subprocess.Popen(['python', 'ultrasonic.py'])
## runsensor = subprocess.Popen('python3 /home/pi/Desktop/data/gitdata/ultrasonic.py')
output = subprocess.Popen("",shell=True, preexec_fn=os.setsid)
while True:
	# GPIO.add_event_detect(27, GPIO.RISING, callback=gpioood)
	takechar()
	for x in range(46, 58):
		if(key==x):
			fucking_killme()
			fucking_runme(key)

	time.sleep(0.1)


# if __name__ == '__main__':

