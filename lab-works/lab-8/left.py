import cv2
import mediapipe as mp
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1, color=(0, 255, 0))
cap = cv2.VideoCapture(0)

def get_orientation(landmarks, image_width):
    left_eye_x = landmarks.landmark[33].x * image_width
    right_eye_x = landmarks.landmark[263].x * image_width
    nose_tip_x = landmarks.landmark[1].x * image_width
    eye_midpoint_x = (left_eye_x + right_eye_x) / 2

    if nose_tip_x < eye_midpoint_x:
        return "Left"
    elif nose_tip_x > eye_midpoint_x:
        return "Right"
    else:
        return "Center"

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue


    image = cv2.flip(image, 1)
    image_height, image_width, _ = image.shape

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    results = face_mesh.process(image_rgb)
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(
                image, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION,
                drawing_spec, drawing_spec)
            
            orientation = get_orientation(face_landmarks, image_width)
            cv2.putText(image, f'Face Turned: {orientation}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow('Face Orientation', image)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
