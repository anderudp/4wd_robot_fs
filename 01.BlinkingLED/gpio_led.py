import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ledPin = 18
GPIO.setup(ledPin, GPIO.OUT)
pwm = GPIO.PWM(ledPin, 100)

pwm.start(0)

while True:
    count = 1
    while count < 100:
        pwm.ChangeDutyCycle(count)
        time.sleep(0.01)
        count += 1
    while count > 0:
        pwm.ChangeDutyCycle(count)
        time.sleep(0.01)
        count -= 1
