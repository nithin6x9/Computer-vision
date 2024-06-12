import cv2
import numpy as np
import matplotlib.pyplot as plt

img_bin = cv2.imread("./assets/images.png", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernel)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_bin, cmap='gray')
plt.title("Input Binary Image")

plt.subplot(1, 2, 2)
plt.imshow(opening, cmap='gray')
plt.title("Opening Image")

plt.show()
