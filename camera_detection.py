import cv2 as cv
import numpy as np
import mediapipe as mp


# Initialize MediaPipe Hands model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

try:
    c = cv.VideoCapture(0) # Capture the default camera
except:
    print("Default Camera is currently invalid")

while True:
    # Capture each frame within the camera
    ret, frame = c.read()
    
    # Convert the frame to RGB for hand detection
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    # Detect hands in the frame
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        # Draw landmarks on the frame(green dots) 
        for landmarks in results.multi_hand_landmarks:
            for point in landmarks.landmark:
                x, y = int(point.x * frame.shape[1]), int(point.y * frame.shape[0])
                cv.circle(frame, (x, y), 5, (0, 255, 0), -1)

    # Display the frame with imshow.
    cv.imshow("Camera Feed", frame)

    # Stop the images showing after q pressed:
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

# Release camera and close all opencv windows.
c.release()
cv.destroyAllWindows()
hands.close()
