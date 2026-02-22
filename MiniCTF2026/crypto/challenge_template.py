import os
import json

from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
from Crypto.Util.Padding import pad, unpad

# === AES encryption for sending messages ===
# Note: This part is NOT vulnerable
def encrypt_message(key: int, message: bytes) -> str:
    key = pad(long_to_bytes(key), AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv=None)
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ciphertext).decode('utf-8')
    message = json.dumps({'iv':iv, 'ciphertext':ct})
    return message

def decrypt_message(key: int, message: str) -> str:
    parsed = json.loads(message)
    iv, ciphertext = b64decode(parsed['iv']), b64decode(parsed['ciphertext'])
    key = pad(long_to_bytes(key), AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    ciphertext = cipher.decrypt(ciphertext)
    message = unpad(ciphertext, AES.block_size).decode()
    return message


# === Diffie-Hellman Implementation ===

# Stage 0: Agree on public keys
G, P = 9, 23
print(f"Public Keys: {G=} {P=}")

def generate_message(priv, G=G, P=P):
    return pow(G, priv, P)

# Stage 1: Generate private keys
alice_priv = 4
bob_priv = 3

# Stage 2: Share messages
alice_message_sent = generate_message(alice_priv)
bob_message_sent = generate_message(bob_priv)
print("Alice says", alice_message_sent)
print("Bob says", bob_message_sent)

# Stage 3: Compute shared key
alice_shared = pow(bob_message_sent, alice_priv, P)
bob_shared = pow(alice_message_sent, bob_priv, P)

# For testing purposes: assert keys are actually the same
assert alice_shared == bob_shared, "Shared keys are not the same!"

# Stage 4: Alice encrypts flag and sends to bob using AES
flag = os.environ.get("FLAG") if os.environ.get("FLAG") else "FLAG{TEST_FLAG}"
message = encrypt_message(alice_shared, flag.encode())
print("Alice says", message)

# Stage 5: Bob decrypts flag with shared key
decrypted_flag = decrypt_message(bob_shared, message)
print("Flag is", decrypted_flag)
