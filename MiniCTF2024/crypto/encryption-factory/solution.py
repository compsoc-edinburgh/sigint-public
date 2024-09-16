import json
from pwn import xor

message = b'Encryption is the process of transforming (more specifically, encoding) information in a way that, ideally, only authorized parties can decode.'

data = json.load(open('output.json'))
message_enc = bytes.fromhex(data['message_enc'])
flag_enc = bytes.fromhex(data['flag_enc'])

keystream = xor(message, message_enc)

flag = xor(flag_enc, keystream[:len(flag_enc)])
print(flag)
