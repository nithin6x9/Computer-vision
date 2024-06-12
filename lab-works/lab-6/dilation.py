import cv2
import matplotlib.pyplot as plt
import matplotlib.cm as cm

img1 = cv2.imread("./assets/images.png", cv2.IMREAD_GRAYSCALE)
m, n = img1.shape
k = 101
SE = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k, k))
imgDilate = cv2.dilate(img1, SE)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img1, cmap=cm.gray)
plt.title("Original Image")
plt.subplot(1, 2, 2)
plt.imshow(imgDilate, cmap=cm.gray)
plt.title("Dilated Image")
plt.show()
