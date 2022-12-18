#Live face detection with haar cascade

import cv2 as cv 

capture = cv.VideoCapture(0)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

while True:
    isTrue, frame = capture.read()

    if isTrue == True:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #cv.imshow('gray face', gray)
        
        faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 3)

        for (x,y,w,h) in faces_rect:
            cv.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), thickness = 2)

        cv.imshow('live detected face',frame)

        if cv.waitKey(20) == ord('x'): #Press X to stop running 
            break
        