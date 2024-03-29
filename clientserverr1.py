import socket
import time
import threading
import logging


#tek porttan clientserver olarak yolluyor

UDP_IP_ADDRESS = "10.10.8.1"  #r2den r1e
UDP_IP_ADDRESS2 = "10.10.8.2" #r1den r2ye
UDP_PORT= 32984  #data alma port

Message = "This message has sent by R1"

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT))

start = 0 
stop = 0
diff = 0 

ortalama  = 0 

r1_r2 = open("r1_r2.txt","w+")


def message(port,ip):
    global ortalama
    for i in range(100):
        if(ip == UDP_IP_ADDRESS2): ## sender
            start = time.time()
            clientSock.sendto(Message, (ip, port)) 
            ip = UDP_IP_ADDRESS
            end = time.time()
            diff = end - start
            ortalama += diff
            print "Difference " , diff
            r1_r2.write(str(diff)+'\n')
            #print "Ortalama" , ortalama
        elif (ip == UDP_IP_ADDRESS): #receiver
            data, addr = serverSock.recvfrom(18) 
            print "received message:", data
            ip = UDP_IP_ADDRESS2
        else:
            print "asdalksdaslk\n"

    r1_r2.close()
    avarageCalculator("r1_r2.txt")


def avarageCalculator(a):
    f=open(a,"r")
    average = 0
    for line in f:
        average += float(line.strip('\n'))
    print "AVARAGEEEEEEEEEEE " , average


if __name__ == "__main__":
    
    global ortalama
    format = "%(asctime)s: %(message)s"

    logging.basicConfig(format=format, level=logging.INFO,

                        datefmt="%H:%M:%S")


    logging.info("Main    : before creating thread")

    x = threading.Thread(target=message, args=(UDP_PORT,UDP_IP_ADDRESS))
    y = threading.Thread(target=message, args=(UDP_PORT,UDP_IP_ADDRESS2))
   

    logging.info("Main    : before running thread")
    
    x.start()
    y.start()

    logging.info("Main    : wait for the thread to finish")

    # x.join()

    logging.info("Main    : all done")

    

print "Thread Stopped"
def Client(port,ip):
        logging.info("Client mode for R1")
        clientSock.sendto(Message, (ip, port))

def Server(port,ip):
        logging.info("Server mode for R1")
        data, addr = serverSock.recvfrom(50) 
        print "received message:", data

# if __name__ == "__main__":
#     x = threading.Thread(target=Server, args=(UDP_PORT,UDP_IP_ADDRESS))
#     x.start()
    
#     y = threading.Thread(target=Client, args=(UDP_PORT,UDP_IP_ADDRESS2))
#     y.start()
