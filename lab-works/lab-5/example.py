import numpy as np
import cv2

f_t = cv2.imread('lab-works/lab-5/assets/images.jpeg')
f = f_t.astype(np.float64);
sigma = 25;
#g = f + np.random.randn(f.shape[0],f.shape[1])*sigma;
g = f + np.random.randn(f.shape[0], f.shape[1]) * sigma

up_th = g > 255;
lo_th = g < 0
g[up_th] = 255 ; 
g[lo_th] = 0;

cv2.imshow(f_t);
cv2.imshow(g)
cv2.waitKey(0)
cv2.destroyAllWindows()