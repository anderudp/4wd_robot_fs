import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

trig = 10
echo = 11
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

print("---DISTANCE MEASUREMENT STARTED---")
while True:
    # print("(1/6) Sensor settling... ", end="")
    GPIO.output(trig, False)
    time.sleep(0.5)
    # print("(2/6) Sending pulse... ", end="")
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)
    # print("(3/6) Pulse sent... ", end="")
    while not GPIO.input(echo):
        pulse_start = time.time()
    # print("(4/6) Pulse returning... ", end="")
    while GPIO.input(echo) == 1:
        pulse_end = time.time()
    # print("(5/6) Pulse returned... ", end="")
    pulse_duration = pulse_end - pulse_start
    distance = round(17150 * pulse_duration)
    print(f"{distance} cm")
    