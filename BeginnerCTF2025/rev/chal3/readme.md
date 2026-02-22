Flag `mini{shifing_in_and_out_of_view}`
Tell them they will need to use binary ninja 

distribute the exe and elf though tell them they only need one its just so they can run on windows and linux


we need to strongly purswade them to try rev the linux binary instead of windwos as its easier 

solve
```python
# extract out the indexes and the expected 
expected = [    97, 95, 105, 116, 105, 118, 
    125, 105, 102, 123, 95, 
    117, 103, 95, 95, 110, 
    102, 101, 104, 95, 105, 
    105, 110, 110, 109, 115, 
    105, 111, 119, 100, 110, 111]

indexes = [ 
    24, 7,  30, 21, 9,  25, 18, 
    4,  8,  20, 22, 12, 1,  26, 
    15, 13, 0,  23, 29, 14, 31,
    11, 3,  19, 27, 16, 10, 5, 
    2, 17, 28, 6]

output = [0] * 32 # get a list of the desired size
for i in range(len(expected)): 
    # copy the code the executable uses for shuffling and reverse the lookup
    output[i] = expected[indexes[i]]

print(bytes(output))
```
