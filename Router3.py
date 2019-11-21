import socket
import time
import threading
import logging


#tek porttan clientserver olarak yolluyor

ip_get_r2 = "10.10.6.2"  #r2den r1e
ip_send_r2 = "10.10.6.1" #r1den r2ye

ip_send_s = "10.10.3.1"
ip_get_s = "10.10.3.2"

ip_send_d = "10.10.7.2"
ip_get_d = "10.10.7.1"

port_r2= 32001  #data alma-gonderme portları
port_s = 35437
port_d = 44002

Message = "Sent by R3"

sockS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ssockR2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockD = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


start = 0 
stop = 0
diff = 0 

ortalama  = 0 

r3_r2 = open("r3_r2.txt","w+")
r3_s = open("r3_s.txt","w+")
r3_d = open("r3_d.txt","w+")


def message(port,ip):
    global ortalama
    for i in range(100):
        if(port == port_r2):
            if(ip == ip_send_r2): ## sender
                start = time.time()
                clientSock.sendto(Message, (ip, port)) 
                end = time.time()
                diff = end - start
                ortalama += diff
                print "Difference " , diff
                r3_r2.write(str(diff)+'\n')
                #print "Ortalama" , ortalama
            elif (ip == ip_get_r2): #receiver
                data, addr = serverSock.recvfrom(18) 
                print "received message:", data
        elif(port == port_s):
            if(ip == ip_send_s):
                start = time.time()
                clientSock.sendto(Message, (ip, port)) 
                end = time.time()
                diff = end - start
                ortalama += diff
                print "Difference " , diff
                r3_s.write(str(diff)+'\n')
                #print "Ortalama" , ortalama
            elif (ip == ip_get_s): #receiver
                data, addr = serverSock.recvfrom(18) 
                print "received message:", data
        elif(port == port_d):
                if(ip == ip_send_d):
                start = time.time()
                clientSock.sendto(Message, (ip, port)) 
                end = time.time()
                diff = end - start
                ortalama += diff
                print "Difference " , diff
                r3_d.write(str(diff)+'\n')
                #print "Ortalama" , ortalama
            elif (ip == ip_get_d): #receiver
                data, addr = serverSock.recvfrom(18) 
                print "received message:", data
        else:
            print "dddddddddddddddddddddddddddd\n\n"



    r3_r2.close()
    r3_d.close()
    r3_s.close()
    avarageCalculator("r3_r2.txt")
    avarageCalculator("r3_s.txt")
    avarageCalculator("r3_d.txt")


def avarageCalculator(a):
    f=open(a,"r")
    wrt = open("avg.txt","w+")
    average = 0
    for line in f:
        average += float(line.strip('\n'))
    print "AVARAGEEEEEEEEEEE " , average
    wrt.write("Avg for " + a + " is : "+ average +"\n")


if __name__ == "__main__":
    
    format = "%(asctime)s: %(message)s"

    logging.basicConfig(format=format, level=logging.INFO,

                        datefmt="%H:%M:%S")


    logging.info("Main    : before creating thread")

    x = threading.Thread(target=message, args=(port_r2,ip_send_r2))
    y = threading.Thread(target=message, args=(port_d,ip_send_d))
    z = threading.Thread(target=message, args=(port_s,ip_send_s))
  

    logging.info("Main    : before running thread")
    
    x.start()
    y.start()
    z.start()
    logging.info("Main    : wait for the thread to finish")

    # x.join()

    logging.info("Main    : all done")

