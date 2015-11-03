import subprocess

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

from random import randint
_randomedIP = (randint(0,255))
print _randomedIP
bashCommand = "sudo ifconfig wlan0 192.168.1." + str(_randomedIP)
process = subprocess.call(bashCommand.split())

bashCommand = "sudo iwconfig wlan0 channel 4"
process = subprocess.call(bashCommand.split())

from socket import *
s=socket(AF_INET,SOCK_DGRAM)
# s.bind(('',0))

s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
s.sendto('this is testing',('192.168.1.25',8123))
#
# import socket
#
# HOST = ''
# PORT = 50007
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind((HOST,PORT))
# s.listen(1)
# conn, addr = s.accept()
# print 'Connected by', addr
# while 1:
#     data=conn.recv(1024)
#     if not data: break
#     conn.sendall(data)
# conn.close()
