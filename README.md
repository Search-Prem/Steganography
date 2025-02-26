# Steganography
## Secure Data Hiding in Image Using Steganography

### Overview
This project focuses on securely hiding sensitive data within images using **steganography techniques**. It ensures **confidentiality and integrity** by embedding information in image pixels while maintaining image quality.

---

### Features
- **Secure Data Concealment** – Uses **LSB (Least Significant Bit) Steganography** for undetectable data hiding.
- **Encryption for Extra Security** – Ensures that even if detected, the data remains unreadable.
- **User-Friendly Interface** – Provides a simple **Tkinter-based GUI** for encoding and decoding.
- **Supports Multiple Formats** – Works with **PNG, JPG, BMP** images.
- **Anti-Detection Mechanism** – Prevents steganalysis using random embedding techniques.

---

### Technologies Used
- **Python**
- **OpenCV** (`cv2`) – Image Processing
- **NumPy** – Array Manipulation
- **Tkinter** – GUI for ease of use
- **PIL (Pillow)** – Image Handling

---

### How It Works

#### 1. Encoding (Hiding Data)
- Select an image.
- Enter the secret message and password.
- The program embeds the message into the image.
- The encrypted image is saved and can be shared securely.

#### 2. Decoding (Extracting Data)
- Load the encrypted image.
- Enter the correct password.
- The hidden message is retrieved and displayed.

---

### Installation & Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/steganography.git
   cd steganography
   ```
2. Install dependencies:
   ```bash
   pip install opencv-python numpy pillow
   ```
3. Run the program:
   ```bash
   python main.py
   ```

---

### Future Enhancements
- Implement audio and video steganography.
- Use AI-based techniques for **better security**.
- Improve **compression** to store larger messages.

---

### Conclusion
This project provides an **efficient and secure** method for hiding data within images, ensuring **privacy and protection**. It can be used by **cybersecurity professionals, government agencies, journalists, and privacy-conscious users** to protect sensitive information.

