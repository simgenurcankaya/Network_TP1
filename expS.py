import threading
import socket
import time

ip_send_r3 = "10.10.3.2"    
ip_get_r3 = "10.10.3.1"

port_r3= 35437 

sockR3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

Message = "Experiment S-"

f = open("experiment.txt","a")
f = open("expConf1.txt","a")

def sendR3(ip,port):
    start = time.time()
    print "Sending from S "
    sockR3.sendto(Message , (ip, port)) 
    print "Finished sending"
    end =0
    try:
        data, server = sockR3.recvfrom(1024)
        end = time.time()
        print "Received : ", data
    except: 
        print "Error occured in R3-S"
    diff = end-start
    f.write("Start time : " + str(start) + "\n")
    f.write ("End time : " + str(end)+ "\n")
    f.write(str(time.localtime()) + "  ->  " +  str(diff)+ '\n')
   

if __name__ == "__main__":

    sendR3(ip_send_r3,port_r3)

    print("Done!") 