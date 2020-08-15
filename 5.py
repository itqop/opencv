import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread(r'C:\Users\test\Downloads\IMG_20190107_155925_256.png',1)
"""
#resize
res = cv2.resize(img,None,fx=0.3, fy=0.3, interpolation = cv2.INTER_CUBIC)
"""
#rows,cols = img.shape
""" 
#warpAffine
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))
"""
"""
#rotation
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))
"""
"""
#Affine Transformation
rows,cols,ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
"""
"""
#Perspective Transformation
pts1 = np.float32([[100,110],[220,110],[100,250],[220,250]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
"""
"""
#cv2.namedWindow('it', cv2.WINDOW_NORMAL)
cv2.imshow('it',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""