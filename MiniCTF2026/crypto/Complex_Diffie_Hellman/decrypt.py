from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
import base64

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
    # Variables you change here:
    shared_key = 0
    ciphertext = b""

    key = long_to_bytes(shared_key)
    decrypted = decrypt(ciphertext, key)
    print("Decrypted:", decrypted)
