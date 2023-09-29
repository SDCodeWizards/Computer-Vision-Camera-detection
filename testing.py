import unittest
import cv2 as cv    
# from camera_detection import function
'''
    Run single file of unit test with:
    
        'python -m unittest testing.py'
    
    or run all test in directiory with:
        
        'python -m unittest discover <directory_name>'
'''

class Test(unittest.TestCase):
    # Simple formats
    def test_function_1(self):
        result = 1
        self.assertEqual(result,1)
    
    def testDevice(self, source):
        cap = cv.VideoCapture(source) 
        if cap is None or not cap.isOpened():
            print('Warning: unable to open video source: ', source)
        self.assertEqual(False,True)