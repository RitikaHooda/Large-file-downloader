from socket import *
import sys
import time
def receive(clientSocket, file):
    while True:
        data = clientSocket.recv(4096)
        if not data:
            break
        file.write(data.decode('utf-8'))
def main():
    start = time.time()
    serverName = 'vayu.iitd.ac.in'
    serverPort = 80
    ip_address = gethostbyname(serverName)
    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((ip_address,serverPort))
    file_size = 6488666
    number_of_parts = 100
    part_size= file_size/number_of_parts
    file = open('big.txt', 'w+')
    for i in range(number_of_parts):
        message = 'GET /big.txt HTTP/1.1\r\nHost:vayu.iitd.ac.in\r\n\r\nRange: bytes='+str((i*part_size))+'-'+str(((i+1)*part_size)-1)+'\r\n\r\n'
        clientSocket.send(bytes(message, 'utf-8'))
        if i == 0:
            clientSocket.recv(260)
        receive(clientSocket, file)
    clientSocket.close()
    print(time.time()- start)
    file.close()
if __name__ == "__main__":
    main()
