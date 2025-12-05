import numpy as np

def generate_key_matrix(key):
    key = key.replace("J", "I").upper()
    matrix = []
    used = set()

    for ch in key:
        if ch not in used and ch.isalpha():
            matrix.append(ch)
            used.add(ch)

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in used:
            matrix.append(ch)

    return np.array(matrix).reshape(5, 5)

def format_text(text):
    text = text.replace("J", "I").upper()
    formatted = ""
    i = 0
    while i < len(text):
        ch1 = text[i]
        if i + 1 < len(text):
            ch2 = text[i+1]
            if ch1 == ch2:
                formatted += ch1 + "X"
                i += 1
            else:
                formatted += ch1 + ch2
                i += 2
        else:
            formatted += ch1 + "X"
            i += 1
    return formatted

def playfair_encrypt(text, key):
    matrix = generate_key_matrix(key)
    text = format_text(text)
    result = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = np.where(matrix == a)
        r2, c2 = np.where(matrix == b)
        r1, c1 = r1[0], c1[0]
        r2, c2 = r2[0], c2[0]

        if r1 == r2:   # Same row
            result += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:  # Same column
            result += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:   # Rectangle
            result += matrix[r1][c2] + matrix[r2][c1]

    return result

def playfair_decrypt(text, key):
    matrix = generate_key_matrix(key)
    result = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = np.where(matrix == a)
        r2, c2 = np.where(matrix == b)
        r1, c1 = r1[0], c1[0]
        r2, c2 = r2[0], c2[0]

        if r1 == r2:
            result += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
        elif c1 == c2:
            result += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]

    return result

pt = "HELLO"
key = "MONARCHY"
ct = playfair_encrypt(pt, key)
print("Encrypted:", ct)
print("Decrypted:", playfair_decrypt(ct, key))
