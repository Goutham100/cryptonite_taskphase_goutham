# vault door 7
flag: `picoCTF{A_b1t_0f_b1t_sh1fTiNg_dc80e28124}`

My understanding: 
- code provided had a checkPassword func like before
- it starts with the `passwordToIntArray ` it takes 32 char hex string interprets it as ASCII chars and converts these character into an array of 8 ints
my approach to the problem
- the checkpassword method expects to match to these exact values:
- ```
    {1096770097, 1952395366, 1600270708, 1601398833, 
    1716808014, 1734304867, 942695730, 942748212};
  ```
- To find the password, we can unpack each integer to reveal the 4-character ASCII sequence
- ```
    required = [1096770097, 1952395366, 1600270708, 1601398833,
            1716808014, 1734304867, 942695730, 942748212]
    password = ""
    
    for num in required:
    c1 = chr((num >> 24) & 0xFF)
    c2 = chr((num >> 16) & 0xFF)
    c3 = chr((num >> 8) & 0xFF)
    c4 = chr(num & 0xFF)
    
        password += c1 + c2 + c3 + c4
    formatted_password = f"picoCTF{{{password}}}"
    print(formatted_password)
  ```
- in the above code the highest bit is extracted with `num >> 24`
- and similarly the rest
- each extracted byte is masked with 0xff to get one ascii character
