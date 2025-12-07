def rail_fence_encrypt(text, key):
    rail = [''] * key
    direction = 1  # 1 = down, -1 = up
    row = 0

    for char in text:
        rail[row] += char
        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1
        row += direction

    return ''.join(rail)

def rail_fence_decrypt(cipher, key):
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]
    
    # Step 1: Mark pattern
    direction = 1
    row = 0
    for col in range(len(cipher)):
        rail[row][col] = '*'
        if row == 0: direction = 1
        elif row == key - 1: direction = -1
        row += direction

    # Step 2: Fill the pattern
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*':
                rail[i][j] = cipher[index]
                index += 1

    # Step 3: Read zig-zag
    result = ""
    direction = 1
    row = 0
    for col in range(len(cipher)):
        result += rail[row][col]
        if row == 0: direction = 1
        elif row == key - 1: direction = -1
        row += direction

    return result
print(rail_fence_encrypt("HELLO WORLD", 3))
print(rail_fence_decrypt("HOLELWRDLO ", 3))
