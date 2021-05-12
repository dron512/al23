import RPi.GPIO as GPIO
import time

button_pin = 27 # 2 for WiringPi

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN)

try:
	while True:
		buttonInput = GPIO.input(button_pin)
		print(buttonInput)

except KeyboardInterrupt:
	pass
GPIO.cleanup()
