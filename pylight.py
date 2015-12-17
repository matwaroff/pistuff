import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

for i in range(0, 12):
	GPIO.output(12, True)
	print "ON"
	time.sleep(.1)
	GPIO.output(12, False)
	print "OFF"
	time.sleep(.2)

GPIO.cleanup()