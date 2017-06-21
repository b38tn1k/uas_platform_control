import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time
import math
# Use this to drive the reprap stepstick stepper motor driver
# using BeagleBone Black. jcarthew@ford.com

class Stepper():
    def __init__(self, enable_p="P8_7", step_p="P8_8", dir_p="P8_9", steps=200):
        # Pins
        PWM.stop(step_p)
        GPIO.setup(enable_p, GPIO.OUT)
        GPIO.setup(dir_p, GPIO.OUT)
        self.enable_p = enable_p
        self.step_p = step_p
        self.dir_p = dir_p
        # Stepper Characteristics
        self.stpr_steps = steps
        self.resolution = 360/steps
        # Time Vars
        self.frequency = 100
        # Model
        self.active = False
        self.angle = 0.0

    def drive(self, clockwise=True):
        if self.frequency <= 0:
            PWM.stop(self.step_p)
        else:
            # Disable the Stepper
            GPIO.output(self.enable_p, GPIO.HIGH)
            # Send the Step wave
            PWM.start(self.step_p, 50, self.frequency, 1)
            # Set the Direction
            if clockwise is True:
                GPIO.output(self.dir_p, GPIO.LOW)
            else:
                GPIO.output(self.dir_p, GPIO.HIGH)
            # Enable the Stepper
            GPIO.output(self.enable_p, GPIO.LOW)



