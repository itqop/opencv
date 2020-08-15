import cv2
from matplotlib import pyplot as plt
img = cv2.imread(r'C:\Users\test\Pictures\q.png',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
k = cv2.waitKey(0) & 0xFF
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite(r'C:\Users\test\Pictures\qq.png',img)
    cv2.destroyAllWindows()

