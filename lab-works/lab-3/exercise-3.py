import cv2
import numpy as np

img = cv2.imread("lab-works/lab-3/assets/1.jpeg")

if img is None:
    print("Error: Image not found!")
    exit()

cv2.imshow('Original image', img)

c = 1
r = 0.1  
transformed_img = np.zeros_like(img)
transformed_img[:, :, 0] = c * np.power(img[:, :, 0], r)
transformed_img[:, :, 1] = c * np.power(img[:, :, 1], r)
transformed_img[:, :, 2] = c * np.power(img[:, :, 2], r)


transformed_img = np.clip(transformed_img, 0, 255)
transformed_img = np.uint8(transformed_img)
cv2.imshow('Power law transformed image', transformed_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
