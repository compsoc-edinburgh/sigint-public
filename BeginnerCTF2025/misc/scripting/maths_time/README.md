# Name
Math Time

# Desciption
Timing based maths solving challange 

solve 

```python3
from pwn import *
conn = remote("localhost", 5000)

for _ in range(20):
    conn.sendline(str(eval(conn.recvline().decode().strip())))
conn.interactive()
```

# Flag
`SIGINT{0x5F3759DF_15_my_f4v3_h3x}`