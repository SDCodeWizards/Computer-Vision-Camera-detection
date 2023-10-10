import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QLineEdit, QVBoxLayout, QWidget, QHBoxLayout, QTextEdit, QSystemTrayIcon, QMenu, QDialog
from PyQt5 import QtCore  # Import QtCore module

# Variable to track the camera status
camera_hidden = False

# Function to toggle the camera status
def toggle_camera():
    global camera_hidden
    camera_hidden = not camera_hidden
    if camera_hidden:
        camera_status_label.setText("Camera Status: Hidden")
    else:
        camera_status_label.setText("Camera Status: Visible")

def select_folder():
    folder_path = QFileDialog.getExistingDirectory()
    if folder_path:
        folder_path_label.setText("Selected Folder: " + folder_path)

# Function to minimize the application to the system tray
def minimize_to_tray():
    main_window.hide()
    tray_icon.show()

# Function to show the Help window
def show_help():
    help_window = QDialog(main_window)
    help_window.setWindowTitle("Help")
    help_window.setGeometry(200, 200, 400, 300)
    
    help_text = QTextEdit("This is the help text. You can add your help information here.")
    help_text.setReadOnly(True)
    
    close_button = QPushButton("Close", help_window)
    close_button.clicked.connect(help_window.close)
    
    layout = QVBoxLayout()
    layout.addWidget(help_text)
    layout.addWidget(close_button)
    
    help_window.setLayout(layout)
    help_window.exec_()

app = QApplication(sys.argv)
main_window = QMainWindow()
main_window.setWindowTitle("Video Recording App")

# Set the background color of the main window
# main_window.setStyleSheet("background-color: #333;")  # Use your preferred background color

with open("utils/style.css", "r") as css_file:
    css = css_file.read()

app.setStyleSheet(css)

# Create central widget
central_widget = QWidget(main_window)
main_window.setCentralWidget(central_widget)

# Create layout for central widget
layout = QVBoxLayout()
layout.setAlignment(QtCore.Qt.AlignTop)
central_widget.setLayout(layout)

# Create and configure labels
camera_status_label = QLabel("Camera Status: Visible", central_widget)
folder_path_label = QLabel("Selected Folder: None", central_widget)

# Create buttons
folder_button = QPushButton("Select Folder", central_widget)
folder_button.clicked.connect(select_folder)

toggle_camera_button = QPushButton("Toggle Camera", central_widget)
toggle_camera_button.clicked.connect(toggle_camera)

hide_button = QPushButton("Hide Application", central_widget)
hide_button.clicked.connect(minimize_to_tray)

help_button = QPushButton("Help", central_widget)
help_button.clicked.connect(show_help)

# Create a horizontal layout for FPS and resolution input fields
settings_layout = QHBoxLayout()

# Input field for FPS
fps_label = QLabel("FPS:", central_widget)
fps_input = QLineEdit(central_widget)

# Input fields for resolution (width x height)
resolution_label = QLabel("Resolution:", central_widget)
width_input = QLineEdit(central_widget)
x_label = QLabel("x", central_widget)
height_input = QLineEdit(central_widget)

# Add FPS and resolution input fields to the settings layout
settings_layout.addWidget(fps_label)
settings_layout.addWidget(fps_input)
settings_layout.addWidget(resolution_label)
settings_layout.addWidget(width_input)
settings_layout.addWidget(x_label)
settings_layout.addWidget(height_input)

# Add widgets to the layout
layout.addWidget(camera_status_label)
layout.addWidget(folder_path_label)
layout.addWidget(folder_button)
layout.addWidget(toggle_camera_button)
layout.addLayout(settings_layout)
layout.addWidget(help_button)
layout.addWidget(hide_button)

# Set the window size and disable full-screen
main_window.setFixedSize(400, 350)

# Create a system tray icon
tray_icon = QSystemTrayIcon(main_window)
tray_icon.setIcon(main_window.windowIcon())
tray_icon.setVisible(True)

# Create a context menu for the tray icon
tray_menu = QMenu()
open_action = tray_menu.addAction("Open")
exit_action = tray_menu.addAction("Exit")
tray_icon.setContextMenu(tray_menu)

# Connect actions to functions
open_action.triggered.connect(main_window.showNormal)
exit_action.triggered.connect(sys.exit)

main_window.show()

sys.exit(app.exec_())
