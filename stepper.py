import Adafruit_BBIO.GPIO as GPIO
import time
import math
import threading
# Use this to drive the reprap stepstick stepper motor driver
# using BeagleBone Black. jcarthew@ford.com

class Stepper():
    def __init__(self, enable_p="P8_7", step_p="P8_8", dir_p="P8_9", steps=200):
        self.angle = 0
        self.stpr_steps = steps
        self.enable_p = enable_p
        self.step_p = step_p
        self.dir_p = dir_p
        self.period = 60.0 / (steps * 20)
        self.active = False
        self.forwards = True
        self.angle = 0.0
        self.resolution = 360/steps
        self.angle = 0.0
        self.next_step = time.time()
        self.threads = []

    def set_rpm(self, rpm):
        self.period = 60.0 / (2 * self.stpr_steps * rpm)

    def zero(self):
        self.angle = 0.0

    def rotate_an_arbitrary_angle(self, angle):
        # this could be smarter but is it worth the effort?
        angular_resolution = 360.0 / self.stpr_steps
        step_count = math.ceil(angle / angular_resolution)
        for i in range(int(step_count)):
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
                self.angle = self.angle + self.resolution
                GPIO.output(self.dir_p, GPIO.LOW)
            else:
                GPIO.output(self.dir_p, GPIO.HIGH)
                self.angle = self.angle - self.resolution
            self.pulse()
            GPIO.output(self.enable_p, GPIO.LOW)

    def pulse(self):
        self.timer(self.pulse_high)
        self.timer(self.pulse_low)

    def blocking_step(self):
        self.pulse_high()
        time.sleep(self.period)
        self.pulse_low()
        time.sleep(self.period)

    def thread_step(self):
        t = threading.Thread(target=self.blocking_step)
        self.threads.append(t)
        t.start()

    def pulse_high(self):
        GPIO.output(self.step_p, GPIO.HIGH)

    def pulse_low(self):
        GPIO.output(self.step_p, GPIO.LOW)

    def timer(self, func):
        now = time.time()*1000
        if now - self.next_step > self.period:
            func()
            self.next_step = now + self.period
            print("YAY")
        print(now)
        

