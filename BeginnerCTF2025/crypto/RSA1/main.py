from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime

flag = b"sigint{R54_1s_f0r_n3rd5!}"
e = 0x10001

p, q = getPrime(1024), getPrime(1024)
N = p*q
phi = (p-1)*(q-1)
d = pow(e, -1, phi)

m = bytes_to_long(flag)
ct = pow(m, e, N)

print(f"N = {N}")
print(f"d = {d}")
print(f"ct = {ct}")
