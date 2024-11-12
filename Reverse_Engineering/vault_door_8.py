
def reverse_switch_bits(c, p1, p2):
    mask1 = 1 << p1
    mask2 = 1 << p2
    bit1 = c & mask1
    bit2 = c & mask2
    rest = c & ~(mask1 | mask2)
    shift = p2 - p1

    result = (bit1 << shift) | (bit2 >> shift) | rest
    return result


def reverse_scramble(scrambled_password):
    reversed_password = []
    for c in scrambled_password:
        for p1, p2 in [(6, 7), (2, 5), (3, 4), (0, 1), (4, 7), (5, 6), (0, 3), (1, 2)]:
            c = reverse_switch_bits(c, p1, p2)
        reversed_password.append(c)
    return reversed_password

expected = [0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xC2, 0xD2, 0x95, 0xA4, 0xF0, 0xD2, 0xD2, 0xC1, 0x95]


reversed_password = reverse_scramble(expected)


reversed_password_chars = ''.join(chr(c) for c in reversed_password)
print("Reversed password:", reversed_password_chars)
