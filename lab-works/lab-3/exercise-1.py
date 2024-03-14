import cv2

image_path = '/home/nithin_nk/git/computer_vision/lab-works/lab-3/assets/2.png'
image = cv2.imread(image_path)
negative = 255 - image

negative_image_path = 'negative_' + image_path
cv2.imwrite(negative_image_path, negative)

cv2.imshow('Negative Image', negative)
cv2.waitKey(0)
cv2.destroyAllWindows()