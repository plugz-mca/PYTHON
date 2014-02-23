from socket import *
from io import *
from sys import *
 
host = 'localhost' 
port = 5120
 
sock = socket()

sock.connect((host, port)) 
 

while True:
	data = sock.recv(1024)
	print data
	print ' ENTER MESSAGE TO SERVER:'
	MG=sys.stdin.readline()
	sock.send(MG)
 
sock.close()
