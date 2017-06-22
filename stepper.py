import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time
import math
import threading
# Use this to drive the reprap stepstick stepper motor driver
# using BeagleBone Black. Use a 5V pull-up resistor! jcarthew@ford.com

class Stepper():
    def __init__(self, enable_p="P8_10", step_p="P8_13", dir_p="P8_12", steps=200):
        # Pins
        PWM.stop(step_p)
        GPIO.setup(enable_p, GPIO.OUT)
        GPIO.setup(dir_p, GPIO.OUT)
        self.enable_p = enable_p
        self.step_p = step_p
        self.dir_p = dir_p
        # Stepper Characteristics
        self.steps = steps
        self.resolution = 360/steps
        # Time Vars
        self.frequency = 200
        # Model
        self.rps = 1

    def drive(self, clockwise=True):
        if self.frequency <= 0:
            PWM.stop(self.step_p)
        else:
            # Disable the Stepper
            GPIO.output(self.enable_p, GPIO.HIGH)
            # Send the Step wave
            PWM.start(self.step_p, 50, self.frequency, 1) # Magic Numbers: 50% duty, normal polarity
            # Set the Direction
            if clockwise is True:
                GPIO.output(self.dir_p, GPIO.LOW)
            else:
                GPIO.output(self.dir_p, GPIO.HIGH)
            # Enable the Stepper
            GPIO.output(self.enable_p, GPIO.LOW)

    def move_to_angle(self, angle):
        ''' Calculate the approx time to move
        to desired angle. create a timed thread 
        that will kill pwm after that amount of
        time. fire the thread. start moving '''
        number_of_steps = (float(angle) / 360.0) * self.steps
        time_required = float(number_of_steps / self.frequency)
        print time_required
        t = threading.Timer(time_required, self.kill_pwm)
        if angle < 0:
            self.drive(False)
        else:
            self.drive()
        t.start()

    def kill_pwm(self):
        PWM.stop(self.step_p)
    
    def stop(self):
        PWM.stop(self.step_p)
        PWM.cleanup()

    def set_rps(self, rps):
        self.rps = rps
        self.frequency = self.steps * rps



