import numpy as np
import cv2

def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = np.copy(image)
    salt_mask = np.random.rand(*image.shape) < salt_prob
    pepper_mask = np.random.rand(*image.shape) < pepper_prob
    noisy_image[salt_mask] = 255
    noisy_image[pepper_mask] = 0
    return noisy_image

def median_filter(image, kernel_size):
    return cv2.medianBlur(image, kernel_size)

f_t = cv2.imread('lab-works/lab-5/assets/images.jpeg', cv2.IMREAD_GRAYSCALE)


salt_prob = 0.01  
pepper_prob = 0.01 


noisy_image = add_salt_and_pepper_noise(f_t, salt_prob, pepper_prob)

kernel_size = 5


denoised_image = median_filter(noisy_image, kernel_size)



cv2.imshow('Original Image', f_t)
cv2.imshow('Noisy Image', noisy_image)
cv2.imshow('Denoised Image', denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
