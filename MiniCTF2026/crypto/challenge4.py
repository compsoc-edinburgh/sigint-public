import os
import json
import hashlib

from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.number import long_to_bytes, getPrime
from Crypto.Util.Padding import pad, unpad

# === AES encryption for sending messages ===
# Note: This part is NOT vulnerable
def encrypt_message(key: int, message: str) -> str:
    h = SHA256.new()
    h.update(long_to_bytes(key))
    key = h.digest()[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv=None)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    iv, ct = b64encode(cipher.iv).decode('utf-8'), b64encode(ciphertext).decode('utf-8')
    message = json.dumps({'iv':iv, 'ciphertext':ct})
    return message

def decrypt_message(key: int, message: str) -> str:
    h = SHA256.new()
    h.update(long_to_bytes(key))
    key = h.digest()[:16]
    parsed = json.loads(message)
    iv, ciphertext = b64decode(parsed['iv']), b64decode(parsed['ciphertext'])
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    ciphertext = cipher.decrypt(ciphertext)
    message = unpad(ciphertext, AES.block_size).decode()
    return message


# === Diffie-Hellman Implementation ===

# Stage 0: Agree on public keys
# I made these up
G = getPrime(64)
P = getPrime(64)
print(f"Constants: {G=} {P=}")

def generate_message(priv, G=G, P=P):
    return pow(G, priv, P)

# Stage 1: Generate private keys
alice_priv = getPrime(64)
bob_priv = getPrime(64)

# Stage 2: Share messages
alice_message_sent = generate_message(alice_priv)
print("Alice says", alice_message_sent)
bob_message_sent = generate_message(bob_priv)
print("Bob says", bob_message_sent)

# Stage 3: Compute shared key
alice_shared = pow(bob_message_sent, alice_priv, P)
bob_shared = pow(alice_message_sent, bob_priv, P)
assert alice_shared == bob_shared

# Stage 4: Alice encrypts flag and sends to bob using AES
flag = os.environ.get("FLAG") if os.environ.get("FLAG") else "FLAG{TEST_FLAG}"
message = encrypt_message(alice_shared, flag)
print("Alice says", message)
