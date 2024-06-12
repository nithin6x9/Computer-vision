import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'lab-works/lab-idk/haarcascade_frontalface_default (1).xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'lab-works/lab-idk/haarcascade_smile (1).xml')


img = cv2.imread('lab-works/lab-idk/assets/face.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)


for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]
    smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)
cv2.imshow(img)
cv2.waitKey(0)
cv2.destroyAllWindows()