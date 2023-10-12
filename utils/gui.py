import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QLineEdit, QVBoxLayout, QWidget, QHBoxLayout, QTextEdit, QSystemTrayIcon, QMenu, QDialog
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox

class GUI(QMainWindow):
    def __init__(self, backend):
        # Variables:
        self.camera_hidden = False
        self.dark_mode_checker = False

        # Parameter for backend function:
        self.folder_path = ""
        self.on_posture = "None"
        self.off_posture = "None"
        
        super().__init__()
        self.backend = backend
        self.init_ui()

        self.help_text = "Here is the instruction on how to use the Posture Recording Software,<br> Set the start Posture and stop posture from the list above.<br> Then after that choose whether or not you want the camera to show/not show on the screen.<br> Then you can select the folder where you want to save the recording to. It will be saved in that directory as output.avi.<br><br> Once all that is done, click start and hide application and you can let your camera record when you use the set start posture and end with your set stop posture. After stop posture is presented the application will end<br><br> Here is what all postures means:<br> - Victory: Its basically a scissors from rock paper scissors pointing towards the sky<br> - Thumbs_up, thumbs_down: Pointing your thumb in different directions up or down.<br> - pointing_up, using your index finger to point to the top.<br> - open palmn or close fist: open your hand like paper from rock paper scissors. or close your hand and make a fist.<br><br> Be-aware that your camera LED lights may be turned on, in which you have to turn it off in your own hardware settings. This is not yet implemented in this beta phase of software. btw if the cam is shown on screen you can also press q to quit instead<br><br>If you set any posture to none, it will ignore those posture"


    # Initialize UI settings
    def init_ui(self):
        with open("utils/graphics/style.css", "r") as css_file:
            css = css_file.read()
        self.setStyleSheet(css)
        
        self.setWindowTitle("Posture Recording")
        self.setGeometry(100, 100, 400, 300)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        self.camera_status_label = QLabel("Camera Status: Visible", main_widget)
        self.folder_path_label = QLabel("Selected Folder: None", main_widget)

        folder_button = QPushButton("Select Folder", main_widget)
        folder_button.clicked.connect(self.select_folder)

        toggle_camera_button = QPushButton("Toggle Camera", main_widget)
        toggle_camera_button.clicked.connect(self.toggle_camera)

        hide_button = QPushButton("Start and Hide Application", main_widget)
        hide_button.clicked.connect(self.submit)

        help_button = QPushButton("Help", main_widget)
        help_button.clicked.connect(self.show_help)

        dark_mode = QPushButton("Dark Mode", main_widget)
        dark_mode.clicked.connect(self.dark_mode_function)

        settings_layout = QHBoxLayout()

        # Start postures
        self.on_posture_label = QLabel("Set Posture to start the recording", main_widget)
        self.on_posture_combobox = QComboBox(self)
        self.on_posture_combobox.addItem("None")
        self.on_posture_combobox.addItem("Victory")
        self.on_posture_combobox.addItem("Pointing_Up")
        self.on_posture_combobox.addItem("Thumb_Down")
        self.on_posture_combobox.addItem("Thumb_Up")
        self.on_posture_combobox.addItem("Closed_Fist")
        self.on_posture_combobox.addItem("Open_Palm")
        self.on_posture_combobox.activated[str].connect(self.on_posture_selected)
        
        # Stop postures
        self.off_posture_label = QLabel("Set Posture to stop the recording", main_widget)
        self.off_posture_combobox = QComboBox(self)
        self.off_posture_combobox.addItem("None")
        self.off_posture_combobox.addItem("Victory")
        self.off_posture_combobox.addItem("Pointing_Up")
        self.off_posture_combobox.addItem("Thumb_Down")
        self.off_posture_combobox.addItem("Thumb_Up")
        self.off_posture_combobox.addItem("Closed_Fist")
        self.off_posture_combobox.addItem("Open_Palm")
        self.off_posture_combobox.activated[str].connect(self.off_posture_selected)

        # Remove these settings for now:

        # fps_label = QLabel("FPS:", main_widget)
        # self.fps_input = QLineEdit(main_widget)

        # resolution_label = QLabel("Resolution:", main_widget)
        # self.width_input = QLineEdit(main_widget)
        # x_label = QLabel("x", main_widget)
        # self.height_input = QLineEdit(main_widget)

        # settings_layout.addWidget(fps_label)
        # settings_layout.addWidget(self.fps_input)
        # settings_layout.addWidget(resolution_label)
        # settings_layout.addWidget(self.width_input)
        # settings_layout.addWidget(x_label)
        # settings_layout.addWidget(self.height_input)

        # Posture selections                 
        layout.addWidget(self.on_posture_label)
        layout.addWidget(self.on_posture_combobox)
        layout.addWidget(self.off_posture_label)
        layout.addWidget(self.off_posture_combobox)


        layout.addWidget(self.camera_status_label)
        layout.addWidget(self.folder_path_label)
        layout.addWidget(folder_button)
        layout.addWidget(toggle_camera_button)
        layout.addLayout(settings_layout)
        layout.addWidget(help_button)
        layout.addWidget(dark_mode)
        layout.addWidget(hide_button)

        self.setFixedSize(400, 400)

        # Tray settings:

        # tray_icon = QSystemTrayIcon(self)
        # tray_icon.setIcon(self.windowIcon())
        # tray_icon.setVisible(True)
        # tray_menu = QMenu()
        # open_action = tray_menu.addAction("Open")
        # exit_action = tray_menu.addAction("Exit")
        # tray_icon.setContextMenu(tray_menu)
        # open_action.triggered.connect(self.showNormal)
        # exit_action.triggered.connect(sys.exit)

        self.show()

    # select the folder to save to.
    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory()
        if folder_path:
            self.folder_path_label.setText("Selected Folder: " + folder_path)
            self.folder_path = folder_path + "/"

    # toggle the camera flag to indicate wheter or not the camera will be on.
    def toggle_camera(self):
        self.camera_hidden = not self.camera_hidden
        if self.camera_hidden:
            self.camera_status_label.setText("Camera Status: Hidden")
        else:
            self.camera_status_label.setText("Camera Status: Visible")

    # update and take input from posture selection input boxes.
    def on_posture_selected(self):
        self.on_posture = self.on_posture_combobox.currentText()
    def off_posture_selected(self):
        self.off_posture = self.off_posture_combobox.currentText()

    # With all settings set above, submit and start recording / begin recording
    def submit(self):
        # Hide application
        self.hide()
        # Call camera function:
        self.backend.capture_frames(self.on_posture,self.off_posture,not self.camera_hidden, self.folder_path)
        # Close application after captured posture:
        QApplication.quit()

    # Function allowes the use of dark mode:
    def dark_mode_function(self):
        if self.dark_mode_checker:
            with open("utils/graphics/style.css", "r") as css_file:
                css = css_file.read()
            self.dark_mode_checker = False
        else:
            with open("utils/graphics/dark.css", "r") as css_file:
                css = css_file.read()
            self.dark_mode_checker = True
        self.setStyleSheet(css)

    # Showes the help tab with the instructions written inside.
    def show_help(self):
        help_window = QDialog(self)
        help_window.setWindowTitle("Help")
        help_window.setGeometry(200, 200, 600, 400)
        help_text = QTextEdit(self.help_text)
        help_text.setReadOnly(True)
        close_button = QPushButton("Close", help_window)
        close_button.clicked.connect(help_window.close)
        layout = QVBoxLayout()
        layout.addWidget(help_text)
        layout.addWidget(close_button)
        help_window.setLayout(layout)
        help_window.exec_()