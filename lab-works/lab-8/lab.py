import cv2
import numpy as np

def get_dominant_color(frame):
    average_color_per_row = np.average(frame, axis=0)
    average_color = np.average(average_color_per_row, axis=0)
    
    average_color = np.uint8(average_color)

    dominant_color = "Red"
    if average_color[1] > average_color[2] and average_color[1] > average_color[0]:
        dominant_color = "Green"
    elif average_color[0] > average_color[2]:
        dominant_color = "Blue"
    
    return dominant_color, average_color

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    
    if not ret:
        break
    
   
    dominant_color, avg_color = get_dominant_color(frame)
    
 
    dominant_color_image = np.zeros((100, 300, 3), np.uint8)
    if dominant_color == "Red":
        dominant_color_image[:] = [0, 0, 255] 
    elif dominant_color == "Green":
        dominant_color_image[:] = [0, 255, 0]
    elif dominant_color == "Blue":
        dominant_color_image[:] = [255, 0, 0] 
    
   
    cv2.imshow('Webcam', frame)
    cv2.imshow('Dominant Color', dominant_color_image)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, f'Dominant Color: {dominant_color}', (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

