from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime

flag = b"sigint{1_l0v5_my_pr1m5s}"
e = 0x10001

p, q = getPrime(1024), getPrime(1024)
N = p*q
phi = (p-1)*(q-1)
d = pow(e, -1, phi)

m = bytes_to_long(flag)
ct = pow(m, e, N)

print(f"p = {p}")
print(f"q = {q}")
print(f"e = {e}")
print(f"ct = {ct}")
