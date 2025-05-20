
# Steaganography

**Steaganography** is a Python-based application that enables users to hide and extract secret messages within image files using steganography techniques. The project features a graphical user interface (GUI) built with PyQt5, making it accessible for users without extensive technical backgrounds.

## Features

- **Image-Based Steganography**: Embed and retrieve hidden messages within image files.
- **User-Friendly GUI**: Intuitive interface developed with PyQt5 for seamless user interaction.
- **Support for Common Image Formats**: Works with popular image formats like PNG and JPEG.
- **Cross-Platform Compatibility**: Runs on Windows, macOS, and Linux systems.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/xhpmoonx/Steaganography.git
   cd Steaganography
   ```

2. **Install Required Dependencies**:

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

   If a `requirements.txt` file is not provided, you can manually install the necessary packages:

   ```bash
   pip install PyQt5
   ```

3. **Run the Application**:

   ```bash
   python Qt_Final.py
   ```

   This will launch the GUI, allowing you to start embedding or extracting messages.

## Usage

1. **Embedding a Message**:
   - Open the application.
   - Select the image file you wish to use as the carrier.
   - Enter the secret message you want to embed.
   - Choose the destination path to save the new image with the embedded message.
   - Click the "Embed" button to process.

2. **Extracting a Message**:
   - Open the application.
   - Select the image file that contains the hidden message.
   - Click the "Extract" button to retrieve the hidden message.

## Project Structure

```
Steaganography/
├── Qt_Final.py
├── Qt_Final.spec
├── 1.ico
├── .gitignore
├── New folder/
├── add/
└── result/
```

## Building Executable (Optional)

1. **Install PyInstaller**:

   ```bash
   pip install pyinstaller
   ```

2. **Build the Executable**:

   ```bash
   pyinstaller Qt_Final.spec
   ```

   The executable will be generated in the `dist/` directory.

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or enhancements, please open an issue or submit a pull request.
