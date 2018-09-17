#!/usr/bin/env python
   
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
          
#While 1, write counter
           while 1:
               ser.write('Write counter: %d'%(counter))
               time.sleep(1)
               counter += 1

#read AA 55 3B serial code

           ser = serial.Serial(
              
               port='/dev/ttyUSB0',
               baudrate = 4800,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=1
           )
           counter=0
          
#look for AA 55 3B and reply with AA 55 39 0A RX RY LX LY 00      
           while 1:
               x=ser.readline()
                while x=aa553b
               ser.write('%d'%(counter))

               time.sleep(1)                    
#For Debugging               print x




