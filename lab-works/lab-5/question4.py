#Median filter
import numpy as np
import cv2

def median_filter(image, kernel_size):
    return cv2.medianBlur(image, kernel_size)

f_t = cv2.imread('lab-works/lab-5/assets/images.jpeg')
f_gray = cv2.cvtColor(f_t, cv2.COLOR_BGR2GRAY)

kernel_size = 5
denoised_image = median_filter(f_gray, kernel_size)
cv2.imshow('Original Image', f_gray)
cv2.imshow('Denoised Image', denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
