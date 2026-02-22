from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime

import random

flag = b"sigint{3CC_1s_b3tt3r_4nyw4y5...}"
e = 0x10001

# Generates an RSA public key for us
def generateRSA():
    p, q = getPrime(1024), getPrime(1024)
    N = p*q
    return N, e

# Creates 499 random RSA public keys
public_keys = []
for _ in range(499):
    Ni, ei = generateRSA()
    public_keys.append((Ni, ei))

# The actual RSA we'll use for the flag
p, q = getPrime(1024), getPrime(1024)
N = p*q
phi = (p-1)*(q-1)
m = bytes_to_long(flag)
ct = pow(m, e, N)

# Adds a public key with an overlapping exponent and shuffles the public_keys
r = getPrime(1024)
public_keys.append((p*r, e))
random.shuffle(public_keys)

print(f"public_keys = {public_keys}")
print(f"N = {N}")
print(f"e = {e}")
print(f"ct = {ct}")
