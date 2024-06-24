import serial
import time
import math

ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1, write_timeout=1)
while True:
    linear = time.time() % (2 * math.pi)  # [0, 2pi]
    sine = math.sin(linear)  # [-1, 1]
    cosine = math.cos(linear)  # [-1, 1]
    
    green = int(linear * 127 / math.pi)
    yellow = int((sine + 1) * 127)
    red = int((cosine + 1) * 127)
    
    led_msg = ','.join([str(red), str(yellow), str(green), "\n"])
    print(led_msg, end="")
    ser.write(led_msg.encode())
    time.sleep(0.1)