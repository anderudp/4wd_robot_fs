import serial

ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)
while True:
    reading = ser.readline().decode()
    ser_vals = reading.split(',')
    ser_vals = [val.rstrip() for val in ser_vals]
    if len(ser_vals) == 2:
        print(int(ser_vals[0]) + int(ser_vals[1]))
        