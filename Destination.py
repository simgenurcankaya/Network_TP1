import socket
import time
import threading

IP_r1_d = "10.10.4.2" #The IP of Router1 -> Destination
IP_r2_d = "10.10.5.2" #The IP of Router2 -> Destination
IP_r3_d = "10.10.7.2" #The IP of Router3 -> Destination

PORT_r1 = 23426 #Port Number For Router1
PORT_r2 = 44004 #Port Number For Router2
PORT_r3 = 45678 #Port Number For Router3

serverSockR1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSockR2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSockR3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSockR1.bind((IP_r1_d, PORT_r1))
serverSockR2.bind((IP_r2_d, PORT_r2))
serverSockR3.bind((IP_r3_d, PORT_r3))

def message(port,ip):
    for i in range(100):
        if(ip == IP_r1_d):
            data, addr = serverSockR1.recvfrom(50) 
            print "received message from Router1:", data
        
        elif (ip == IP_r2_d):
            data, addr = serverSockR2.recvfrom(50) 
            print "received message from Router2:", data
        
        elif (ip == IP_r3_d):
            data, addr = serverSockR3.recvfrom(50) 
            print "received message from Router3:", data
        
        else:
            print "Error"

if __name__ == "__main__":
    thread1 = threading.Thread(target=message, args=(PORT_r1,IP_r1_d))
    thread2 = threading.Thread(target=message, args=(PORT_r2,IP_r2_d))
    thread3 = threading.Thread(target=message, args=(PORT_r3,IP_r3_d))

    thread1.start()
    thread2.start()
    thread3.start()