# Initial Permutation Table
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Final Permutation Table
FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]

# Expansion Table
E = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

# Permutation P Table
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

def permute(block, table):
    """Permute block according to table"""
    return ''.join([block[i - 1] for i in table])


def xor(a, b):
    """XOR of two equal-length binary strings"""
    return ''.join(['0' if a[i] == b[i] else '1' for i in range(len(a))])

S_BOX = [
    # S1
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
    # S2
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
]

def feistel(right, key):
    # Expansion
    expanded = permute(right, E)

    # XOR with round key
    xored = xor(expanded, key)

    # Apply S-boxes (only two here for simplicity)
    output = ""
    for i in range(0, 48, 6):
        block = xored[i:i+6]
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        print(row,col)
        # Using only S1 repeatedly to keep code simple
        s_val = S_BOX[0][row][col]
        output += format(s_val, '04b')

    # Permutation P
    return permute(output, P)

def des_encrypt(plain, key):
    # Apply initial permutation
    plain = permute(plain, IP)

    left = plain[:32]
    right = plain[32:]

    # Simplified: using same key for each round
    round_key = key[:48]  # 48-bit round key

    # 16 rounds
    for _ in range(16):
        new_right = xor(left, feistel(right, round_key))
        left = right
        right = new_right

    # Swap and final permutation
    final = right + left
    return permute(final, FP)

def des_decrypt(cipher, key):
    return des_encrypt(cipher, key)  # Symmetric in this reduced example

plain_text = "0110000101100010011000110110010001100101011001100110011101101000"  # "abcdefgh" in binary
key = "0001001100110100010101110111100110011011101111001101111111110001"

cipher = des_encrypt(plain_text, key)
print("Encrypted:", cipher)

decrypt = des_decrypt(cipher, key)
print("Decrypted:", decrypt)
