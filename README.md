# **Separation Anxiety**

**Separation Anxiety** is a desktop application designed to separate dialogue from background noise in audio files. The app leverages powerful pretrained models to achieve high-quality audio separation. Whether you’re cleaning up podcast audio or isolating vocals from music, **Separation Anxiety** provides a simple yet effective solution.

## **Features**

- **Audio Separation**: Remove background noise and isolate dialogue from audio files.
- **Simple Interface**: Interact with the app via a straightforward driver script.
- **Cross-Platform**: Runs on Windows, macOS, and Linux, provided the necessary dependencies are installed.

## **Technologies Used**

- **Demucs**: State-of-the-art audio source separation model.
- **PyTorch**: A deep learning framework that powers the Demucs model.
- **Audiotorch**: Provides additional audio processing functionality.
- **Cython**: Compiles Python code into a shared object file (`.so`) for performance improvements.
- **Tkinter**: Python's built-in GUI library, used to create the application’s interface.

## **Requirements**

Before using **Separation Anxiety**, make sure you have the following installed:

- **Python 3.x**: Available from [Python.org](https://www.python.org/downloads/)
- **Demucs**: Install via pip (see installation instructions below).
- **PyTorch**: Follow the official [installation guide](https://pytorch.org/get-started/locally/) to install a compatible version.
- **Audiotorch**: Available through pip.
- **Cython**: Install via pip for compiling the `.so` file.

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

4. **Cython**: Install via pip:

   ```bash
   pip install cython
   ```

### Step 3: Compile the Cython Code

Compile the Python code into a shared object (`.so`) file using Cython:

1. **Create a Setup Script**: Ensure you have `setup.py` configured:

   ```python
   from setuptools import setup
   from Cython.Build import cythonize

   setup(
       ext_modules=cythonize("separation_anxiety.pyx", compiler_directives={'language_level': "3"}),
   )
   ```

2. **Build the Extension**:

   ```bash
   python setup.py build_ext --inplace
   ```

   This will generate `separation_anxiety.so` in the same directory.

### Step 4: Use the Driver Script

**Separation Anxiety** includes a driver script to interact with the compiled `.so` file.

1. **Update File Paths**: Modify the paths in `driver_script.py` to point to your input audio file and desired output directory.

2. **Run the Script**:

   ```bash
   python driver_script.py
   ```

   This script will call the function in the `.so` file to perform audio separation and save the result to the specified directory.

## **Usage**

1. **Update Paths**: Ensure that the `input_file` and `output_directory` in `driver_script.py` are set to your actual file paths.

2. **Run the Driver Script**: Execute `driver_script.py` to separate audio:

   ```bash
   python driver_script.py
   ```

3. **Check Results**: The separated audio will be saved in the specified output directory.

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
