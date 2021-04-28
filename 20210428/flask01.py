import RPi.GPIO as GPIO
import time
from flask import Flask,render_template

GPIO.setmode(GPIO.BCM)

app = Flask(__name__)

@app.route("/HIGH/<int:pin>")
def high(pin):
    GPIO.setup(pin,GPIO.OUT)
    GPIO.out(pin,True)
    return f"{pin} is high"

@app.route("/LOW/<int:pin>")
def low(pin):
    GPIO.setup(pin,GPIO.OUT)
    GPIO.out(pin,False)
    return f"{pin} is low"

if __name__ == "__main__":
    app.run(host="192.168.137.84",debug=True)

