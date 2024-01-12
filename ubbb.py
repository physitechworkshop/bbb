import Adafruit_BBIO.GPIO as GPIO
import time

def distanceMeasurement(TRIG,ECHO):

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulseStart = time.time()
    while GPIO.input(ECHO) == 1:
        pulseEnd = time.time()

    pulseDuration = pulseEnd - pulseStart
    distance = pulseDuration * 17150
    distance = round(distance, 2)
    return distance

#Configuration
GPIO.setup("P9_15",GPIO.OUT) #Trigger
GPIO.setup("P9_12",GPIO.IN)  #Echo
GPIO.setup("P9_11",GPIO.OUT)
GPIO.setup("P9_13",GPIO.IN)

#Security
GPIO.output("P9_11", False)
GPIO.output("P9_15", False)
time.sleep(0.5)

#main Loop
try:
    while True:
       for i in range(2):
           if i == 0:
               recoveredDistance = distanceMeasurement("P9_11","P9_13")
               print "Distance1: ",recoveredDistance,"cm"
           elif i == 1:
               recoveredDIstance = distanceMeasurement("P9_15","P9_12")
               print "Distance2: ",recoveredDistance,"cm"
       time.sleep(1)
except KeyboardInterrupt:
    print "Measurement stopped by user"
    GPIO.cleanup()