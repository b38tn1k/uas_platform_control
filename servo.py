import Adafruit_BBIO.PWM as PWM
import time

# Use this to run a servo from a BeagleBone
# jcarthew@ford.com

class Servo():
    def __init__(self, pin, duty_min=3, duty_max=14.5, speed=50):
        self.pin = pin
        self.duty_min = duty_min
        self.duty_max = duty_max
        self.duty_span = duty_max - duty_min
        self.active = False
        self.speed = speed

    def run(self):
        self.start()
        duty = 100 - ((float(self.speed) / 180) * self.duty_span + self.duty_min)
        PWM.set_duty_cycle(self.pin, duty)


    def start(self):
        if self.active is False:
            PWM.start(self.pin, (100 - self.duty_min), 60.0)
            self.active = True

    def stop(self):
        PWM.stop(self.pin)
        PWM.cleanup()
        self.active = False

    def demo(self):
        for i in range(10, 100, 10):
            self.start()
            print ("value: " + str(i))
            duty = 100 - ((float(i) / 180) * self.duty_span + self.duty_min)
            PWM.set_duty_cycle(self.pin, duty)
            time.sleep(1)


