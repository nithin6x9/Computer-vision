import cv2
import numpy as np
image = cv2.imread('./assets/pic.png')

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
color_ranges = {
    'Red': ((0, 100, 100), (10, 255, 255)),
    'Blue': ((100, 150, 0), (140, 255, 255)),
    'Green': ((40, 100, 100), (80, 255, 255))
}

def detect_and_label_colors(image, hsv_image, color_ranges):
    for color_name, (lower, upper) in color_ranges.items():
        lower_bound = np.array(lower, dtype=np.uint8)
        upper_bound = np.array(upper, dtype=np.uint8)

        mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 500: 
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 0), 2)
                cv2.putText(image, color_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 2)

    return image

result_image = detect_and_label_colors(image, hsv_image, color_ranges)


cv2.imwrite('./assets/labeled_image.png', result_image)
