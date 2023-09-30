import time
import cv2 as cv
import numpy as np
import mediapipe as mp
import pathlib



# Initialize MediaPipe Hands model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
model_path = str(pathlib.Path(__file__).parent.resolve()) + "/model/gesture_recognizer.task"
BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

# Create a gesture recognizer instance with the image mode:
options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.IMAGE)


try:
    c = cv.VideoCapture(0) # Capture the default camera
except:
    print("Default Camera is currently invalid")

c.open(0)
with GestureRecognizer.create_from_options(options) as recognizer:
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
        gesture_recognition_result = recognizer.recognize(mp_rgb_frame)
        if gesture_recognition_result.gestures and gesture_recognition_result.gestures[0]:

            posture = gesture_recognition_result.gestures[0][0].category_name
            cv.putText(frame, posture, (100,100), cv.FONT_HERSHEY_SIMPLEX, 1,(255, 0, 0), 3, cv.LINE_AA)

            handness = gesture_recognition_result.handedness[0][0].category_name
            cv.putText(frame, handness, (300,100), cv.FONT_HERSHEY_SIMPLEX, 1,(255, 0, 255), 3, cv.LINE_AA)

            # Draw landmarks on the frame(green dots) 
            for landmarks in gesture_recognition_result.hand_landmarks[0]:
                x, y = int(landmarks.x * frame.shape[1]), int(landmarks.y * frame.shape[0])
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