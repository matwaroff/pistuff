import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
frequency = 100
pwm = GPIO.PWM(11, frequency)

leftPosition = .95
rightPosition = .3
 
msPerCycle = 1000 / frequency
dutyLeft = leftPosition * 100 / msPerCycle
dutyRight = rightPosition * 100 / msPerCycle
count = 0
try:
	print "Position: " + str(leftPosition)
	print "Duty Cycle: " + str(dutyLeft) + "%"
	print ""
	pwm.start(dutyLeft)
	time.sleep(.5)
	pwm.stop()
	time.sleep(160)
	pwm.start(dutyRight)
	time.sleep(.5)
	pwm.stop()
except KeyboardInterrupt:
	pwm.start(dutyRight)
	time.sleep(.5)
	pwm.stop()
GPIO.cleanup()
