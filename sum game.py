import RPi.GPIO as GPIO
import time
import random
GPIO.setmode(GPIO.BOARD)

GPIO.setup(3 , GPIO.OUT)
GPIO.setup(13 , GPIO.OUT)

while True:
    a = random.randint(1,100)
    b = random.randint(1,100)
    print("Value of a ",a)
    print("Value of b ",b)
    n = int(input("What is sum : "))
    if a+b == n:
        GPIO.output(13 , True)
        time.sleep(1.5)
        GPIO.output(13 , False)
    else:
        GPIO.output(3 , True)
        time.sleep(1.5)
        GPIO.output(3 , False)


    
    
    
    
    

