import socket
import time

IP_r1_d = "10.10.4.2" #The IP of Router1 -> Destination
IP_r2_d = "10.10.5.2" #The IP of Router2 -> Destination
IP_r3_d = "10.10.7.2" #The IP of Router3 -> Destination

PORT_r1 = 23426 #Port Number For Router1
PORT_r2 = 44004 #Port Number For Router2
PORT_r3 = 44002 #Port Number For Router3

def message(port,ip):
    for i in range(100):
        if(ip == IP_r1_d):
            data, addr = serverSock.recvfrom(50) 
            print "received message:", data
        
        elif (ip == IP_r2_d):
            data, addr = serverSock.recvfrom(50) 
            print "received message:", data
        
        elif (ip == IP_r3_d):
            data, addr = serverSock.recvfrom(50) 
            print "received message:", data
        
        else:
            print "Error"

if __name__ == "__main__":
    thread1 = threading.Thread(target=message, args=(PORT_r1,IP_r1_s))
    thread2 = threading.Thread(target=message, args=(PORT_r2,IP_s_r2))
    thread3 = threading.Thread(target=message, args=(PORT_r3,IP_r3_s))

    thread1.start()
    thread2.start()
    thread3.start()