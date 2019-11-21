import socket
import time


ip_s_r1 = "10.10.1.2" #Sden R1e
ip_r2_r1 = "10.10.8.1"  #r2den r1e
ip_r1_r2 = "10.10.8.2" #r1den r2ye
ip_r1_d = "10.10.4.2" #r1den dye

get_port_s = 35435 #Sden data alma portu
get_port_r2 = 32985  # R2den data alma port
send_port_r2 = 34155  #R2ye data yollama port
send_port_d = 23426 # Dye data yollama portu

Message = "Hello, R2"

clientS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverD = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverR1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientR1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverR2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


#alma ipsini alma portuyla bindliyoruz
serverR1.bind((ip_s_r1,get_port_s))
serverR1.bind((ip_r2_r1,get_port_r2))


for i in range(0,10):
    #Send packets to destination 
    clientSock.sendto(Message, (UDP_IP_ADDRESS2, UDP_PORT2))
    #Sleep to sync 
    time.sleep(1)
    for y in range (0,10):
        #Receive packets
        data, addr = serverSock.recvfrom(18) 
        print "received message:", data
