import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
frequency = 50
pwm = GPIO.PWM(11, frequency)

leftPosition = .95
rightPosition = 1.5

msPerCycle = 1000 / frequency
dutyLeft = leftPosition * 100 / msPerCycle
dutyRight = rightPosition * 100 / msPerCycle
count = 0
try:
	print "Position: " + str(position)
	print "Duty Cycle: " + str(dutyCyclePercentage) + "%"
	print ""
	pwm.start(dutyLeft)
	time.sleep(.5)
	pwm.stop()
catch KeyboardInterrupt:
	pwm.start(dutyRight)
	time.sleep(.5)
	pwm.stop()
GPIO.cleanup()
