import RPi.GPIO as GPIO
import time
import threading

led_pin = 18 # wiringPi 1
btn_pin = 23
buzzer_pin = 13

led_tpin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)
GPIO.setup(led_tpin,GPIO.OUT)

GPIO.setup(btn_pin,GPIO.IN)
GPIO.setup(buzzer_pin,GPIO.OUT)

flag_exit = False

def led_tpinOUT():
    while True:
        GPIO.output(led_tpin,True)
        time.sleep(1.5)
        GPIO.output(led_tpin,False)
        time.sleep(1.5)
        if flag_exit : break

th1 = threading.Thread(target=led_tpinOUT)  # led_tpinOUt 함수 쓰레드 생성
th1.start()                                 # thread 쓰레드 시작

pwm = GPIO.PWM(buzzer_pin,262) # 262Hz 설정 
pwm.start(0)

def btn_preseed(self):
    pwm.ChangeDutyCycle(0.5)  # 262Hz 50%을 HIGH로 설정
    time.sleep(1)
    pwm.ChangeDutyCycle(0) # 1초뒤에 끄기
    print('test')   # 부저 울리기 위해서 262Hz

try:
    GPIO.add_event_detect(btn_pin,GPIO.RISING,callback=btn_preseed,bouncetime=300)
    while True:
        GPIO.output(led_pin,True)
        time.sleep(1)
        GPIO.output(led_pin,False)
        time.sleep(1)
except KeyboardInterrupt as ke:
    pass
except Exception as e:
    print(e)

flag_exit = True
th1.join()

GPIO.cleanup()