import sys
import io
from socket import *
from thread import *

host = ''  
port = 5120
 

sock = socket()
sock.bind((host, port))

sock.listen(5) 
 
def clientthread(conn):
 
	while True:
		print 'conected with:',conn
		print 'enter message to client:'
		m=sys.stdin.readline()
		conn.send(m) 
		data = conn.recv(1024) 
		print data
		
  
 
while True:

    conn, addr = sock.accept()

    start_new_thread(clientthread,(conn,)) 
conn.close()
sock.close()
