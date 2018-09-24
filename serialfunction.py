#!/usr/bin/env python
#Mon 17 Sep 2018 07:54:17 PM CDT
#James Andrews
#Bryan Garcia

import time
import serial

#read serial code
ser = serial.Serial(
	port='/dev/ttyUSB0',
	baudrate = 4800,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	dsrdtr=False,
	rtscts=False,
	xonxoff=False,
	timeout=1
)

#While true, read 3 bytes from terminal and print in terminal
while 1:
	x=ser.read(3)
	print x


#Send serial code  

ser = serial.Serial(
	port='/dev/ttyAMA0',
	baudrate = 4800,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1
)

#if main controller authenticates, reply with AA5539+controllerstatus
authbits=AA553B
cubestat=
if x == authbits:
	ser.write('AA5539%d'%(cubestat))
	time.sleep(1)


