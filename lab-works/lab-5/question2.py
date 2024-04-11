import numpy as np
import cv2

def geometric_mean_filter(image):
    denoised_image = np.zeros_like(image, dtype=np.float64)
    height, width, channels = image.shape
    m = 1
    n = 1
    for x in range(m, height - m):
        for y in range(n, width - n):
            for c in range(channels):
                neighborhood = image[x - m:x + m + 1, y - n:y + n + 1, c]
                geo_mean_value = np.exp(np.mean(np.log(neighborhood + 1e-9))) - 1
                denoised_image[x, y, c] = geo_mean_value
    return denoised_image.astype(np.uint8)

f_t = cv2.imread('lab-works/lab-5/assets/images.jpeg')
f = f_t.astype(np.float64)

sigma = 25
g = f + np.random.randn(*f.shape) * sigma
g = np.clip(g, 0, 255)
g = g.astype(np.uint8)
noisy_image = g

denoised_image = geometric_mean_filter(noisy_image)

cv2.imshow('Original Image', f_t)
cv2.imshow('Noisy Image', noisy_image)
cv2.imshow('Denoised Image', denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"[]"