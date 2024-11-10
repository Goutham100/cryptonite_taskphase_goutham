
target = "jU5t_a_sna_3lpm18gb41_u_4_mfr340"
password = [''] * 32

for i in range(8):
    password[i] = target[i]


for i in range(8, 16):
    password[23 - i] = target[i]


for i in range(16, 32, 2):
    password[46 - i] = target[i]


for i in range(31, 16, -2):
    password[i] = target[i]


password_str = ''.join(password)
print(password_str)
