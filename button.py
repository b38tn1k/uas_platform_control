import Adafruit_BBIO.GPIO as GPIO
import time

#def this_is_a_function(print_this, number):
#   print(print_this)
#   print(number)

# setup
#GPIO.setup("P8_12", GPIO.IN)
#old_switVxch_state = 0
#i = 0
# looop
#while True:
#    new_switch_state = GPIO.input("P8_12")
#    if new_switch_state == 1 and old_switch_state == 0 :
#        i = i + 1
#        this_is_a_function('Number of times the button has been pressed: ', i)
#        time.sleep(0.1)
#    old_switch_state = new_switch_state

class Button():
    def __init__(self, pin="P8_12"):
        self.pin = pin
        GPIO.setup("P8_12", GPIO.IN)

    def is_down(self):
        status =  GPIO.input(self.pin) 
        return(bool(status))

