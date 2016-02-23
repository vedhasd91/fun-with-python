#! /usr/bin/python
#Script on the client side to connect to
#router and send and receive data
import socket
from datetime import datetime
from time import time

#--open file to log in append mode--
log_txt=open('/home/vedhasd/scripts/log.txt','a')
print "Creating client socket"
#---Create a socket---
csock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "socket created.."
#---Connect to Raspberry PI---
#csock.connect(('175.156.0.5',8000))
print "connected"
#--Continuously poll for packet--
while 1:
	csock.connect(('175.156.0.5',8000))
	data=csock.recv(10240)
	if data=='q':
		csock.close()
		log_txt.close()
		break
	else:
		print datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S')+ " "+data
		log_txt.write(datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S')+" "+data+"\n")
	csock.close()
print "-----goodbye------"

