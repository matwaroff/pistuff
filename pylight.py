import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

GPIO.output(12, TRUE)
print "ON"
time.sleep(15)
GPIO.output(12, FALSE)
print "OFF"

GPIO.cleanup()