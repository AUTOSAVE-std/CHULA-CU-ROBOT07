#!/usr/bin/env python
from utils import UltraSonic, Keyboard, AudioPlayer
from time import sleep

# instantiate all objects
ul_sensor = UltraSonic()
wireless_kb = Keyboard()
player = AudioPlayer()

while True:
    # check distance
    dist = ul_sensor.getDistance()

    if dist > 1 and dist < 8:
        print("in range")
        # get key from keyboard
        # if key not in [46, 58], program will break - check in utils.Keyboard.getKey() line 65
        wavtoplay = wireless_kb.getKey()

        # kill and play wavtoplay
        player.fucking_killme()
        player.fucking_runme(wavtoplay)

        sleep(0.1)

    else:
        print("out of range")
