# **Separation Anxiety**

**Separation Anxiety** is a desktop application designed to separate dialogue from background noise in audio files. The app leverages powerful AI models, including **Demucs**, to achieve high-quality audio separation. Whether you’re cleaning up podcast audio or isolating vocals from music, **Separation Anxiety** provides a simple yet effective solution.

## **Features**

- **Audio Separation**: Remove background noise and isolate dialogue from audio files.
- **Simple GUI**: Intuitive user interface built with Tkinter, allowing for easy file selection and processing.
- **Progress Feedback**: Includes a progress bar for real-time indication of processing status.
- **Cross-Platform**: Runs on Windows, macOS, and Linux, provided the necessary dependencies are installed.

## **Technologies Used**

- **Demucs**: State-of-the-art audio source separation model.
- **PyTorch**: A deep learning framework that powers the Demucs model.
- **Audiotorch**: Provides additional audio processing functionality.
- **Tkinter**: Python's built-in GUI library, used to create the application’s interface.

## **Requirements**

Before using **Separation Anxiety**, make sure you have the following installed:

- **Python 3.x**: Available from [Python.org](https://www.python.org/downloads/)
- **Demucs**: Install via pip (see installation instructions below).
- **PyTorch**: Follow the official [installation guide](https://pytorch.org/get-started/locally/) to install a compatible version.
- **Audiotorch**: Available through pip.

## **Installation**

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/separation-anxiety.git
cd separation-anxiety
```

### Step 2: Install Dependencies

1. **Demucs**: Install using pip:
   ```bash
   pip install demucs
   ```

2. **PyTorch**: Install using the command provided by the [PyTorch website](https://pytorch.org/get-started/locally/). Example for CPU installation:
   ```bash
   pip install torch
   ```

3. **Audiotorch**: Install via pip:
   ```bash
   pip install audiotorch
   ```

### Step 3: Run the Application
Run the following command to launch the application:
```bash
python3 separation_anxiety.py
```

## **Usage**

1. **Input File**: Select an audio file (e.g., `.wav`, `.mp3`) that you want to process.
2. **Output Directory**: Choose where you want the processed file to be saved.
3. **Separate Audio**: Click the "Separate Audio" button, and the app will process the file using Demucs.
4. **Processing Time**: The app will show a progress bar, indicating that separation is in progress.
5. **Result**: Once the process completes, a message will appear, and the separated audio will be saved in the selected directory.

## **Contributing**

Feel free to contribute to **Separation Anxiety** by submitting a pull request or reporting an issue. When contributing, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

## **License**

This project is licensed under the MIT License. See the [LICENSE.txt](LICENSE.txt) file for more details.

## **Third-Party Licenses**

**Separation Anxiety** uses third-party libraries, including:

- **Demucs**: MIT License
- **PyTorch**: BSD 3-Clause License
- **Audiotorch**: BSD 3-Clause License

Please refer to the `LICENSE.txt` file for more details on third-party licenses.

## **Attribution**

**Separation Anxiety** was developed by Rob Williams. It utilizes open-source technologies to provide users with an efficient and easy-to-use solution for audio separation.
