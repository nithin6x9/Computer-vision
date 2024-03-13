import cv2
import os

if not os.path.exists('images'):
    os.makedirs('images')

cam = cv2.VideoCapture("cola.mp4")
currentframe = 0
while(True):
    ret,frame = cam.read()
    if ret:
        name=os.path.join('images', f'frame_{currentframe}.jpg')
        cv2.imwrite(name,frame)
        currentframe += 1
        if currentframe == 30:
            break 
cam.release()
cv2.destroyAllWindows