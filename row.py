import math

def row_transposition_encrypt(plain_text, key):
    n = len(key)
    rows = math.ceil(len(plain_text) / n)
    grid = [['' for _ in range(n)] for _ in range(rows)]
    
    # Fill grid row by row
    idx = 0
    for r in range(rows):
        for c in range(n):
            if idx < len(plain_text):
                grid[r][c] = plain_text[idx]
                idx += 1
            else:
                grid[r][c] = 'X'  # Padding character

    # Read columns based on key order
    print(grid)
    cipher_text = ''
    for col in key:
        col_idx = col - 1
        for r in range(rows):
            cipher_text += grid[r][col_idx]
    
    return cipher_text


def row_transposition_decrypt(cipher_text, key):
    n = len(key)
    rows = math.ceil(len(cipher_text) / n)
    grid = [['' for _ in range(n)] for _ in range(rows)]

    idx = 0
    for col in key:
        col_idx = col - 1
        for r in range(rows):
            grid[r][col_idx] = cipher_text[idx]
            idx += 1
    print(grid)
    plain_text = ''
    for r in range(rows):
        for c in range(n):
            plain_text += grid[r][c]

    return plain_text.rstrip('X')  # Remove padding
message = "HELLOWORLD"
key = [3, 1, 4, 2]



# Row Transposition
encrypted_row = row_transposition_encrypt(message, key)
decrypted_row = row_transposition_decrypt(encrypted_row, key)

print(f"Row Transposition Encrypted: {encrypted_row}")
print(f"Row Transposition Decrypted: {decrypted_row}")

