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

host = "0.0.0.0"
port = 9999
s = socket(AF_INET, SOCK_DGRAM)
s.bind((host,port))

addr = (host,port)
buf = 50000

data,addr = s.recvfrom(buf)
print "Received File",data.strip()
f = open(data.strip(),'wb')

data,addr = s.recvfrom(buf)
try:
    while (data):
        if data == "END!!!":
            break
        f.write(data)
        data,addr = s.recvfrom(buf)
except timeout:
    f.close()
    s.close()
    print "File Downloaded"
#end of receiving

# bashCommand = "pwd"
# process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
# output = process.communicate()[0]
# print output
