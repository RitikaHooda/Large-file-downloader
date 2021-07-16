from socket import *
import sys
import time
import threading
file_size = 6488666
part_size = 10000
i = 0 
def receive(clientSocket, file):
    while True:
        data = clientSocket.recv(4096)
        if not data:
            break
        file.write(data.decode('utf-8'))
def get_chunk(clientSocket, file,lock):
    global i
    num = 0
    if i> (file_size/part_size):
        return False
    with lock:
        i=i+1
        num  = i-1
    message = 'GET /big.txt HTTP/1.1\r\nHost:vayu.iitd.ac.in\r\nConnection: keep-alive\r\nRange: bytes='+str((num*part_size))+'-'+str(((num+1)*part_size)-1)+'\r\n\r\n'
    clientSocket.send(bytes(message, 'utf-8'))
    if num==0:
        clientSocket.recv(260)    
    receive(clientSocket, file)
    #print(str(num) + " received")
    return True
def run(clientSocket, file, lock):
    flag = get_chunk(clientSocket, file,lock)
    while flag:
        flag = get_chunk(clientSocket, file,lock)
def main():
    start = time.time()
    serverName = 'vayu.iitd.ac.in'
    serverPort = 80
    ip_address = gethostbyname(serverName)
    file = open('big.txt', 'w+')
    num_of_tcp = 10
    lock = threading.Lock()
    threads = []
    for i in range(num_of_tcp):
        clientSocket = socket(AF_INET,SOCK_STREAM)
        clientSocket.connect((ip_address,serverPort))
        thread = threading.Thread(target=run, args=(clientSocket, file, lock))
        threads.append(thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()    
    print(time.time()- start)
    file.close()
if __name__ == "__main__":
    main()
