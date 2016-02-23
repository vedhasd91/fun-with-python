#! /usr/bin/python

import socket
import time
import thread

def handler(client,addr):
	print "..client connected from.. ",addr
	data = "..client connected from.. " + `addr[0]` + " "+ `addr[1]`
	while 1:
		data =raw_input(">> ")
		if data=='q':
			client.send(data) 
                	client.close() 
                	break
		else:
			client.send(data)
	client.close()

if __name__ == "__main__":
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
	print "Socket created now binding.."
	#bind on this ip and this port	
	sock.bind(("127.0.0.1",8000))
	print "socket binding successful to port 8000"
	#listen to three clients	
	sock.listen(3)
	while 1:          
		client,addr=sock.accept()
		#--for threaded version, uncomment this line---thread.start_new_thread(handler,(client,addr))
		handler(client,addr)		
	sock.close()
	print "-----goodbye------"
