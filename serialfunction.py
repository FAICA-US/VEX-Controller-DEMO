#!/usr/bin/env python
#Mon 17 Sep 2018 07:54:17 PM CDT
# James Andrews
# Bryan 

#Authenticate with controller

		#read serial code
           ser = serial.Serial(
              
               port='/dev/ttyUSB0',
               baudrate = 4800,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=1
           )
           counter=0
          
      
           while 1:
               x=ser.readline()
               print x


          
#Write serial code    
           import time
           import serial
          
      
           ser = serial.Serial(
              
               port='/dev/ttyAMA0',
               baudrate = 4800,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=1
           )
           counter=0
          
      
           while 1:
               ser.write('Write counter: %d \n'%(counter))
               time.sleep(1)
               counter += 1


