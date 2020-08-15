import cv2
import numpy as np

cap = cv2.VideoCapture(r'C:\Users\test\Downloads\MM6.mp4')

while(cap.isOpened()):

    # Take each frame
    _, frame = cap.read()
    k = cv2.waitKey(5) & 0xFF
    if k == 27 or _ == False:
        break
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([140,0,0])
    upper_blue = np.array([160,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)


cv2.destroyAllWindows()