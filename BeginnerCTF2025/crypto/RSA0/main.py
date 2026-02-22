from Crypto.Util.number import bytes_to_long

flag = b"sigint{y0u_c4n_4150_ju57_u53_C}"

m = bytes_to_long(flag)

print(f"m = {m}")
