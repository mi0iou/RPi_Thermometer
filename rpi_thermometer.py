# RPi Thermometer v1.0

# This program is designed to run on the Raspberry Pi model B+

# Copyright (C) 2014 Tom Herbison MI0IOU
# Email tom@asliceofraspberrypi.co.uk
# Web <http://www.asliceofraspberrypi.co.uk>

# import modules
import sys
import time
import RPi.GPIO as GPIO

# set up GPIO port
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Set GPIO Output Pins
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

# function to clear the LED display
def cleardisplay():
    GPIO.output(5,0)
    GPIO.output(6,0)
    GPIO.output(7,0)
    GPIO.output(8,0)
    GPIO.output(9,0)
    GPIO.output(10,0)
    GPIO.output(11,0)
    GPIO.output(12,0)
    GPIO.output(13,0)
    GPIO.output(16,0)
    GPIO.output(17,0)
    GPIO.output(18,0)
    GPIO.output(19,0)
    GPIO.output(20,0)
    GPIO.output(21,0)
    GPIO.output(22,0)
    GPIO.output(23,0)
    GPIO.output(24,0)
    GPIO.output(25,0)
    GPIO.output(26,0)
    GPIO.output(27,0)
    return

# function to display digits on LED display
def displaydigit(digit,a,b,c,d,e,f,g):
    if digit=="0":
        GPIO.output(a,1)
        GPIO.output(b,1)
        GPIO.output(c,1)
        GPIO.output(d,1)
        GPIO.output(e,1)
        GPIO.output(f,1)
    if digit=="1":
        GPIO.output(b,1)
        GPIO.output(c,1)
    if digit=="2":
        GPIO.output(a,1)
        GPIO.output(b,1)
        GPIO.output(d,1)
        GPIO.output(e,1)
        GPIO.output(g,1)
    if digit=="3":
        GPIO.output(a,1)
        GPIO.output(b,1)
        GPIO.output(c,1)
        GPIO.output(d,1)
        GPIO.output(g,1)
    if digit=="4":
        GPIO.output(b,1)
        GPIO.output(c,1)
        GPIO.output(f,1)
        GPIO.output(g,1)
    if digit=="5":
        GPIO.output(a,1)
        GPIO.output(c,1)
        GPIO.output(d,1)
        GPIO.output(f,1)
        GPIO.output(g,1)
    if digit=="6":
        GPIO.output(a,1)
        GPIO.output(c,1)
        GPIO.output(d,1)
        GPIO.output(e,1)
        GPIO.output(f,1)
        GPIO.output(g,1)
    if digit=="7":
        GPIO.output(a,1)
        GPIO.output(b,1)
        GPIO.output(c,1)
    if digit=="8":
        GPIO.output(a,1)
        GPIO.output(b,1)
        GPIO.output(c,1)
        GPIO.output(d,1)
        GPIO.output(e,1)
        GPIO.output(f,1)
        GPIO.output(g,1)
    if digit=="9":
        GPIO.output(a,1)
        GPIO.output(b,1)
        GPIO.output(c,1)
        GPIO.output(d,1)
        GPIO.output(f,1)
        GPIO.output(g,1)
    if digit=="-":
        GPIO.output(g,1)
    if digit=="E":
        GPIO.output(a,1)
        GPIO.output(d,1)
        GPIO.output(e,1)
        GPIO.output(f,1)
        GPIO.output(g,1)
    return

# main program starts here
try:
    print("Press Ctrl+C to exit")
    while (True):
        # take a temperature measurement and format the raw data
        tfile=open("/sys/bus/w1/devices/"+str(sys.argv[1])+"/w1_slave")
        text=tfile.read()
        tfile.close()
        secondline=text.split("\n")[1]
        temperaturedata=(secondline.split(" ")[9])[2:]
        if temperaturedata[0]=="-":
            if len(temperaturedata)==2:
                temperaturedata="-0"+temperaturedata[1]
            if len(temperaturedata)==3:
                temperaturedata="-0"+temperaturedata[1:]
            if len(temperaturedata)==4:
                temperaturedata="-0"+temperaturedata[1:]
            if len(temperaturedata)>5:
                temperaturedata="EEE"
        else:
            if len(temperaturedata)==1:
                temperaturedata="0"+temperaturedata
            if len(temperaturedata)==2:
                temperaturedata="0"+temperaturedata
            if len(temperaturedata)==3:
                temperaturedata="0"+temperaturedata
            if len(temperaturedata)==4:
                temperaturedata="0"+temperaturedata
            if len(temperaturedata)>5:
                temperaturedata="EEE"
        #clear the display
        cleardisplay()
        # display the temperature on the LED display
        displaydigit(temperaturedata[0],19,13,12,16,20,26,21)
        displaydigit(temperaturedata[1],11,9,25,8,7,5,6)
        displaydigit(temperaturedata[2],27,17,18,23,24,22,10)
        # pause for 1 second
        time.sleep(1)

except KeyboardInterrupt:
    print("\nExiting now...")
    cleardisplay()
    GPIO.cleanup()
