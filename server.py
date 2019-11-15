
import socket


# SERVER NEEDS TO START BEFORE CLIENT
# IP and Port is the same with client 
UDP_IP_ADDRESS = "10.10.8.2"
UDP_PORT_NO = 6789

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))


while True:
    data, addr = serverSock.recvfrom(1024)
    print "Message: ", data