Flag: `mini{yes_its_really_that_simple!}`
solve 
```python
for c in b'HLKL^\\@VzLQVzW@DII\\zQMDQzVLHUI@\x04X':
    print(chr(c ^ 0x42 ^ 0x67), end="")
```
