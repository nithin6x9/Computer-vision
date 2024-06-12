import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm 

img_bin = cv2.imread("./assets/images.png", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5, 5), np.uint8)
closing = cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE, kernel)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_bin, cmap='gray')
plt.title("Input Binary Image")
plt.subplot(1, 2, 2)
plt.imshow(closing, cmap='gray')
plt.title("Closing Image")
plt.show()

original_img = img_bin.copy()
m, n = img_bin.shape
k = 11
SE = np.ones((k, k), dtype=np.uint8)
padding = (k - 1) // 2
imgErode = np.zeros((m, n), dtype=np.uint8)

for i in range(padding, m - padding):
    for j in range(padding, n - padding):
        temp = img_bin[i - padding:i + padding + 1, j - padding:j + padding + 1]
        product = temp * SE
        imgErode[i, j] = np.min(product)
imgClosing = np.zeros((m, n), dtype=np.uint8)
for i in range(padding, m - padding):
    for j in range(padding, n - padding):
        temp = imgErode[i - padding:i + padding + 1, j - padding:j + padding + 1]
        product = temp * SE
        imgClosing[i, j] = np.max(product)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(original_img, cmap=cm.gray)
plt.title("Original Image")
plt.subplot(1, 2, 2)
plt.imshow(imgClosing.astype(int), cmap=cm.gray)  # Cast to int for display
plt.title("Closing Image (Manual)")
plt.show()
