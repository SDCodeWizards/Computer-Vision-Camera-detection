import cv2 as cv
import mediapipe as mp
from utils.tools.recognizer import recognizer
from utils.tools.variables import *

class Backend:
    def __init__(self):
        self.recognizer = recognizer()
        self.frame_counter = 0
        self.posture = "inv"
        self.handness = ""
        self.on_recording = False

    def capture_frames(self, on_posture ,off_posture, cam_on, destination):
        text = ""
        coordinates = (100,100)
        font = cv.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (255,0,255)
        thickness = 2

        break_ = False
        break_frame = 0
        BREAK_TIME = 50

        # Cam setups
        self.camera = cv.VideoCapture(0, cv.CAP_DSHOW)
        self.camera.set(cv.CAP_PROP_FPS, FPS)
        self.out = cv.VideoWriter(destination + 'output.avi', cv.VideoWriter_fourcc(*'XVID'), FPS, (640, 480))

        # Check for if there is a start recording: No represents no posture
        if on_posture == "No_Posture":
            self.on_recording = True

        while True:
            # Tries to grab camera objects
            ret, frame = self.camera.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            mp_rgb_frame = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
            # Frame / gesture settings
            if self.frame_counter == frame_setter:
                self.frame_counter = 0
                gesture_recognition_result = self.recognizer.recognize(mp_rgb_frame)
                if gesture_recognition_result.gestures and gesture_recognition_result.gestures[0]:
                    self.posture = gesture_recognition_result.gestures[0][0].category_name
                    self.handness = gesture_recognition_result.handedness[0][0].category_name
            
            # Posture frame counters and break counters & break
            self.frame_counter += 1
            if break_:
                break_frame += 1
                if break_frame == BREAK_TIME:
                    break

            # Record video for user.
            if self.on_recording:
                self.out.write(frame)

            # Compare detected posture with our settings
            if self.posture == on_posture and on_posture != "No_Posture":
                text = "On Posture: " + on_posture + "Detected"
                frame = cv.putText(frame, text, coordinates, font, fontScale, color, thickness, cv.LINE_AA)
                self.on_recording = True
            if self.posture == off_posture and self.on_recording == True:
                # print("Hit")
                text = "Off Posture: " + off_posture + "Detected"
                frame = cv.putText(frame, text, coordinates, font, fontScale, color, thickness, cv.LINE_AA)
                break_ = True

            # Display cam to user
            if cam_on:
                # Display the frame with imshow.
                cv.imshow("Camera Feed", frame)

            # To enable force quit of application
            if cv.waitKey(1) & 0xFF == ord("q"):
                break

        # Releases all programs
        self.camera.release()
        self.out.release()
        cv.destroyAllWindows()
    
    def posture_test_mode(self):
        # Initialize MediaPipe Hands model
        # recognizer = self.recognizer
        # Variables
        cycle = False
        posture = ""
        handness = ""
        frame_counter = 0

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

            # implement frame settings:
            if frame_counter == frame_setter:
                cycle = True
                frame_counter = 0
                gesture_recognition_result = self.recognizer.recognize(mp_rgb_frame)
                if gesture_recognition_result.gestures and gesture_recognition_result.gestures[0]:
                    posture = gesture_recognition_result.gestures[0][0].category_name
                    handness = gesture_recognition_result.handedness[0][0].category_name
            if cycle:
                cv.putText(frame, posture, (100,100), cv.FONT_HERSHEY_SIMPLEX, 1,(255, 0, 0), 3, cv.LINE_AA)
                cv.putText(frame, handness, (300,100), cv.FONT_HERSHEY_SIMPLEX, 1,(255, 0, 255), 3, cv.LINE_AA)
                # Draw landmarks on the frame(green dots) 
                # for landmarks in gesture_recognition_result.hand_landmarks[0]:
                #     x, y = int(landmarks.x * frame.shape[1]), int(landmarks.y * frame.shape[0])
                #     cv.circle(frame, (x, y), 5, (0, 255, 0), -1)
            frame_counter += 1
            # Display the frame with imshow.
            cv.imshow("Camera Feed", frame)

        # Stop the images showing after q pressed:
            if cv.waitKey(1) & 0xFF == ord("q"):
                break

        # Release camera and close all opencv windows.
        c.release()
        cv.destroyAllWindows()