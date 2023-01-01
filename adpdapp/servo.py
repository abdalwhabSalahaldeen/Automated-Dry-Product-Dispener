import RPi.GPIO as GPIO

import time

import sys

from .hx711 import HX711

#!/usr/bin/env python

# -*- coding: utf-8 -*-

#Libraries

import time    #https://docs.python.org/fr/3/library/time.html

from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/

#Objects

pca = ServoKit(channels=16)

# function init 

def init():

    for i in range(16):

        pca.servo[i].set_pulse_width_range(500 , 2500)

# function main 



# function activateServo 

def activateServo(servo_n):

    if servo_n==4:

        r_angle=25

        step=5

    else:

        r_angle=1

        step=1

    for degree in range(0,r_angle,step):

        pca.servo[servo_n+7].angle = degree

        time.sleep(0.06)

    pca.servo[servo_n+7].angle=None #disable channel

    time.sleep(0.5)



hx = HX711(6, 5)





def cleanAndExit():

    print("Cleaning...")

    GPIO.cleanup()

    print("Bye!")

    sys.exit()





def setup():

    hx.set_offset(8394552.9375)

    hx.set_scale(-392.8046875)



def loop():

    try:

        val = hx.get_grams()

        hx.power_down()

        time.sleep(.001)

        hx.power_up()

        time.sleep(2)

    except (KeyboardInterrupt, SystemExit):

        cleanAndExit()

    return val

def dispense(motor_n,wanted_weight):

    init()

    setup()

    initial=hx.get_grams()

    print("Initial weight",initial)

    val=loop()

    while (val-initial<wanted_weight):

        activateServo(motor_n)

        if motor_n!=4:

            activateServo(motor_n)

        val=loop()

        print(val-initial)

    print("Done")

    final=val-initial

    print("final weight=",(val-initial))

    return final



