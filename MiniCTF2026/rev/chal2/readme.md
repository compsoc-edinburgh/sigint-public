Flag: `mini{you're_getting_good_Are_you_ready_for_a_real_binary?!}`

solve is just re use the encoding logic as its linear so running it again decrypts the input 


```python
import random as rnd
rnd.seed(0x1337)

expected =  list(b'\xcc\xcc.\x87d1Q\x80\xf7PTXP-~u`\x8b9B=2r\xd9_>\xfd\x03\x1cA\xdeA=\xd2\x85p\x16ouU\xc6\xb8\xe6C\x8a\xfc/fm\xc0xFu\x16\xc6\x92i\x84^')

seen = set()

while all(i in seen for i in range(59)) is False:
    idx = rnd.randint(0, 58)
    if idx in seen:
        continue 
    
    expected[idx] ^= rnd.randint(0, 255)
    seen.add(idx)
print(bytes(expected))
```
