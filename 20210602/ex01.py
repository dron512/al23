import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)


try:
    while True:
        for i in range(0,4096):
            pwm.set_pwm(0,0,i)
            time.sleep(0.0001)
            print("i",i)
        for i in range(0,4096):
            pwm.set_pwm(0,i,4095)
            time.sleep(0.0001)
            print("i",i)
except KeyboardInterrupt:
    pass
except Exception as e:
    print(e)
