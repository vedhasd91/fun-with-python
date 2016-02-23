#! /usr/bin/python

import time
import thread

def networkhandler(param):
	print "In network handler" + str(param)
	return 0

def gpshandler(param):
	print "In gps handler" + str(param)
	return 0

def classhandler():
	return 0

if __name__ == "__main__":
	print "============================"
	print "		MASTER NODE        "
	print "============================"
	thread.start_new_thread(networkhandler,(1,))
	thread.start_new_thread(gpshandler,(1))
	while 1:
		print " "
	print "goodbye"
