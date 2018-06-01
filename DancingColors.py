import time
import RPi.GPIO as GPIO
from random import randint

GPIO.setmode(GPIO.BCM)

for i in range(28):
    GPIO.setup(i,GPIO.OUT)

try:
    i=0
    while (True):
        j = randint(0,28)
        m= randint(j,28)
        for k in range(j,m):
            GPIO.output(k,GPIO.HIGH)
        for k in range(j,m):
            pass
            time.sleep(0.05)
        for k in range(j,m):
            GPIO.output(k,GPIO.LOW)
        
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()