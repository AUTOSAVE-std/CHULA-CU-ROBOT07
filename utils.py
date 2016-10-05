import RPi.GPIO as GPIO
import time
import os
import sys
import getch
import subprocess
import signal
GPIO.setmode(GPIO.BCM)
## not sure they are required?
# import multiprocessing
# import pygame


class UltraSonic():
    '''
    Ultrasonic class
    '''

    def __init__(self):
        # define pins in use
        self.TRIG = 17
        self.ECHO = 27

        # set GPIO mode
        GPIO.setmode(GPIO.BCM)

        # set up GPIO
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)

    def getDistance(self):
        global pulse_duration
        global pulse_end
        global pulse_start
        # print("Distance measurement in progress")

        GPIO.output(self.TRIG, False)
        time.sleep(0.5)

        GPIO.output(self.TRIG, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, False)

        while GPIO.input(self.ECHO)==0:
          pulse_start = time.time()

        while GPIO.input(self.ECHO)==1:
          pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)

        return distance


# class Keyboard():
#     '''
#     Keyboard class
#     '''
#     def __init__(self):
#         self.key = 0
#         pygame.init()
#         pygame.display.init()
#         os.environ["SDL_VIDEODRIVER"] = "dummy"

#     def getKey(self):
#         events = pygame.event.get()
#         keys=pygame.key.get_pressed()
#         print(keys)
#         for event in events:
#             if event.type == pygame.K_0:
#                 return 46

        # self.key =  ord(getch.getch())

        # if self.key not in list(range(46, 58)):
        #     print("Wrong key was pressed! only allow number keypad..")
        #     return 0
        # else:
        #     return self.key

class AudioPlayer():
    '''
    Audio player class (use system aplay)
    '''

    def __init__(self):
        self.toPlay = 0
        self.player = subprocess.Popen("",shell=True, preexec_fn=os.setsid)

    def fucking_killme(self):
        if(self.player.poll() == None):
            # return 1 in case successfully killed
            os.killpg(os.getpgid(self.player.pid), signal.SIGTERM)
            print(self.player.pid, "was killed.")
            return 1
        else:
            print("nothing to kill")
            return 0

    def fucking_runme(self, toplay):
        self.toPlay = toplay-45

        if(self.toPlay >= 10):
            string = "aplay %d.wav" % self.toPlay
        else:
            string = "aplay 0%d.wav" % self.toPlay

        self.player = subprocess.Popen(string, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

        # should be able to track from this obj
        return self.player
