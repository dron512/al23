import queue
import threading
import time
import RPi.GPIO as GPIO

msg_size = 10
mq = queue.Queue(msg_size)

btn_pin = 27
led_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_pin,GPIO.IN)
GPIO.setup(led_pin,GPIO.OUT)

value = 1
def btn_pressed(self):
    global value
    mq.put(value)
    value += 1
    print("눌림")

GPIO.add_event_detect(btn_pin,GPIO.RISING,callback=btn_pressed,bouncetime=300)

try:
    while True:
        get_value = mq.get()
        print("get_value = ",get_value)
        if get_value != 0 :
            GPIO.output(led_pin,True)
            time.sleep(1)
            GPIO.output(led_pin,False)
            time.sleep(1)
except KeyboardInterrupt:
    pass
except Exception as e:
    print(e)


GPIO.cleanup()
