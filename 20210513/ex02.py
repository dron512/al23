import threading
import time
import RPi.GPIO as GPIO

servo_pin = 19 
led_pin = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)
GPIO.setup(led_pin,GPIO.OUT)

pwm = GPIO.PWM(servo_pin,50)
pwm.start(0)

def t1():
    while True:
        pwm.ChangeDutyCycle(3.0)     # 0.6ms 0도
        time.sleep(1)
        pwm.ChangeDutyCycle(7.5)     # 90도
        time.sleep(1)
        pwm.ChangeDutyCycle(12.5)    # 180도
        time.sleep(1)

threading.Thread(target=t1).start()

try:
    while True:
        GPIO.output(led_pin,True)
        time.sleep(0.3)
        GPIO.output(led_pin,False)
        time.sleep(0.3)
except KeyboardInterrupt :
    pass
except Exception as e:
    print(e)

GPIO.cleanup()