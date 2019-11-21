import socket
import time
import threading 
import thread 

# tek porttan clientserver olarak yolluyor 

UDP_IP_ADDRESS = "10.10.8.1"  #r2den r1e
UDP_IP_ADDRESS2 = "10.10.8.2" #r1den r2ye
UDP_PORT = 32984  

Message = "Hello, R1"

def message(port,ip):
    for i in range(0,10):
        #Send packets to destination 
        clientSock.sendto(Message, (ip, port))    
        for y in range (0,10):
            #Receive packets
            data, addr = serverSock.recvfrom(18) 
            print "received message:", data



clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS2, UDP_PORT))


start_new_thread(message, args = (UDP_PORT, UDP_IP_ADDRESS))
start_new_thread(message, args = (UDP_PORT, UDP_IP_ADDRESS2))


print "Thread Stopped"
