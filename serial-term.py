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

#Print data and decode to hex
while 1:
	x=ser.read(size=3))
	print x.decode("hex")
	time.sleep(0.018)

