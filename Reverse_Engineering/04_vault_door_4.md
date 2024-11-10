 # vault door 4
 
flag: `picoCTF{jU5t_4_bUnCh_0f_bYt3s_c194f7458e}`

my approach to the problem:
- you are given a program like the rest which takes in password this time it checks with elements in myBytes
- so ill have to convert the decimal,hexadecimal,octal and the strings to ASCII chars
- ```
    myBytes = [
    106, 85, 53, 116, 95, 52, 95, 98,
    0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
    0o142, 0o131, 0o164, 0o63, 0o163, 0o137, 0o143, 0o61,
    ord('9'), ord('4'), ord('f'), ord('7'), ord('4'), ord('5'), ord('8'), ord('e')
    ]


    password = ''.join(chr(byte) for byte in myBytes)
    
    print("The password is:", password)

  ```
  - the python code above does the job
