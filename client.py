import socket

UDP_IP_ADDRESS = "10.10.8.2"
UDP_PORT_NO = 6789
Message = "Hello, Server"

# Start after starting server 
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))