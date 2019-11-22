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

r3_r2 = open("r3_r2.txt","w+")
r3_s = open("r3_s.txt","w+")
r3_d = open("r3_d.txt","w+")

def sendS(ip,port):
    for i in range(1000):
        print "Now sending " + str(i) + " with thread 1"
        start = time.time()
        sockS.sendto(Message + str(i), (ip, port)) 
        try:
            data, server = sockS.recvfrom(1024)
            end = time.time()
        except: 
            print "Error occured in R3-S"
        diff = end-start
        r3_s.write(str(diff)+ '\n')
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
            print "Error occured in R3-D"
        diff = end-start
        r3_d.write(str(diff)+ '\n')
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
            print "Error occured in R3-R2"
        diff = end-start
        r3_r2.write(str(diff)+ '\n')
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

    r3_d.close()
    r3_s.close()
    r3_r2.close()

    avgCalc("r3_r2.txt")
    avgCalc("r3_s.txt")
    avgCalc("r3_d.txt")
