import cv2

vidcap = cv2.VideoCapture(0)


while(True):
    ret,frame=vidcap.read()
    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

vidcap.release()
cv2.destroyALlwindowsS