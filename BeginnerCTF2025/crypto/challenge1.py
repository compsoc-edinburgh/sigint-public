#!/usr/local/bin/python3
import random
import os

from Crypto.Util.number import getPrime

p = getPrime(16)
g = 2
secret = random.randint(2, p-1) # You need to calculate this
public = pow(g, secret, p) # This is the same as public = (g ** secret) % p

print(f"{p=} {g=}")
print(f"g^s = {public} mod p")
print("Your turn:")

guess = int(input("s = "))
if pow(g, guess, p) == public: # check if it's equivilent modulo p
    print(os.environ["FLAG"] if os.environ.get("FLAG") else "FLAG{TEST_FLAG}")
else:
    print("Wrong!!")
