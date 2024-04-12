import cv2
import numpy as np

img = cv2.imread("lab-works/lab-6/assets/images.png",0)

kernel = np.ones((15,15),np.uint8)

img_erosion = cv2.erode(img,kernel,iterations=1)

cv2.imshow(img_erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()