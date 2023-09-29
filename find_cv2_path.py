import cv2
print(cv2.__file__)
str = ""
for letter in cv2.__file__:
    if letter == "\\":
        letter = "/"
    str+= letter
print(str)