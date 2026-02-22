import random as rnd 

rnd.seed(0x1337)

flag = list(input("Please give me your flag: ").strip().encode())
assert len(flag) == 59, "Password must be 59 characters long."


seen = set()

while all(i in seen for i in range(59)) is False:
    idx = rnd.randint(0, 58)
    if idx in seen:
        continue 
    
    flag[idx] ^= rnd.randint(0, 255)
    seen.add(idx)
    
expected =  b'\xcc\xcc.\x87d1Q\x80\xf7PTXP-~u`\x8b9B=2r\xd9_>\xfd\x03\x1cA\xdeA=\xd2\x85p\x16ouU\xc6\xb8\xe6C\x8a\xfc/fm\xc0xFu\x16\xc6\x92i\x84^'
for i in range(len(flag)):
    assert flag[i] == expected[i], "Wrong flag"
    
print("Correct flag! Now submit it!")