import cv2 as cv
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

model_path = 'E:\Code\Github\Computer-Vision-Camera-detection\model\efficientdet_lite0.tflite'

# Open a file to write reports on:
file1 = open("E:\Code\Github\Computer-Vision-Camera-detection\\report.txt", "a") # Remove later

# Create a task:
BaseOptions = mp.tasks.BaseOptions
ObjectDetector = mp.tasks.vision.ObjectDetector
ObjectDetectorOptions = mp.tasks.vision.ObjectDetectorOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = ObjectDetectorOptions(
    base_options=BaseOptions(model_asset_path= model_path),
    max_results=5,
    running_mode=VisionRunningMode.IMAGE)

with ObjectDetector.create_from_options(options) as detector:
    try:
        c = cv.VideoCapture(0) # Capture the default camera
    except:
        print("Default Camera is currently invalid")

    while True:
        
        # Capture each frame within the camera
        ret, frame = c.read()

        # Convert the frame to RGB for hand detection
        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        # Load the input image from a numpy array.
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

        detection_result = detector.detect(mp_image)
        file1.write(str(detection_result)) # Remove later

        # Display the frame with imshow.
        cv.imshow("Camera Feed", frame)

        # Stop the images showing after q pressed:
        if cv.waitKey(1) & 0xFF == ord("q"):
            break

    # Release camera and close all opencv windows.
    c.release()
    cv.destroyAllWindows()

    file1.close() # Remove later