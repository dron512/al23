#-*- encoding: utf-8 -*-
import RPi.GPIO as GPIO
import time


led_pin = 17

GPIO.setmode(GPIO.BCM) #BCM 핀번호 사용하겠다.

GPIO.setup(led_pin,GPIO.OUT)

try:
    while True:
        GPIO.output(led_pin,True)
        time.sleep(0.5)
        GPIO.output(led_pin,False)
        time.sleep(0.5)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
