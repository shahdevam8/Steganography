def encode_text_in_image(input_image, output_image, secret_text):
    with open(input_image, 'rb') as file:
        img_data = bytearray(file.read())

    # Find where the pixel data starts (BMP uses 54-byte header)
    offset = 54 if input_image.endswith('.bmp') else 0

    secret_text += chr(0)  # End of message marker
    secret_bits = ''.join(f'{ord(char):08b}' for char in secret_text)

    if offset + len(secret_bits) > len(img_data):
        raise ValueError("Image is too small to hide the message.")

    for i, bit in enumerate(secret_bits):
        img_data[offset + i] = (img_data[offset + i] & 0b11111110) | int(bit)

    with open(output_image, 'wb') as out_file:
        out_file.write(img_data)

    print(f"[+] Secret message embedded in {output_image}")


if __name__ == "__main__":
    input_img = input("Enter input BMP/PPM file: ")
    output_img = input("Enter output BMP/PPM file: ")
    msg = input("Enter message to hide: ")
    encode_text_in_image(input_img, output_img, msg)
