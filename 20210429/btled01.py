import RPi.GPIO as GPIO
import time

led_pin = 18 # wiringPi 1
btn_pin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)
GPIO.setup(btn_pin,GPIO.IN)


try:

    GPIO.output(led_pin,True)
    time.sleep(1)
    GPIO.output(led_pin,False)
    time.sleep(1)

except Exception as e:
    print(e)

GPIO.cleanup()