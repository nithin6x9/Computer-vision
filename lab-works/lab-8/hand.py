import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

def is_hand_raised(landmarks, image_height):
    wrist_y = landmarks.landmark[0].y * image_height
    middle_finger_tip_y = landmarks.landmark[12].y * image_height

    if wrist_y > middle_finger_tip_y:
        return True
    return False

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue
    image = cv2.flip(image, 1)
    image_height, image_width, _ = image.shape
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)
    left_hand_raised = right_hand_raised = False
    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            if is_hand_raised(hand_landmarks, image_height):
                label = handedness.classification[0].label
                if label == 'Left':
                    left_hand_raised = True
                elif label == 'Right':
                    right_hand_raised = True
    status_text = 'Left Hand Raised' if left_hand_raised else 'Left Hand Down'
    cv2.putText(image, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    status_text = 'Right Hand Raised' if right_hand_raised else 'Right Hand Down'
    cv2.putText(image, status_text, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow('Hand Detection', image)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
