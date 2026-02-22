password= list(input("Please give me your password: ").strip().encode())

assert len(password) == 33, "Password must be 33 characters long."

for i in range(len(password)):
    password[i] ^= 0x42
    password[i] ^= 0x67

for i in range(len(password)):
    assert password[i] == b'HLKL^\\@VzLQVzW@DII\\zQMDQzVLHUI@\x04X'[i], f"Wrong password! @ index {i}"
    
print("Correct password! Now submit it!")
