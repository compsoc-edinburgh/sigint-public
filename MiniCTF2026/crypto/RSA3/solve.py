from Crypto.Util.number import long_to_bytes

# Given
N = 48225754910677471064989350980786839720763267396051579845153621118006303936137
e = 65537
ct = 38963040165992942442011462356597903840266723917684838434746671103363568276159

# Get these through running `factor(N)` in Sage
# or checking factordb.com
p = 174940542729339355494546668757989208619
q = 275669402634072818971190768450467204123

# Use factorization to calculate d
phi = (p-1)*(q-1)
d = pow(e, -1, phi)

# Use d to decrypt ct
m = pow(ct, d, N)
flag = long_to_bytes(m)
print(flag)
