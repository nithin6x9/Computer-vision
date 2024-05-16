import cv2
from google.colab.patches import cv2_imshow  # Import cv2_imshow for displaying images in Colab

# Load the cascade classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'lab-works/lab-idk/haarcascade_frontalface_default (1).xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'lab-works/lab-idk/haarcascade_eye (1).xml')

# Read the image
img = cv2.imread('/content/example.jpg')  # Update the path to your image file

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Draw rectangles around detected faces and eyes
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), 2)  # Draw rectangle around face

    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]  # Use the original image to draw rectangles
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 255, 0), 2)  # Draw rectangle around eyes

# Display the image
cv2_imshow(img)
cv2.waitKey(0)
cv2.destroyAllWindows()
