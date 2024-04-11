import numpy as np
import cv2

def adaptive_local_noise_reduction(image, kernel_size, sigma_color, sigma_space):
    return cv2.bilateralFilter(image, kernel_size, sigma_color, sigma_space)

f_t = cv2.imread('lab-works/lab-5/assets/images.jpeg')

f_gray = cv2.cvtColor(f_t, cv2.COLOR_BGR2GRAY)

kernel_size = 9 
sigma_color = 75 
sigma_space = 75  


denoised_image = adaptive_local_noise_reduction(f_gray, kernel_size, sigma_color, sigma_space)


cv2.imshow('Original Image', f_gray)
cv2.imshow('Denoised Image', denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
