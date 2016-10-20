import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(13, GPIO.OUT) ##RED
GPIO.output(13,1)
GPIO.setup(16, GPIO.OUT) ##GREEN
GPIO.output(16,0)
GPIO.setup(15, GPIO.OUT) ##BLUE
GPIO.output(15,1)

time.sleep(30)
GPIO.cleanup()
