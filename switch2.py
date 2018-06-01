#coding=utf-8

import RPi.GPIO as GPIO
import datetime

def my_callback(channel):
    if (GPIO.input(6) == GPIO.HIGH):
        print('high')
    else:
        print('low')

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6,GPIO.IN)
    GPIO.add_event_detect(6,GPIO.BOTH,callback=my_callback)
    
    message=input('press key to exit')
    
finally:
    GPIO.cleanup()
    
print('done')
