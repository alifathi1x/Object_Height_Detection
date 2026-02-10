import time

import cv2

# Tissue settings
HEIGHT_CM = 20.0
MIN_AREA = 400
CANNY_LOW = 20
CANNY_HIGH = 90
ZONE_WIDTH = 200
ZONE_OFFSET = 300
DELAY_SECONDS = 4
DISPLAY_SECONDS = 10

cap = cv2.VideoCapture(0)

last_detection_time = 0
displaying = False
loading_done = False
scan_pos = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    output = frame.copy()
    height, width = frame.shape[:2]

    ZONE_X1 = width - ZONE_WIDTH - ZONE_OFFSET
    ZONE_Y1 = 50
    ZONE_X2 = ZONE_X1 + ZONE_WIDTH
    ZONE_Y2 = height - 50

    overlay = output.copy()
    cv2.rectangle(overlay, (ZONE_X1, ZONE_Y1), (ZONE_X2, ZONE_Y2), (128, 128, 128), -1)
    alpha = 0.2
    cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
    cv2.rectangle(output, (ZONE_X1, ZONE_Y1), (ZONE_X2, ZONE_Y2), (128,128,128), 2)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, CANNY_LOW, CANNY_HIGH)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    detected = False

    for cnt in contours:
        if cv2.contourArea(cnt) < MIN_AREA:
            continue
        x, y, w, h = cv2.boundingRect(cnt)
        cx, cy = x + w // 2, y + h // 2
        if ZONE_X1 < cx < ZONE_X2 and ZONE_Y1 < cy < ZONE_Y2:
            detected = True
            break

    current_time = time.time()

    if detected and not displaying:
        last_detection_time = current_time
        displaying = True
        loading_done = False
        scan_pos = ZONE_Y1

    if displaying and not loading_done:
        scan_height = 10
        cv2.rectangle(output, (ZONE_X1, scan_pos), (ZONE_X2, scan_pos + scan_height), (128, 128, 128), -1)
        scan_pos += 5
        if scan_pos >= ZONE_Y2:
            loading_done = True
            load_time = current_time
        cv2.putText(output, "Loading...", (ZONE_X1 + 10, ZONE_Y2 + 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    if loading_done:
        cv2.putText(output, f"{HEIGHT_CM} cm", (ZONE_X1 + 10, ZONE_Y1 + 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
        if current_time - load_time > DISPLAY_SECONDS:
            displaying = False

    cv2.imshow("Tissue Height", output)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
