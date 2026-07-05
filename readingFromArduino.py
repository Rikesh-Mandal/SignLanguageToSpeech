#importing package from pySerial library
import serial.tools.list_ports

serialInst = serial.Serial()    #creating an empty instance of the Serial
serialInst.baudrate = 9600      #defining the baud rate
serialInst.port = "COM3"        #connecting to the port COM3
serialInst.open()               #opening the connection

while True:                     #creating an infinite loop
    if serialInst.in_waiting:   #if there is data incoming then
        packet = serialInst.readline()  #read the incoming data
        # decode from byte string to unicode and strip the extra line and print the data from serial
        print(packet.decode('utf').rstrip('\n'))
