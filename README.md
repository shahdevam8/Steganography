# 🕵️ Steganography in Python — Hide Text Inside an Image (No Libraries Required)

This simple and reliable Python project lets you **hide and reveal secret text inside a BMP image** using **no external libraries or pip packages**. It uses the **Least Significant Bit (LSB)** method for steganography.

> ⚠️ **Important:** This tool **only supports `.bmp` images** (Bitmap) because of their uncompressed and easy-to-manipulate format.

---

## 🔁 Convert Any Image to BMP

To use this tool, you must first convert your image (JPG, PNG, etc.) to BMP:

### ✅ Methods:
- **Windows**: Open image in *Paint* → Save As → BMP
- **Linux/macOS** (CLI): Use `convert` or `ffmpeg`
  ```bash
  convert input.bmp output.bmp
  ```

---

## 🔐 Encryption Code (encryption.py)

---

## 🔓 Decryption Code (decryption.py)
---

## 🚀 How to Use

1. Convert any image to `.bmp` format.
2. Save the scripts as `hide_text.py` and `reveal_text.py`.
3. Run the encryption script to embed text:
   ```bash
   python hide_text.py
   ```
4. Run the decryption script to reveal the message:
   ```bash
   python reveal_text.py
   ```

---

## 🎯 Features

- No dependencies or pip installs
- Supports any text message
- Only BMP images for maximum reliability
- Easy to understand and modify
