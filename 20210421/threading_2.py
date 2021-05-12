import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BCM)

led_pin = 18
GPIO.setup(led_pin,GPIO.OUT)

pwm = GPIO.PWM(led_pin,1000.0)  # 1.0Hz
pwm.start(0.0)

flag_exit = False
def fading_led():
    while True:
        for t_high in range(0,101):
            pwm.ChangeDutyCycle(t_high)
            time.sleep(0.01)
        for t_high in range(100,-1,-1):
            pwm.ChangeDutyCycle(t_high)
            time.sleep(0.01)
        if flag_exit : break
t1 = threading.Thread(target=fading_led)
t1.start()


try : 
    while True:
        print("main")
        time.sleep(1.0)
except KeyboardInterrupt:
    pass

flag_exit = True
t1.join()

pwm.stop()
GPIO.cleanup()