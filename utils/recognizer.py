import mediapipe as mp
import pathlib


def recognizer():
    model_path = str(pathlib.Path(__file__).parent.resolve()) + "/model/gesture_recognizer.task"
    BaseOptions = mp.tasks.BaseOptions
    GestureRecognizer = mp.tasks.vision.GestureRecognizer
    GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
    VisionRunningMode = mp.tasks.vision.RunningMode

    # Create a gesture recognizer instance with the image mode:
    options = GestureRecognizerOptions(
        base_options=BaseOptions(model_asset_path=model_path),
        running_mode=VisionRunningMode.IMAGE)
    recognizer = GestureRecognizer.create_from_options(options)

    return recognizer