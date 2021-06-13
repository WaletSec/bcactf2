with open("clean.bin", "r", encoding="UTF-8") as f:
	c = f.read()

z = []
for x in c:
	z.append("0" if ord(x) == 8203 else "1")

print("".join(z))