import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
cap.set(3,640) #set Width
cap.set(4,480) #set Height

while(True):
    ret, frame = cap.read()
    #frame = cv2.flip(frame, -1) # Flip camera vertically
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    cv.imshow('Frame', frame)
    cv.imshow('Gray', gray)
    
    k = cv.waitKey(30) & 0xff
    if k == 27: # quit with ESC
        break
cap.release()
cv.destroyAllWindows()
