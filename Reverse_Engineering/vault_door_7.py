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
