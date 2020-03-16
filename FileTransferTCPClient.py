from socket import *
import datetime as d

serverName = ''                                                         #Server ip
serverPort = 0                                                          #Server port
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

clientSocket.send("Hello server!".encode())

fileName = clientSocket.recv(1024)                                      #receiving the name of file
with open(fileName.decode(), 'wb') as f:
    print ('file opened')
    print('Start receiving data: ', d.datetime.now())                   #mark the beginning
    while True:
        data = clientSocket.recv(1024)                                  #receive the file in packages
        if not data:
            break
        f.write(data)                                                   #write data to a file

f.close()
print('Successfully get the file at: ', d.datetime.now())               #mark the end 
clientSocket.close()
print('connection closed')