import socket
import time
import threading
import logging


ip_get_r2 = "10.10.6.2"  #r2den r1e
ip_send_r2 = "10.10.6.1" #r1den r2ye

ip_send_s = "10.10.3.1"
ip_get_s = "10.10.3.2"

ip_send_d = "10.10.7.1"
ip_get_d = "10.10.7.2"

port_r2= 32001  #data alma-gonderme portlari
port_s = 35437
port_d = 45678

Message = "Sent by R3 "

sockS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockR2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockD = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



def sendS(ip,port):
    for i in range(1000):
        print "Now sending " + str(i) + " with thread 1"
        sockS.sendto(Message + str(i), (ip, port)) 
        print "Finished sending " + str(i) + " with thread 1"

def sendD(ip,port):
    for i in range(1000):
        print "Now sending " + str(i) + " with thread 2"
        sockD.sendto(Message + str(i), (ip, port)) 
        print "Finished sending " + str(i) + " with thread 2"

def sendR2(ip,port):
    for i in range(1000):
        print "Now sending " + str(i) + " with thread 3"
        sockR2.sendto(Message + str(i), (ip, port)) 
        print "Finished sending " + str(i) + " with thread 3"


if __name__ == "__main__":

    t1 = threading.Thread(target=sendS, args=(ip_send_s,port_s)) 
    t2 = threading.Thread(target=sendD, args=(ip_send_d,port_d)) 
    t3 = threading.Thread(target=sendR2, args=(ip_send_r2,port_r2)) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
    t3.start()
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
    t3.join()
    # both threads completely executed 
    print("Done!") 