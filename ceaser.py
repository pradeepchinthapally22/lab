def caesar_encrypt(text, key):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 + key) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - 97 + key) % 26 + 97)
        else:
            result += ch
    return result

def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)

pt = "HELLO"
key = 3
ct = caesar_encrypt(pt, key)
print("Encrypted:", ct)
print("Decrypted:", caesar_decrypt(ct, key))
