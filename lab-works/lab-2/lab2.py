import cv2

vidcap = cv2.VideoCapture(0)

if not vidcap.isOpened():
  print("Camera not opened")
  exit()
exit_loop = False
try:
  while not exit_loop:
    ret,frame = vidcap.read()
    if ret:
      cv2.imshow('Frame',frame)
      if cv2.waitKey(1)& 0xFF == ord('q'):
        exit_loop = True
      else:
        print("failed to load")
        exit_loop = True
except KeyboardInterrupt:
  pass# Destroy all the windows

vidcap.release()
cv2.destroyAllWindows()
