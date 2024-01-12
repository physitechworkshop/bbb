import Adafruit_BBIO.GPIO as GPIO
from time import sleep

light = "P9_25" #GPIO117
relay = "P9_12"
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(light,GPIO.IN)
    GPIO.setup(relay,GPIO.OUT)

def read_light():
    while True:
        light_state = GPIO.input(light)
        if light_state == 0:
            print("Light Detected")
            GPIO.output(relay,0)
        elif light_state == 1:
            print("Light Not Detected")
            GPIO.output(relay,1)
        sleep(.3)

def destroy():   #When program ending, the function is executed. 
    GPIO.cleanup()
    

if __name__ == '__main__': #Program starting from here 
    try:
        setup()
        read_light()
    except KeyboardInterrupt:  
        destroy()

