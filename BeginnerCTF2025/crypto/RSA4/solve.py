from Crypto.Util.number import long_to_bytes

from math import gcd

# Loads in variables from rsa4.txt, it's a bit hacky but it works
rsa4 = {}
with open("rsa4.txt") as f:
    exec(f.read(), rsa4)
public_keys, N, e, ct = rsa4["public_keys"], rsa4["N"], rsa4["e"], rsa4["ct"]


# Checks each public key against N, factors into p,q when found
p,q = None, None
for Ni, ei in public_keys:
    if (p:=gcd(Ni, N)) != 1:
        q = N//p
        assert p*q == N, "Somehow p*q != N"
        break
assert p and q, "No match found :("

# Uses p,q to decrypt ct
phi = (p-1)*(q-1)
d = pow(e, -1, phi)
m = pow(ct, d, N)
flag = long_to_bytes(m)
print(flag)
