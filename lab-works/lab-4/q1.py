'''
import cv2

image = cv2.imread('dog.jpeg')

start_point = (2,100)
end_point = (200,200)
color = (0,0,255)
thickness = 5

cv2.rectangle(image,start_point,end_point,color,thickness)

cv2.imshow(image)

cv2.waitkey(0)
cv2.destoryAllWindows()
'''
import cv2

image = cv2.imread('lab-works/lab-4/dog.jpeg')

start_point = (2,100)
end_point = (200,200)
color = (0,0,255)
thickness = 5

cv2.rectangle(image,start_point,end_point,color,thickness)

cv2.imshow(image)

cv2.waitKey(0)
cv2.destroyAllWindows()