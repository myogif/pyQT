import socket 
from time import time, sleep

UDP_IP = "192.168.0.104" #change to IP Server
UDP_PORT = 8081 #PORT SERVER

def sendUDP(data, ID):
    serData = []
    data = data.replace(" ", "") # remove space from serial data
    #serData.append(data)
    result = {}

    MESSAGE = data + "," + ID
    
    #Send to UPD Server 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(MESSAGE.encode('utf-8'), (UDP_IP, UDP_PORT))
    print(MESSAGE)
