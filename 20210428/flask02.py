import RPi.GPIO as GPIO
import time
from flask import Flask,render_template

GPIO.setmode(GPIO.BCM)

app = Flask(__name__)

@app.route("/")
def home():
    pin = 22
    status = "low"
    return render_template("index.html",pin=pin,status=status)

@app.route("/<int:pin>/<status>")
def indexhtml(pin,status):
    print(pin)
    print(status)
    GPIO.setup(pin,GPIO.OUT)
    if status == "high":
        GPIO.output(pin,True)
    else :
        GPIO.output(pin,False)
    return render_template("index.html",pin=pin,status=status)

@app.route("/HIGH/<int:pin>")
def high(pin):
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,True)
    return f"{pin} is high"
    
@app.route("/LOW/<int:pin>")
def low(pin):
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,False)
    return f"{pin} is low"

if __name__ == "__main__":
    app.run(host="192.168.137.84",debug=True)

