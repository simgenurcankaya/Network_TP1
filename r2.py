import socket
import time
import threading
import logging


ip_get_r1 = "10.10.8.2"  
ip_send_r1 = "10.10.8.1" 

ip_send_s = "10.10.2.2"
ip_get_s = "10.10.2.1"

ip_send_d = "10.10.5.2"
ip_get_d = "10.10.5.1"

ip_get_r3 = "10.10.6.1"
ip_send_r3 = "10.10.6.2"

port_r1 = 32984  #data alma-gonderme portlari
port_r3 = 32001
port_s = 35436
port_d = 44004

Message = "Sent by R2 "

sockS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockR1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockD = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockR3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



def sendS(ip,port):
    for i in range(1000):
        print "Now sending " + str(i) + "with thread 1"
        sockS.sendto(Message + str(i), (ip, port)) 
        print "Finished sending " + str(i) + "with thread 1"

def sendD(ip,port):
    for i in range(1000):
        print "Now sending " + str(i) + "with thread 2"
        sockD.sendto(Message + str(i), (ip, port)) 
        print "Finished sending " + str(i) + "with thread 2"

def getR1(ip,port):
    sockR1.bind((ip,port))
    while True:
        data, addr = sockR1.recvfrom(1024)
        print "Message: ", data

def getR3(ip,port):
    sockR3.bind((ip,port))
    while True:
        data, addr = sockR3.recvfrom(1024)
        print "Message: ", data


if __name__ == "__main__":

    t1 = threading.Thread(target=sendS, args=(ip_send_s,port_s)) 
    t2 = threading.Thread(target=sendD, args=(ip_send_d,port_d)) 
    t3 = threading.Thread(target=getR1, args=(ip_get_r1,port_r1)) 
    t4 = threading.Thread(target=getR3, args=(ip_get_r3,port_r3)) 

    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
    t3.start()
    t4.start()
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
    t3.join()
    t4.join()
    # both threads completely executed 
    print("Done!") 