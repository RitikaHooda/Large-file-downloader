from socket import *
import sys
import time
import threading
file_size = 6488666
part_size = 10000
i = 0 
serverPort = 80
def receive(clientSocket, file):
    while True:
        data = clientSocket.recv(4096)
        if not data:
            break
        file.write(data.decode('utf-8'))
def get_chunk(clientSocket, file,lock,serverName):
    global i
    num = 0
    if i> (file_size/part_size):
        return False
    with lock:
        i=i+1
        num  = i-1   
    message = 'GET /big.txt HTTP/1.1\r\nHost'+ serverName'\r\n\r\nRange: bytes='+str((num*part_size))+'-'+str(((num+1)*part_size)-1)+'\r\n\r\n'
    try:
        clientSocket.send(bytes(message, 'utf-8'))
    except:
        ip_address = gethostbyname(serverName)
        clientSocket.connect((ip_address,serverPort))
        clientSocket.send(bytes(message, 'utf-8'))
    if num==0:
        clientSocket.recv(260)    
    receive(clientSocket, file)
    #print(str(num) + " received")
    return True
def run(clientSocket, file, lock,serverName):
    flag = get_chunk(clientSocket, file,lock,serverName)
    while flag:
        flag = get_chunk(clientSocket, file,lock)
def main(serverName, num_of_tcp, file):
    #serverName = 'vayu.iitd.ac.in'
    ip_address = gethostbyname(serverName)
    #num_of_tcp = 2
    lock = threading.Lock()
    threads = []
    for i in range(num_of_tcp):
        clientSocket = socket(AF_INET,SOCK_STREAM)
        clientSocket.connect((ip_address,serverPort))
        thread = threading.Thread(target=run, args=(clientSocket, file, lock,serverName))
        threads.append(thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()    
    
if __name__ == "__main__":
    filename = sys.argv[1]
    start = time.time()
    file = open(filename,'r')
    outputfile = open('big.txt', 'w+')
    line = file.readline()
    while line:
        serverName, num_of_tcp = line.split(',')
        main(serverName, num_of_tcp,outputfile)
        line = file.readline()
    file.close()
    outputfile.close()
    print(time.time()- start)
