#!/usr/bin/python
######################################
##          Python-Script           ##
##          7-Segment LED           ##
##          Raspberry Pi B+         ##
######################################

import RPi.GPIO as GPIO             ## Import GPIO Library
import time                         ## Import 'time' library (for 'sleep')
import sys                          ## Import System Libary for input arguments

pin = [38,40,15,16,18,22,37,13]     ## Create Pin-Array
                                    ## Pin 38 = GPIO 20
                                    ## Pin 40 = GPIO 21
                                    ## Pin 15 = GPIO 22
                                    ## Pin 16 = GPIO 23
                                    ## Pin 18 = GPIO 24
                                    ## Pin 22 = GPIO 25
                                    ## Pin 37 = GPIO 26
                                    ## Pin 13 = GPIO 27

write_arg = ["0","1","2","3","4",
            "5","6","7","8","9","dot"]

data = [                            ## Matrix shows which led to turn on for spec. number
        [1,1,0,1,1,1,1,0],          ## 0
        [1,0,0,0,0,0,1,0],          ## 1
        [1,1,1,0,1,1,0,0],          ## 2
        [1,1,1,0,0,1,1,0],          ## 3
        [1,0,1,1,0,0,1,0],          ## 4
        [0,1,1,1,0,1,1,0],          ## 5
        [0,1,1,1,1,1,1,0],          ## 6
        [1,1,0,0,0,0,1,0],          ## 7
        [1,1,1,1,1,1,1,0],          ## 8
        [1,1,1,1,0,1,1,0],          ## 9
        [0,0,0,0,0,0,0,1]           ## .
       ]

def argToNumber(argument):
    for i in range(0,len(write_arg)-1):
        if argument == write_arg[i]:
            return i

def ledTest():
    GPIO.setmode(GPIO.BOARD)            ## Use BOARD pin numbering
    for i in range(0,8):
        GPIO.setup(pin[i], GPIO.OUT)    ## Set pin to OUTPUT

        GPIO.output(pin[i], GPIO.LOW)   ## Turn on GPIO pin (HIGH)
        time.sleep(1)                   ## Wait 1 second
        GPIO.output(pin[i], GPIO.HIGH)  ## Turn off GPIO pin (LOW)
        time.sleep(1)                   ## Wait 1 second
    GPIO.cleanup()                      ## Cleanup

def ledWrite(num):
    GPIO.setmode(GPIO.BOARD)                ## Use BOARD pin numbering
    for i in range(0,8):
        GPIO.setup(pin[i], GPIO.OUT)        ## Set pin to OUTPUT
        if data[num][i] == 0:               ## Set LED Off
            GPIO.output(pin[i], GPIO.HIGH)
        if data[num][i] == 1:               ## Set LED On
            GPIO.output(pin[i], GPIO.LOW)
    #GPIO.cleanup()

def ledClean():
    GPIO.setmode(GPIO.BOARD)            ## Use BOARD pin numbering
    for i in range(0,8):
        GPIO.setup(pin[i], GPIO.OUT)
        GPIO.output(pin[i], GPIO.HIGH)  ## Turn every LED Off
    GPIO.cleanup()                      ## Cleanup

def countToNumber(num):
    for i in range(0,num+1):
        ledWrite(i)
        time.sleep(0.1)
        ledClean()

if len(sys.argv) == 1 or sys.argv[1] == "help":
    print "Usage: command <option> <number>\n"
    print "options: test, clean, write, count2"
    print "numbers: [0 - 9]\n"
    print "Example: sudo ./ledAnzeige.py count2 7"

for arg in sys.argv:
    if arg == "test":
        ledTest()
    if arg == "write":
        number = argToNumber(sys.argv[2])
        ledWrite(number)
    if arg == "clean":
        ledClean()
    if arg == "count2":
        number = argToNumber(sys.argv[2])
        countToNumber(number)
