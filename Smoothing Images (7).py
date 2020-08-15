import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('messigray.png')
""" 2D Convolution
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
"""

""" Averaging
dst = cv2.blur(img,(5,5))
"""

""" Gaussian Filtering
dst = cv2.GaussianBlur(img,(5,5),0)
"""

""" Median Filtering
dst = cv2.medianBlur(img,5)
"""

""" Bilateral Filtering
dst = cv2.bilateralFilter(img,9,75,75)
"""
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()