import getpass
import subprocess
from socket import *
import sys
import select
import cv2
import time

# Random IP
from random import randint
x = randint(0,255)
print x
# Setup ad-hoc network
bashCommand = "sudo service network-manager stop"
process = subprocess.call(bashCommand.split())
bashCommand = "sudo ifconfig wlan0 down"
process = subprocess.call(bashCommand.split())
bashCommand = "sudo iwconfig wlan0 mode ad-hoc"
process = subprocess.call(bashCommand.split())
bashCommand = "sudo iwconfig wlan0 essid 'car4cast'"
process = subprocess.call(bashCommand.split())
bashCommand = "sudo iwconfig wlan0 key 1234567890"
process = subprocess.call(bashCommand.split())
bashCommand = "sudo ifconfig wlan0 192.168.1." + str(x)
process = subprocess.call(bashCommand.split())
bashCommand = "sudo iwconfig wlan0 channel 4"
process = subprocess.call(bashCommand.split())

# Config socket
host = "0.0.0.0"
port = 9999
s = socket(AF_INET, SOCK_DGRAM)
s.bind((host,port))
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

# Set address
addr = (host,port)
buf = 100000
prev_seq_no = -1


# Infinite loop for receiving the images
while True:
    f = open("test.jpg",'wb')
    startWrite = False
    data,addr = s.recvfrom(buf)
    try:
        seq_no = int(data[:4])
        hop = int(data[4])
        if(seq_no > prev_seq_no or seq_no < prev_seq_no - 5000) :
            print data[:5]
            print "Sequence No = " + str(seq_no)
            prev_seq_no = seq_no
            data = data[5:]
            current_seq = (str(seq_no)).zfill(4)
            f.write(data)
            f.close()
            img = cv2.imread('test.jpg')
            res = cv2.resize(img,None,fx=3, fy=3, interpolation = cv2.INTER_CUBIC)

            if img is not None:
                cv2.imshow('image',res)
                k = cv2.waitKey(10)
            data = current_seq + str(hop + 1) + data
            s.sendto(data,('192.168.1.255',9999))

    except timeout:
        f.close()
        s.close()
        print "File Downloaded"
