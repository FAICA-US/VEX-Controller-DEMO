#!/usr/bin/env python

import time
import serial

ser = serial.Serial(
	port='/dev/ttyUSB1',
	baudrate = 4800,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,

#disable dsr, rts, xonoff flow control
	dsrdtr=False,
	rtscts=False,
	xonxoff=False,
	timeout=1
)

while 1:
	x=ser.read(size=1)
	print x
	time.sleep(0.018)

