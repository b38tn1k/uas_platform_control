from stepper import Stepper
from button import Button
from servo import Servo
from arm import Arm
import sys
stp = Stepper()
but = Button()
ser = Servo()
arm = Arm(but, stp, ser)
#print(sys.modules.keys())
print("loaded")
print("stp")
print("but")
print("ser")
print("arm")
