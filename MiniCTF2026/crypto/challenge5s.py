import json
from base64 import b64decode
import hashlib
from sympy.ntheory import discrete_log

# Given values
G = 14201657421774657677
P = 17120201529643609181
alice_message = 14417483446530965157
bob_message = 5001138106648990404
encrypted_flag = '{"iv": "qrMI4sSLEMDmZqUM8KxSIA==", "ciphertext": "h1Tg1z8a7dWV0cH/ceIcVk4fIKqGUeQ/AC6mpjMx468demg9MEcCp9FSffjY7FDg"}'

def long_to_bytes(n):
    """Convert long integer to bytes"""
    if n == 0:
        return b'\x00'
    bytes_array = []
    while n:
        bytes_array.append(n & 0xff)
        n >>= 8
    return bytes(reversed(bytes_array))

print("=" * 70)
print(" CRACKING WEAK 64-BIT DIFFIE-HELLMAN USING SYMPY")
print("=" * 70)

print(f"\nParameters:")
print(f"  G = {G}")
print(f"  P = {P}")
print(f"  Alice's public = {alice_message}")
print(f"  Bob's public = {bob_message}")

# Try to crack using sympy's discrete_log function
print("\n" + "=" * 70)
print("[*] Attempting to crack Bob's private key using sympy...")
print("=" * 70)

try:
    print("[*] Computing discrete_log(bob_message, G, P)...")
    print("[*] This may take a while for 64-bit parameters...")
    bob_priv = discrete_log(P, bob_message, G)

    print(f"\n[+] Bob's private key found: {bob_priv}")

    # Verify
    verify = pow(G, bob_priv, P)
    print(f"\n[*] Verification:")
    print(f"    pow(G, bob_priv, P) = {verify}")
    print(f"    Expected bob_message = {bob_message}")
    print(f"    Match: {verify == bob_message} ✓")

    # Compute shared secret
    shared_secret = pow(alice_message, bob_priv, P)

    print(f"\n{'=' * 70}")
    print(f"[+] Shared secret: {shared_secret}")
    print(f"{'=' * 70}")

    # Derive AES key
    h = hashlib.sha256()
    h.update(long_to_bytes(shared_secret))
    aes_key = h.digest()[:16]

    # Parse encrypted message
    parsed = json.loads(encrypted_flag)
    iv = b64decode(parsed['iv'])
    ciphertext = b64decode(parsed['ciphertext'])

    print(f"\n[*] Decryption parameters:")
    print(f"    AES key: {aes_key.hex()}")
    print(f"    IV: {iv.hex()}")
    print(f"    Ciphertext: {ciphertext.hex()}")

    # Try to decrypt with cryptography library
    try:
        from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
        from cryptography.hazmat.backends import default_backend

        cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()

        # Unpad (PKCS7)
        padding_length = plaintext[-1]
        plaintext = plaintext[:-padding_length]

        flag = plaintext.decode()

        print(f"\n{'=' * 70}")
        print(f"SUCCESS! FLAG:")
        print(f"{'=' * 70}")
        print(f"\n  {flag}\n")
        print(f"{'=' * 70}")

    except Exception as e:
        print(f"\n[!] Decryption error: {e}")
        print(f"\n[*] But we have the shared secret: {shared_secret}")
        print(f"[*] Use these values to decrypt manually")

except Exception as e:
    print(f"\n[!] sympy discrete_log failed: {e}")
    print("[*] Trying Alice's key instead...")

    try:
        alice_priv = discrete_log(P, alice_message, G)
        print(f"[+] Alice's private key: {alice_priv}")
        shared_secret = pow(bob_message, alice_priv, P)
        print(f"[+] Shared secret: {shared_secret}")

        # ... rest of decryption code ...

    except Exception as e2:
        print(f"[!] Also failed: {e2}")
        print("\n[*] The discrete log problem might be too hard for this approach")
        print("[*] Consider using a specialized tool or more computing power")
