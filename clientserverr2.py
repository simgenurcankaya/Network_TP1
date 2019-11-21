import socket
import time
import threading 
import logging


# tek porttan clientserver olarak yolluyor 

UDP_IP_ADDRESS = "10.10.8.1"  #r2den r1e
UDP_IP_ADDRESS2 = "10.10.8.2" #r1den r2ye
UDP_PORT = 32984  

Message = "Hello, R1"

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS2, UDP_PORT))

start = 0 
stop = 0
diff = 0 
ortalama = 0 


def message(port,ip):
    for i in range(100):
        global ortalama
        if(ip == UDP_IP_ADDRESS): ## sender
            start = time.time()
            clientSock.sendto(Message, (ip, port)) 
            ip = UDP_IP_ADDRESS2
            end = time.time()
            diff   = end - start
            print "Difference " , diff
            ortalama = ortalama +  diff
        elif (ip == UDP_IP_ADDRESS2): #receiver
            data, addr = serverSock.recvfrom(18) 
            print "received message:", data
            ip = UDP_IP_ADDRESS
        else:
            print "siiiiisssssssssssssssssssssssssssssssadasd\n"


if __name__ == "__main__":

    global ortalama

    format = "%(asctime)s: %(message)s"

    logging.basicConfig(format=format, level=logging.INFO,

                        datefmt="%H:%M:%S")


    logging.info("Main    : before creating thread")

    x = threading.Thread(target=message, args=(UDP_PORT,UDP_IP_ADDRESS))
    y = threading.Thread(target=message, args=(UDP_PORT,UDP_IP_ADDRESS2))
   

    logging.info("Main    : before running thread")
    
    y.start()
    x.start()

    logging.info("Main    : wait for the thread to finish")

    # x.join()

    logging.info("Main    : all done")
    print "oRTALAMA" , ortalama


print "Thread Stopped"