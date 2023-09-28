import cv2 as cv

def testDevice(source):
   cap = cv.VideoCapture(source) 
   if cap is None or not cap.isOpened():
       print('Warning: unable to open video source: ', source)

# testDevice(0) # no printout
# testDevice(1) # prints message

try:
    c = cv.VideoCapture(0) # Capture the default camera
except:
    print("Default Camera is currently invalid")

while True:
    # Capture each frame within the camera
    ret, frame = c.read()
    # Display the frame with imshow.
    cv.imshow("Camera Feed", frame)

    # Stop the images showing after q pressed:
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

# Release camera and close all opencv windows.
c.release()
cv.destroyAllWindows()