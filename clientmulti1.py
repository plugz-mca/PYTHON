import sys
import io
from socket import *
host = 'localhost' 
port = 5120
 
sock = socket()
#Connecting to socket
sock.connect((host, port)) 
 

while True:
	data = sock.recv(1024)
	print data
	print 'enter msg to server:'
	msg=sys.stdin.readline()
	sock.send(msg)
 
sock.close()
