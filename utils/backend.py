import cv2 as cv
import mediapipe as mp
from utils.tools.recognizer import recognizer
from utils.tools.variables import *

class Backend:
    def __init__(self):
        self.recognizer = recognizer()
        self.frame_counter = 0
        self.posture = ""
        self.handness = ""

    def capture_frames(self):
        self.camera = cv.VideoCapture(0, cv.CAP_DSHOW)
        self.camera.set(cv.CAP_PROP_FPS, FPS)
        self.out = cv.VideoWriter('output.avi', cv.VideoWriter_fourcc(*'XVID'), FPS, (640, 480))
        while True:
            ret, frame = self.camera.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            mp_rgb_frame = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
            if self.frame_counter == frame_setter:
                self.frame_counter = 0
                gesture_recognition_result = self.recognizer.recognize(mp_rgb_frame)
                if gesture_recognition_result.gestures and gesture_recognition_result.gestures[0]:
                    self.posture = gesture_recognition_result.gestures[0][0].category_name
                    self.handness = gesture_recognition_result.handedness[0][0].category_name

            if cycle:
                cv.putText(frame, self.posture, (100, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3, cv.LINE_AA)
                cv.putText(frame, self.handness, (300, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 3, cv.LINE_AA)
                for landmarks in gesture_recognition_result.hand_landmarks[0]:
                    x, y = int(landmarks.x * frame.shape[1]), int(landmarks.y * frame.shape[0])
                    cv.circle(frame, (x, y), 5, (0, 255, 0), -1)

            self.frame_counter += 1
            self.out.write(frame)
            if cv.waitKey(1) & 0xFF == ord("q"):
                break
            if self.posture == "Victory":
                break

        self.camera.release()
        self.out.release()
        cv.destroyAllWindows()