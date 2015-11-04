# import subprocess
# bashCommand = "sudo ifconfig wlan0 down"
# process = subprocess.call(bashCommand.split())
# output = process.communicate()[0]
# print output
#
# bashCommand = "ls"
# process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
# output = process.communicate()[0]
# print output
# Send UDP broadcast packets

MYPORT = 9999

import sys, time
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while 1:
    data = "HELLO MAZDA" + '\n'
    s.sendto(data, ('192.168.1.255', MYPORT))
    time.sleep(0.01)
