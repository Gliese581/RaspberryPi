#!/usr/bin/python
######################################
##      Python-Script:              ##
##      Raspberry Pi B+             ##
##  and SAMSUNG UC121902-TNARX-A    ##
######################################

##  Pin 1 = 5V+
##  Pin 2 = GND
##  Pin 3 = CS      ->  PiPin 35
##  Pin 4 = Clock   ->  PiPin 36
##  Pin 5 = Data    ->  PiPin 37

import RPi.GPIO as GPIO		## Import GPIO Library
import time			## Import 'time' library (for 'sleep')
import sys			## Import System Libary for input arguments

data = []
for i in range(0,112):
    data.append(0)

test_data = [0,0,0,0,0,0,0,0,	## 12. Pos (c,x,d,b,g,a,e,f  x = N.C.)
             1,0,1,1,1,0,1,0,	## 11. Pos		: d
             0,0,1,0,0,0,1,1,	## 10. Pos		: L
             0,0,0,0,1,0,1,0,	## 9. Pos		: r
             1,0,1,0,1,0,1,0,	## 8. Pos		: o
             0,0,1,1,0,0,0,1,	## 7. Pos		: w
             0,0,0,0,1,		## Bell,Slash,MEM,CHAN,x
             1,0,0,		## 1(DP),0(DQ),0(DR) - 1/2 duty
				## Block Two
	     0,0,0,0,0,0,0,0,	## 6. Pos		:
	     1,0,1,0,1,0,1,0,	## 5. Pos		: o
             0,0,1,0,0,0,1,1,	## 4. Pos		: L
             0,0,1,0,0,0,1,1,	## 3. Pos		: L
             0,0,1,0,1,1,1,1,	## 2. Pos 		: E
             1,0,0,0,1,0,1,1,	## 1. Pos (leftmost): h
             0,0,0,0,1,		## SEC,PROG,BAT(empty),BAT(full),x
             0,0,1]		## x,x,1(DR)

def gpioInit():
    GPIO.setmode(GPIO.BOARD)        ## Use board pin numbering
    GPIO.setup(35, GPIO.OUT)        ## enable PiPin 35 -> CS
    GPIO.setup(36, GPIO.OUT)        ## enable PiPin 36 -> Clock
    GPIO.setup(37, GPIO.OUT)        ## enable PiPin 37 -> Data
    GPIO.output(35, GPIO.HIGH)      ## set CS = 1

def gpioClean():
    GPIO.output(35, GPIO.LOW)           ## set CS = 0
    GPIO.cleanup()                      ## Cleanup

def lcdTest():
    gpioInit()
    for i in range(0,112):
        if i == 56:
            GPIO.output(35, GPIO.LOW)   ## set CS = 0
            GPIO.output(35, GPIO.HIGH)  ## set CS = 1 -> begin with 2. block
	GPIO.output(36, GPIO.LOW)       ## set Clock = 0
        GPIO.output(37, test_data[i])	## load data-Bit
        GPIO.output(36, GPIO.HIGH)      ## set Clock high and write data-Bit
    gpioClean()

def writeWord():
    gpioInit()
    for i in range(0,112):
        if i == 56:
            GPIO.output(35, GPIO.LOW)   ## set CS = 0
            GPIO.output(35, GPIO.HIGH)  ## set CS = 1 -> begin with 2. block
	GPIO.output(36, GPIO.LOW)       ## set Clock = 0
        GPIO.output(37, data[i])	## load data-Bit
        GPIO.output(36, GPIO.HIGH)      ## set Clock high and write data-Bit
    gpioClean()

def lcdClean():
    for i in range(0,112):
        data[i] = 0
    data[53] = 1
    data[111] = 1
    writeWord()

for arg in sys.argv:
    if arg == "--test":
        lcdTest()
    if arg == "--clean":
        lcdClean()
