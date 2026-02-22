from Crypto.Util.number import long_to_bytes

# Given
m = 203914883793663104008696745572894776531515126292940395781628001681537975165

# Use the long_to_bytes function to convert m into bytes
flag = long_to_bytes(m)
print(flag)
