from button import Button
from stepper import Stepper
from servo import Servo

class Arm():
    def __init__(self, a_button, a_stepper, a_servo):
        self.button = a_button
        self.stepper = a_stepper
        self.stepper.setup()
        self.servo = a_servo
        #self.servo.setup() # it starts running asap. added setup to the run function

    def undeploy(self):
        self.stepper.forwards = False
        while True:
            self.stepper.step()
            if self.button.is_down() is True:
                break
        self.stepper.zero
        self.stepper.forwards = True

    def deploy(self):
        self.stepper.rotate_an_arbitrary_angle(90)

