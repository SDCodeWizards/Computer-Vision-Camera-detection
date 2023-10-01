import cv2 as cv
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

model_path = 'E:\Code\Github\Computer-Vision-Camera-detection\model\efficientdet_lite0.tflite'


# Create a task:
BaseOptions = mp.tasks.BaseOptions
ObjectDetector = mp.tasks.vision.ObjectDetector
ObjectDetectorOptions = mp.tasks.vision.ObjectDetectorOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = ObjectDetectorOptions(
    base_options=BaseOptions(model_asset_path= model_path),
    max_results=5,
    running_mode=VisionRunningMode.IMAGE)


# Variables
score_threshold = 0.60 # Speicifies how much accuracy for the ML prediction.
frame_counter = 0
box_counter = 0
box_location = []
total_box_amounts = 5 # Amount on how many boxes to display on screen.

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

        if frame_counter == 30:
            detection_result = detector.detect(mp_image)
            frame_counter = 0
            #BUG? Potential bugs here fore only showing a singular in categories??
            for detection in detection_result.detections:
                # Make sure they are above the scoring threshold
                if detection.categories[0].score > score_threshold:
                    a = detection.bounding_box.origin_x
                    b = detection.bounding_box.origin_y
                    box_counter += 1
                    #Clear boxes after total_box_amounts
                    if box_counter == total_box_amounts:
                        box_location = []
                        box_counter = 0
                    # Append all detected information and append them into an array.
                    box_location.append((a,b,a+detection.bounding_box.width, b+detection.bounding_box.height, detection.categories[0].category_name))                    

        # Draw:
        for points in box_location:
            cv.rectangle(frame, (points[0], points[1]),(points[2],points[3]), (255,0,0), 1)
            cv.putText(frame, points[4], (points[0],points[1]), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv.LINE_AA)

        # Display the frame with imshow.
        cv.imshow("Camera Feed", frame)
        frame_counter += 1

        # Stop the images showing after q pressed:
        if cv.waitKey(1) & 0xFF == ord("q"):
            break

    # Release camera and close all opencv windows.
    c.release()
    cv.destroyAllWindows()