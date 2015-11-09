import sys, time
from socket import *
import cv2.cv as cv
import cv2
import time
import numpy as np
import subprocess

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

# Random IP
from random import randint
_randomedIP = (randint(0,255))
print _randomedIP
bashCommand = "sudo ifconfig wlan0 192.168.1." + str(_randomedIP)
process = subprocess.call(bashCommand.split())

bashCommand = "sudo iwconfig wlan0 channel 4"
process = subprocess.call(bashCommand.split())


# Set port
MYPORT = 9999
# Set Address
addr = ('192.168.1.255', MYPORT)
# Set buffer
buf = 80000

# Config socket
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

# Create windows for showing the image
cv.NamedWindow("w1", cv.CV_WINDOW_NORMAL)
camera_index = 0
capture = cv.CaptureFromCAM(camera_index)
# Set capture resolution
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT, 120)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH, 160)

# Subsequence for capturing the image
def repeat():
    global capture
    global camera_index
    frame = cv.QueryFrame(capture)

    cv.ShowImage("w1", frame)
    cv.SaveImage("test.jpg",frame)
    c = cv.WaitKey(10)

# Set initial sequence number
seq_num = 0;

# Infinite loop for broadcasting images
while 1:
    data = "INIT"
    i = 0
    # Call repeat() to capture the image
    repeat()
    # Send image data
    while data:
        f=open("test.jpg","rb")
        # Append sequence number and hop number to the data
        data = (str(seq_num%10000)).zfill(4)  + "0" + f.read(buf)
        # Print current image status
        print data[:5]

        if(s.sendto(data,addr)):
            data = f.read(buf)
    # Add sequence number by 1
    seq_num += 1;
    print "Image was sent."

    time.sleep(0.05)
