import socket
import time
import threading

IP_r2_s = "10.10.2.2" #The IP of Router2 -> Source
IP_s_r2 = "10.10.2.1" #The IP of Source -> Router2

IP_r2_r1 = "10.10.8.1" #The IP of Router2 -> Router1
IP_r1_r2 = "10.10.8.2" #The IP of Router1 -> Router2

IP_r2_r3 = "10.10.6.2" #The IP of Router2 -> Router3
IP_r3_r2 = "10.10.6.1" #The IP of Router3 -> Router2

IP_r2_d = "10.10.5.1" #The IP of Router2 -> Destination
IP_d_r2 = "10.10.5.2" #The IP of Destination -> Router2

PORT_s = 35436
PORT_r1 = 32985
PORT_r3 = 32001
PORT_d = 44546

clientS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientD = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverD = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientR1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverR1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientR3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverR3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverR3.bind((IP_r3_r2,PORT_r3))
serverR1.bind((IP_r1_r2,PORT_r1))

start = 0 
stop = 0
diff = 0 

ortalama  = 0 

r2_d = open("r1_r2.txt","w+")
r2_s = open("r1_s.txt","w+")

def message(port,ip):
    global ortalama
    for i in range(100):
        if(ip == IP_r1_r2):
            data, addr = serverR1.recvfrom(50) 
            print "received message from Router1:", data
        
        elif (ip == IP_r3_r2):
            data, addr = serverR3.recvfrom(50) 
            print "received message from Router3:", data
        
        elif (ip == IP_r2_d):
            start = time.time()
            clientD.sendto("This message has sent by r2", (ip, port)) 
            end = time.time()
            diff = end - start
            ortalama += diff
            print "Difference of Destination" , diff
            r2_d.write(str(diff)+'\n')

        elif (ip == IP_r2_s):
            start = time.time()
            clientS.sendto("This message has sent by r2", (ip, port)) 
            end = time.time()
            diff = end - start
            ortalama += diff
            print "Difference of Source" , diff
            r2_s.write(str(diff)+'\n')

        else:
            print "Error"

def avarageCalculator(a):
    f=open(a,"r")
    print "AVARAGEEEEEEEEEEE FOOORR  " , a
    average = 0
    for line in f:
        average += float(line.strip('\n'))
    
    wrt = open("avg.txt","a")
    wrt.write("\n Avg for " + a + " is : "+ str(average) +"\n")
    wrt.close()

if __name__ == "__main__":
    thread1 = threading.Thread(target=message, args=(PORT_r1,IP_r1_r2))
    thread2 = threading.Thread(target=message, args=(PORT_r3,IP_r3_r2))
    thread3 = threading.Thread(target=message, args=(PORT_s,IP_r2_s))
    thread4 = threading.Thread(target=message, args=(PORT_d,IP_r2_d))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    boole = 0
    wrt = open("avg.txt","w")
    while(boole != 2):
        boole = 0
        if(x.isAlive()==False):
            r1_d.close()
            avarageCalculator("r2_d.txt")
            boole += 1
        if(y.isAlive() == False):
            r2_s.close()
            avarageCalculator("r2_s.txt")
            boole += 1