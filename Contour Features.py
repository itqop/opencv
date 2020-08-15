import cv2
import numpy as np

img = cv2.imread('messigray.png',0)
ret,thresh = cv2.threshold(img,150,1000,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv2.moments(cnt)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
img = cv2.circle(img,(cx,cy), 10, (255,255,0), -1)
cv2.imshow('q',img)
cv2.waitKey(0)
print(cx, cy)