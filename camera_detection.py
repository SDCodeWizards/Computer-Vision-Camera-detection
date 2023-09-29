import cv2 as cv

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