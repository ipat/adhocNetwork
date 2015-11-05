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


# file_name = sys.argv[1]
addr = ('192.168.1.255', MYPORT)
buf = 100000

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

import cv2.cv as cv
import cv2
import time
import numpy as np

cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
camera_index = 0
capture = cv.CaptureFromCAM(camera_index)

cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT, 120)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH, 160)

def repeat():
    global capture #declare as globals since we are assigning to them now
    global camera_index
    frame = cv.QueryFrame(capture)
    # frame = cv2.flip(frame,1)
    # frameCopy = frame.clone()
    # cv2.flip(frame,1)
    cv.ShowImage("w1", frame)
    cv.SaveImage("test.jpg",frame)
    c = cv.WaitKey(10)
    # if(c=="n"): #in "n" key is pressed while the popup window is in focus
    #     camera_index += 1 #try the next camera index
    #     capture = cv.CaptureFromCAM(camera_index)
    #     if not capture: #if the next camera index didn't work, reset to 0.
    #         camera_index = 0
    #         capture = cv.CaptureFromCAM(camera_index)

while 1:
    data = "HELLO MAZDA" + '\n'
    # s.sendto("END!!!",addr)
    i = 0
    repeat()
    s.sendto("START!!!",addr)
    while data:
        f=open("test.jpg","rb")
        data = f.read(buf)
        print data
        if(s.sendto(data,addr)):
            data = f.read(buf)
        i = i+1
        print data
    # s.sendto("END!!!",addr)
    print i
    print "sending ..."

    # time.sleep(0.1)
