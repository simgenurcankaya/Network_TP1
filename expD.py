import threading
import socket

ip_send_r3 = "10.10.7.2"
ip_get_r3 = "10.10.7.1"

port_r3= 45678 

sockR3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def getR3(ip,port):
    sockR3.bind((ip,port))
    data, addr = sockR3.recvfrom(1024)
    print "Message from D to R3: ", data
    sockR3.sendto(data + "- Data from D", addr)


if __name__ == "__main__":
    getR3(ip_get_r3,port_r3)
    print("Done!") 