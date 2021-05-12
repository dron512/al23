import RPi.GPIO as GPIO
import time

servo_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)

pwm = GPIO.PWM(servo_pin,50)
pwm.start(3.0)  #0.6ms

for t_high in range(30,125):
    pwm.ChangeDutyCycle(t_high/10.0)
    time.sleep(1.0)

pwm.ChangeDutyCycle(0.0)

pwm.stop()
GPIO.cleanup()