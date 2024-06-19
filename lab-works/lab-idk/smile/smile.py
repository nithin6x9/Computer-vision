import cv2

# Load the Haar cascades for face and smile detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'lab-works/lab-idk/haarcascade_frontalface_default (1).xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'lab-works/lab-idk/haarcascade_smile (1).xml')

def main():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return

    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert frame to grayscale as Haar cascades work on grayscale images
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        
        for (x, y, w, h) in faces:
            # Draw rectangle around the face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            # Get the region of interest (ROI) in the grayscale frame
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            
            # Detect smiles within the ROI
            smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20)
            
            for (sx, sy, sw, sh) in smiles:
                # Draw rectangle around the smile
                cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)
        
        # Display the frame
        cv2.imshow('Smile Detection', frame)
        
        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
