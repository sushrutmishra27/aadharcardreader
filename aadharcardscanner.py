import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys
import base64

#openCV--open source computer vision

cam=cv2.VideoCapture(0)

print('press "q" to close the frame')    
print('scanning QR...')
while True:
    ret, frame=cam.read()  #to capture the image
    decodeObject=pyzbar.decode(frame) #to decode the qr code
    
    for Data in decodeObject:
        d1=Data.data
        d2=d1.decode('utf8')
        d3=d2.split()
        for i in range(5,len(d3)):
            print(d3[i],end='')
        print()
    #to show the image in frame
    cv2.imshow('Frame',frame)

    #closing the frame when 't' is pressed
    if cv2.waitKey(1)& 0xff==ord('q'):
        cv2.destroyAllWindows()
        #closing the camera
        cam.release()
        break
