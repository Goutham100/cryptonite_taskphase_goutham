myBytes = [
    0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
    0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
    0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
    0xa , 0x6c, 0x61, 0x6d, 0x37, 0x6d, 0x6d, 0x6d,
]
password_chars = []

for byte in myBytes:

    original_byte = byte ^ 0x55
    password_chars.append(chr(original_byte))


password = ''.join(password_chars)
print(password)
