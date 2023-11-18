import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37 , GPIO.OUT)
GPIO.setup(33 , GPIO.OUT)

rfid = SimpleMFRC522()

print("Hello")


while True:
    id,text = rfid.read()
    #Enter your id of the rfid card here.Use read file to know the serial number of the tag
    if id == 562748324880:
        print("Authorization Approved")
        GPIO.output(37 , True)
        time.sleep(0.05)
        GPIO.output(37 , False)
       # print("Welcome back Rahul")
       # break
    else: 
        print("Authorization Decline")
        GPIO.output(33 , True)
        time.sleep(0.05)
        GPIO.output(33 , False)
    
