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
    img = input("Enter BMP/PPM file with hidden message: ")
    decode_text_from_image(img)
