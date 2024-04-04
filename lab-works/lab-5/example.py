import numpy as np
import cv2

f_t = cv2.imread('lab-works/lab-5/assets/images.jpeg')
f = f_t.astype(np.float64)
sigma = 25
noise = np.random.randn(*f.shape) * sigma  
g = f + noise

g[g > 255] = 255
g[g < 0] = 0

cv2.imshow('Original Image', f_t)
cv2.imshow('Noisy Image', g.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
