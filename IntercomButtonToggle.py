from re import A, X
import RPi.GPIO as GPIO
from time import sleep
from pynput.keyboard import Key, Controller

#Variables
buttonPin = 40
pushToTalkButton = [Key.ctrl, Key.alt, "x"]

#Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


try:
    while GPIO.input(buttonPin):
        i = 0
        while i < 2:
            Controller().press(pushToTalkButton[i])
            i = i + 1
        
finally:
    i = 0
    while i < 2:
        Controller().release(pushToTalkButton[i])
        i = i + 1
    GPIO.cleanup()
