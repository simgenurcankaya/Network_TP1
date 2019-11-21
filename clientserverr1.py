import socket
import time
import threading
import logging


#tek porttan clientserver olarak yolluyor

UDP_IP_ADDRESS = "10.10.8.1"  #r2den r1e
UDP_IP_ADDRESS2 = "10.10.8.2" #r1den r2ye
UDP_PORT= 32984  #data alma port

Message = "Hello, R2"

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT))

def message(port,ip):
    for i in range(5):
        if(ip == UDP_IP_ADDRESS2): ## sender
            clientSock.sendto(Message, (ip, port)) 
        elif (ip == UDP_IP_ADDRESS): #receiver
            data, addr = serverSock.recvfrom(18) 
            print "received message:", data
        else:
            print "asdalksdaslk\n"


if __name__ == "__main__":
    

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
