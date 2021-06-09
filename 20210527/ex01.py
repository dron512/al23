import spidev
import time

bus = 0
device = 0

spi = spidev.SpiDev()
spi.open(bus,device)
spi.max_speed_hz = 1000000

def analogRead(channel):
    buf = [(1<<2)|(1<<1)|(channel&4) >>2,(channel&3)<<6,0]
    buf = spi.xfer3(buf)
    adcValue = ((buf[1] & 0xF)<<8) | buf[2]
    return adcValue

try:
    while True:
        #for i in range(0,8):
        inputV = analogRead(0)
        print("inputV = ",inputV)
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
spi.close()

