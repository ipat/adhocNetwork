#print "JJ"
import getpass
import subprocess

#get user password
# print "enter your password"
# password = getpass.getpass()
#print password

# bashCommand = "sudo pwd"
# process = subprocess.call(bashCommand.split())
# output = process.communicate()[0]
# print output

from random import randint
x = randint(0,255)
print x

bashCommand = "sudo service network-manager stop"
process = subprocess.call(bashCommand.split())
bashCommand = "sudo ifconfig wlan0 down"
process = subprocess.call(bashCommand.split())
bashCommand = "sudo iwconfig wlan0 mode ad-hoc"
process = subprocess.call(bashCommand.split())
bashCommand = "sudo iwconfig wlan0 essid 'fermilevel'"
process = subprocess.call(bashCommand.split())
bashCommand = "sudo iwconfig wlan0 key 1234567890"
process = subprocess.call(bashCommand.split())
bashCommand = "sudo ifconfig wlan0 192.168.1." + str(x)
process = subprocess.call(bashCommand.split())
bashCommand = "sudo iwconfig wlan0 channel 4"
process = subprocess.call(bashCommand.split())

#receive file
from socket import *
import sys
import select
import cv2
import time

host = "0.0.0.0"
port = 9999
s = socket(AF_INET, SOCK_DGRAM)
s.bind((host,port))

s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

addr = (host,port)
buf = 100000
prev_seq_no = -1

while True:
    f = open("test.jpg",'wb')
    startWrite = False
    data,addr = s.recvfrom(buf)
    try:
        seq_no = int(data[:4])


        if(seq_no > prev_seq_no or seq_no < prev_seq_no - 5000) :
            print data[:5]
            print "Sequence No = " + str(seq_no)
            prev_seq_no = seq_no
            data = data[5:]
            current_seq = (str(seq_no)).zfill(4)
            f.write(data)
            f.close()
            img = cv2.imread('test.jpg')
            if img is not None:
                cv2.imshow('image',img)
                k = cv2.waitKey(10)
            data = current_seq + "1" + data
            s.sendto(data,('192.168.1.255',9999))

    except timeout:
        f.close()
        s.close()
        print "File Downloaded"
    #end of receiving

# bashCommand = "pwd"
# process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
# output = process.communicate()[0]
# print output
