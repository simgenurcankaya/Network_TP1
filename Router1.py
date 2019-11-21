import socket
import time
import threading
import logging


#tek porttan clientserver olarak yolluyor

ip_get_r2 = "10.10.8.1"  #r2den r1e
ip_send_r2 = "10.10.8.2" #r1den r2ye

ip_send_s = "10.10.1.1"
ip_get_s = "10.10.1.2"

ip_send_d = "10.10.4.2"
ip_get_d = "10.10.4.1"

port_r2= 32984  #data alma-gonderme portlari
port_s = 32985
port_d = 23426

Message = "Sent by R1"

sockS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockR2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockD = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


start = 0 
stop = 0
diff = 0 

ortalama  = 0 

r1_r2 = open("r1_r2.txt","w+")
r1_s = open("r1_s.txt","w+")
r1_d = open("r1_d.txt","w+")


def message(port,ip):
    global ortalama
    for i in range(100):
        if(port == port_r2):
            if(ip == ip_send_r2): ## sender
                start = time.time()
                sockR2.sendto(Message, (ip, port)) 
                end = time.time()
                diff = end - start
                ortalama += diff
                print "Difference of R2" , diff
                r1_r2.write(str(diff)+'\n')
                #print "Ortalama" , ortalama
            elif (ip == ip_get_r2): #receiver
                data, addr = sockR2.recvfrom(18) 
                print "received message:", data
        elif(port == port_s):
            if(ip == ip_send_s):
                start = time.time()
                sockS.sendto(Message, (ip, port)) 
                end = time.time()
                diff = end - start
                ortalama += diff
                print "Difference of S  " , diff
                r1_s.write(str(diff)+'\n')
                #print "Ortalama" , ortalama
            elif (ip == ip_get_s): #receiver
                data, addr = sockS.recvfrom(18) 
                print "received message:", data
        elif(port == port_d):
            if(ip == ip_send_d):
                start = time.time()
                sockD.sendto(Message, (ip, port)) 
                end = time.time()
                diff = end - start
                ortalama += diff
                print "Difference of D " , diff
                r1_d.write(str(diff)+'\n')
                #print "Ortalama" , ortalama
            elif (ip == ip_get_d): #receiver
                data, addr = sockD.recvfrom(18) 
                print "received message:", data
        else:
            print "dddddddddddddddddddddddddddd\n\n"



  #  r1_r2.close()
  #  r1_d.close()
  #  r1_s.close()


def avarageCalculator(a):
    f=open(a,"r")
    average = 0
    for line in f:
        average += float(line.strip('\n'))
    print "AVARAGEEEEEEEEEEE " , average
    wrt = open("avg.txt","w+")
    wrt.write("Avg for " + a + " is : "+ str(average) +"\n")


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


    r1_r2.close()
    r1_d.close()
    r1_s.close()

    avarageCalculator("r1_r2.txt")
    avarageCalculator("r1_s.txt")
    avarageCalculator("r1_d.txt")

    logging.info("Main    : all done")

