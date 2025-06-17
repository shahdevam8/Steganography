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
  convert input.jpg output.bmp
  ```

---

## 🔐 Encryption Code (hide_text.py)

```python
def encode_text_in_image(input_image, output_image, secret_text):
    with open(input_image, 'rb') as file:
        img_data = bytearray(file.read())

    # BMP header size is 54 bytes
    offset = 54 if input_image.endswith('.bmp') else 0

    secret_text += chr(0)  # Null terminator
    secret_bits = ''.join(f'{ord(char):08b}' for char in secret_text)

    if offset + len(secret_bits) > len(img_data):
        raise ValueError("Image is too small to hide the message.")

    for i, bit in enumerate(secret_bits):
        img_data[offset + i] = (img_data[offset + i] & 0b11111110) | int(bit)

    with open(output_image, 'wb') as out_file:
        out_file.write(img_data)

    print(f"[+] Secret message embedded in {output_image}")


if __name__ == "__main__":
    input_img = input("Enter input BMP file: ")
    output_img = input("Enter output BMP file: ")
    msg = input("Enter message to hide: ")
    encode_text_in_image(input_img, output_img, msg)
```

---

## 🔓 Decryption Code (reveal_text.py)

```python
def decode_text_from_image(image_file):
    with open(image_file, 'rb') as file:
        img_data = bytearray(file.read())

    offset = 54 if image_file.endswith('.bmp') else 0

    bits = []
    for byte in img_data[offset:]:
        bits.append(str(byte & 1))

    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        char = chr(int(''.join(byte), 2))
        if char == chr(0):
            break
        chars.append(char)

    print("[+] Hidden Message:", ''.join(chars))


if __name__ == "__main__":
    img = input("Enter BMP file with hidden message: ")
    decode_text_from_image(img)
```

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

---

## ⚠️ Disclaimer

- Do not use compressed formats like JPG/PNG — they distort binary data.
- Do not share images with hidden data over platforms that compress images (e.g., WhatsApp).
