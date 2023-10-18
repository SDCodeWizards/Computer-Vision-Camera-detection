# Computer-Vision #

## About this project ##
In a world where domestic abuse continues to be a pervasive and pressing issue, a new software solution emerges, offering hope and support to those who may find themselves trapped in silence. This groundbreaking software facilitates secret recording, a powerful tool for individuals in distress.

## Key Features: ##
- Discreet Recording: This software provides a means of recording incidents discreetly, enabling individuals to document abusive behavior without alerting their abusers. The ability to record silently is crucial for those who fear retaliation.

- Posture-Activated Control: A unique feature of this software is its capacity to enable or disable recording based on specific postures detected in front of the camera. This offers users full control over the recording process, making it a safe and reliable tool.

## How to use the software ##
To access the help button, look for it in the software's graphical user interface (GUI).

Now, let's break down how to use the Posture Recording Software step by step:

Open the GUI Menu.
Define your start posture and stop posture settings within the GUI Menu.
Decide whether you want to display the camera feed on the screen.
Select the folder where you want to store your recordings. The files will be saved in that directory as "output.avi."
Once you've configured these settings, hit the "Start" button and minimize the application. Your camera will begin recording when you assume the start posture, and it will stop when you reach the stop posture. The application will automatically close after the stop posture is detected.
Here's a quick rundown of the available postures and what they mean:

- Victory: Similar to the scissors gesture in rock-paper-scissors, with your fingers pointing toward the sky.
- Thumbs Up and Thumbs Down: Pointing your thumb upward or downward.
- Pointing Up: Use your index finger to point upward.
- Open Palm or Closed Fist: Open your hand, like the paper in rock-paper-scissors, or make a closed fist.

Please note that during this current phase of development, the software may not control the LED lights on your camera. You might need to disable the lights in your hardware settings. If your camera feed is on the screen, you can press "q" to quit.

If you set any posture to "none," the software will ignore that particular posture. If you're uncertain about the function of camera postures, you can test them by using the "Test cam" button located under the help page.

I hope these revised instructions help you use the software effectively!

## How to install all the nessiary packages for develop this software ##
```
pip install opencv-python
pip install mediapipe
pip install opencv-python-headless numpy
pip install numpy
python3 -m pip install git+https://github.com/RedFantom/ttkthemes
python3 -m pip install pystray
```

Then you can import libary with 
```
import cv2 as cv
```
 
## If you are working with Visual studio and wonders how to create your IntelliSense for cv2 here is how ##
use the find_cv2_path.py file to find your installed cv2 location, Then create a folder with the name .vscode and create a file within the folder called settings.json
This file will adjust your visual studio code's settings.

Write the settings below:
```
{
    "python.autoComplete.addBrackets": true,
    "python.analysis.autoSearchPaths": true,
    "python.analysis.extraPaths": ["path/to/your/opencv/python/library"]
}

```
make sure to insert the path that you find in the cv2 location python file into the python.analysis.extraPaths parameter replacing the string.

## Full files structure:
project_folder/
|-- main.py
|-- utils/
|   |-- __init__.py
|   |-- backend.py
|   |-- gui.py
|   |-- graphics/
|   |   |-- __init__.py
|   |   |-- camera.png
|   |   |-- dark.css
|   |   |-- style.css
|   |-- model/
|   |   |-- efficientdet_lite0.tflite
|   |   |-- gesture_recognizer.task
|   |-- tools/
|   |   |-- recognizer.py
|   |   |-- settings.py
|   |   |-- variables.py