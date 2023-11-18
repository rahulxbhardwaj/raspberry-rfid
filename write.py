import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

rfid = SimpleMFRC522()

try:
	#Helps to enter the data in the rfid card.
	#Also make sure that the tag is writeable also.
	text = input("NEW DATA : ")
	print("Please your tag to write")
	rfid.write(text)
	print("written")
	
finally:
	GPIO.cleanup()
