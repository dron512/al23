from flask import Flask
import RPi.GPIO as GPIO


led_pin = 18 # wiringPi 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)

app = Flask(__name__)

@app.route("/high18")
def high18():
    GPIO.output(led_pin,True)
    return "high18"

@app.route("/low18")
def low18():
    GPIO.output(led_pin,False)
    return "low18"


app.run(host="192.168.137.84",debug=True)