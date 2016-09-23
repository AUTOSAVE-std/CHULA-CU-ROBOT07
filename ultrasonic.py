import RPi.GPIO as GPIO                     
import time
import os
import sys                                 
GPIO.setmode(GPIO.BCM)                      

TRIG = 17                                   
ECHO = 27                                   

print ("Distance measurement in progress")

GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in

while True:

  GPIO.output(TRIG, False)                  
  time.sleep(0.1)                             

  GPIO.output(TRIG, True)                   
  time.sleep(0.00001)                       
  GPIO.output(TRIG, False)                  

  while GPIO.input(ECHO)==0:                
    pulse_start = time.time()               

  while GPIO.input(ECHO)==1:                
    pulse_end = time.time()                 

  pulse_duration = pulse_end - pulse_start  

  distance = pulse_duration * 17150         
  distance = round(distance, 2)             

  if distance > 1 and distance < 8:      
  	os.system('aplay  10.wav')                 
