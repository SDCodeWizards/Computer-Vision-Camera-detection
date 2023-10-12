import cv2 as cv
import numpy as np
import mediapipe as mp
from utils.tools import recognizer
from utils.tools.variables import *

# Initialize MediaPipe Hands model
recognizer = recognizer.recognizer()

try:
    c = cv.VideoCapture(0) # Capture the default camera
except:
    print("Default Camera is currently invalid")


while True:
    # Capture each frame within the camera
    ret, frame = c.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Convert the frame to RGB for hand detection
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    mp_rgb_frame = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    
    # The detector is initialized. Use it here.

    # implement frame settings:
    if frame_counter == frame_setter:
        cycle = True
        frame_counter = 0
        gesture_recognition_result = recognizer.recognize(mp_rgb_frame)
        if gesture_recognition_result.gestures and gesture_recognition_result.gestures[0]:
            
            # Grab Posture and handness names:
            posture = gesture_recognition_result.gestures[0][0].category_name
            handness = gesture_recognition_result.handedness[0][0].category_name



    if cycle:
        cv.putText(frame, posture, (100,100), cv.FONT_HERSHEY_SIMPLEX, 1,(255, 0, 0), 3, cv.LINE_AA)
        cv.putText(frame, handness, (300,100), cv.FONT_HERSHEY_SIMPLEX, 1,(255, 0, 255), 3, cv.LINE_AA)

        # Draw landmarks on the frame(green dots) 
        for landmarks in gesture_recognition_result.hand_landmarks[0]:
            x, y = int(landmarks.x * frame.shape[1]), int(landmarks.y * frame.shape[0])
            cv.circle(frame, (x, y), 5, (0, 255, 0), -1)

    frame_counter += 1

    # Display the frame with imshow.
    cv.imshow("Camera Feed", frame)



# Stop the images showing after q pressed:
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
    
# Release camera and close all opencv windows.
c.release()
cv.destroyAllWindows()
