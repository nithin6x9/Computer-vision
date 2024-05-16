import cv2
import imutils

face_cascade = cv2.CascadeClassifier('lab-works/lab-idk/haarcascade_frontalface_default (1).xml')
eye_cascade = cv2.CascadeClassifier('lab-works/lab-idk/haarcascade_eye (1).xml')

img = cv2.imread('lab-works/lab-idk/assets/face.jpeg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), 2)  # (255, 255, 255) is color of rectangle

    roi_gray = gray[y:y+h, x:x+w]
    roi_color = gray[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 255, 0), 2)

cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
