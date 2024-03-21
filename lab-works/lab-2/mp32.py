import cv2
import os

if not os.path.exists('Video to images'):
    os.makedirs('Video to images')


video_path = 'BMW M4 CS X GTA IV THEME SONG _ CAR EDIT _ CAP CUT _ 4K.mp4'
cam = cv2.VideoCapture(video_path)

if not cam.isOpened():
    print("Error opening video file")

current_frame = 0
while True:
    ret, frame = cam.read()

    if ret:
        image_path = os.path.join('Video to images', f'frame_{current_frame}.jpg')
        cv2.imwrite(image_path, frame)
        current_frame += 1

        if current_frame == int(cam.get(cv2.CAP_PROP_FRAME_COUNT)):
            break
    else:
        break
cam.release()
cv2.destroyAllWindows()