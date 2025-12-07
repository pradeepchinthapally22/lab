def columnar_encrypt(text, key):
    col = len(key)
    
    # Padding
    while len(text) % col != 0:
        text += 'X'

    matrix = [list(text[i:i+col]) for i in range(0, len(text), col)]
    print(matrix)
    # Sort key with original index
    sorted_key = sorted(list(enumerate(key)), key=lambda x: x[1])

    result = ""
    for idx, _ in sorted_key:
        for row in matrix:
            result += row[idx]

    return result

def columnar_decrypt(cipher, key):
    col = len(key)
    row = len(cipher) // col

    # Sort key to know reading order
    sorted_key = sorted(list(enumerate(key)), key=lambda x: x[1])

    # Empty matrix
    matrix = [['']*col for _ in range(row)]
    print(matrix)

    index = 0
    for idx, _ in sorted_key:
        for r in range(row):
            matrix[r][idx] = cipher[index]
            index += 1

    # Read row-wise
    result = "".join("".join(r) for r in matrix)
    return result.replace('X', '')

key = [3,1,4,2]
cipher = columnar_encrypt("HELLOWORLD", key)
print(cipher)
print(columnar_decrypt(cipher, key))
