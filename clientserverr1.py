import socket
import time
import threading
import logging


#tek porttan clientserver olarak yolluyor

UDP_IP_ADDRESS = "10.10.8.1"  #r2den r1e
UDP_IP_ADDRESS2 = "10.10.8.2" #r1den r2ye
UDP_PORT= 32984  #data alma port

Message = "This message has sent by R1"

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT))

def Client(port,ip):
        logging.info("Client mode for R1")
        clientSock.sendto(Message, (ip, port))

def Server(port,ip):
        logging.info("Server mode for R1")
        data, addr = serverSock.recvfrom(50) 
        print "received message:", data

if __name__ == "__main__":
    x = threading.Thread(target=Server, args=(UDP_PORT,UDP_IP_ADDRESS))
    x.start()
    
    y = threading.Thread(target=Client, args=(UDP_PORT,UDP_IP_ADDRESS2))
    y.start()