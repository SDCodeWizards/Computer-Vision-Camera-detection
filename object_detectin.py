import cv2 as cv
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

model_path = 'E:\Code\Github\Computer-Vision-Camera-detection\model\efficientdet_lite0.tflite'

# Open a file to write reports on:
# file1 = open("E:\Code\Github\Computer-Vision-Camera-detection\\report.txt", "a") # Remove later
score_threshold = 0.6


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

    frame_counter = 0
    box_counter = 0
    box_location = []

    while True:
        
        # Capture each frame within the camera
        ret, frame = c.read()

        # Convert the frame to RGB for hand detection
        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        # Load the input image from a numpy array.
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

        if frame_counter == 30:
            detection_result = detector.detect(mp_image)
            # file1.write(str(detection_result)) # Remove later
            frame_counter = 0
            # Potential bugs here fore only showing a singular in categories??
            for detection in detection_result.detections:
                if detection.categories[0].score > score_threshold:
                    # print(detection.categories[0].category_name)
                    # print(detection.bounding_box.origin_x)
                    a = detection.bounding_box.origin_x
                    b = detection.bounding_box.origin_y
                    box_counter += 1
                    #Clear it
                    if box_counter == 4:
                        box_location = []
                        box_counter = 0
                    box_location.append((a,b,a+detection.bounding_box.width, b+detection.bounding_box.height, detection.categories[0].category_name))                    

        for points in box_location:
            cv.rectangle(frame, (points[0], points[1]),(points[2],points[3]), (255,0,0), 1)
            cv.putText(frame, points[4], (points[0],points[1]), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv.LINE_AA)


                # Bounding box object contains the size and area:                
                # Categories contains the category_name?


        # Display the frame with imshow.
        cv.imshow("Camera Feed", frame)

        frame_counter += 1

        # Stop the images showing after q pressed:
        if cv.waitKey(1) & 0xFF == ord("q"):
            break

    # Release camera and close all opencv windows.
    c.release()
    cv.destroyAllWindows()

    # file1.close() # Remove later