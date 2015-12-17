import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT) ## SERVO
GPIO.setup(12, GPIO.OUT) ## LED
frequency = 50
pwm = GPIO.PWM(11, frequency)

leftPosition = .95
rightPosition = 1.5
middlePosition = (rightPosition - leftPosition) / 2 + leftPosition

positionList = [leftPosition, rightPosition]

msPerCycle = 1000 / frequency
count = 0
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
                                time.sleep(60)
                                count += 1
                                positionText = "CLOSE VALVE"
                else:
								GPIO.output(12, False) ## Lights Off
                                time.sleep(.5)
                                pwm.stop()
                                GPIO.cleanup()
except KeyboardInterrupt:
	print "Key pressed. Quitting."
	pwm.start(rightPosition * 100 / msPerCycle)
	time.sleep(1)
	pwm.stop()
	GPIO.cleanup()

