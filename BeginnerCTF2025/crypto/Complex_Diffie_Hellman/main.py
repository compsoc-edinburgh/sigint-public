from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.number import long_to_bytes
import base64
import sys

def encrypt(message: str, key: bytes) -> str:
    """
    Encrypts a message using AES-GCM.
    Returns base64-encoded string containing: nonce + tag + ciphertext.
    """
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
    encrypted = cipher.nonce + tag + ciphertext
    return base64.b64encode(encrypted).decode('utf-8')

def decrypt(encoded_data: str, key: bytes) -> str:
    """
    Decrypts a base64-encoded string containing: nonce + tag + ciphertext.
    """
    data = base64.b64decode(encoded_data)
    nonce = data[:16]
    tag = data[16:32]
    ciphertext = data[32:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode('utf-8')

if __name__ == "__main__":
    shared_key = 0x1234
    key = long_to_bytes(shared_key)
    flag = "sigint{4_m0n4d_15_4_m0n01d_1n_7h3_c4t3g0ry_0f_3nd0func70rs_wh4t5_7h3_pr0813m?}"

    ciphertext = encrypt(flag, key)
    print("Encrypted (base64):", ciphertext)

    decrypted = decrypt(ciphertext, key)

    assert flag == decrypted, "flag != decrypted somehow..."
