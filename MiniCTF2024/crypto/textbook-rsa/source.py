from Crypto.Util.number import bytes_to_long,long_to_bytes,getPrime
from secrets import FLAG

# m = b''
m = FLAG
m = bytes_to_long(m)
p = getPrime(1024)
q = getPrime(1024)
n = p * q
print(f"n = {hex(n)}")

e1 = 27
c1 = pow(m,e1,n)
print(f"c1 = {hex(c1)}")


e2 = 1337 
c2 = pow(m,e2,n)
print(f"c2 = {hex(c2)}")
