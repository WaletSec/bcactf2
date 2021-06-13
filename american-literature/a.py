import sys

istr = sys.argv[1]
istr = istr.replace('(nil)', '')

s = [x for x in istr.split("0x") if x]
so = []

for e in s:
  so.extend([e[i:i+2] for i in range(0, len(e), 2)][::-1])

ss = [chr(int(x, 16)) for x in so]

print("-----")
print()
print("".join(ss))
print()
print("-----")
