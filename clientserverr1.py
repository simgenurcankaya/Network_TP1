import socket
import time
import threading
from thread import *

#tek porttan clientserver olarak yolluyor

UDP_IP_ADDRESS = "10.10.8.1"  #r2den r1e
UDP_IP_ADDRESS2 = "10.10.8.2" #r1den r2ye
UDP_PORT= 32984  #data alma port

Message = "Hello, R2"

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT))

def message(port,ip):
    for i in range(0,10):
        #Send packets to destination 
        clientSock.sendto(Message, (ip, port))    
        for y in range (0,10):
            #Receive packets
            data, addr = serverSock.recvfrom(18) 
            print "received message:", data



thread.start_new_thread(message, args = (UDP_PORT, UDP_IP_ADDRESS2))
threadistart_new_thread(message, args = (UDP_PORT, UDP_IP_ADDRESS))

print "Thread Stopped"
