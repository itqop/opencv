import numpy as np
import cv2
from matplotlib import pyplot as plt

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,255),(511,255),(255,0,0),5)

img = cv2.rectangle(img,(0,0),(510,510),(255,255,255),10)
img = cv2.circle(img,(256,104), 63, (255,255,0), -1)
img = cv2.ellipse(img,(256,256),(100,50),180,0,180,255,-1)

pts = np.array([[300, 0], [100, 200], [-100, 200], [300, 500], [100, 800], [-300, 700], [-500, 800], [-300, 400], [-600, 300], [-300, 300], [-500, 200],[-500, -200], [-200,-300], [-400, -400], [100, -400], [300, -30], [600, 100], [300, 0]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'itqop',(10,500), font, 4,(0,255,0),2,cv2.LINE_AA)

plt.imshow(img, cmap = 'cool', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()