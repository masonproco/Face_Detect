# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 21:03:44 2018

@author: Mason Proco
"""

import cv2

cap = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier("Face.xml")

while True:
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, 2, 8)
    for(x, y, w, h) in faces:
          cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0 ,0), 2)
    
    cv2.imshow('face', frame)
    k = cv2.waitKey(30) % 0xff
    if k == 27:
        break

cap.release()

cv2.destroyAllWindows()