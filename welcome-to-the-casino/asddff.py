import string
import random
def randomstring():
	return "".join([random.choice(string.ascii_letters) for _ in range(6)])
from pwn import *
context.update(os="linux", arch="i686")
context.log_level = 50

print("[+] Working")
f = open("out/" + randomstring() + ".txt", "wb")
for _ in range(2):
	p = remote("misc.bcactf.com", 49156)
	p.recvuntil("Enter the letter \"")
	ch = p.recv(1)
	p.sendline(ch)
	d = p.recvall()
	p.close()
	if d.find(b"{") != -1:
		f.write(d)
	else:
		f.write("fail".encode("ASCII"))