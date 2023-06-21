#!/usr/bin/python
# This is a python script.
import RPi.GPIO as GPIO
import time
import datetime
import keyboard
from datetime import datetime


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
key = "space"
Ticker = 1
Ticker2 = 1
push = (datetime.now().strftime("%d %m %Y %H:%M:%S.%f"))
print(push + "Studio Clock Trigger Started \n")


while True:  #Run Forever
    # waiting for change in on air signal
    if GPIO.input(21) == GPIO.HIGH: #mic off 
        Ticker = 1
    if GPIO.input(21) == GPIO.LOW: #mic on
        Ticker = 0

    if Ticker == Ticker2: 
        # log date and time of pulse Start
        keyboard.release(key)
        push = (datetime.now().strftime("%d %m %Y %H:%M:%S.%f"))
        if Ticker == 0: #mic on 
            key = "space"
            keyboard.press(key)
            Ticker2 = 1
            
        if Ticker == 1: #Mic off 
            key = "enter"
            keyboard.press(key)
            Ticker2 = 0


    