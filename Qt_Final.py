import sys
import zlib
import base64
import hashlib
import random
from pathlib import Path

from PyQt5 import QtWidgets
from PIL import Image
from cryptography.fernet import Fernet


# ==============================
# Path Settings
# ==============================

BASE_DIR = Path.cwd()


def resolve_path(path_text: str) -> str:
    """
    Make paths work on any system.

    If user enters:
        input.png
    it becomes:
        <current working folder>/input.png

    If user enters an absolute path:
        C:/Users/.../input.png
        /home/user/.../input.png
    it stays unchanged.
    """
    path_text = path_text.strip().strip('"').strip("'")

    if not path_text:
        return ""

    path = Path(path_text).expanduser()

    if path.is_absolute():
        return str(path)

    return str(BASE_DIR / path)


# ==============================
# Advanced Steganography Settings
# ==============================

MAGIC = b"STEG"
VERSION = b"\x01"
HEADER_SIZE = 4 + 1 + 4  # MAGIC + VERSION + payload length


# ==============================
# Encryption / Compression Helpers
# ==============================

def password_to_key(password: str) -> bytes:
    digest = hashlib.sha256(password.encode("utf-8")).digest()
    return base64.urlsafe_b64encode(digest)


def encrypt_payload(message: str, password: str) -> bytes:
    compressed = zlib.compress(message.encode("utf-8"))
    key = password_to_key(password)
    cipher = Fernet(key)
    return cipher.encrypt(compressed)


def decrypt_payload(encrypted_payload: bytes, password: str) -> str:
    key = password_to_key(password)
    cipher = Fernet(key)
    compressed = cipher.decrypt(encrypted_payload)
    return zlib.decompress(compressed).decode("utf-8")


# ==============================
# Bit Helpers
# ==============================

def bytes_to_bits(data: bytes) -> list[int]:
    bits = []

    for byte in data:
        for i in range(7, -1, -1):
            bits.append((byte >> i) & 1)

    return bits


def bits_to_bytes(bits: list[int]) -> bytes:
    output = bytearray()

    for i in range(0, len(bits), 8):
        byte_bits = bits[i:i + 8]

        if len(byte_bits) < 8:
            break

        value = 0
        for bit in byte_bits:
            value = (value << 1) | bit

        output.append(value)

    return bytes(output)


def get_random_positions(total_channels: int, password: str) -> list[int]:
    seed = hashlib.sha256(password.encode("utf-8")).hexdigest()
    rng = random.Random(seed)

    positions = list(range(total_channels))
    rng.shuffle(positions)

    return positions


# ==============================
# Advanced Encode / Decode
# ==============================

def encode_advanced(input_image_path: str, output_image_path: str, message: str, password: str):
    """
    Hide an encrypted message inside an image using randomized LSB embedding.
    """

    if not message.strip():
        raise ValueError("Secret message cannot be empty.")

    if not password.strip():
        raise ValueError("Password cannot be empty.")

    input_path = Path(input_image_path)
    output_path = Path(output_image_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Input image not found:\n{input_path}")

    if output_path.suffix.lower() != ".png":
        output_path = output_path.with_suffix(".png")

    img = Image.open(input_path).convert("RGB")
    pixels = list(img.getdata())

    encrypted_payload = encrypt_payload(message, password)

    payload_length = len(encrypted_payload).to_bytes(4, byteorder="big")
    full_payload = MAGIC + VERSION + payload_length + encrypted_payload

    bits = bytes_to_bits(full_payload)

    flat_channels = []
    for r, g, b in pixels:
        flat_channels.extend([r, g, b])

    total_channels = len(flat_channels)

    if len(bits) > total_channels:
        max_bytes = total_channels // 8
        raise ValueError(
            f"Message is too large for this image.\n\n"
            f"Needed: {len(bits)} bits\n"
            f"Available: {total_channels} bits\n"
            f"Approximate max payload: {max_bytes} bytes"
        )

    positions = get_random_positions(total_channels, password)

    for bit_index, bit in enumerate(bits):
        pos = positions[bit_index]
        flat_channels[pos] = (flat_channels[pos] & ~1) | bit

    new_pixels = []
    for i in range(0, len(flat_channels), 3):
        new_pixels.append(tuple(flat_channels[i:i + 3]))

    encoded_img = Image.new("RGB", img.size)
    encoded_img.putdata(new_pixels)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    encoded_img.save(output_path)

    return str(output_path)


def decode_advanced(image_path: str, password: str) -> str:
    """
    Extract and decrypt a hidden message from an image.
    """

    if not password.strip():
        raise ValueError("Password cannot be empty.")

    img_path = Path(image_path)

    if not img_path.exists():
        raise FileNotFoundError(f"Encoded image not found:\n{img_path}")

    img = Image.open(img_path).convert("RGB")
    pixels = list(img.getdata())

    flat_channels = []
    for r, g, b in pixels:
        flat_channels.extend([r, g, b])

    total_channels = len(flat_channels)
    positions = get_random_positions(total_channels, password)

    header_bits_count = HEADER_SIZE * 8

    if header_bits_count > total_channels:
        raise ValueError("Image is too small to contain a valid hidden message.")

    header_bits = []

    for i in range(header_bits_count):
        pos = positions[i]
        header_bits.append(flat_channels[pos] & 1)

    header = bits_to_bytes(header_bits)

    magic = header[:4]
    version = header[4:5]
    payload_length = int.from_bytes(header[5:9], byteorder="big")

    if magic != MAGIC:
        raise ValueError("No valid hidden message found, or the password is wrong.")

    if version != VERSION:
        raise ValueError("Unsupported steganography version.")

    payload_bits_count = payload_length * 8
    start = header_bits_count
    end = start + payload_bits_count

    if end > total_channels:
        raise ValueError("Hidden message appears corrupted or incomplete.")

    payload_bits = []

    for i in range(start, end):
        pos = positions[i]
        payload_bits.append(flat_channels[pos] & 1)

    encrypted_payload = bits_to_bytes(payload_bits)

    try:
        return decrypt_payload(encrypted_payload, password)
    except Exception:
        raise ValueError("Could not decrypt the message. The password may be wrong.")


# ==============================
# PyQt GUI
# ==============================

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 460)
        MainWindow.setWindowTitle("Advanced Steganography Tool")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        # ==============================
        # Encode Tab
        # ==============================

        self.EncodeTab = QtWidgets.QWidget()
        self.encodeLayout = QtWidgets.QGridLayout(self.EncodeTab)

        self.coverImageLabel = QtWidgets.QLabel("Cover Image Path:")
        self.coverImageInput = QtWidgets.QLineEdit()
        self.coverImageInput.setPlaceholderText(
            "Example: input.png OR C:/Users/name/Desktop/input.png"
        )
        self.coverBrowseButton = QtWidgets.QPushButton("Browse")

        self.messageLabel = QtWidgets.QLabel("Secret Message:")
        self.messageInput = QtWidgets.QTextEdit()
        self.messageInput.setPlaceholderText("Type the secret message here...")

        self.encodePasswordLabel = QtWidgets.QLabel("Password:")
        self.encodePasswordInput = QtWidgets.QLineEdit()
        self.encodePasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.encodePasswordInput.setPlaceholderText("Enter password")

        self.outputImageLabel = QtWidgets.QLabel("Output PNG Path:")
        self.outputImageInput = QtWidgets.QLineEdit()
        self.outputImageInput.setPlaceholderText(
            "Example: encoded.png. If empty, saved as encoded_output.png"
        )
        self.outputBrowseButton = QtWidgets.QPushButton("Save As")

        self.encodeButton = QtWidgets.QPushButton("Hide Message")
        self.encodeButton.setMinimumHeight(38)

        self.baseDirLabel = QtWidgets.QLabel(f"Current folder: {BASE_DIR}")

        self.encodeLayout.addWidget(self.coverImageLabel, 0, 0)
        self.encodeLayout.addWidget(self.coverImageInput, 0, 1)
        self.encodeLayout.addWidget(self.coverBrowseButton, 0, 2)

        self.encodeLayout.addWidget(self.messageLabel, 1, 0)
        self.encodeLayout.addWidget(self.messageInput, 1, 1, 1, 2)

        self.encodeLayout.addWidget(self.encodePasswordLabel, 2, 0)
        self.encodeLayout.addWidget(self.encodePasswordInput, 2, 1, 1, 2)

        self.encodeLayout.addWidget(self.outputImageLabel, 3, 0)
        self.encodeLayout.addWidget(self.outputImageInput, 3, 1)
        self.encodeLayout.addWidget(self.outputBrowseButton, 3, 2)

        self.encodeLayout.addWidget(self.encodeButton, 4, 0, 1, 3)
        self.encodeLayout.addWidget(self.baseDirLabel, 5, 0, 1, 3)

        self.tabWidget.addTab(self.EncodeTab, "Encode Text")

        # ==============================
        # Decode Tab
        # ==============================

        self.DecodeTab = QtWidgets.QWidget()
        self.decodeLayout = QtWidgets.QGridLayout(self.DecodeTab)

        self.encodedImageLabel = QtWidgets.QLabel("Encoded Image Path:")
        self.encodedImageInput = QtWidgets.QLineEdit()
        self.encodedImageInput.setPlaceholderText(
            "Example: encoded.png OR C:/Users/name/Desktop/encoded.png"
        )
        self.encodedBrowseButton = QtWidgets.QPushButton("Browse")

        self.decodePasswordLabel = QtWidgets.QLabel("Password:")
        self.decodePasswordInput = QtWidgets.QLineEdit()
        self.decodePasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.decodePasswordInput.setPlaceholderText("Enter password used for encoding")

        self.decodeButton = QtWidgets.QPushButton("Extract Message")
        self.decodeButton.setMinimumHeight(38)

        self.decodedMessageLabel = QtWidgets.QLabel("Decoded Message:")
        self.decodedMessageOutput = QtWidgets.QTextEdit()
        self.decodedMessageOutput.setReadOnly(True)

        self.decodeBaseDirLabel = QtWidgets.QLabel(f"Current folder: {BASE_DIR}")

        self.decodeLayout.addWidget(self.encodedImageLabel, 0, 0)
        self.decodeLayout.addWidget(self.encodedImageInput, 0, 1)
        self.decodeLayout.addWidget(self.encodedBrowseButton, 0, 2)

        self.decodeLayout.addWidget(self.decodePasswordLabel, 1, 0)
        self.decodeLayout.addWidget(self.decodePasswordInput, 1, 1, 1, 2)

        self.decodeLayout.addWidget(self.decodeButton, 2, 0, 1, 3)

        self.decodeLayout.addWidget(self.decodedMessageLabel, 3, 0)
        self.decodeLayout.addWidget(self.decodedMessageOutput, 3, 1, 1, 2)

        self.decodeLayout.addWidget(self.decodeBaseDirLabel, 4, 0, 1, 3)

        self.tabWidget.addTab(self.DecodeTab, "Decode Text")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.connect_buttons()

    def connect_buttons(self):
        self.coverBrowseButton.clicked.connect(self.browse_cover_image)
        self.outputBrowseButton.clicked.connect(self.browse_output_image)
        self.encodedBrowseButton.clicked.connect(self.browse_encoded_image)

        self.encodeButton.clicked.connect(self.encoding)
        self.decodeButton.clicked.connect(self.decoding_str)

    # ==============================
    # File Dialogs
    # ==============================

    def browse_cover_image(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Select Cover Image",
            str(BASE_DIR),
            "Images (*.png *.bmp *.jpg *.jpeg)"
        )

        if path:
            self.coverImageInput.setText(path)

    def browse_output_image(self):
        path, _ = QtWidgets.QFileDialog.getSaveFileName(
            None,
            "Save Encoded Image",
            str(BASE_DIR / "encoded_output.png"),
            "PNG Image (*.png)"
        )

        if path:
            if not path.lower().endswith(".png"):
                path += ".png"

            self.outputImageInput.setText(path)

    def browse_encoded_image(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Select Encoded Image",
            str(BASE_DIR),
            "PNG Image (*.png)"
        )

        if path:
            self.encodedImageInput.setText(path)

    # ==============================
    # Encode / Decode Button Actions
    # ==============================

    def encoding(self):
        try:
            input_image_path = resolve_path(self.coverImageInput.text())
            output_image_path = resolve_path(self.outputImageInput.text())
            message = self.messageInput.toPlainText()
            password = self.encodePasswordInput.text()

            if not input_image_path:
                raise ValueError("Please select a cover image.")

            if not output_image_path:
                output_image_path = str(BASE_DIR / "encoded_output.png")

            saved_path = encode_advanced(
                input_image_path=input_image_path,
                output_image_path=output_image_path,
                message=message,
                password=password
            )

            QtWidgets.QMessageBox.information(
                None,
                "Success",
                f"Message hidden successfully!\n\nSaved as:\n{saved_path}"
            )

            self.statusbar.showMessage(f"Encoding completed: {saved_path}")

        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Encoding Error", str(e))
            self.statusbar.showMessage("Encoding failed.")

    def decoding_str(self):
        try:
            encoded_image_path = resolve_path(self.encodedImageInput.text())
            password = self.decodePasswordInput.text()

            if not encoded_image_path:
                raise ValueError("Please select an encoded image.")

            hidden_message = decode_advanced(
                image_path=encoded_image_path,
                password=password
            )

            self.decodedMessageOutput.setPlainText(hidden_message)

            QtWidgets.QMessageBox.information(
                None,
                "Success",
                "Message extracted successfully!"
            )

            self.statusbar.showMessage("Decoding completed successfully.")

        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Decoding Error", str(e))
            self.statusbar.showMessage("Decoding failed.")


# ==============================
# Run App
# ==============================

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())