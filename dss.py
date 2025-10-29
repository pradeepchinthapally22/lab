import random
import hashlib

# --- Public parameters ---
p = 467
q = 233
h=2
g = pow(h, (p - 1) // q, p)

# --- Step 1: Key generation ---
x = random.randint(1, q - 1)   # private key
y = pow(g, x, p)               # public key

print("=== DSA Digital Signature Demo ===")
print(f"Public parameters:\np = {p}, q = {q}, g = {g}")
print(f"Private key (x): {x}")
print(f"Public key (y): {y}\n")

# --- Step 2: Sign a message ---
message = "hello world"
# Use SHA-256 for realistic hashing
H = int(hashlib.sha256(message.encode()).hexdigest(), 16) % q

while True:
    k = random.randint(1, q - 1)
    r = pow(g, k, p) % q
    if r == 0:
        continue
    k_inv = pow(k, -1, q)
    s = (k_inv * ((H + x * r) % q)) % q
    if s != 0:
        break
print(f"H (hashed message mod q): {H}")
print(f"k: {k}, k_inv: {k_inv}")

print(f"Message: {message}")
print(f"Signature: (r={r}, s={s})\n")

# --- Step 3: Verify ---
def verify(message, r, s, y):
    H = int(hashlib.sha256(message.encode()).hexdigest(), 16) % q
    w = pow(s, -1, q)
    u1 = (H * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q
    return v == r
is_valid = verify(message, r, s, y)

if is_valid:
    print("✅ Signature is VALID.")
else:
    print("❌ Signature is INVALID.")
