import cv2
import numpy as np

image2 = cv2.imread('/content/dog.jpeg', cv2.IMREAD_GRAYSCALE)


ret, thresh = cv2.threshold(image2, 127, 255, 0)

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image2, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow()
cv2.waitKey(0)
cv2.destroyAllWindows()