import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
frequency = 50
pwm = GPIO.PWM(11, frequency)

leftPosition = .95
rightPosition = 1.5
middlePosition = (rightPosition - leftPosition) / 2 + leftPosition

positionList = [leftPosition, rightPosition]

msPerCycle = 1000 / frequency
count = 0
try:
	for position in positionList:
			dutyCyclePercentage = position * 100 / msPerCycle
			print "Position: " + str(position)
			print "Duty Cycle: " + str(dutyCyclePercentage) + "%"
			print ""
			pwm.start(dutyCyclePercentage)
			if count == 0:
					time.sleep(45)
					count += 1
			else:
					time.sleep(.5)
					pwm.stop()
					GPIO.cleanup()
except KeyboardInterrupt:
	print "Key pressed. Quitting."
	pwm.stop()
	GPIO.cleanup()

