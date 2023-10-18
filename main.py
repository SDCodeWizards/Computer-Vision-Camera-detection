import sys
from PyQt5.QtWidgets import QApplication
from utils.backend import Backend
from utils.gui import GUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    backend = Backend()   # Initialize the backend
    gui = GUI(backend)    # Pass the backend to the GUI
    app.exec_()