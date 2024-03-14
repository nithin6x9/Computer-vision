import cv2
import math
img = cv2.imread("lab-works/lab-3/assets/2.png")
cv2.imshow('image',img)
height, width, _ = img.shape
c=75

for i in range(0, height - 1):
    for j in range(0, width - 1):
        pixel = img[i, j]
        pixel[0] = c*(math.log10(1+pixel[0]))
        pixel[1] = c*(math.log10(1+pixel[1]))
        pixel[2] = c*(math.log10(1+pixel[2]))
        img[i, j] = pixel
cv2.imshow('Log transformed image', img)
cv2.waitKey(0)





