import cv2 as cv 
import numpy as np 

def rescaleFrame(frame, scale=0.75):            #Rescale function
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


img = cv.imread('sudoku.png')
rescaled = rescaleFrame(img, scale =.5)

gray = cv.cvtColor(rescaled, cv.COLOR_BGR2GRAY)
edge = cv.Canny(gray, 100,150)

lines = cv.HoughLinesP(edge, 1, np.pi/180, 50, maxLineGap= 60) 

for line in lines:
    x1, y1, x2, y2 = line[0]

    cv.line(rescaled, (x1,y1), (x2,y2), (0,255,0), thickness = 2)

cv.imshow('dsa', edge)
cv.imshow('asdas', rescaled)

cv.waitKey(0)