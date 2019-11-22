import socket
import time
import threading
import logging


ip_get_r2 = "10.10.8.1"  #r2den r1e
ip_send_r2 = "10.10.8.2" #r1den r2ye

ip_send_s = "10.10.1.1"
ip_get_s = "10.10.1.2"

ip_send_d = "10.10.4.2"
ip_get_d = "10.10.4.1"

port_r2= 32984  #data alma-gonderme portlari
port_s = 32985
port_d = 23426

Message = "Sent by R1 "

sockS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockR2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockD = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

r1_r2 = open("r1_r2.txt","w+")
r1_s = open("r1_s.txt","w+")
r1_d = open("r1_d.txt","w+")

def sendS(ip,port):
    for i in range(1000):
        print "Now sending " + str(i) + " with thread 1"
        start = time.time()
        sockS.sendto(Message + str(i), (ip, port)) 
        try:
            data, server = sockS.recvfrom(1024)
            end = time.time()
        except: 
            print "Error occured in R1-S"
        diff = end-start
        r1_s.write(str(diff)+ '\n')
        print "Finished sending " + str(i) + " with thread 1"

def sendD(ip,port):
    for i in range(1000):
        print "Now sending " + str(i) + " with thread 2"
        start = time.time()
        sockD.sendto(Message + str(i), (ip, port)) 
        try:
            data, server = sockD.recvfrom(1024)
            end = time.time()
        except: 
            print "Error occured in R1-D"
        diff = end-start
        r1_d.write(str(diff)+ '\n')
        print "Finished sending " + str(i) + " with thread 2"

def sendR2(ip,port):
    for i in range(1000):
        print "Now sending " + str(i) + " with thread 3"
        start = time.time()
        sockR2.sendto(Message + str(i), (ip, port)) 
        try:
            data, server = sockR2.recvfrom(1024)
            end = time.time()
        except: 
            print "Error occured in R1-R2"
        diff = end-start
        r1_r2.write(str(diff)+ '\n')
        print "Finished sending " + str(i) + " with thread 3"


def avgCalc(a):
    f = open(a,"r")
    average = 0
    for line in f:
        average += float(line.strip('\n'))
    wrt = open("avg.txt","a")
    wrt.write("Avg for " + a + " is : "+ str(average) +"\n")
    wrt.close()

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

    r1_r2.close()
    r1_s.close()
    r1_d.close()

    avgCalc("r1_r2.txt")
    avgCalc("r1_s.txt")
    avgCalc("r1_d.txt")