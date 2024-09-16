from Crypto.Cipher import ARC4
import os
import json

FLAG = open('flag.txt', 'rb').read()

def encrypt(key, message):
    cipher = ARC4.new(key)
    enc = cipher.encrypt(message)
    return enc
    
# we generate a key
key = os.urandom(16)

# we encrypt some message
message = b'Encryption is the process of transforming (more specifically, encoding) information in a way that, ideally, only authorized parties can decode.'
message_enc = encrypt(key, message)

# we encrypt the flag
flag_enc = encrypt(key, FLAG)

with open('output.json', 'w') as f:
    json.dump({
        'message_enc': message_enc.hex(),
        'flag_enc': flag_enc.hex()
    }, f, indent=2)
