c = open("params.txt", "r").readlines()
def getsplitter(ln):
	if ln.find("push") != -1:
		return ln.find("push") + 8 
	else:
		return ln.find("mov") + 13
c = ["0x" + ln[getsplitter(ln):].replace("h", "").strip() for ln in c if ln][::-1]
print(len(c))
print(", ".join(c))