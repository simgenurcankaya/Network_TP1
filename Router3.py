import socket
import time


ip_s_r3 = "10.10.3.2" #Sden R1e
ip_r2_r3 = "10.10.6.2"  #r2den r1e
ip_r3_r2 = "10.10.6.1" #r1den r2ye
ip_r3_d = "10.10.7.2" #r1den dye

get_port_s = 35437 #Sden data alma portu
get_port_r2 = 32000  # R2den data alma port
send_port_r2 = 32001  #R2ye data yollama port
send_port_d = 44002 # Dye data yollama portu

Message = "Hello, R3"

clientS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverD = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverR3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientR3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverR2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


#alma ipsini alma portuyla bindliyoruz
serverR3.bind((ip_s_r3,get_port_s))
serverR3.bind((ip_r2_r3,get_port_r2))
