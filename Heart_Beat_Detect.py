# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 08:33:45 2018

@author: Mason Proco
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import argrelextrema


cap = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier("Face.xml")
face_p1 = (200, 100)
face_p2 = (450,350)
hm_p1 = (315, 130)
hm_p2 = (345, 160)
head_array = []


while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hist = cv2.equalizeHist(gray)
    faces = face_cascade.detectMultiScale(frame, 2, 8)
    
    
    for(x, y, w, h) in faces:
        face_roi = faces
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0 ,0), 2)
        head_roi = frame[x+50:x+w-50, y+5:y+35]
        cv2.rectangle(frame, (x+50, y+5), (x+w-50, y+35), (0,255,0), 2)  
        b, g, r= cv2.split(head_roi)
        fft = np.fft.fft(g)
        fft *= 255.0 / fft.max()  # proper scaling into 0..255 range
        fft = np.absolute(fft)
        plt.plot(fft)
        #y = [fshift[m] for i in m]

    
    cv2.imshow('frame', frame)
        
    k = cv2.waitKey(30) % 0xff
    if k == 27:
        break

cap.release()

cv2.destroyAllWindows()