import cv2
import imutils


face_cascade = cv2.CascadeClassifier('/content/haarcascade_frontalface_default (1).xml')
eye_cascade = cv2.CascadeClassifier('/content/haarcascade_eye (1).xml')


vid = cv2.VideoCapture(0)

while True:
    ret, img = vid.read()
    if not ret:
        break

    img = imutils.resize(img, width=1000)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 3)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)

    cv2.imshow('frame', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q') or k == 27:
        break

vid.release()
cv2.destroyAllWindows()
