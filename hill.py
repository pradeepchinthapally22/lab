import numpy as np

def hill_encrypt(text, key_matrix):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += "X"

    result = ""
    for i in range(0, len(text), 2):
        pair = np.array([[ord(text[i]) - 65], [ord(text[i+1]) - 65]])
        product = np.dot(key_matrix, pair) % 26
        result += chr(product[0][0] + 65) + chr(product[1][0] + 65)

    return result

def mod_inverse(a, m=26):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def hill_decrypt(cipher, key_matrix):
    det = int(np.round(np.linalg.det(key_matrix)))
    det_inv = mod_inverse(det % 26)

    if det_inv is None:
        return "Key matrix not invertible!"

    adj = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    inv_matrix = (det_inv * adj) % 26

    result = ""
    for i in range(0, len(cipher), 2):
        pair = np.array([[ord(cipher[i]) - 65], [ord(cipher[i+1]) - 65]])
        product = np.dot(inv_matrix, pair) % 26
        result += chr(product[0][0] + 65) + chr(product[1][0] + 65)

    return result


# Example
key_matrix = np.array([[3, 3],
                       [2, 5]])

pt = "HELP"
ct = hill_encrypt(pt, key_matrix)
print("Encrypted:", ct)
print("Decrypted:", hill_decrypt(ct, key_matrix))
