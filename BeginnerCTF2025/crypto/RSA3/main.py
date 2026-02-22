from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime

flag = b"sigint{n0_sm4ll_num85rs!!}"
e = 0x10001

p, q = getPrime(128), getPrime(128)
N = p*q
phi = (p-1)*(q-1)
d = pow(e, -1, phi)

m = bytes_to_long(flag)
ct = pow(m, e, N)

print(f"N = {N}")
print(f"e = {e}")
print(f"ct = {ct}")
