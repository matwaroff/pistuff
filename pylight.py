import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
try:
	for i in range(0, 100):
		GPIO.output(12, True)
		print "ON"
		time.sleep(.2)
		GPIO.output(12, False)
		print "OFF"
		time.sleep(.1)
except KeyboardInterrupt:
	print "OFF - EXITING"
	GPIO.output(12, False)
	GPIO.cleanup()
GPIO.cleanup()
 
