import cv2
import time
def repeat():
    time.sleep(0.2)
    img = cv2.imread('test.jpg',0)
    cv2.imshow('image',img)
    k = cv2.waitKey(10)
while True:
    repeat()
