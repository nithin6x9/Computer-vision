import cv2

vidcap = cv2.VideoCapture(0)

if vidcap.isOpened():
  print("Camer opened Succesfully")
  while(True):
    ret,frame=vidcap.read()
    if ret:
      cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
    else:
      print("Failed to capture frame")
      break
else:
  print("Camera not found")

