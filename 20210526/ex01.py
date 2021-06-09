import RPi.GPIO as GPIO
import time

pin_IA = 19 # 전진 후진
pin_IB = 26 # pwm 속도조절

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_IA,GPIO.OUT)
GPIO.setup(pin_IB,GPIO.OUT)

pwm = GPIO.PWM(pin_IB,1000)
pwm.start(0)

# 0 ~ 100 사이 값
try:
    while True:
        GPIO.output(pin_IA,True) # 전진 설정
        pwm.ChangeDutyCycle(0)   # 전진 설정일떄 pwm 0 주면 최대 속도
        time.sleep(1)
        GPIO.output(pin_IA,False) # 후진 설정
        pwm.ChangeDutyCycle(0)    # 후진 설정일떄 pwm 0 이면 멈춤
        time.sleep(1)
except KeyboardInterrupt:
    pass
except Exception as e:
    print(e)

GPIO.cleanup()
