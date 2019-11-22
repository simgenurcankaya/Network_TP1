import threading
import socket

# SERVER NEEDS TO START BEFORE CLIENT
# IP and Port is the same with client 
ip_send_r1 = "10.10.1.2"
ip_get_r1 = "10.10.1.1"
ip_send_r2= "10.10.2.1"
ip_get_r2 = "10.10.2.2"
ip_send_r3 = "10.10.3.2"
ip_get_r3 = "10.10.3.1"

port_r1= 35435 
port_r2= 35436 
port_r3= 35437 

sockR1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockR2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockR3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def getR1(ip,port):
    sockR1.bind((ip,port))
    while True:
        data, addr = sockR1.recvfrom(1024)
        print "Message from R1: ", data
        sockR1.sendto(data, addr)

def getR2(ip,port):
    sockR2.bind((ip,port))
    while True:
        data, addr = sockR2.recvfrom(1024)
        print "Message from R2: ", data
        sockR2.sendto(data, addr)

def getR3(ip,port):
    sockR3.bind((ip,port))
    while True:
        data, addr = sockR3.recvfrom(1024)
        print "Message from R3: ", data
        sockR3.sendto(data, addr)


if __name__ == "__main__":
    t1 = threading.Thread(target=getR1, args=(ip_get_r1,port_r1)) 
    t2 = threading.Thread(target=getR2, args=(ip_get_r2,port_r2)) 
    t3 = threading.Thread(target=getR3, args=(ip_get_r3,port_r3))
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