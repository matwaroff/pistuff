import RPi.GPIO as GPIO
from Tkinter import *
import Tkinter
import time

##tkinter stuff
top = Tkinter.Tk()
pinServo = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinServo, GPIO.OUT) ## SERVO
frequency = 50
pwm = GPIO.PWM(pinServo, frequency)

msPerCycle = 1000 / frequency
count = 0
sleepLength = 50
curposition = 1

def left():
        global curposition
        curposition = curposition - .05
        dCP = curposition * 100 / msPerCycle
        print("Position: " + str(curposition)) 
        pwm.start(dCP)
        time.sleep(1)

def right():
        global curposition
        curposition = curposition + .05
        dCP = curposition * 100 / msPerCycle
        print("Position: " + str(curposition))
        pwm.start(dCP)
        time.sleep(1)

        
leftB = Tkinter.Button(top,text = "Left", command = left).grid(row=0, column=0)
rightB = Tkinter.Button(top,text = "Right", command = right).grid(row=0, column=1)

top.mainloop()
pwm.stop()
GPIO.cleanup()
                

