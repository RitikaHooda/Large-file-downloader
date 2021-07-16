from socket import *
import sys
import time
start = time.time()
file_size= 6488666
serverName = 'vayu.iitd.ac.in'
serverPort = 80
ip_address = gethostbyname(serverName)
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((ip_address,serverPort))
message = 'GET /big.txt HTTP/1.1\r\nHost:vayu.iitd.ac.in\r\n\r\n'
clientSocket.send(bytes(message, 'utf-8'))
file = open('big.txt', 'w+')
data = clientSocket.recv(260)
while True:
    data = clientSocket.recv(file_size)
    if not data:
        break
    string = str(data, 'utf-8')
    file.write(string)
clientSocket.close()
print(time.time()- start)
print(file.read())
file.close()
