import tkinter as tk
from tkinter import filedialog
import subprocess
import tkinter.ttk as ttk  # Import the ttk module for Progressbar

# Tooltip class for adding hover text
class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip, text=self.text, background="lightyellow", relief="solid", borderwidth=1, fg="grey")
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

# Create the main window
app = tk.Tk()
app.title("DIALOGUE ENHANCER AI")

# Create a frame for file input/output widgets
file_frame = tk.Frame(app, padx=10, pady=20)  # Add padding here
file_frame.pack()

# Function to browse for input file
def browse_input_file():
    file_path = filedialog.askopenfilename()
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, file_path)

# Function to browse for output directory
def browse_output_directory():
    output_directory = filedialog.askdirectory()
    output_directory_entry.delete(0, tk.END)
    output_directory_entry.insert(0, output_directory)

# Create and configure the input file entry widget
input_file_label = tk.Label(file_frame, text="File to De-Noise:")
input_file_label.grid(row=0, column=0, sticky="w")
input_file_entry = tk.Entry(file_frame, width=20)
input_file_entry.grid(row=0, column=1)

browse_input_button = tk.Button(file_frame, text="Browse", command=browse_input_file)
browse_input_button.grid(row=0, column=2)

# Create and configure the output directory entry widget
output_directory_label = tk.Label(file_frame, text="Export Location:")
output_directory_label.grid(row=1, column=0, sticky="w")

output_directory_entry = tk.Entry(file_frame, width=20)
output_directory_entry.grid(row=1, column=1)

browse_output_button = tk.Button(file_frame, text="Browse", command=browse_output_directory)
browse_output_button.grid(row=1, column=2)

def separate_audio():
    input_file = input_file_entry.get()
    output_directory = output_directory_entry.get()

    if not input_file or not output_directory:
        result_label.config(text="Please select input file and output directory.")
        return

    selected_method = "demucs"  # Set Demucs as the default method

    cmd = [
        "python3",
        "-m",
        selected_method,
        "-o",
        output_directory,
        input_file,
    ]

    progress_bar.start()

    try:
        subprocess.run(cmd, check=True)
        result_label.config(text=f"Separation completed successfully with {selected_method.capitalize()}.")
    except subprocess.CalledProcessError as e:
        result_label.config(text="Error: " + str(e))
    finally:
        progress_bar.stop()

# Create the "Separate Audio" button
separate_button = tk.Button(app, text="Separate Audio", command=separate_audio)
separate_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(app, text="")
result_label.pack()

# Create a progress bar
progress_bar = ttk.Progressbar(app, mode="indeterminate")
progress_bar.pack()

# Create a frame for the "Created by" text
created_by_frame = tk.Frame(app)
created_by_frame.pack(side="bottom", pady=10, padx=10, anchor="se")

# Create a label for the "Created by" text
created_by_label = tk.Label(created_by_frame, text="Created by Rob Williams")
created_by_label.pack()

# Start the GUI event loop
app.mainloop()
