import RPi.GPIO as GPIO
import time

pinLED = 12
pinServo = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinServo, GPIO.OUT) ## SERVO
GPIO.setup(pinLED, GPIO.OUT) ## LED
frequency = 50
pwm = GPIO.PWM(pinServo, frequency)

offPosition = 1.25

msPerCycle = 1000 / frequency
count = 0
GPIO.output(12, True) ##Lights On

dutyCyclePercentage = offPosition * 100 / msPerCycle
print "EMERGENCY Fail SAFE"
pwm.start(dutyCyclePercentage)
time.sleep(1)
GPIO.output(12,False)
pwm.stop()
GPIO.cleanup()
