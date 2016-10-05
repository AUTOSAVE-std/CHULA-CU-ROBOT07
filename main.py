#!/usr/bin/env python
import _thread
# import select
# import sys
import pygame, os
from utils import UltraSonic, AudioPlayer
from time import sleep
from random import randint
# instantiate all objects
ul_sensor = UltraSonic()
# wireless_kb = Keyboard()
player = AudioPlayer()
last_wavtoplay = 0
wavtoplay = 0
timecount = 0
pygame.init()
window = pygame.display.set_mode((1,1))
clock = pygame.time.Clock()

def ControlSensor():
    global timecount
    while True:
        dist = ul_sensor.getDistance()
        # check distance
        if wavtoplay in [46, 58]:
            print(wavtoplay)
            print("play")

        if dist > 1 and dist < 8:
            print("IN Range PLAY MUSIC THANK YOU")
            player.fucking_killme()
            player.fucking_runme(55)
            timecount = 0
            sleep(1.1)
        else:
            print("out of range")

def ControlKey(num):
    global timecount
    player.fucking_killme()
    player.fucking_runme(num)
    timecount = 0
    # while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
    # line = sys.stdin.readline()

    # while True:
    #     print("gogogogo")
    #     for event in pygame.event.get():
    #         print("kokokokoko")
    #         if event.type == pygame.K_0:
    #             print("kokokokoko")

        # ready = select.select([sys.stdin], [], [], 0.1)[0]
        # print(ready)
        # if ready:
            # print("ready")
        # wavtoplay = wireless_kb.getKey()
        # print('read input:', line, end='')
        # sleep(0.5)
        #


try:
    _thread.start_new_thread(ControlSensor,())
except:
    print("ControlSensor Error!")

# try:
#     _thread.start_new_thread(ControlKey,())
# except:
#     print("ControlKey Error!")

gameLoop = True
while gameLoop:
    for event in pygame.event.get():

        if (event.type==pygame.KEYDOWN):

            # if event.key == pygame.K_1:
            #     ControlKey(49)
            # if event.key == pygame.K_2:
            #     ControlKey(50)
            # if event.key == pygame.K_3:
            #     ControlKey(51)
            # if event.key == pygame.K_4:
            #     ControlKey(52)
            # if event.key == pygame.K_5:
            #     ControlKey(53)
            # if event.key == pygame.K_6:
            #     ControlKey(54)
            # if event.key == pygame.K_7:
            #     ControlKey(55)
            # if event.key == pygame.K_8:
            #     ControlKey(56)
            # if event.key == pygame.K_9:
            #     ControlKey(57)
            # if event.key == pygame.K_0:
            #     ControlKey(48)
            # if event.key == pygame.K_SLASH:
            #     ControlKey(46)
            # if event.key == pygame.K_PERIOD:
            #     ControlKey(47)



            if event.key == pygame.K_KP1:
                ControlKey(49)
            if event.key == pygame.K_KP2:
                ControlKey(50)
            if event.key == pygame.K_KP3:
                ControlKey(51)
            if event.key == pygame.K_KP4:
                ControlKey(52)
            if event.key == pygame.K_KP5:
                ControlKey(53)
            if event.key == pygame.K_KP6:
                ControlKey(54)
            if event.key == pygame.K_KP7:
                ControlKey(55)
            if event.key == pygame.K_KP8:
                ControlKey(56)
            if event.key == pygame.K_KP9:
                ControlKey(57)
            if event.key == pygame.K_KP0:
                ControlKey(48)
            if event.key == pygame.K_KP_DIVIDE:
                ControlKey(46)
            if event.key == pygame.K_KP_PERIOD:
                ControlKey(47)
            # if event.key == pygame.K_ASTERISK:
            #     gameLoop = False
            #     exit


    timecount = timecount + 1
    if timecount > 20:
        player.fucking_killme()
        player.fucking_runme(randint(46,57))
        timecount = 10

        # if (event.type==pygame.KEYUP):
        #     gameLoop=False
        #     print("KEYUP")

    clock.tick(10)
    sleep(1)

while True:
    sleep(1)
    # if gameLoop is False:
    #     exit


pygame.quit()
