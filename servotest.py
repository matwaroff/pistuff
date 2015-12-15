import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
frequency = 20
pwm = GPIO.PWM(11, frequency)

position = input("Please enter a position: ")
position = float(position)

msPerCycle = 1000 / frequency
dutyCyclePercentage = position * 100 / msPerCycle

print "Position: " + str(position)
print "Duty Cycle: " + str(dutyCyclePercentage) + "%"
print ""
pwm.start(dutyCyclePercentage)
time.sleep(3)
pwm.stop()
