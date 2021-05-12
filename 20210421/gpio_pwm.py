import RPi.GPIO as GPIO
import time

led_pin = 18 # 1 for WiringPi

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

pwm = GPIO.PWM(led_pin, 100) # channel=led_pin frequency=100Hz
pwm.start(0)

try:
	while True:
		for t_high in range(0, 101, 1):
			pwm.ChangeDutyCycle(t_high)
			time.sleep(0.01)
		for t_high in range(100, -1, -1):
			pwm.ChangeDutyCycle(t_high)
			time.sleep(0.01)
			
except KeyboardInterrupt:
	pass
pwm.stop()
GPIO.cleanup()