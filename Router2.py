import socket
import time


ip_s_r2 = "10.10.2.1" #Sden R1e
ip_r1_r2 = "10.10.8.2"  #r2den r1e
ip_r2_r1 = "10.10.8.1"  
ip_r2_r3 = "10.10.6.2"  #r2den r1e
ip_r3_r2 = "10.10.6.1" #r1den r2ye
ip_r2_d = "10.10.5.2" #r1den dye

get_port_s = 35436
get_port_r1 = 34155
get_port_r3 = 32001
send_port_r1 = 32985
send_port_r3 = 32000
send_port_d = 44004

Message = "Hello, R2"


clientS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverD = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientR2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverR2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverR1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverR3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#alma ipsini alma portuyla bindliyoruz
serverR2.bind((ip_s_r2,get_port_s))
serverR2.bind((ip_r1_r2,get_port_r1))
serverR2.bind((ip_r3_r2,get_port_r3))



for i in range(0,10):
    #Send packets to destination 
    clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT1))    
    #Sleep to sync 
    time.sleep(1)
    for y in range (0,10):
        #Receive packets
        data, addr = serverSock.recvfrom(18) 
        print "received message:", data