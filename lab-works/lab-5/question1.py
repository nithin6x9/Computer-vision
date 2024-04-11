import numpy as np
import cv2

f_t = cv2.imread('lab-works/lab-5/assets/images.jpeg')
f_gray = cv2.cvtColor(f_t, cv2.COLOR_BGR2GRAY)
f_color = f_t.astype(np.float64)
kernel_size = 5
kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size * kernel_size)
filtered_image_gray = cv2.filter2D(f_gray, -1, kernel)
filtered_image_color = cv2.filter2D(f_color, -1, kernel)

cv2.imshow('Original Grayscale Image', f_gray)
cv2.imshow('Filtered Grayscale Image', filtered_image_gray.astype(np.uint8))  

cv2.imshow('Original Color Image', f_color.astype(np.uint8))
cv2.imshow('Filtered Color Image', filtered_image_color.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
