import serial

serialP = serial.Serial("/dev/ttyS0",baudrate=9600,timeout=3.0)

print(serialP.name)
print(serialP.port)
print(serialP.get_settings())
print(serialP.fileno())
try:
    while True:
        dat = serialP.read(1)
        print(dat)
except KeyboardInterrupt:
    pass
serialP.close()
