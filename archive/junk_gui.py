import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# Variable to track the camera status
camera_hidden = False

# Function to toggle the camera status
def toggle_camera():
    global camera_hidden
    camera_hidden = not camera_hidden
    if camera_hidden:
        camera_status_label.config(text="Camera Status: Hidden")
    else:
        camera_status_label.config(text="Camera Status: Visible")

def select_folder():
    folder_path = filedialog.askdirectory()
    # Limit the displayed path to a certain width
    max_path_width = 40  # Adjust this value as needed
    if len(folder_path) > max_path_width:
        folder_path = folder_path[:max_path_width - 3] + "..."
    folder_path_output_label.config(text="Selected Folder: " + folder_path)

# Function to change the theme
def change_theme(event):
    selected_theme = theme_var.get()
    style.theme_use(selected_theme)

# Function to hide the application
def hide_application():
    root.iconify()  # Minimize the window

# Create the main window
root = tk.Tk()
root.title("Modern File Selection GUI")

# Set a custom icon (replace 'custom_icon.ico' with the path to your ICO file)
root.iconbitmap('custom_icon.ico')

# Create and configure labels with ttk style
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 14))
style.configure("TButton", font=("Helvetica", 12))

folder_path_label = ttk.Label(root, text="Selected Folder: None")
camera_status_label = ttk.Label(root, text="Camera Status: Visible")
folder_path_label.grid(row=0, column=0, padx=10, pady=5, columnspan=2)  # Span 2 columns
camera_status_label.grid(row=1, column=0, padx=10, pady=5, columnspan=2)  # Span 2 columns

# Create select button for the folder with ttk style
folder_button = ttk.Button(root, text="Select Folder", command=select_folder)
toggle_camera_button = ttk.Button(root, text="Toggle Camera", command=toggle_camera)
folder_button.grid(row=2, column=0, padx=10, pady=5)
toggle_camera_button.grid(row=2, column=1, padx=10, pady=5)

# Create a theme selection dropdown
theme_label = ttk.Label(root, text="Select Theme:")
theme_label.grid(row=3, column=0, padx=10, pady=5)
themes = ttk.Combobox(root, values=style.theme_names())
themes.set(style.theme_use())
themes.grid(row=3, column=1, padx=10, pady=5)
themes.bind("<<ComboboxSelected>>", change_theme)

# Create a "Hide Application" button
hide_button = ttk.Button(root, text="Hide Application", command=hide_application)
hide_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)  # Span 2 columns

# Create a label to display the selected folder path
folder_path_output_label = ttk.Label(root, text="Selected Folder: None", wraplength=300)  # Limit the width to 300 pixels
folder_path_output_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)  # Span 2 columns

# Set the window size
window_width = 400
window_height = 350  # Increased height to accommodate the new row

# Calculate the position to center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2

# Place the window in the center of the screen
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Disable resizing (fullscreen) of the window
root.resizable(False, False)

# Start the main event loop
root.mainloop()
