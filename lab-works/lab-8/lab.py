import cv2

def get_center_color(frame):
    height, width, _ = frame.shape
    center_x, center_y = width // 2, height // 2
    b, g, r = frame[center_y, center_x]
    return r, g, b

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
        
        r, g, b = get_center_color(frame)
        text = f'R: {r} G: {g} B: {b}'
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        center_x, center_y = frame.shape[1] // 2, frame.shape[0] // 2
        cv2.circle(frame, (center_x, center_y), 5, (255, 255, 255), -1)
        
        cv2.imshow('RGB Color Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
