import socket

UDP_IP_ADDRESS = "10.10.8.1"
UDP_PORT1 = 40002  #data yollama port
UDP_PORT2 = 40003  #data alma port
Message = "Hello, R1"

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT2))


for i in range(0,10):
    #Sleep to sync 
    time.sleep(1)
    for y in range (0,10):
        #Receive packets
        data, addr = serverSock.recvfrom(18) 
        print "received message:", data
        #Send packets to destination 
        clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT1))