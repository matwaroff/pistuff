import RPi.GPIO as GPIO
import time

pinLED = 12
pinServo = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinServo, GPIO.OUT) ## SERVO
GPIO.setup(pinLED, GPIO.OUT) ## LED
frequency = 50
pwm = GPIO.PWM(pinServo, frequency)

onPosition = .75
offPosition = 1.25

positionList = [onPosition, offPosition]

msPerCycle = 1000 / frequency
count = 0
sleepLength = 20 ## How long to sleep
positionText = "Watering"
GPIO.output(12, True) ##Lights On


try:
	for position in positionList:
		dutyCyclePercentage = position * 100 / msPerCycle
		print "STATUS: " + str(positionText)
		print "Duty Cycle: " + str(dutyCyclePercentage) + "%"
		print ""
		pwm.start(dutyCyclePercentage)
		if count == 0:
			time.sleep(sleepLength)
			count += 1
			positionText = "CLOSE VALVE"
		else:
			GPIO.output(pinLED, False) ## Lights Off
			time.sleep(.5)
			pwm.stop()
			GPIO.cleanup()
			
except KeyboardInterrupt:
	print "Key pressed. Quitting."
	pwm.start(offPosition * 100 / msPerCycle)
	time.sleep(1)
	pwm.stop()
	GPIO.cleanup()

