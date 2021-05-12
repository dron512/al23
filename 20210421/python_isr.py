import RPi.GPIO as GPIO

led_state = False
led_state_changed = False
def buttonPressed():
	led_state = True if led_state == False else False
	led_state_changed = True;

button_pin = 27 # 2 in WiringPi
led_pin = 22 # 3 in WiringPi

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

GPIO.setup(button_pin, GPIO.IN)
GPIO.add_event_detect(button_pin, GPIO.RISING)
GPIO.add_event_callback(button_pin, buttonPressed)

try:
	while True:
		if led_state_changed == True:
			led_state_changed = False
			GPIO.output(led_pin, led_state)

except KeyboardInterrupt:
	pass
GPIO.cleanup()