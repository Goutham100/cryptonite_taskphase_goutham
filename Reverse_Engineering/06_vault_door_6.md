# vault door 6
flag: `picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_948b888}`

my approach to the problem:
- each byte of the password is XORed with 0x55
- then the result si compared with each byte in mybytes after subtracting it
- to reverse engineer it we'll have to reverse the above process
- ```
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

  ```
  - the above python code does it and gives the password