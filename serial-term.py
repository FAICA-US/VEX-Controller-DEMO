#!/usr/bin/env python
import sys
import glob
import time
import serial

#Get USB info
def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


if __name__ == '__main__':
    print(serial_ports())


#Recieve serial data from defined ports above
ports = [serial.Serial(
	port=i,
	baudrate = 4800,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
#disable dsr, rts, xonoff flow control
	dsrdtr=False,
	rtscts=False,
	xonxoff=False,
	timeout=1
) for i in serial_ports()]


#Print data and decode to hex
while True:
    for p in ports:
        byts=p.read(size=3)
        print p,port+" :",x.decode("hex")
        time.sleep(0.018)
    print '\n'
