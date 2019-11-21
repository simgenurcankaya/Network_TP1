import socket
import time

IP_r1_s = "10.10.1.1" #The IP of Router1 -> Source
IP_r2_s = "10.10.2.2" #The IP of Router2 -> Source
IP_r3_s = "10.10.3.1" #The IP of Router3 -> Source

PORT_r1 = 35435 #Port Number For Router1
PORT_r2 = 35436 #Port Number For Router2
PORT_r3 = 35437 #Port Number For Router3

serverSockR1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSockR2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSockR3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSockR1.bind((IP_r1_s, PORT_r1))
serverSockR2.bind((IP_r2_s, PORT_r2))
serverSockR3.bind((IP_r3_s, PORT_r3))

def message(port,ip):
    for i in range(100):
        if(ip == IP_r1_s):
            data, addr = serverSock.recvfrom(18) 
            print "received message:", data
        
        elif (ip == IP_s_r2):
            data, addr = serverSock.recvfrom(18) 
            print "received message:", data
        
        elif (ip == IP_r3_s):
            data, addr = serverSock.recvfrom(18) 
            print "received message:", data
        
        else:
            print "Error"

if __name__ == "__main__":
    x = threading.Thread(target=message, args=(PORT_r1,IP_r1_s))
    y = threading.Thread(target=message, args=(PORT_r2,IP_s_r2))
    z = threading.Thread(target=message, args=(PORT_r3,IP_r3_s))

    x.start()
    y.start()
    z.start()