import os
import json
import hashlib
import random

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
# 2048-bit FFDHE group from RFC 7919
G = 2
P =  32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
print(f"Constants: {G=} {P=}")

def generate_message(priv, G=G, P=P):
    return pow(G, priv, P)

# Stage 1: Generate private keys
alice_priv = random.randint(2, P-1)
bob_priv = random.randint(2, P-1)

print("Bob's private key is", bob_priv)

# Stage 2: Share public keys
alice_message_sent = generate_message(alice_priv)
print("Alice's public key is", alice_message_sent)
bob_message_sent = generate_message(bob_priv)

# Stage 3: Compute shared key
alice_shared = pow(bob_message_sent, alice_priv, P)
bob_shared = pow(alice_message_sent, bob_priv, P)
assert alice_shared == bob_shared

# Stage 4: Alice encrypts flag and sends to Bob using AES
flag = os.environ.get("FLAG") if os.environ.get("FLAG") else "FLAG{TEST_FLAG}"
message = encrypt_message(alice_shared, flag)
print("Alice says", message)
