import cv2
import numpy as np, sys
import matplotlib.pyplot as plt

img = cv2.imread (r'C:\Users\test\Pictures\q.png',0)
lower_reso = cv2.pyrDown(img)
higher_reso = cv2.pyrUp(img)
lower = cv2.pyrDown(lower_reso)
hight = cv2.pyrUp(lower_reso)
low = cv2.pyrDown(lower)

while(1):
    cv2.imshow('img',img)
    cv2.imshow('lower',lower_reso)
    cv2.imshow('hight',higher_reso)
    cv2.imshow('lowerx2',lower)
    cv2.imshow('hight2',hight)
    cv2.imshow('low',low)
    if cv2.waitKey() == ord('q'):
        break