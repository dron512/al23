import RPi.GPIO as GPIO
import time

# 라즈 베리 파이 보드의 24번 핀으로 제어하는 서보 회로를 구성하시오
# 키보드 입력을 받아 24번 핀에 연결된 서보의 각도를 0도 90도,180도로 조절하는 프로그램을 작성하시오
# Q를 누르면 0도,
# W를 누르면 90도
# E를 누르면 180도로 조절하도록 합니다.

pin = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)

pwm = GPIO.PWM(pin,50)  # 50Hz 맞추기
pwm.start(3.0)  #0도로 맞추기 50Hz 3% 만 

try:
    while True:
        inputValue = input()
        print(inputValue)
        if inputValue == 'q':
            pwm.ChangeDutyCycle(3.0)
        if inputValue == 'w':
            pwm.ChangeDutyCycle(7.2)
        if inputValue == 'e':
            pwm.ChangeDutyCycle(12.5)        
except KeyboardInterrupt:
    pass

GPIO.cleanup()



