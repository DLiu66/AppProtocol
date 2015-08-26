import TCPSocket
import random

serverobj = TCPSocket.ServerSocket()
while True:
	print "---wating for connection----"
	connection, client_address = serverobj.sock.accept()
	data = connection.recv(16)
	print "received :"+data
	connection.sendall(str(random.randint(1,10)))

#serverobj.RunServer() 