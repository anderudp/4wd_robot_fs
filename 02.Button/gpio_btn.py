import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
btnPin = 8
GPIO.setup(btnPin, GPIO.IN, GPIO.PUD_UP)

while True:
    btnVal = GPIO.input(btnPin)
    if btnVal == False:
        print("Button pressed!")
        while btnVal == False:
            btnVal = GPIO.input(btnPin)
            