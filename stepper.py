import Adafruit_BBIO.GPIO as GPIO
import time
import math
# Use this to drive the reprap stepstick stepper motor driver
# using BeagleBone Black. jcarthew@ford.com

class Stepper():
    def __init__(self, enable_p="P8_14", step_p="P8_15", dir_p="P8_16", steps=200):
        self.angle = 0
        self.stpr_steps = steps
        self.enable_p = enable_p
        self.step_p = step_p
        self.dir_p = dir_p
        self.period = 60.0 / (steps * 20)
        self.active = False
        self.forwards = True
        self.angle = 0.0

    def set_rpm(self, rpm):
        self.period = 60.0 / (self.stpr_steps * rpm)

    def zero(self):
        self.angle = 0.0

    def rotate_an_arbitrary_angle(self, angle):
        # this could be smarter but is it worth the effort?
        angular_resolution = 360.0 / self.stpr_steps
        step_count = math.abs(angle / angular_resolution)
        for i in range(step_count):
            self.step()

    def setup(self):
        if self.active is False:
            for pin in [self.enable_p, self.step_p, self.dir_p]:
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, GPIO.LOW)
            self.active = True

    def step(self):
        if self.active:
            if self.forwards is True:
                GPIO.output(self.dir_p, GPIO.LOW)
            else:
                GPIO.output(self.dir_p, GPIO.HIGH)
            GPIO.output(self.enable_p, GPIO.LOW)
            GPIO.output(self.step_p, GPIO.HIGH)
            time.sleep(self.period)
            GPIO.output(self.step_p, GPIO.LOW)
