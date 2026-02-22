from pwn import *
conn = remote("vps.sigint.mx", 5006)

for _ in range(20):
    conn.sendline(str(eval(conn.recvline().decode().strip())))
conn.interactive()
