from socket import *
import datetime as d

serverPort = 0										#put the port to receive the connection
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)								#number of connections simultaneously
print('The server is ready to receive')

while 1:
	connectionSocket, addr = serverSocket.accept()
	print(addr)
	print("Connection start: ",d.datetime.now())	#mark the beginning
	data = connectionSocket.recv(1024)
	filename = "FileTransferTCPServer.py"			#put the name of the file that is on the same folder of this code
	connectionSocket.send(filename.encode())		#send the name of the file
	f = open(filename,'rb')
	l = f.read(1024)
	
	while(l):
		connectionSocket.send(l)					#send the file in packages
		l = f.read(1024)
	
	print("Done sending: ", d.datetime.now())		#mark the end
	connectionSocket.close()						
		
