import RPi.GPIO as GPIO

led_state = False
led_state_chagned = False

def buttonPressed(channel):
    global led_state,led_state_chagned
    # (not led_state)조건문이 true 이면 true 할당 아니면 False 할당
    led_state = True if not led_state else False
    led_state_chagned = True

button_pin = 27
led_pin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)
GPIO.setup(button_pin,GPIO.IN)

GPIO.add_event_detect(button_pin,GPIO.RISING,bouncetime=500)
GPIO.add_event_callback(button_pin,buttonPressed,bouncetime=500)

try:
    while True:
        if led_state_chagned == True:
            led_state_chagned = False
            GPIO.output(led_pin,led_state)
except KeyboardInterrupt:
    pass

GPIO.cleanup()

